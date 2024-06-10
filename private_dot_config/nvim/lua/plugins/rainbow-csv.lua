return {
  "mechatroner/rainbow_csv",
  config = function()
    vim.keymap.set("n", "<M-Up>", ":RainbowCellGoUp<CR>", { desc = "RainbowCSV Move up" })
    vim.keymap.set("n", "<M-Down>", ":RainbowCellGoDown<CR>", { desc = "RainbowCSV Move up" })
    vim.keymap.set("n", "<M-Left>", ":RainbowCellGoLeft<CR>", { desc = "RainbowCSV Move up" })
    vim.keymap.set("n", "<M-Right>", ":RainbowCellGoRight<CR>", { desc = "RainbowCSV Move up" })
    vim.keymap.set("n", "<M-l>", ":CSVLint<CR>", { desc = "CSVLint" })
    vim.keymap.set("n", "<M-a>", ":RainbowAlign<CR>", { desc = "RainbowCSV [A]lign" })
    vim.keymap.set("n", "<M-s>", ":RainbowShrink<CR>", { desc = "RainbowCSV [S]hrink" })
  end,
}
