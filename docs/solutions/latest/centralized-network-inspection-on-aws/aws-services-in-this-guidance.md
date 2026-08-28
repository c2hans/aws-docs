---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/aws-services-in-this-guidance.html
---

# AWS services in this guidance
<a name="aws-services-in-this-guidance"></a>

|  AWS service  |  Description  |
| --- | --- |
|  [AWS CodeBuild](https://aws.amazon.com/codebuild/)  |  Core. CodeBuild validates the configuration files (firewall, firewall policy, and rule group) and checks if the JSON format is valid.  |
|  [AWS CodePipeline](https://aws.amazon.com/codepipeline/)  |  Core. CodePipeline validates, tests, and implements changes based on updates to the configuration package in the S3 bucket.  |
|  [AWS Network Firewall](https://aws.amazon.com/network-firewall/)  |  Core. This guidance automates the process of provisioning a centralized Network Firewall to inspect traffic between VPCs.  |
|  [Amazon VPC](https://aws.amazon.com/vpc/)  |  Core. This guidance creates an inspection VPC with four subnets to support Transit Gateway attachments and Network Firewall endpoints.  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Supporting. This guidance creates S3 buckets for firewall configurations, source code, artifacts, and logs.  |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  Supporting. Provides application-level resource monitoring and visualization of resource operations and cost data.  |
|  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)  |  Optional. This guidance creates Transit Gateway attachments for your VPCs if you provide an existing transit gateway ID.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
