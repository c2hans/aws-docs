---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-non-billable.html
---

# Resource types stored but not billed
<a name="next-gen-troubleshoot-non-billable"></a>

Next generation Resilience Hub discovers and stores the following resource types for context, but does not count them toward your billable resource quota. They do not appear in resilience analysis.

| Resource type |
| --- |
| `AWS::IAM::Role` |
| `AWS::IAM::Policy` |
| `AWS::IAM::ManagedPolicy` |
| `AWS::IAM::InstanceProfile` |
| `AWS::Lambda::LayerVersion` |
| `AWS::Lambda::Permission` |
| `AWS::EC2::LaunchTemplate` |
| `AWS::EC2::SecurityGroup` |
| `AWS::EC2::SubnetRouteTableAssociation` |
| `AWS::CloudFront::OriginRequestPolicy` |
| `AWS::CloudFront::CloudFrontOriginAccessIdentity` |
| `AWS::SecretsManager::Secret` |
| `AWS::CloudWatch::Alarm` |
| `AWS::CDK::Metadata` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
