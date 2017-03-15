#!/bin/bash
#===============================================================================
#
#          FILE:  xr.sh
# 
#         USAGE:  ./xr.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:   (), 
#       COMPANY:  
#       VERSION:  1.0
#       CREATED:  04/30/2012 08:48:16 AM EEST
#      REVISION:  ---
#===============================================================================
#senas monikas
#xrandr --output HDMI2 --mode 1920x1200 --pos 0x0 --rotate normal --primary --output HDMI1 --mode 1680x1050 --left-of HDMI2
#naujas monikas
xrandr --output HDMI-0 --mode 1920x1200 --pos 0x0 --rotate normal --primary --output DVI-0 --mode 1920x1200 --left-of HDMI-0
#naujas + persuktas
#xrandr --output HDMI2 --mode 1920x1200 --pos 0x0 --rotate left --primary --output HDMI1 --mode 1920x1200 --left-of HDMI2
