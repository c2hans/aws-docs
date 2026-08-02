---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html
---

# IP address and port requirements for WorkSpaces Personal
<a name="workspaces-port-requirements"></a>

To connect to your WorkSpaces, the network that your WorkSpaces clients are connected to must have certain ports open to the IP address ranges for the various AWS services (grouped in subsets). These address ranges vary by AWS Region. These same ports must also be open on any firewall running on the client. For more information about the AWS IP address ranges for different Regions, see [AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *Amazon Web Services General Reference*.

For additional architecture diagrams, see [Best Practices for Deploying Amazon WorkSpaces](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/best-practices-deploying-amazon-workspaces.html).

## Ports for client applications
<a name="client-application-ports"></a>

The WorkSpaces client application requires outbound access on the following ports:

Port 53 (UDP)
This port is used to access DNS servers. It must be open to your DNS server IP addresses so that the client can resolve public domain names. This port requirement is optional if you are not using DNS servers for domain name resolution.

Port 443 (UDP and TCP)
This port is used for client application updates, registration, and authentication. The desktop client applications support the use of a proxy server for port 443 (HTTPS) traffic. To enable the use of a proxy server, open the client application, choose **Advanced Settings**, select **Use Proxy Server**, specify the address and port of the proxy server, and choose **Save**.
This port must be open to the following IP address ranges:
+ The `AMAZON` subset in the `GLOBAL` Region.
+ The `AMAZON` subset in the Region that the WorkSpace is in.
+ The `AMAZON` subset in the `us-east-1` Region.
+ The `AMAZON` subset in the `us-west-2` Region.
+ The `S3` subset in the `us-west-2` Region.

Port 4172 (UDP and TCP)
This port is used for streaming the WorkSpace desktop and health checks for PCoIP WorkSpaces. This port must be open to the PCoIP Gateway and to the health check servers in the Region that the WorkSpace is in. For more information, see [Health check servers](#health_check) and [PCoIP gateway servers](#gateway_IP).
For PCoIP WorkSpaces, the desktop client applications do not support the use of a proxy server nor TLS decryption and inspection for port 4172 traffic in UDP (for desktop traffic). They require a direct connection to ports 4172.

Ports 50002 and 55002 (UDP)
The PCoIP client initiates outbound UDP communication on ports 50002 and 55002 for streaming. Ensure that the client's local firewall or network allows outbound UDP traffic on these ports. If outbound UDP on ports 50002 and 55002 is blocked on the client side, users may experience a black screen when connecting to their WorkSpaces.
If your firewall uses stateful filtering, return traffic on ephemeral ports 50002 and 55002 is automatically permitted. If your firewall uses stateless filtering, you must open ephemeral ports 49152–65535 to allow return communication.

Port 4195 (UDP and TCP)
This port is used for streaming the WorkSpace desktop and health checks for DCV WorkSpaces. This port must be open to the DCV Gateway IP address ranges and the health check servers in the Region that the WorkSpace is in. For more information, see [Health check servers](#health_check) and [DCV gateway servers](#gateway_WSP).
For DCV WorkSpaces, the WorkSpaces Windows client application (version 5.1 and above) and macOS client application (version 5.4 and above) support the use of HTTP proxy servers for port 4195 TCP traffic, but the use of a proxy is not recommended. TLS decryption and inspection are not supported. For more information, see **Configure device proxy server settings for internet access** for [ Windows WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_device_proxy), [ Amazon Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_device_proxy_linux), and [ Ubuntu WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_device_proxy_ubuntu).

**Note**
If your firewall uses stateful filtering, ephemeral ports (also known as dynamic ports) are automatically opened to allow return communication. If your firewall uses stateless filtering, you must open ephemeral ports explicitly to allow return communication. The required ephemeral port range that you must open will vary depending on your configuration.
Proxy server function is not supported for UDP traffic. If you choose to use a proxy server, the API calls that the client application makes to the Amazon WorkSpaces services are also proxied. Both API calls and desktop traffic should pass through the same proxy server.
The WorkSpaces client application first attempts to stream using UDP (QUIC) for optimal performance. If the client network only allows TCP, then TCP will be used. The WorkSpaces web client will connect over TCP port 4195 or 443. If port 4195 is blocked, the client will only attempt to connect to over port 443.

## Ports for Web Access
<a name="web-access-ports"></a>

WorkSpaces Web Access requires outbound access for the following ports:

Port 53 (UDP)
This port is used to access DNS servers. It must be open to your DNS server IP addresses so that the client can resolve public domain names. This port requirement is optional if you are not using DNS servers for domain name resolution.

Port 80 (UDP and TCP)
This port is used for initial connections to `https://clients.amazonworkspaces.com`, which then switch to HTTPS. It must be open to all IP address ranges in the `EC2` subset in the Region that the WorkSpace is in.

Port 443 (UDP and TCP)
This port is used for registration and authentication using HTTPS. It must be open to all IP address ranges in the `EC2` subset in the Region that the WorkSpace is in.

Port 4195 (UDP and TCP)
For WorkSpaces that are configured for DCV, this port is used for streaming the WorkSpaces desktop traffic. This port must be open to the DCV Gateway IP address ranges. For more information, see [DCV gateway servers](#gateway_WSP).
DCV web access supports the use of a proxy server for port 4195 TCP traffic, but it’s not recommended. For more information, see **Configure device proxy server settings for internet access** for [ Windows WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_device_proxy), [ Amazon Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_device_proxy_linux), or [ Ubuntu WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_device_proxy_ubuntu).

**Note**
If your firewall uses stateful filtering, ephemeral ports (also known as dynamic ports) are automatically opened to allow return communication. If your firewall uses stateless filtering, you must open ephemeral ports explicitly to allow return communication. The required ephemeral port range that you must open varies depending on your configuration.
The WorkSpaces client application first attempts to stream using UDP (QUIC) for optimal performance. If the client network only allows TCP, then TCP will be used. The WorkSpaces web client will connect over TCP port 4195 or 443. If port 4195 is blocked, the client will only attempt to connect to over port 443.

Typically, the web browser randomly selects a source port in the high range to use for streaming traffic. WorkSpaces Web Access does not have control over the port that the browser selects. You must ensure that return traffic to this port is allowed.

## Domains and IP addresses to add to your allow list
<a name="allowlisted_ports"></a>

For the WorkSpaces client application to be able to access the WorkSpaces service, you must add the following domains and IP addresses to the allow list on the network from which the client is trying to access the service.

**Domains and IP addresses to add to your allow list**

| Category | Domain or IP address |
| --- | --- |
| CAPTCHA |  https://opfcaptcha-prod.s3.amazonaws.com/  |
| Client Auto-update |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  |  https://fls-na.amazon.com/  |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| User Login Pages | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)https://{{directory\_id}}.awsapps.com/**directory id** is the customer's domain.<br />In the AWS GovCloud (US-West) and AWS GovCloud (US-East) Regions:<br />https://login.us-gov-home.awsapps.com/directory/{{directory id}}/ **directory id** is the customer's domain. |
| WS Broker |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| WorkSpaces API Endpoints |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| WorkSpaces Endpoints for SAML Single Sign-On (SSO) | Domains:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

**Domains and IP addresses to add to your allow list for PCoIP**

| Category | Domain or IP address |
| --- | --- |
| PCoIP Session Gateway (PSG) | [PCoIP gateway servers](#gateway_IP) |
| Session Broker (PCM) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Web Access TURN Servers for PCoIP |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |

**Domains and IP addresses to add to your allow list for DCV**

| Category | Domain or IP address |
| --- | --- |
| DCV Session Gateway (WSG) |  [DCV gateway servers](#gateway_WSP)  |
| Web Access TURN Servers for DCV |  [DCV gateway servers](#gateway_WSP)  |

## Health check servers
<a name="health_check"></a>

The WorkSpaces client applications perform health checks over ports 4172 and 4195. These checks validate whether TCP or UDP traffic streams from the WorkSpaces servers to the client applications. For these checks to finish successfully, your firewall policies must allow outbound traffic to the IP addresses of the following Regional health check servers.

| Region | Health check hostname | IP addresses |
| --- | --- | --- |
| US East (N. Virginia) | IPv4:<br />drp-iad.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.us-east-1.api.aws | IPv4:<br />3.209.215.252<br />3.212.50.30<br />3.225.55.35<br />3.226.24.234<br />34.200.29.95<br />52.200.219.150<br />IPv6:<br />2600:1f18:74e9:4400::/56 |
| US West (Oregon) | IPv4:<br />drp-pdx.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.us-west-2.api.aws | IPv4:<br />34.217.248.177<br />52.34.160.80<br />54.68.150.54<br />54.185.4.125<br />54.188.171.18<br />54.244.158.140<br />IPv6:<br />2600:1f14:278e:5700::/56 |
| Asia Pacific (Mumbai) | IPv4:<br />drp-bom.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.ap-south-1.api.aws | IPv4:<br />13.127.57.82<br />13.234.250.73<br />IPv6:<br />2406:da1a:502:b800::/56 |
| Asia Pacific (Seoul) | IPv4:<br />drp-icn.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.ap-northeast-2.api.aws | IPv4:<br />13.124.44.166<br />13.124.203.105<br />52.78.44.253<br />52.79.54.102<br />IPv6:<br />2406:da12:c8c:4900::/56 |
| Asia Pacific (Singapore) | IPv4:<br />drp-sin.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.ap-southeast-1.api.aws | IPv4:<br />3.0.212.144<br />18.138.99.116<br />18.140.252.123<br />52.74.175.118<br />IPv6:<br />2406:da18:991:4a00::/56 |
| Asia Pacific (Sydney) | IPv4:<br />drp-syd.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.ap-southeast-2.api.aws | IPv4:<br />3.24.11.127<br />13.237.232.125<br />IPv6:<br />2406:da1c:9b5:9d00::/56 |
| Asia Pacific (Tokyo) | IPv4:<br />drp-nrt.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.ap-northeast-1.api.aws | IPv4:<br />18.178.102.247<br />54.64.174.128<br />IPv6:<br />2406:da14:785:5300::/56 |
| Canada (Central) | IPv4:<br />drp-yul.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.ca-central-1.api.aws | IPv4:<br />52.60.69.16<br />52.60.80.237<br />52.60.173.117<br />52.60.201.0<br />IPv6:<br />2600:1f11:759:d900::/56 |
| Europe (Frankfurt) | IPv4:<br />drp-fra.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.eu-central-1.api.aws | IPv4:<br />52.59.191.224<br />52.59.191.225<br />52.59.191.226<br />52.59.191.227<br />IPv6:<br />2a05:d014:b5c:500::/56 |
| Europe (Ireland) | IPv4:<br />drp-dub.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.eu-west-1.api.aws | IPv4:<br />18.200.177.86<br />52.48.86.38<br />54.76.137.224<br />IPv6:<br />2a05:d018:10ca:f400::/56 |
| Europe (London) | IPv4:<br />drp-lhr.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.eu-west-2.api.aws | IPv4:<br />35.176.62.54<br />35.177.255.44<br />52.56.46.102<br />52.56.111.36<br />IPv6:<br />2a05:d01c:263:f400::/56 |
| Europe (Paris) | IPv4:<br />drp-cdg.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.eu-west-3.api.aws | IPv4:<br />51.17.52.90<br />51.17.109.231<br />51.16.190.43<br />IPv6:<br />2a05:d012:16:8600::/56 |
| South America (São Paulo) | IPv4:<br />drp-gru.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.sa-east-1.api.aws | IPv4:<br />18.231.0.105<br />52.67.55.29<br />54.233.156.245<br />54.233.216.234<br />IPv6:<br />2600:1f1e:bbf:fa00::/56 |
| Africa (Cape Town) | IPv4:<br />drp-cpt.amazonworkspaces.com/<br />IPv6:<br />drp-workspaces.af-south-1.api.aws | IPv4:<br />13.244.128.155<br />13.245.205.255<br />13.245.216.116<br />IPv6:<br />2406:da11:685:2400::/56 |
| Israel (Tel Aviv) | IPv4:<br />drp-tlv.amazonworkspaces.com/<br />IPv6:<br />drp-workspaces.il-central-1.api.aws | IPv4:<br />51.17.52.90<br />51.17.109.231<br />51.16.190.43<br />IPv6:<br />2a05:d025:c78:fc00::/56 |
| AWS GovCloud (US-West) | IPv4:<br />drp-pdt.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.us-gov-west-1.api.aws | IPv4:<br />52.61.60.65<br />52.61.65.14<br />52.61.88.170<br />52.61.137.87<br />52.61.155.110<br />52.222.20.88<br />IPv6:<br />2600:1f12:28f:af00::/56 |
| AWS GovCloud (US-East) | IPv4:<br />drp-osu.amazonworkspaces.com<br />IPv6:<br />drp-workspaces.us-gov-east-1.api.aws | IPv4:<br />18.253.251.70<br />18.254.0.118<br />IPv6:<br />2600:1f15:a45:3e00::/56 |

## PCoIP gateway servers
<a name="gateway_IP"></a>

WorkSpaces uses PCoIP to stream the desktop session to clients over port 4172. For its PCoIP gateway servers, WorkSpaces uses a small range of Amazon EC2 public IPv4 and IPv6 addresses. This enables you to set more finely grained firewall policies for devices that access WorkSpaces. Note that the WorkSpaces client prioritizes IPv6 connections when IPv6 is supported and gateways are reachable. If IPv6 is unavailable, it falls back to IPv4.

| Region | Region code | Public IP address range |
| --- | --- | --- |
| US East (N. Virginia) | us-east-1 | 3.217.228.0 - 3.217.231.255<br />3.235.112.0 - 3.235.119.255<br />52.23.61.0 - 52.23.62.255<br />2600:1f32:8000::/39  |
| US West (Oregon) | us-west-2 | 35.80.88.0 - 35.80.95.255<br />44.234.54.0 - 44.234.55.255<br />54.244.46.0 - 54.244.47.255<br />2600:1f32:4000::/39  |
| Asia Pacific (Mumbai) | ap-south-1 | 13.126.243.0 - 13.126.243.255<br />2406:da32:a000::/40 |
| Asia Pacific (Seoul) | ap-northeast-2 | 3.34.37.0 - 3.34.37.255<br />3.34.38.0 - 3.34.39.255<br />13.124.247.0 - 13.124.247.255<br />2406:da32:2000::/40 |
| Asia Pacific (Singapore) | ap-southeast-1 | 18.141.152.0 - 18.141.152.255<br />18.141.154.0 - 18.141.155.255<br />52.76.127.0 - 52.76.127.255<br />2406:da32:8000::/40 |
| Asia Pacific (Sydney) | ap-southeast-2 | 3.25.43.0 - 3.25.43.255<br />3.25.44.0 - 3.25.45.255<br />54.153.254.0 - 54.153.254.255<br />2406:da32:c000::/40 |
| Asia Pacific (Tokyo) | ap-northeast-1 | 18.180.178.0 - 18.180.178.255<br />18.180.180.0 - 18.180.181.255<br />54.250.251.0 - 54.250.251.255<br />2406:da32:4000::/40 |
| Canada (Central) | ca-central-1 | 15.223.100.0 - 15.223.100.255<br />15.223.102.0 - 15.223.103.255<br />35.183.255.0 - 35.183.255.255<br />2600:1f32:1000::/40 |
| Europe (Frankfurt) | eu-central-1 | 18.156.52.0 - 18.156.52.255<br />18.156.54.0 - 18.156.55.255<br />52.59.127.0 - 52.59.127.255<br />2a05:d032:4000::/40 |
| Europe (Ireland) | eu-west-1 | 3.249.28.0 - 3.249.29.255<br />52.19.124.0 - 52.19.125.255<br />2a05:d032:8000::/40 |
| Europe (London) | eu-west-2 | 18.132.21.0 - 18.132.21.255<br />18.132.22.0 - 18.132.23.255<br />35.176.32.0 - 35.176.32.255<br />2a05:d032:c000::/40 |
| Europe (Paris) | eu-west-3 | 51.44.204.0-51.44.207.255 |
| South America (São Paulo) | sa-east-1 | 18.230.103.0 - 18.230.103.255<br />18.230.104.0 - 18.230.105.255<br />54.233.204.0 - 54.233.204.255<br />2600:1f32:e000::/40 |
| Africa (Cape Town) | af-south-1 | 13.246.120.0 - 13.246.123.255<br />2406:da32:1000::/40 |
| Israel (Tel Aviv) | il-central-1 |  51.17.28.0-51.17.31.255<br />2a05:d032:5000::/40 |
| AWS GovCloud (US-West) | us-gov-west-1 | 52.61.193.0 - 52.61.193.255<br />2600:1f32:2000::/40 |
| AWS GovCloud (US-East) | us-gov-east-1 | 18.254.140.0 - 18.254.143.255<br />2600:1f32:5000::/40 |

## DCV gateway servers
<a name="gateway_WSP"></a>

**Important**
Starting in June 2020, WorkSpaces streams the desktop session for DCV WorkSpaces to clients over port 4195 instead of port 4172. If you want to use DCV WorkSpaces, make sure that port 4195 is open to traffic.

**Note**
For non-BYOL WorkSpaces Pools, IP address ranges are not guaranteed. Instead, you must allowlist the DCV gateway domain names. For more information, see [ DCV gateway domain names](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#dns-wsp).

WorkSpaces uses a small range of Amazon EC2 public IPv4 and IPv6 addresses for its DCV gateway servers. This enables you to set more finely grained firewall policies for devices that access WorkSpaces. WorkSpaces use a separate range of public IPv4 addresses for the dedicated AWS Global Accelerator (AGA) endpoints. Make sure to configure your firewall policies to allowlist the IP ranges if you plan to enable AGA for your WorkSpaces. Note that the WorkSpaces client prioritizes IPv6 connections when IPv6 is supported and gateways are reachable. If IPv6 is unavailable, it falls back to IPv4.

If you use AGA \+ IPv6, you need to allowlist the IPv6 CIDR ranges from the `GLOBALACCELERATOR` ranges. See [Location and IP address ranges of Global Accelerator Edge servers](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-ip-ranges.html) in the *AWS Global Accelerator Developer Guide* for more information.

| Region | Region code | Public IP address range |
| --- | --- | --- |
| US East (N. Virginia) | us-east-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| US East (Ohio) | us-east-2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| US West (Oregon) | us-west-2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Asia Pacific (Mumbai) | ap-south-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Asia Pacific (Seoul) | ap-northeast-2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Asia Pacific (Singapore) | ap-southeast-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Asia Pacific (Sydney) | ap-southeast-2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Asia Pacific (Malaysia) | ap-southeast-5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Asia Pacific (Tokyo) | ap-northeast-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Canada (Central) | ca-central-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Europe (Frankfurt) | eu-central-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Europe (Ireland) | eu-west-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Europe (London) | eu-west-2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Europe (Paris) | eu-west-3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| South America (São Paulo) | sa-east-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Africa (Cape Town) | af-south-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Israel (Tel Aviv) | il-central-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| AWS GovCloud (US-West) | us-gov-west-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| AWS GovCloud (US-East) | us-gov-east-1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |

## DCV gateway domain names
<a name="dns-wsp"></a>

The following table lists the DCV WorkSpace gateway domain names. These domains must be contactable, for the WorkSpaces client application to be able to access the WorkSpace DCV service.

| Region | Domain |
| --- | --- |
| US East (N. Virginia) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| US West (Oregon) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Asia Pacific (Mumbai) | \*.prod.ap-south-1.highlander.aws.a2z.com |
| Asia Pacific (Seoul) | \*.prod.ap-northeast-2.highlander.aws.a2z.com |
| Asia Pacific (Singapore) | \*.prod.ap-southeast-1.highlander.aws.a2z.com |
| Asia Pacific (Sydney) | \*.prod.ap-southeast-2.highlander.aws.a2z.com |
| Asia Pacific (Tokyo) | \*.prod.ap-northeast-1.highlander.aws.a2z.com |
| Canada (Central) | \*.prod.ca-central-1.highlander.aws.a2z.com |
| Europe (Frankfurt) | \*.prod.eu-central-1.highlander.aws.a2z.com |
| Europe (Ireland) | \*.prod.eu-west-1.highlander.aws.a2z.com |
| Europe (London) | \*.prod.eu-west-2.highlander.aws.a2z.com |
| Europe (Paris) | \*.prod.eu-west-3.highlander.aws.a2z.com |
| South America (São Paulo) | \*.prod.sa-east-1.highlander.aws.a2z.com |
| Africa (Cape Town) | \*.prod.af-south-1.highlander.aws.a2z.com |
| Israel (Tel Aviv) | \*.prod.il-central-1.highlander.aws.a2z.com |
| AWS GovCloud (US-West) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| AWS GovCloud (US-East) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

## DCV PrivateLink domain names
<a name="dns-wsp-privatelink"></a>

If you use VPC endpoints for WorkSpaces streaming, the following domains must be allowed through your firewall or proxy. Replace <region> with your AWS Region (for example, us-east-1).

| DNS Name Type | Domain |
| --- | --- |
| Unique publicly resolvable DNS name | \*.prod.highlander.<region>.vpce.amazonaws.com |
| Generic private DNS name | privatelink.prod.<region>.highlander.aws.a2z.com |

## Network interfaces
<a name="network-interfaces"></a>

Each WorkSpace has the following network interfaces:
+ The primary network interface (eth1) provides connectivity to the resources within your VPC and on the internet, and is used to join the WorkSpace to the directory.
+ The management network interface (eth0) is connected to a secure WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to WorkSpaces clients, and to allow WorkSpaces to manage the WorkSpace.

WorkSpaces selects the IP address for the management network interface from various address ranges, depending on the Region that the WorkSpaces are created in. When a directory is registered, WorkSpaces tests the VPC CIDR and the route tables in your VPC to determine if these address ranges create a conflict. If a conflict is found in all available address ranges in the Region, an error message is displayed and the directory is not registered. If you change the route tables in your VPC after the directory is registered, you might cause a conflict.

**Warning**
Do not modify or delete any of the network interfaces that are attached to a WorkSpace. Doing so might cause the WorkSpace to become unreachable or lose internet access. For example, if you have [enabled automatic assignment of Elastic IP addresses](automatic-assignment.md) at the directory level, an [ Elastic IP address](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html) (from the Amazon-provided pool) is assigned to your WorkSpace when it is launched. However, if you associate an Elastic IP address that you own to a WorkSpace, and then you later disassociate that Elastic IP address from the WorkSpace, the WorkSpace loses its public IP address, and it doesn't automatically get a new one from the Amazon-provided pool.
To associate a new public IP address from the Amazon-provided pool with the WorkSpace, you must [rebuild the WorkSpace](rebuild-workspace.md). If you don't want to rebuild the WorkSpace, you must associate another Elastic IP address that you own to the WorkSpace.

### Management interface IP ranges
<a name="management-ip-ranges"></a>

The following table lists the IP address ranges used for the management network interface.

**Note**
**If you're using Bring Your Own License (BYOL) Windows WorkSpaces**, the IP address ranges in the following table do not apply. Instead, PCoIP BYOL WorkSpaces use the 54.239.224.0/20 IP address range for management interface traffic in all AWS Regions. For DCV BYOL Windows WorkSpaces, both the 54.239.224.0/20 and 10.0.0.0/8 IP address ranges apply in all AWS Regions. (These IP address ranges are used in addition to the /16 CIDR block that you select for management traffic for your BYOL WorkSpaces.)
**If you're using DCV WorkSpaces created from public bundles**, the IP address range 10.0.0.0/8 also applies for management interface traffic in all AWS Regions, in addition to the PCoIP/DCV ranges shown in the following table.

| Region | IP address range |
| --- | --- |
| US East (N. Virginia) | PCoIP/WSP: 172.31.0.0/16, 192.168.0.0/16, 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| US West (Oregon) | PCoIP/WSP: 172.31.0.0/16, 192.168.0.0/16, and 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Asia Pacific (Mumbai) | PCoIP/WSP: 192.168.0.0/16<br />WSP: 10.0.0.0/8 |
| Asia Pacific (Seoul) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Asia Pacific (Singapore) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Asia Pacific (Sydney) | PCoIP/WSP: 172.31.0.0/16, 192.168.0.0/16, and 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Asia Pacific (Tokyo) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Canada (Central) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Europe (Frankfurt) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Europe (Ireland) | PCoIP/WSP: 172.31.0.0/16, 192.168.0.0/16, and 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Europe (London) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Europe (Paris) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| South America (São Paulo) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Africa (Cape Town) | PCoIP/WSP: 172.31.0.0/16 and 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| Israel (Tel Aviv) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |
| AWS GovCloud (US-West) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 and 192.169.0.0/16 |
| AWS GovCloud (US-East) | PCoIP/WSP: 198.19.0.0/16<br />WSP: 10.0.0.0/8 |

### Management interface ports
<a name="management_ports"></a>

The following ports must be open on the management network interface of all WorkSpaces:
+ Inbound TCP on port 4172. This is used for establishment of the streaming connection on the PCoIP protocol.
+ Inbound UDP on port 4172. This is used for streaming user input on the PCoIP protocol.
+ Inbound TCP on port 4489. This is used for access using the web client.
+ Inbound TCP on port 8200. This is used for management and configuration of the WorkSpace.
+ Inbound TCP on ports 8201-8250. These ports are used for establishment of the streaming connection and for streaming user input on the DCV protocol.
+ Inbound UDP on port 8220. This port is used for establishment of the streaming connection and for streaming user input on the DCV protocol
+ Outbound TCP on ports 8443 and 9997. This is used for access using the web client.
+ Outbound UDP on ports 3478, 4172, and 4195. This is used for access using the web client.
+ Outbound TCP on port 80, as defined in [ Management interface IP ranges](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#management-ip-ranges), to IP address 169.254.169.254 for access to the EC2 metadata service. Any HTTP proxy assigned to your WorkSpaces must also exclude 169.254.169.254.
+ Outbound TCP on port 1688 to IP addresses 169.254.169.250 and 169.254.169.251 to allow access to Microsoft KMS for Windows activation for Workspaces that are based on public bundles. If you're using Bring Your Own License (BYOL) Windows WorkSpaces, you must allow access to your own KMS servers for Windows activation.
+ Outbound TCP on port 1688 to IP address 54.239.236.220 to allow access to Microsoft KMS for Office activation for BYOL WorkSpaces.

  If you're using Office through one of the WorkSpaces public bundles, the IP address for Microsoft KMS for Office activation varies. To determine that IP address, find the IP address for the management interface of the WorkSpace, and then replace the last two octets with `64.250`. For example, if the IP address of the management interface is 192.168.3.5, the IP address for Microsoft KMS Office activation is 192.168.64.250.
+ Outbound TCP to IP address 127.0.0.2 for DCV WorkSpaces when the WorkSpace host is configured to use a proxy server.
+ Communications originating from loopback address 127.0.01.

Under normal circumstances, the WorkSpaces service configures these ports for your WorkSpaces. If any security or firewall software is installed on a WorkSpace that blocks any of these ports, the WorkSpace may not function correctly or may be unreachable.

### Primary interface ports
<a name="primary_ports"></a>

No matter which type of directory you have, the following ports must be open on the primary network interface of all WorkSpaces:
+ For internet connectivity, the following ports must be open outbound to all destinations and inbound from the WorkSpaces VPC. You need to add these manually to the security group for your WorkSpaces if you want them to have internet access.
  + TCP 80 (HTTP)
  + TCP 443 (HTTPS)
+ To communicate with the directory controllers, the following ports must be open between your WorkSpaces VPC and your directory controllers. For a Simple AD directory, the security group created by Directory Service will have these ports configured correctly. For an AD Connector directory, you might need to adjust the default security group for the VPC to open these ports.
  + TCP/UDP 53 - DNS
  + TCP/UDP 88 - Kerberos authentication
  + UDP 123 - NTP
  + TCP 135 - RPC
  + UDP 137-138 - Netlogon
  + TCP 139 - Netlogon
  + TCP/UDP 389 - LDAP
  + TCP/UDP 445 - SMB
  + TCP/UDP 636 - LDAPS (LDAP over TLS/SSL)
  + TCP 1024-65535 - Dynamic ports for RPC
  + TTCP 3268-3269 - Global Catalog

  If any security or firewall software is installed on a WorkSpace that blocks any of these ports, the WorkSpace may not function correctly or may be unreachable.

## IP address and port requirements by Region
<a name="ip-address-regions"></a>

### US East (N. Virginia)
<a name="us-east"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.us-east-1.amazonaws.com  |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://ws-client-service.us-east-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.us-east-1.signin.aws |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domains:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domains:<br />https://workspaces.us-east-1.amazonaws.com |
| Session Broker (PCM) | Domains:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-iad.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| DCV gateway domain name | \*.prod.us-east-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### US West (Oregon)
<a name="us-west"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.us-west-2.amazonaws.com  |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://ws-client-service.us-west-2.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.us-west-2.signin.aws |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domains:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domains:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domains:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-pdx.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 34.223.96.0/22 |
| DCV gateway domain name | \*.prod.us-west-2.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Asia Pacific (Mumbai)
<a name="ap-south"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.ap-south-1.amazonaws.com  |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://ws-client-service.ap-south-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Web Access isn't currently available in the Asia Pacific (Mumbai) Region |
| Health check hostname | drp-bom.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges | 13.126.243.0 - 13.126.243.255 |
| DCV gateway servers IP address range | 65.1.156.0/22 |
| DCV gateway domain name | \*.prod.ap-south-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Asia Pacific (Seoul)
<a name="ap-northeast-2"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Device Metrics (for 1.0\+ and 2.0\+ WorkSpaces client applications) | https://device-metrics-us-2.amazon.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.ap-northeast-2.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://ws-client-service.ap-northeast-2.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-icn.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 3.35.160.0/22 |
| DCV gateway domain name | \*.prod.ap-northeast-2.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Asia Pacific (Singapore)
<a name="ap-southeast-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.ap-southeast-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: https://ws-client-service.ap-southeast-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-sin.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 13.212.132.0/22 |
| DCV gateway domain name | \*.prod.ap-southeast-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Asia Pacific (Sydney)
<a name="ap-southeast-2"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.ap-southeast-2.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.ap-southeast-2.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.ap-southeast-2.signin.aws |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-syd.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 3.25.248.0/22 |
| DCV gateway domain name | \*.prod.ap-southeast-2.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Asia Pacific (Tokyo)
<a name="ap-northeast-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.ap-northeast-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.ap-northeast-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.ap-northeast-1.signin.aws |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-nrt.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 3.114.164.0/22 |
| DCV gateway domain name | \*.prod.ap-northeast-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Canada (Central)
<a name="ca-central-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.ca-central-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.ca-central-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-yul.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 3.97.20.0/22 |
| DCV gateway domain name | \*.prod.ca-central-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Europe (Frankfurt)
<a name="eu-central-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.eu-central-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.eu-central-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-fra.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 18.192.216.0/22 |
| DCV gateway domain name | \*.prod.eu-central-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Europe (Ireland)
<a name="eu-west-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.eu-west-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.eu-west-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.eu-west-1.signin.aws |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-dub.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 3.248.176.0/22 |
| DCV gateway domain name | \*.prod.eu-west-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Europe (London)
<a name="eu-west-2"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.eu-west-2.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.eu-west-2.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-lhr.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 18.134.68.0/22 |
| DCV gateway domain name | \*.prod.eu-west-2.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Europe (Paris)
<a name="eu-west-3"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/Client  |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.eu-west-3.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.eu-west-3.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-cdg.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range |  51.17.72.0/22 |
| DCV gateway domain name | \*.prod.eu-west-3.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### South America (São Paulo)
<a name="sa-east-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.sa-east-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.sa-east-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-gru.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 15.228.64.0/22 |
| DCV gateway domain name | \*.prod.sa-east-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Africa (Cape Town)
<a name="sa-east-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.af-south-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.af-south-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-cpt.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 15.228.64.0/22 |
| DCV gateway domain name | \*.prod.af-south-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### Israel (Tel Aviv)
<a name="il-central-1"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://d2td7dqidlhjx7.cloudfront.net/ |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://skylight-client-ds.il-central-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain: <br />https://ws-client-service.il-central-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://<directory id>.awsapps.com/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Web Access TURN Servers for PCoIP | Server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-tlv.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 51.17.72.0/22 |
| DCV gateway domain name | \*.prod.il-central-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### AWS GovCloud (US-West) Region
<a name="govcloud-west-region"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://s3.amazonaws.com/workspaces-client-updates/prod/pdt/windows/WorkSpacesAppCast.xml |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />hhttps://skylight-client-ds.us-gov-west-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://ws-client-service.us-gov-west-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.signin.amazonaws-us-gov.com |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://login.us-gov-home.awsapps.com/directory/<directory id>/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-pdt.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway domain name | \*.prod.us-gov-west-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |

### AWS GovCloud (US-East) Region
<a name="govcloud-east-region"></a>

**Domains and IP Addresses to add to your allowlist**

| Category | Details |
| --- | --- |
| CAPTCHA | https://opfcaptcha-prod.s3.amazonaws.com/ |
| Client Auto-update | https://s3.amazonaws.com/workspaces-client-updates/prod/osu/windows/WorkSpacesAppCast.xml |
| Connectivity Check | https://connectivity.amazonworkspaces.com/ |
| Client Metrics (for 3.0\+ WorkSpaces client applications) | Domain:<br />hhttps://skylight-client-ds.us-gov-east-1.amazonaws.com |
| Dynamic Messaging Service (for 3.0\+ WorkSpaces client applications) | Domain:<br />https://ws-client-service.us-gov-east-1.amazonaws.com |
| Directory Settings |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)  |
| Forrester Log Service  | https://fls-na.amazon.com/ |
| Health Check (DRP) Servers | [Health check servers](#health_check) |
| Pre-session Smart Card Authentication Endpoints | https://smartcard.signin.amazonaws-us-gov.com |
| Registration Dependency (for Web Access and Teradici PCoIP Zero Clients) | https://s3.amazonaws.com |
| User Login Pages | https://login.us-gov-home.awsapps.com/directory/<directory id>/ (where <directory id> is the customer's domain) |
| WS Broker | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| WorkSpaces API Endpoints | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Session Broker (PCM) | Domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| Health check hostname | drp-osu.amazonworkspaces.com |
| Health check IP addresses |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| PCoIP gateway servers public IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
| DCV gateway servers IP address range | 18.254.148.0/22 |
| DCV gateway domain name | \*.prod.us-gov-east-1.highlander.aws.a2z.com |
| Management interface IP address ranges |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) |
