#!/bin/bash
sshpass -p $(cat Level_$1/pass) ssh bandit$1@bandit.labs.overthewire.org -p 2220

