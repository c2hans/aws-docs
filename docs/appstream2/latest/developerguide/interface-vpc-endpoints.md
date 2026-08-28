---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/interface-vpc-endpoints.html
---

# WorkSpaces Applications Interface VPC Endpoints
<a name="interface-vpc-endpoints"></a>

A virtual private cloud (VPC) is a virtual network in your own logically isolated area in the Amazon Web Services Cloud. If you use Amazon Virtual Private Cloud to host your AWS resources, you can establish a private connection between your VPC and WorkSpaces Applications. You can use this connection to enable WorkSpaces Applications to communicate with your resources on your VPC without going through the public internet.

Interface endpoints are powered by AWS PrivateLink, a technology that lets you keep streaming traffic within a VPC that you specify by using private IP addresses. When you use the VPC with an Direct Connect or AWS Virtual Private Network tunnel, you can keep the streaming traffic within your network.

The following topics provide information about WorkSpaces Applications interface endpoints.

**Topics**
+ [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md)
+ [Access WorkSpaces Applications API Operations and CLI Commands Through an Interface VPC Endpoint](access-api-cli-through-interface-vpc-endpoint.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
