#!/bin/bash
gpio write $1 1
echo -n "Pin" $1 "set to ON. "
date


