" Automatically detect file type
filetype plugin on

" Autoindent when returning on a line
set autoindent

" Size of autoindent
set tabstop=2

" Autoindents inside curly braces with two spaces
set shiftwidth=2

" Turn \t into spaces
set expandtab

" Autoinserts asterisks inside block comments
set formatoptions+=r

" Adds line numbers on the left hand side
set number

" Allows click to line
set mouse=a

" Sets highlight on search
set hlsearch

" Start searching while typing search string
set incsearch

" Set hidden buffers
set hidden

" Colors code keywords
syntax on
colorscheme default

" Create keybind to highlight lines over 80 characters long
" See https://bit.ly/3TsiRTE for source
let mapleader=","
nnoremap <Leader>H :call<SID>LongLineHLToggle()<cr>
hi OverLength ctermbg=none cterm=none
match OverLength /\%>80v/
fun! s:LongLineHLToggle()
 if !exists('w:longlinehl')
  let w:longlinehl = matchadd('ErrorMsg', '.\%>80v', 0)
  echo "Long lines highlighted"
 else
  call matchdelete(w:longlinehl)
  unl w:longlinehl
  echo "Long lines unhighlighted"
 endif
endfunction

autocmd FileType python setlocal ts=2 | setlocal expandtab
