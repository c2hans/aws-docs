---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/appendix-a-proxy-configuration-example.html
---

# Appendix A – Proxy configuration example
<a name="appendix-a-proxy-configuration-example"></a>

 The following configuration is for a Squid-based proxy running in us-east-1 with peers in us-west-2 and eu-west-1. It denies all other traffic for the `amazonaws.com` domain, but allows all other domains to be forwarded normally. This configuration will need to be kept up to date with global AWS services that do not use a Region name in their domain name.

```
    cache_effective_user squid
prefer_direct off
nonhierarchical_direct off

## Define acls for local networks that are forwarding here
acl rfc_1918 src 10.0.0.0/8        # RFC1918 possible internal network
acl rfc_1918 src 172.16.0.0/12     # RFC1918 possible internal network
acl rfc_1918 src 192.168.0.0/16    # RFC1918 possible internal network
acl localnet src fc00::/7          # RFC 4193 local private network range
acl localnet src fe80::/10         # RFC 4291 link-local (directly plugged) machines
acl localnet src 127.0.0.1         # localhost loopback

## Additional ACLs
acl ssl_ports port 443             # ssl
acl safe_ports port 80             # http
acl safe_ports port 21             # ftp
acl safe_ports port 443            # https
acl safe_ports port 70             # gopher
acl safe_ports port 210            # wais
acl safe_ports port 1025-65535     # unregistered ports
acl safe_ports port 280            # http-mgmt
acl safe_ports port 488            # gss-http
acl safe_ports port 591            # filemaker
acl safe_ports port 777            # multiling http
acl CONNECT method CONNECT

## Define acls for amazonaws.com
acl aws_domain dstdomain .amazonaws.com
acl us_east_1 dstdomain .s3.amazonaws.com
acl us_east_1 dstdomain .sts.amazonaws.com
acl us_east_1 dstdomain .cloudfront.amazonaws.com
acl us_west_2 dstdomain .globalaccelerator.amazonaws.com
acl us_east_1 dstdomain .iam.amazonaws.com
acl us_east_1 dstdomain .route53.amazonaws.com
acl us_east_1 dstdomain .queue.amazonaws.com
acl us_east_1 dstdomain .sdb.amazonaws.com
acl us_east_1 dstdomain .waf.amazonaws.com
acl us_east_1 dstdomain .us-east-1.amazonaws.com
acl us_east_2 dstdomain .us-east-2.amazonaws.com
acl us_west_2 dstdomain .us-west-2.amazonaws.com
acl eu_west_1 dstdomain .eu-west-1.amazonaws.com
acl us_east_1_alt dstdom_regex \.us-east-1\..*?\.amazonaws.com
acl us_east_2_alt dstdom_regex \.us-east-2\..*?\.amazonaws.com
acl us_west_2_alt dstdom_regex \.us-west-2\..*?\.amazonaws.com
acl eu_west_1_alt dstdom_regex \.eu-west-1\..*?\.amazonaws.com

## Deny access to anything other than SSL
http_access deny !safe_ports
http_access deny CONNECT !ssl_ports

## Now specify the cache peer for each Region
never_direct allow us_east_2
never_direct allow us_east_2_alt
never_direct allow us_west_2
never_direct allow us_west_2_alt
never_direct allow eu_west_1
never_direct allow eu_west_1_alt
cache_peer us-east-2.proxy.local parent 3128 0 no-query proxy-only name=cmh
cache_peer_access cmh allow us_east_2
cache_peer_access cmh allow us_east_2_alt
cache_peer us-west-2.proxy.local parent 3128 0 no-query proxy-only name=pdx
cache_peer_access pdx allow us_west_2
cache_peer_access pdx allow us_west_2_alt
cache_peer eu-west-1.proxy.local parent 3128 0 no-query proxy-only name=dub
cache_peer_access dub allow eu_west_1
cache_peer_access dub allow eu_west_1_alt

# Only allow cachemgr access from localhost
http_access allow localhost manager
http_access deny manager

## Explicitly allow approved AWS Regions so we can block
## all other Regions using .amazonaws.com below
http_access allow rfc_1918 us_east_1
http_access allow rfc_1918 us_east_2
http_access allow rfc_1918 us_west_2
http_access allow rfc_1918 eu_west_1
http_access allow rfc_1918 us_east_1_alt
http_access allow rfc_1918 us_east_2_alt
http_access allow rfc_1918 us_west_2_alt
http_access allow rfc_1918 eu_west_1_alt

## Block all other AWS Regions
http_access deny aws_domain

## Allow all other access from local networks
http_access allow rfc_1918
http_access allow localnet

## Finally deny all other access to the proxy
http_access deny all

## Listen on 3128
http_port 3128

## Logging
access_log stdio:/var/log/squid/access.log
strip_query_terms off
logfile_rotate 1

## Turn off caching
cache deny all

## Enable the X-Forwarded-For header
forwarded_for on

## Suppress sending squid version information
httpd_suppress_version_string on

## How long to wait when shutting down squid
shutdown_lifetime 30 seconds

## Hostname
visible_hostname aws_proxy

## Prefer ipv4 over v6
dns_v4_first on
```
