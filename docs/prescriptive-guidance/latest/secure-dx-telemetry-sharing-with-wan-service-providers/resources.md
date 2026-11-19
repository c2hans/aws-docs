---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/resources.html
---

# Resources

## AWS Documentation
<a name="aws-documentation.fe6bc87f-c98a-57b9-a3b3-73c3bfffe25c"></a>

|
|
| **Resource** | **Link** |
| --- |--- |
| AWS Direct Connect User Guide | [https://docs.aws.amazon.com/directconnect/latest/UserGuide/](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) |
| IAM Best Practices for Cross-Account Access (ExternalId) | [https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_common-scenarios\_third-party.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) |
| The Confused Deputy Problem | [https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) |
| AWS STS AssumeRole API Reference | [https://docs.aws.amazon.com/STS/latest/APIReference/API\_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) |
| Direct Connect Resiliency Toolkit | [https://docs.aws.amazon.com/directconnect/latest/UserGuide/resilency\_toolkit.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resilency_toolkit.html) |
| CloudWatch Network Synthetic Monitor | [https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) |
| AWS Well-Architected Framework — Security Pillar | [https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/) |
| AWS Well-Architected Framework — Reliability Pillar | [https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/) |
| Revoking IAM Role Temporary Credentials | [https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_roles\_use\_revoke-sessions.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html) |
| EventBridge Cross-Account Event Delivery | [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html) |
| AWS Health Events | [https://docs.aws.amazon.com/health/latest/ug/](https://docs.aws.amazon.com/health/latest/ug/) |

## Tools for Testing and Automation
<a name="tools-for-testing-and-automation.022fe2bc-66d9-592f-a48e-b9850114e763"></a>

|
|
| Tool | Purpose |
| --- |--- |
| **AWS CLI** (`aws sts assume-role`) | Validate role assumption with/without ExternalId |
| **AWS CloudFormation** | Deploy and manage the framework stack (IaC) |
| **AWS CloudTrail** | Audit all WSP access patterns and API calls |
| **AWS Config** (where supported) | Governance validation — tag compliance monitoring via custom rules |
| **Amazon EventBridge** | Real-time DX state change notifications (Option 2) |
| **CloudWatch Network Synthetic Monitor** | Synthetic path monitoring and NHI fault isolation (Option 3) |
| **CloudWatch GetMetricData API** | Retrieve DX metrics programmatically (ConnectionState, LightLevel, BPS) |
| **Resource Groups Tagging API** (`tag:GetResources`) | Query DX resources by tag filter (`DXInfoSharing=enabled`) |
| **uuid generators** (`uuidgen` / Python `uuid4()`) | Generate ExternalId values |
| **jq** | Parse JSON output from AWS CLI role assumption and validation commands |
| **cfn-lint** | Validate CloudFormation templates before deployment |
| **ScoutSuite / Prowler** | Third-party security auditing tools to validate IAM least-privilege and detect overpermissioned roles |
