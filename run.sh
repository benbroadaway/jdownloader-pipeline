#!/usr/bin/env bash

if [ -z "${SERVER_URL}" ]; then
  echo "SERVER_URL is not set!"
fi

tmpDir=./target


# remove temporary directory and re-create it
rm -rf ${tmpDir} && mkdir ${tmpDir}

# copy project files to temporary directory
cp -r concord.yml inventories playbook ${tmpDir}

cd ${tmpDir} && zip -r payload.zip ./* 2>&1>/dev/null && cd .. 

curl -n \
  -F archive=@target/payload.zip \
  -F entryPoint=default \
  ${SERVER_URL}/api/v1/process
