---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-never-discovered.html
---

# Resource types never discovered
<a name="next-gen-troubleshoot-never-discovered"></a>

Next generation Resilience Hub never stores the following resource types during discovery. These resource types include auxiliary infrastructure, point-in-time backups, and operational tooling with no bearing on resilience analysis.

| Resource type |
| --- |
| `AWS::EC2::EIP` |
| `AWS::EC2::Volume` |
| `AWS::EC2::Snapshot` |
| `AWS::FSx::Snapshot` |
| `AWS::Lightsail::DiskSnapshot` |
| `AWS::RDS::DBSnapshot` |
| `AWS::RDS::DBClusterSnapshot` |
| `AWS::EC2::FlowLog` |
| `AWS::CloudWatch::Dashboard` |
| `AWS::Logs::LogGroup` |
| `AWS::Logs::MetricFilter` |
| `AWS::SSM::ResourceDataSync` |
| `AWS::RDS::DBParameterGroup` |
| `AWS::RDS::DBClusterParameterGroup` |
| `AWS::ElastiCache::ParameterGroup` |
| `AWS::RDS::DBSubnetGroup` |
| `AWS::ElastiCache::SubnetGroup` |
| `AWS::EC2::SubnetNetworkAclAssociation` |
| `AWS::EC2::VPCGatewayAttachment` |
| `AWS::CloudFormation::Stack` |
| `AWS::CloudFormation::WaitConditionHandle` |
| `AWS::CodeDeploy::DeploymentGroup` |
| `AWS::KMS::Alias` |
| `AWS::SecretsManager::SecretTargetAttachment` |
| `AWS::CloudFormation::CustomResource` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
