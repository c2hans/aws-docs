---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/faq.html
---

# FAQ
<a name="faq"></a>

## Can updating the deployment of a CloudFormation stack (involving IaC code changes) fix drift?
<a name="update-fix-drift-question"></a>

CloudFormation performs an update with a fail-safe approach. That is, CloudFormation doesn't apply the template changes with the `--force option` on its resources. Instead, CloudFormation identifies the changes to be performed on an existing resource by creating a [change set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html). To identify the change set, CloudFormation uses the resource's current properties instead of relying on the previous template version. The stack update can fail depending on the resource type and the contract of the resource's API. In the hypothetical scenario covered previously, an EBS volume contract doesn't allow you to downgrade the volume size and such updates result in a failed state. CloudFormation recommends that you manage a resource's state through CloudFormation only and not directly with APIs.

## What's the business impact of an outage?
<a name="business-impact-question"></a>

There is a direct financial impact that depends on the number of resources involved in a service outage. If the pipeline is unaware of the changes done to a stack through API calls on resources and the stack fails, then troubleshooting the root cause of the problem and restoring the infrastructure to a working state can become a time-consuming and difficult process due to the `UPDATE_ROLLBACK_FAILED` state.

## What other issues should I consider?
<a name="other-issues-question"></a>

If a CloudFormation stack involves custom resources and the EDP solution makes changes to a resource's state, it's possible for the resource to revert back to an old configuration (blind spot). This is because the CloudFormation template is unaware of the change to a resource or property. There is an unintended restore to an old configuration, and the stack could deploy successfully but with the incorrect configuration. It can be time-consuming to troubleshoot the issue, depending on the specific resource.

## Is the scenario with the EBS volume an edge case?
<a name="ebs-volume-question"></a>

The EBS volume scenario isn't an edge case. The EBS volume scenario illustrates the importance of ensuring synchronization between CloudFormation and actual AWS resources. Another example of a common scenario involves modifying an Amazon Simple Storage Service (Amazon S3) bucket policy. You can make a policy update to an S3 bucket by using the AWS Management Console or an API (when you [use an S3 bucket as an origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html#using-s3-as-origin) for an Amazon CloudFront distribution). In this scenario, the Amazon S3 policy could be overwritten by pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
