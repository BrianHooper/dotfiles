#!/bin/bash

# Easier navigation:
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias -- -="cd -"

# Clear the terminal
alias cls='clear'

# Set as executable
alias chmox='chmod -x'

# Change directory to flash drive
alias fd="cd /media/brian/Hoopflash"

# Shortcut for cd ~/Downloads && ls
alias ds="cd ~/Downloads && ls -1"

# Edit this file
alias vA='nano ~/.bash_aliases && source ~/.bashrc'

# Install a program using apt
alias aptg='sudo apt-get install'

# Search for a program using apt
alias apts='sudo apt-cache search'

# Run last command as root
alias fuck='sudo $(history -p \!\!)'

# Ping google.com by ip address
alias testnet="ping -c 1 -i 15 172.217.8.174"

# Git notes
alias gitnotes="cat /home/brian/admin/notes/gitnotes"

alias lcc="/media/brian/veracrypt/lc.sh && exit"

# Screen profiles
alias scrtv="/home/brian/.screenlayout/tv.sh"
alias notv="/home/brian/.screenlayout/default.sh"

# Number of days until graduation
alias days="echo $(expr '(' $(date -d 2019/06/08 +%s) - $(date +%s) + 86399 ')' / 86400)"

# Switch to school folder
alias school="cd /home/brian/Documents/code/cwu_assignments"

# Copy with progress
alias copy="rsync -ah --progress"

# List ls
alias lll="ls -1"

# Extract archives - use: extract <file>
# Based on http://dotfiles.org/~pseup/.bashrc
extract() {
    if [[ -z "$1" ]]; then
        # display usage if no parameters given
        echo "Usage: extract <archive file>"
        return 1
    else
        for n in "$@"; do
            if [[ -f "$n" ]]; then
                case "${n%,}" in
                    *.tar.bz2|*.tar.gz|*.tar.xz|*.tbz2|*.tgz|*.txz|*.tar)
                                tar xvf "$n"       ;;
                    *.lzma)     unlzma ./"$n"      ;;
                    *.bz2)      bunzip2 ./"$n"     ;;
                    *.rar)      unrar x -ad ./"$n" ;;
                    *.gz)       gunzip ./"$n"      ;;
                    *.zip)      unzip ./"$n"       ;;
                    *.z)        uncompress ./"$n"  ;;
                    *.7z|*.arj|*.cab|*.chm|*.deb|*.dmg|*.iso|*.lzh|*.msi|*.rpm|*.udf|*.wim|*.xar)
                                7z x ./"$n"        ;;
                    *.xz)       unxz ./"$n"        ;;
                    *.exe)      cabextract ./"$n"  ;;
                    *)
                echo "extract: '$n' - unknown archive format"
                return 1
                esac
            else
                echo "'$n' - file does not exist"
                return 1
            fi
        done
    fi
}

# What is my external ip
alias myip="curl https://api.ipify.org"

# Show file size
alias fs="stat -c \"%s bytes\""

# preview csv files. source: http://stackoverflow.com/questions/1875305/command-line-csv-viewer
function csvpreview(){
      sed 's/,,/, ,/g;s/,,/, ,/g' "$@" | column -s, -t | less -#2 -N -S
}

# Create a new directory and enter it
function md() {
	mkdir -p "$@" && cd "$@"
}

# find shorthand
function f() {
	find . -name "$1" 2>&1 | grep -v 'Permission denied'
}

# Run in background
function run() {
    nohup $1 > /dev/null 2>&1&
}

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Lists each directory in the path
alias path="echo "$PATH" | tr \":\" \"\n\""
