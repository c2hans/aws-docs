---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

To uninstall the solution, delete the CloudFormation stacks:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Select the solution’s parent stack. All other solution stacks will be deleted automatically.

1. Choose **Delete**.

**Note**
Uninstalling the solution deletes all the AWS resources used by the solution except for the Amazon S3 buckets. If some IP sets fail to delete due to rate exceeded throttling issue caused by the [AWA WAF API quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html), manually delete those IP sets, and then delete the stack.
