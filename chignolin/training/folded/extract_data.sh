#!/bin/bash

cut -d' ' -f223-267 COLVAR > contacts_folded

cut -d' ' -f7-216 COLVAR > distances_folded
