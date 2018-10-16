#!/bin/bash
#
# Copyright IBM Corp All Rights Reserved
#
# SPDX-License-Identifier: Apache-2.0
#
# Exit on first error, print all commands.
set -ev

docker-compose -f docker-compose.yml down

docker-compose -f docker-compose.yml up -d core.facecheckin.com report.facecheckin.com mongo.facecheckin.com
