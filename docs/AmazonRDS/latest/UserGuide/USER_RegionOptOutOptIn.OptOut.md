---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RegionOptOutOptIn.OptOut.html
---

# What happens when you opt out of a Region
<a name="USER_RegionOptOutOptIn.OptOut"></a>

When you opt out of an AWS Region, the following changes apply to your Amazon RDS resources in that Region:
+ A snapshot of your DB instances and DB clusters in that Region is taken; then, your DB instances and DB clusters are deleted.
+ You can't create new DB instances or DB clusters in the opted-out Region.

You are charged for snapshots in the Region while the Region is opted out.

Opting out of a Region is a reversible action. Your resources are deleted only after taking a snapshot. After you opt back in to the Region, you can restore your resources using the snapshots.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
