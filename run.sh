#!/bin/bash

ssh 192.168.2.4 rm ~/mediagoblin/podcast/* -r
scp -r ./podcast/* 192.168.2.4:~/mediagoblin/podcast
ssh 192.168.2.4 gmg dbupdate
