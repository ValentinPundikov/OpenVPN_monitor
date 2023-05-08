#!/bin/bash
# This is a comment
cat /var/log/openvpn.log | grep -P 'primary virtual IP|client-instance exiting'