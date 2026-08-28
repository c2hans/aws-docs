---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/set-up-your-network.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Set up your network
<a name="set-up-your-network"></a>

 Traditional Voice over IP (VoIP) solutions require you to allow both inbound and outbound traffic for specific User Datagram Protocol (UDP) port ranges and IPs, such as 80 and 443. These solutions also apply to Transmission Control Protocol (TCP). In comparison, the network requirements for using the Contact Control Panel (CCP) with a softphone are less intrusive. You can establish persistent outbound send/receive connections through your web browser. As a result, you don't need to open a client-side port to listen for inbound traffic.

 The following diagram shows you what each port is used for:

![Diagram of Amazon Connect port and fully qualified domain name (FQDN) usage.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/amazon-connect-port.png)

## Allow IP address ranges
<a name="allow-ip-address-ranges"></a>

 In the [AWS ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json) file, the whole `/19` IP address range is owned by Amazon Connect. All traffic to and from the `/19` range comes to and from Amazon Connect. The `/19` IP address range isn't shared with other services. It's for the exclusive use of Amazon Connect globally. In the AWS `ip-ranges.json` file, you can see the same range listed twice. For example:

```
                { "ip_prefix": "15.193.0.0/19",
                "region": "GLOBAL",
                "service": "AMAZON"
                },
                {
                "ip_prefix": "15.193.0.0/19",
                "region": "GLOBAL",
                "service": "AMAZON_CONNECT"
                },
```

 AWS always publishes any IP range twice: once for the specific service, and once for “AMAZON” service. There could even be a third listing for a more specific use case within a service.

 When there are new IP address ranges supported for Amazon Connect, they are added to the publicly available `ip-ranges.json` file. They are kept for a minimum of 30 days before they are used by the service. After 30 days, softphone traffic through the new IP address ranges increases over the subsequent two weeks. After two weeks, traffic is routed through the new ranges equivalent to all available ranges.

**Note**
To significantly reduce your blast radius, consider setting up a [domain allowlist](https://docs.aws.amazon.com/connect/latest/adminguide/ccp-networking.html#option1) instead.

## Stateless firewalls
<a name="stateless-firewalls"></a>

 If you're using a stateless firewall for both options, use the requirements described in the previous sections. Then you must add to your allow list the ephemeral port range used by your browser, as shown in the following table.

* Table 1 — Ephemeral IP port range *

|  IP-Range entry  |  Port  |  Direction  |  Traffic  |
| --- | --- | --- | --- |
|  AMAZON\_CONNECT  |  49152-65535 (UDP)  |  INBOUND  |  SEND/RECEIVE  |

## Port and protocol considerations
<a name="port-and-protocol-considerations"></a>

 Consider the following when implementing your network configuration changes for Amazon Connect:
+  Allow traffic for all addresses and ranges for the Region in which you created your Amazon Connect instance.
+  If you are using a proxy or firewall between the Contact Control Panel (CCP) and Amazon Connect, increase the Secure Sockets Layer (SSL) certificate cache timeout to cover the duration of an entire shift for your agents; do this to avoid connectivity issues with certificate renewals during their scheduled working time. For example, if your agents are scheduled to work eight-hour shifts that include breaks, increase the interval to eight hours plus time for breaks and lunch.
+  When opening ports, Amazon Connect requires only the ports for endpoints in the same Region as your instance. CloudFront, however, serves static content from an edge location that has the lowest latency in relation to where your agents are located. IP range allow lists for CloudFront are global, and require all IP ranges associated with "service" and "CLOUDFRONT" in `ip-ranges.json`.
+  Once the `ip-ranges.json` is updated, the associated AWS service will begin using the updated IP ranges after 30 days. To avoid intermittent connectivity issues when the service begins routing traffic to the new IP ranges, be sure to add the new IP ranges to your allow list, within 30 days from the time they were added to `ip-ranges.json`.
+  If you are using a custom CCP with the Amazon Connect Streams API, you can create a media-less CCP that does not require opening ports for communication with Amazon Connect, but still requires ports opened for communication with CloudFront.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
