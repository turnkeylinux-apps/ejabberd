#!/bin/bash -e
# Configure ejabberd and speeqe

usage() {
    echo "usage: $0 XMPP_DOMAIN ADMIN_PASS"
    exit 1
}

if [ $# -ne "2" ]; then
    usage
fi

XMPP_DOMAIN=$1
ADMIN_PASS=$2

ROBOT_PASS=$(mcookie)

# enumerate current domain
RE_XMPP_DOMAIN=$(grep ^{host_config /etc/ejabberd/ejabberd.cfg | cut -d " " -f 2 | sed "s|\"||g" | sed "s|,||")

# get service status so we can return to the original status later
EJABBERD_ORIG_STATE=$(ejabberdctl status >/dev/null; echo $?)

# completely stop ejabberd and other related services
stop_ejabberd() {
    /etc/init.d/ejabberd stop || true
    killall epmd || true
    killall beam || true
}

stop_ejabberd

# clean out mnesia database
rm -f /var/lib/ejabberd/*

# set ejabberd required permissions
chown -R root:ejabberd /etc/ejabberd
chmod 750 /etc/ejabberd
chmod 640 /etc/ejabberd/*

# update ejabberd and speeqe configuration
sed -i "s/$RE_XMPP_DOMAIN/$XMPP_DOMAIN/" /etc/ejabberd/ejabberd.cfg
sed -i "s/$RE_XMPP_DOMAIN/$XMPP_DOMAIN/" /etc/speeqe/settings.py
sed -i "s/$RE_XMPP_DOMAIN/$XMPP_DOMAIN/" /etc/speeqe/local_settings.js

sed -i "s/XMPP_PASS = \(.*\)/XMPP_PASS = \'$ROBOT_PASS\'/" /etc/speeqe/settings.py

# start ejabberd (wait a little for the service to come up), create ejabberd users
/etc/init.d/ejabberd start
sleep 4
ejabberdctl register admin $XMPP_DOMAIN $ADMIN_PASS
ejabberdctl register robot $XMPP_DOMAIN $ROBOT_PASS

# return ejabberd to it's original state
[ "$EJABBERD_ORIG_STATE" == "0" ] || stop_ejabberd

exit 0

