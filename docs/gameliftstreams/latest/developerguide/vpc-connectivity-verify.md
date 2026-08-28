---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/vpc-connectivity-verify.html
---

# Verifying connectivity
<a name="vpc-connectivity-verify"></a>

To verify that VPC connectivity is working correctly:

1. Start a stream session using your stream group.

1. From within your streaming application, connect to a resource in your VPC using its private IP address.

1. Verify that the connection succeeds and data can be exchanged.

If connectivity fails, check the following:
+ The transit gateway attachment is in the `available` state.
+ Routes are correctly configured in both your VPC route table and the transit gateway route table.
+ Security groups allow inbound traffic from the service VPC CIDR block.
+ Network ACLs (if used) allow the required traffic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
