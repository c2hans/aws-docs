---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/api-using.html
---

# Using the AWS Network Firewall REST API
<a name="api-using"></a>

AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for your virtual private cloud (VPC) that you create in Amazon Virtual Private Cloud (Amazon VPC). With Network Firewall, you can filter traffic at the perimeter of your VPC. This includes filtering traffic going to and coming from an internet gateway, NAT gateway, or over VPN or Direct Connect. Network Firewall uses the open source intrusion prevention system (IPS), Suricata, for stateful inspection. Network Firewall supports Suricata compatible rules.

This section describes how to make requests to the Network Firewall API for creating and managing firewalls in Network Firewall. This section covers the components of requests, the content of responses, and how to authenticate requests.

For general guidance on accessing the AWS APIs, see the [AWS APIs](https://docs.aws.amazon.com/general/latest/gr/aws-apis.html) in the *AWS General Reference*.

**Note**
If you use a programming language that has an AWS SDK, use the SDK rather than trying to work your way through the APIs. The SDKs make authentication simpler, integrate more easily with your development environment, and provide easy access to Network Firewall commands. For more information about the AWS SDKs, see [Setting up tool access](setting-up.md#setting-up-tools) in the topic [Setting up](setting-up.md).

**Topics**
+ [Making HTTPS requests to AWS Network Firewall](api-making-requests.md)
+ [HTTP responses](api-making-requests-response.md)
+ [Authenticating requests](authenticating-requests.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
