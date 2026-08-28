---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/review-examples.html
---

# Examples
<a name="review-examples"></a>

The following are examples of the mature phase. These examples dive deeper into the models, tools, and processes for different business objectives, at a practical level.

## Mature: Threat detection example
<a name="mature-threat-detection-example"></a>

**Business outcome for detective controls: **Increase visibility and speed of detection of cloud incidents in order to lower risk and enable accelerated use and development of cloud resources.

**Tool: **[Assisted Log Enabler for AWS](https://github.com/awslabs/assisted-log-enabler-for-aws) (GitHub) is an open source tool that helps you turn on logging in the middle of a security incident. It can quickly increase your visibility into an incident.

**Sample use case: **Consider the single account use case depicted in the following diagram. There are events that require further investigation. You are unsure whether logging is enabled. In this case, the best course of action is to perform a dry run with the Assisted Log Enabler to see which services are enabled or disabled. Assisted Log Enabler checks for AWS CloudTrail trails, DNS query logs, VPC flow logs, and other logs. If they are not enabled, Assisted Log Enabler enables them. Assisted Log Enabler can check for and turn on logging across all AWS Regions.

You can also throttle Assisted Log Enabler up or down. After you complete your dry run, close the event, and resolve the issue, you realize that you no longer need this level of logging. You can quickly clean up the deployment to stop logging. This feature allows you to use Assisted Log Enabler as a triage tool.

![Use Assisted Log Enabler to see which services have logging enabled or disabled](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/3dee80dc-ab64-4167-9f73-a58fd1de60aa.png)

The following are the key features of Assisted Log Enabler for AWS:
+ You can run it in a single-account or multi-account environment.
+ You can use it to establish a baseline for logging into your environment.
+ You can use the dry run feature to check the current state and determine which services have logging enabled.
+ You can select which services you want to enable logging for.
+ You can throttle Assisted Log Enabler up or down, for your use case.

## Mature: IAM example
<a name="mature-iam-example"></a>

**IAM business outcome: **Automate visibility and measure against best practices to continuously reduce risk, to enable secure, external connections, and to quickly provision new users and environments

**Tool:** [AWS Identity and Access Management Access Analyzer (IAM Access Analyzer)](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) helps you identify resources that are shared with an external entity, validates IAM policies against policy grammar and best practices, and generates IAM policies based on historical access activity. We highly recommend that you enable IAM Access Analyzer at both the account and organization levels.

**Service benefits: **IAM Access Analyzer provides a wealth of insightful findings. It can identify your organization's resources and accounts that are shared with an external entity. It can detect resources such as a public S3 bucket, an AWS KMS key shared with another account, or a role shared with an external account, giving you excellent visibility into identifying resources that are not under your organization's control. It not only validates IAM policies but can also generate them for you.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
