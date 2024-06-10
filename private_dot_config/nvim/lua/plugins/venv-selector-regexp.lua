return {
  "linux-cultist/venv-selector.nvim",
  dependencies = { "neovim/nvim-lspconfig", "nvim-telescope/telescope.nvim", "mfussenegger/nvim-dap-python" },
  lazy = false,
  branch = "regexp", -- This is the regexp branch, use this until its merged with the main branch later
  config = function()
    require("venv-selector").setup {
      settings = {
        search = {
          my_venvs = {
            command = "fd 'python$' ~/venvs", -- Sample command, need to be changed for your own venvs
          },
        },
      },
    }
  end,
  keys = {
    { "n", "<leader>vs", "<cmd>VenvSelect<cr>" },
  },
}
