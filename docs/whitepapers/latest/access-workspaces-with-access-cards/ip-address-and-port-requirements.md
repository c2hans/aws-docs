---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/ip-address-and-port-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# IP address and port requirements
<a name="ip-address-and-port-requirements"></a>

The Amazon WorkSpaces client application requires outbound access on ports 443 (TCP) and 4195 (UDP and TCP).

Port 443 (TCP) is used for client application updates, registration, and authentication. The desktop client applications support the use of a proxy server for port 443 (HTTPS) traffic.

 **To enable the use of a proxy server**:

1.  Open the client application.

1.  Choose **Advanced Settings**.

1.  Choose **Use Proxy Server**.

1.  Specify the address and port of the proxy server.

1.  Choose **Save**.

 Port 4195 (UDP and TCP) is used for streaming the WorkSpace desktop and for health checks. The desktop client applications do not support the use of a proxy server for port 4195 traffic; they require a direct connection to port 4195. This port must be open to the WorkSpaces Streaming Protocol (WSP) Gateway IP address ranges, and to the health check servers in the Region that the WorkSpace is in. For more information, refer to [Health Check Servers](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#health_check) and [WSP Gateway Servers](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html#gateway_WSP).

**Note**
The TURN protocol is also used over port 4195 for client connections to the WorkSpaces Streaming Gateway. Refer to steps eight and nine in the [Architecture overview](architecture-overview.md).

* Table 1 — Required ports and protocols *

|  Source  |  Destination  |  Port  |  Type  |
| --- | --- | --- | --- |
|  WorkSpace Client  |  WorkSpaces  |  TCP 443  |  HTTPS  |
|  WorkSpace Client  |  WorkSpaces  |  TCP/UDP 4195  |  WSP  |
|  WorkSpaces  |  AD Domain Controller  |  TCP/UDP 53  |  DNS  |
|  WorkSpaces  |  AD Domain Controller  |  TCP/UDP 88  |  Kerberos Auth  |
|  WorkSpaces  |  AD Domain Controller  |  UDP 123  |  NTP  |
|  WorkSpaces  |  AD Domain Controller  |  TCP 135  |  RPC  |
|  WorkSpaces  |  AD Domain Controller  |  UDP 137 - 138  |  Netlogon  |
|  WorkSpaces  |  AD Domain Controller  |  TCP 139  |  Netlogon  |
|  WorkSpaces  |  AD Domain Controller  |  TCP/UDP 389  |  LDAP  |
|  WorkSpaces  |  AD Domain Controller  |  TCP/UDP 445  |  SMB  |
|  WorkSpaces  |  AD Domain Controller  |  TCP/UDP 464  |  Kerberos  |
|  WorkSpaces  |  AD Domain Controller  |  TCP/UDP 636  |  LDAP  |
|  WorkSpaces  |  AD Domain Controller  |  TCP 49152 - 65535  |  Dynamic RPC  |
|  WorkSpaces  |  AD Domain Controller  |  UDP 1812  |  RADIUS  |
|  AD Connector  |  AD Domain Controller  |  TCP/UDP 53  |  DNS  |
|  AD Connector  |  AD Domain Controller  |  TCP/UDP 88  |  Kerberos Auth  |
|  AD Connector  |  AD Domain Controller  |  TCP/UDP 389  |  LDAP  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
