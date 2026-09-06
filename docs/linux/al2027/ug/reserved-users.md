---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/reserved-users.html
---

# List of AL2027 reserved users
<a name="reserved-users"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The following tables list the user names that AL2027 packages reserve, as of the AL2027 public preview. A numeric UID is listed when the user account is created with a static UID. A user account marked *dynamic* is allocated a UID from the system range (201-999) when the owning package is installed, so the number varies between instances. The list grows as packages are added to AL2027.

**Listed by UID**

| User name | UID |
| --- | --- |
| root | 0 |
| bin | 1 |
| daemon | 2 |
| adm | 3 |
| lp | 4 |
| sync | 5 |
| shutdown | 6 |
| halt | 7 |
| mail | 8 |
| operator | 11 |
| games | 12 |
| ftp | 14 |
| squid | 23 |
| named | 25 |
| postgres | 26 |
| mysql | 27 |
| rpcuser | 29 |
| rpc | 32 |
| gdm | 42 |
| mailnull | 47 |
| apache | 48 |
| smmsp | 51 |
| tomcat | 53 |
| ldap | 55 |
| tss | 59 |
| nslcd | 65 |
| avahi | 70 |
| tcpdump | 72 |
| sshd | 74 |
| radvd | 75 |
| dbus | 81 |
| postfix | 89 |
| radiusd | 95 |
| dovecot | 97 |
| polkitd | 114 |
| stap-server | 155 |
| stapunpriv | 159 |
| avahi-autoipd | 170 |
| sanlock | 179 |
| haproxy | 188 |
| hacluster | 189 |
| systemd-network | 192 |
| systemd-resolve | 193 |
| ec2-user | 1000 |
| nobody | 65534 |
| chrony | dynamic |
| clamilt | dynamic |
| clamscan | dynamic |
| clamupdate | dynamic |
| colord | dynamic |
| debuginfod | dynamic |
| dnsmasq | dynamic |
| dovenull | dynamic |
| ec2-instance-connect | dynamic |
| flatpak | dynamic |
| geoclue | dynamic |
| gnome-remote-desktop | dynamic |
| libstoragemgmt | dynamic |
| memcached | dynamic |
| munge | dynamic |
| networkflowmonitor | dynamic |
| nfsnobody | dynamic |
| nginx | dynamic |
| ods | dynamic |
| opendkim | dynamic |
| openvpn | dynamic |
| pcscd | dynamic |
| pesign | dynamic |
| pipewire | dynamic |
| rtkit | dynamic |
| saslauth | dynamic |
| sphinx | dynamic |
| sssd | dynamic |
| stapdev | dynamic |
| stapsys | dynamic |
| stapusr | dynamic |
| systemd-coredump | dynamic |
| systemd-journal-remote | dynamic |
| systemd-oom | dynamic |
| systemd-timesync | dynamic |
| unbound | dynamic |
| uuidd | dynamic |
| valkey | dynamic |
| wsdd | dynamic |

**Listed by name**

| User name | UID |
| --- | --- |
| adm | 3 |
| apache | 48 |
| avahi | 70 |
| avahi-autoipd | 170 |
| bin | 1 |
| chrony | dynamic |
| clamilt | dynamic |
| clamscan | dynamic |
| clamupdate | dynamic |
| colord | dynamic |
| daemon | 2 |
| dbus | 81 |
| debuginfod | dynamic |
| dnsmasq | dynamic |
| dovecot | 97 |
| dovenull | dynamic |
| ec2-instance-connect | dynamic |
| ec2-user | 1000 |
| flatpak | dynamic |
| ftp | 14 |
| games | 12 |
| gdm | 42 |
| geoclue | dynamic |
| gnome-remote-desktop | dynamic |
| hacluster | 189 |
| halt | 7 |
| haproxy | 188 |
| ldap | 55 |
| libstoragemgmt | dynamic |
| lp | 4 |
| mail | 8 |
| mailnull | 47 |
| memcached | dynamic |
| munge | dynamic |
| mysql | 27 |
| named | 25 |
| networkflowmonitor | dynamic |
| nfsnobody | dynamic |
| nginx | dynamic |
| nobody | 65534 |
| nslcd | 65 |
| ods | dynamic |
| opendkim | dynamic |
| openvpn | dynamic |
| operator | 11 |
| pcscd | dynamic |
| pesign | dynamic |
| pipewire | dynamic |
| polkitd | 114 |
| postfix | 89 |
| postgres | 26 |
| radiusd | 95 |
| radvd | 75 |
| root | 0 |
| rpc | 32 |
| rpcuser | 29 |
| rtkit | dynamic |
| sanlock | 179 |
| saslauth | dynamic |
| shutdown | 6 |
| smmsp | 51 |
| sphinx | dynamic |
| squid | 23 |
| sshd | 74 |
| sssd | dynamic |
| stap-server | 155 |
| stapdev | dynamic |
| stapsys | dynamic |
| stapunpriv | 159 |
| stapusr | dynamic |
| sync | 5 |
| systemd-coredump | dynamic |
| systemd-journal-remote | dynamic |
| systemd-network | 192 |
| systemd-oom | dynamic |
| systemd-resolve | 193 |
| systemd-timesync | dynamic |
| tcpdump | 72 |
| tomcat | 53 |
| tss | 59 |
| unbound | dynamic |
| uuidd | dynamic |
| valkey | dynamic |
| wsdd | dynamic |
