---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/federation.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Federation
<a name="federation"></a>

The **Federation** section has available options for communications internal to the Enterprise deployment and external communications with other Wickr Enterprise, or guest users. Federation is available only if a super admin provisions it.
+ **Local Federation:** Choose **Edit** next to Local Federation to view the available options. Available options are **Disable federation**, **Enable federation**, and **Restricted federation**.
+ **Permitted Networks:** Only shown when restricted federation is enabled. Add labels and Network IDs for other local networks within the Enterprise deployment.
+ **Global Federation:** This controls external Wickr Enterprise, and AWS Wickr network access if Global Federation has been enabled by the super admin. Should not be shown if Global Federation is disabled.
+ **Allow guest users:** Only shown when global federation is enabled. This allows Wickr users in your network and in the selected security group to collaborate with Wickr guest users.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
