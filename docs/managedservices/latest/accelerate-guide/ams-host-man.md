---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ams-host-man.html
---

# AMS host management reports
<a name="ams-host-man"></a>

**Topics**
+ [SSM Agent Coverage report](#reportintg-ssm-coverage)

## SSM Agent Coverage report
<a name="reportintg-ssm-coverage"></a>

AMS SSM Agent Coverage report informs you whether or not the EC2 instances in the account have the SSM Agent installed.

| **Field Name** | **Definition** |
| --- | --- |
| Customer Name | Customer name for situations where there are multiple sub-customers |
| Resource Region | AWS Region where the resource is located |
| Account name | The name of the account |
| AWS Account ID | The ID of the AWS account |
| Resource Id | ID of EC2 instance |
| Resource Name | Name of EC2 instance |
| Compliant flag | Indicates if the resource has the SSM Agent installed ("Compliant") or not ("NON\_COMPLIANT") |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
