---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setting-up-trusted-entity.html
---

# IAM permissions for MediaLive as a trusted entity
<a name="setting-up-trusted-entity"></a>

AWS Elemental MediaLive must be set up so that when a channel is running, MediaLive itself has access to perform operations on resources that belong to your organization's AWS account. In other words, MediaLive must be set up as a *trusted entity* in your organization's AWS account.

**Topics**
+ [About the trusted entity role](about-trusted-entity.md)
+ [Options for implementing the trusted entity](scenarios-for-medialive-role.md)
+ [Create the trust entity – simple option](setup-trusted-entity-simple.md)
+ [Create the trusted entity - complex option](setup-trusted-entity-complex.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
