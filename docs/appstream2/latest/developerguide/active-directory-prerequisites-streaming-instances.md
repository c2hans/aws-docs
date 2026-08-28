---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites-streaming-instances.html
---

# Domain-Joined WorkSpaces Applications Streaming Instances
<a name="active-directory-prerequisites-streaming-instances"></a>

SAML 2.0-based user federation is required for application streaming from domain-joined Always-On and On-Demand fleets. You cannot launch sessions to domain-joined instances by using [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) or the WorkSpaces Applications user pool.

Also, you must use an image that supports joining image builders and fleets to an Active Directory domain. All public images published on or after July 24, 2017 support joining an Active Directory domain. For more information, see [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md) and [Tutorial: Setting Up Active Directory](active-directory-directory-setup.md).

**Note**
You can join Always-On and On-Demand fleet streaming instances to an Active Directory domain. Supported operating systems include Windows, Red Hat Enterprise Linux, and Rocky Linux.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
