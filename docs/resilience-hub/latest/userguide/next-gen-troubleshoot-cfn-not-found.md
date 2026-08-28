---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-cfn-not-found.html
---

# CloudFormation stack not found
<a name="next-gen-troubleshoot-cfn-not-found"></a>

**Symptom:** Resource discovery fails with "stack not found."

**Solutions:**
+ Verify the stack ARN is correct and the stack exists.
+ Verify the invoker role has `cloudformation:DescribeStackResources` permission.
+ For cross-account stacks, verify the cross-account role has access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
