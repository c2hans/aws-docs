---
source_url: https://docs.aws.amazon.com/ram/latest/userguide/tshoot-limits-exceeded.html
---

# Error: Limit exceeded
<a name="tshoot-limits-exceeded"></a>

## Scenario
<a name="tshoot-limits-exceeded-scenario"></a>

You receive "You have reached the limit on the number of resources you can share" or "ResourceShareLimitExceededException" when trying to share resources.

## Cause
<a name="tshoot-limits-exceeded-cause"></a>

These errors occur when you reach the maximum number of resources you can share using either the AWS RAM service or the AWS service that created the resource you're trying to share. This quota (formerly referred to as a limit) can affect both the sharing account or the account you're sharing the resource with.

## Solution
<a name="tshoot-limits-exceeded-fix"></a>

1. To view your quotas, in the AWS account where you are seeing the error, navigate to one of the following pages, depending on the type of quota you're reaching:
   + The [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas)
   + The [page for the AWS service](https://console.aws.amazon.com/servicequotas/home/services) whose resources are impacted by the quota

1. Scroll down and choose the relevant quota.

1. If it's available for this quota, choose **Request quota increase**.

1. Enter a new value for the quota, and then choose **Request**.

1. The request appears on the [Quota request history](https://console.aws.amazon.com/servicequotas/home/requests) page, where you can check on the status of the request until it's finalized.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
