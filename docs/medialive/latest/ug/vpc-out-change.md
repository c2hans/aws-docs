---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/vpc-out-change.html
---

# Changing the setup
<a name="vpc-out-change"></a>

If you have set up a MediaLive channel for VPC delivery, note the following:
+ You can't change an existing channel to either start delivering via your VPC or stop delivering via your VPC.
+ You can't change the [channel class](plan-redundancy-mode.md) on an existing channel that is set up for delivery via your VPC.
+ If you add another input that uses your VPC, make sure that it follows the already [established rules](vpc-out-AZ-subnet-reqs.md) for VPCs, subnets, and Availability Zones.
+ If you delete the channel or if you delete all the output groups, MediaLive deletes the elastic interface points that it created in your Amazon EC2 instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
