---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/custom.html
---

# Custom controls

After you have conducted your risk assessment, identified your security and compliance requirements, and selected the AWS Control Tower controls to guardrail these requirements, there might be some requirements that still aren't addressed. You can implement custom service control policies (SCPs), AWS Config Rules, and CloudFormation Hooks to cover these requirements. However, these controls aren't implemented as AWS Control Tower controls—they're implemented outside AWS Control Tower.

The following table provides examples of custom controls that you can append to your controls table.

|
|
| Control | Guidance level | Behavior | Security OU | Infrastructure OU | Suspended OU | Workloads OU | Deployments OU | Sandbox OU | Purpose |   |
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| Protect Amazon CloudWatch | Custom SCP | Preventive | Yes | Yes | Yes | Yes | Yes | No | Deny `cloudwatch:DeleteAlarms`, `cloudwatch:DeleteDashboards`, `cloudwatch:DisableAlarmActions`, `cloudwatch:PutDashboard`, `cloudwatch:PutMetricAlarm`, `cloudwatch:SetAlarmState` |   |
| Enforce encryption for Amazon S3 buckets | Custom SCP | Preventive | Yes | Yes | Yes | Yes | Yes | No | Deny `s3:PutObject` on the condition that encryption is `false` |   |
| IAM user creation | Custom SCP | Preventive | Yes | Yes | Yes | Yes | Yes | Yes | Deny `iam:CreateUser` |   |
| Protect account and billing settings | Custom SCP | Preventive | Yes | Yes | Yes | Yes | Yes | Yes | Deny `aws-portal:ModifyAccount`, `aws-portal:ModifyBilling`, `aws-portal:ModifyPaymentMethods` |   |
