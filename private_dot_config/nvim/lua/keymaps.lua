-- [[ Basic Keymaps ]]
--  See `:help vim.keymap.set()`

-- Set highlight on search, but clear on pressing <Esc> in normal mode
vim.opt.hlsearch = true
vim.keymap.set("n", "<Esc>", "<cmd>nohlsearch<CR>")

-- Diagnostic keymaps
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous [D]iagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next [D]iagnostic message" })
vim.keymap.set("n", "<leader>de", vim.diagnostic.open_float, { desc = "Show [D]iagnostic [E]rror messages" })
vim.keymap.set("n", "<leader>dq", vim.diagnostic.setloclist, { desc = "Open [D]iagnostic [Q]uickfix list" })

-- Exit terminal mode in the builtin terminal with a shortcut that is a bit easier
-- for people to discover. Otherwise, you normally need to press <C-\><C-n>, which
-- is not what someone will guess without a bit more experience.
--
-- NOTE: This won't work in all terminal emulators/tmux/etc. Try your own mapping
-- or just use <C-\><C-n> to exit terminal mode
vim.keymap.set("t", "<Esc><Esc>", "<C-\\><C-n>", { desc = "Exit terminal mode" })

-- TIP: Disable arrow keys in normal mode
-- vim.keymap.set('n', '<left>', '<cmd>echo "Use h to move!!"<CR>')
-- vim.keymap.set('n', '<right>', '<cmd>echo "Use l to move!!"<CR>')
-- vim.keymap.set('n', '<up>', '<cmd>echo "Use k to move!!"<CR>')
-- vim.keymap.set('n', '<down>', '<cmd>echo "Use j to move!!"<CR>')

-- Keybinds to make split navigation easier.
--  Use CTRL+<hjkl> to switch between windows
--
--  See `:help wincmd` for a list of all window commands
--  NOTE: disabled in favour of more compact ones further below
--
-- vim.keymap.set('n', '<C-h>', '<C-w><C-h>', { desc = 'Move focus to the left window' })
-- vim.keymap.set('n', '<C-l>', '<C-w><C-l>', { desc = 'Move focus to the right window' })
-- vim.keymap.set('n', '<C-j>', '<C-w><C-j>', { desc = 'Move focus to the lower window' })
-- vim.keymap.set('n', '<C-k>', '<C-w><C-k>', { desc = 'Move focus to the upper window' })

-- [[ Basic Autocommands ]]
--  See `:help lua-guide-autocommands`

-- Highlight when yanking (copying) text
--  Try it with `yap` in normal mode
--  See `:help vim.highlight.on_yank()`
vim.api.nvim_create_autocmd("TextYankPost", {
  desc = "Highlight when yanking (copying) text",
  group = vim.api.nvim_create_augroup("kickstart-highlight-yank", { clear = true }),
  callback = function()
    vim.highlight.on_yank()
  end,
})

-- WARN: custom parts here!
-- INFO: Open a simple terminal in new buffer
-- vim.keymap.set('n', '<leader>t', function()
--   vim.cmd 'cd %:p:h'
--   vim.cmd 'terminal'
--   vim.cmd 'startinsert'
-- end)

-- INFO: Enable keymaps to interact with tmux
vim.keymap.set("n", "<C-h>", ":wincmd h<CR>")
vim.keymap.set("n", "<C-j>", ":wincmd j<CR>")
vim.keymap.set("n", "<C-k>", ":wincmd k<CR>")
vim.keymap.set("n", "<C-l>", ":wincmd l<CR>")

-- INFO: Set swenv keymap to select venv
-- vim.keymap.set("n", "<leader>vs", function()
--   require("swenv.api").pick_venv()
-- end, { desc = "[Venv] [s]elect" })

-- INFO: plenary commands
vim.keymap.set("n", "]t", function()
  require("todo-comments").jump_next()
end, { desc = "Next todo comment" })

-- INFO: set venv-selector keymap
vim.keymap.set("n", "<leader>vs", "<cmd>VenvSelect<CR>", { desc = "[V]env [S]elector" })

-- INFO: mini.map keymaps
vim.keymap.set("n", "<Leader>mc", function()
  require("mini.map").close()
end, { desc = "[C]lose Minimap" })
vim.keymap.set("n", "<Leader>mf", function()
  require("mini.map").toggle_focus()
end, { desc = "Toggle [F]ocus Minimap" })
vim.keymap.set("n", "<Leader>mo", function()
  require("mini.map").open()
end, { desc = "[O]pen Minimap" })
vim.keymap.set("n", "<Leader>mr", function()
  require("mini.map").refresh()
end, { desc = "[R]efresh Minimap" })
vim.keymap.set("n", "<Leader>ms", function()
  require("mini.map").toggle_side()
end, { desc = "Toggle [S]ide Minimap" })
vim.keymap.set("n", "<Leader>mt", function()
  require("mini.map").toggle()
end, { desc = "[T]oggle Minimap" })

vim.keymap.set("n", "[t", function()
  require("todo-comments").jump_prev()
end, { desc = "Previous todo comment" })

-- function to toggle relative/nonrelative line numbers
NumberToggle = function()
  if vim.o.number == false then
    --set number
    vim.o.number = true
  else
    vim.o.relativenumber = true
  end
end

local function ToggleNumber()
  if vim.o.number == false then
    vim.o.number = true
  else
    vim.o.relativenumber = true
  end
end

vim.keymap.set("n", "C-b", function()
  ToggleNumber()
end)
-- vim: ts=2 sts=2 sw=2 et
