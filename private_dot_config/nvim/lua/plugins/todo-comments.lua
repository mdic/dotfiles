-- Highlight todo, notes, etc in comments
return {
  {
    "folke/todo-comments.nvim",
    event = "VimEnter",
    dependencies = { "nvim-lua/plenary.nvim" },
    opts = {
      signs = true,
      vim.keymap.set("n", "<leader>sc", ":TodoTelescope<CR>", { desc = "[S]earch Todo[C]omments w/ Telescope" }),
    },
  },
}
-- TODO:
-- vim: ts=2 sts=2 sw=2 et
