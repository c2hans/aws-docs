---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-connections-to-appstream2.html
---

# User Connections to Amazon WorkSpaces Applications
<a name="user-connections-to-appstream2"></a>

Users can connect to WorkSpaces Applications streaming instances through the default public internet endpoint, or by using an interface VPC endpoint (interface endpoint) that you create in your virtual private cloud (VPC). For more information, see [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md).

By default, WorkSpaces Applications is configured to route streaming connections over the public internet. Internet connectivity is required to authenticate users and deliver the web assets that WorkSpaces Applications requires to function. To allow this traffic, you must allow the domains listed in [Allowed Domains](allowed-domains.md).

**Note**
For user authentication, WorkSpaces Applications supports user pools, Security Assertion Markup Language 2.0 (SAML 2.0), and the [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) API action. For more information, see [User Authentication](authentication-authorization.md).

The following topics provide information about how to enable user connections to WorkSpaces Applications.

**Topics**
+ [Bandwidth Recommendations](bandwidth-recommendations-user-connections.md)
+ [IP Address and Port Requirements for WorkSpaces Applications User Devices](client-application-ports.md)
+ [Allowed Domains](allowed-domains.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
