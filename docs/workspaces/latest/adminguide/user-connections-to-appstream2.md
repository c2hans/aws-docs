---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/user-connections-to-appstream2.html
---

# User connections to WorkSpaces Pools
<a name="user-connections-to-appstream2"></a>

Users can connect to WorkSpaces in WorkSpaces Pools through the default public internet endpoint.

By default, WorkSpaces Pools is configured to route streaming connections over the public internet. Internet connectivity is required to authenticate users and deliver the web assets that WorkSpaces Pools requires to function. To allow this traffic, you must allow the domains listed in [Allowed Domains](allowed-domains.md).

**Note**
For user authentication, WorkSpaces Pools supports Security Assertion Markup Language 2.0 (SAML 2.0). For more information, see [Configure SAML 2.0 and create a WorkSpaces Pools directory](create-directory-pools.md).

The following topics provide information about how to enable user connections to WorkSpaces Pools.

**Topics**
+ [Bandwidth Recommendations](bandwidth-recommendations-user-connections.md)
+ [IP Address and Port Requirements for WorkSpaces Pools User Devices](pools-client-application-ports.md)
+ [Allowed Domains](allowed-domains.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
