---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/vpc-connectivity.html
---

# Giving Amazon GameLift Streams access to resources in an Amazon VPC
<a name="vpc-connectivity"></a>

By default, Amazon GameLift Streams runs your streaming applications on compute resources that have access to the public internet but not to resources in your private Amazon VPCs. To give your streaming applications access to private resources such as databases, cache servers, or internal APIs, you can configure VPC connectivity when creating a stream group.

Amazon GameLift Streams uses AWS Transit Gateway to establish private network connectivity between the service-managed VPC where your streams run and your own Amazon VPC. This allows your streaming applications to communicate with resources in your Amazon VPC over private IP addresses without exposing traffic to the public internet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
