WEBMIN_FW_TCP_INCOMING = 22 80 443 5222 5223 5269 12320 12321 12322
WEBMIN_FW_TCP_INCOMING_REJECT = 4369

COMMON_CONF = postfix-local apache-credit apache-vhost

CREDIT_ANCHORTEXT = ejabberd Appliance
CREDIT_LOCATION = ~ "^/(?!(room))"

include $(FAB_PATH)/common/mk/turnkey.mk
