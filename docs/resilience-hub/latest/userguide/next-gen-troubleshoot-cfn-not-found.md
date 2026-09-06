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
