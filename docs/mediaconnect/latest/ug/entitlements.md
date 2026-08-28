---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements.html
---

# Managing entitlements in MediaConnect
<a name="entitlements"></a>

Content originators can grant entitlements to share their content with other AWS accounts (subscriber accounts). Subscribers can then set up their own AWS Elemental MediaConnect flows using the originator's flow as their source. The following illustration shows this process.

**Note**
MediaConnect doesn't support entitlements on CDI flows. You can only grant entitlements on transport stream flows, with the exception of TR-07 sources.

![This illustration shows how content originators can grant entitlements to share their content with other AWS accounts (subscriber accounts). Subscribers can then set up their own MediaConnect flows using the originator's flow as their source.](http://docs.aws.amazon.com/mediaconnect/latest/ug/images/use-case-entitlement.png)

**Topics**
+ [Sharing content in your AWS Elemental MediaConnect flow with other AWS accounts](entitlements-originator.md)
+ [Subscribing to streaming media content provided by another AWS account using MediaConnect](entitlements-subscriber.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
