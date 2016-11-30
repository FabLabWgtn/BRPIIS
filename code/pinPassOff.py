#!/bin/bash
gpio write $1 0
echo -n "Pin" $1 "set to OFF. "
date


