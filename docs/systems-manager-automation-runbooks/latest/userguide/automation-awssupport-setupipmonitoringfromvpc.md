---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-setupipmonitoringfromvpc.html
---

# `AWSSupport-SetupIPMonitoringFromVPC`

 **Description**

 `AWSSupport-SetupIPMonitoringFromVPC` creates a temporary Amazon Elastic Compute Cloud (Amazon EC2) instance running Amazon Linux 2023 in the specified subnet. The runbook continuously runs ping, MTR, traceroute, and tracetcp tests against the selected target IPs (IPv4 or IPv6). It stores the results in Amazon CloudWatch log groups and applies metric filters to quickly visualize latency and packet loss statistics in a CloudWatch dashboard.

**Additional costs**
This runbook incurs additional AWS costs. It provisions an Amazon EC2 instance, CloudWatch log groups, and a CloudWatch dashboard in your account using AWS CloudFormation. The test instance runs continuously until you delete the CloudFormation stack. If you set `RetainDashboardAndLogsOnDeletion` to `True` (default), the CloudWatch dashboard and log groups remain after stack deletion. These resources continue to incur charges until you manually remove them. For pricing details, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

 **Additional Information**

You can use the test results in Amazon CloudWatch Logs for network troubleshooting and analysis of patterns and trends. Additionally, you can configure CloudWatch alarms with Amazon Simple Notification Service notifications when packet loss or latency reaches a threshold. You can also use these results when opening a case with AWS Support, to help isolate an issue quickly and reduce time to resolution when investigating a network issue.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-SetupIPMonitoringFromVPC)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ CloudWatchLogGroupNamePrefix

  Type: String

   Default: `/AWSSupport-SetupIPMonitoringFromVPC`

  Description: (Optional) Prefix used for each CloudWatch log group created for the test results.
+ CloudWatchLogGroupRetentionInDays

  Type: String

  Valid values: 1 \| 3 \| 5 \| 7 \| 14 \| 30 \| 60 \| 90 \| 120 \| 150 \| 180 \| 365 \| 400 \| 545 \| 731 \| 1827 \| 3653

  Default: 7

  Description: (Optional) Number of days you want to keep the network monitoring results for.
+ InstanceType

  Type: String

  Valid values: t2.micro \| t2.small \| t2.medium \| t2.large \| t3.micro \| t3.small \| t3.medium \| t3.large \| t4g.micro \| t4g.small \| t4g.medium \| t4g.large

  Default: t3.micro

  Description: (Optional) The Amazon EC2 instance type for the monitoring instance. Recommended size: t3.micro.
+ SubnetId

  Type: String

  Description: (Required) The subnet ID for the monitor instance. Be aware that if you specify a private subnet, then you must make sure there is internet access to allow the monitor instance to set up the test (for example, install the CloudWatch agent, interact with AWS Systems Manager and CloudWatch).
+ TargetIPs

  Type: String

  Description: (Required) Comma-separated list of IPv4 or IPv6 addresses to monitor. No spaces allowed. Maximum size is 255 characters. Be aware that if you provide an invalid IP, then the automation will fail and roll back the test setup.
+ TestInstanceSecurityGroupId

  Type: String

  Description: (Optional) The security group ID for the test instance. If not specified, the automation creates one during the instance creation. Make sure the security group allows outbound access to the monitoring IPs.
+ TestInstanceProfileName

  Type: String

  Description: (Optional) The name of an existing AWS Identity and Access Management instance profile for the test instance. If not specified, the automation creates one during the instance creation. The role must have the following permissions: `logs:CreateLogStream`, `logs:DescribeLogGroups`, `logs:DescribeLogStreams`, and `logs:PutLogEvents` and the AWS Managed Policy `AmazonSSMManagedInstanceCore`.
+ TestInterval

  Type: String

  Description: (Optional) The number of minutes between test intervals. The default value is `1` minute and the maximum is `10` minutes.
+ RetainDashboardAndLogsOnDeletion

  Type: String

  Description: (Optional) Specify `False` to delete the CloudWatch dashboard and log groups when deleting the CloudFormation stack. The default value is `True`. By default, the runbook retains the dashboard and logs. You must manually delete them when they are no longer needed.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.

**Important**
We recommend that you pass the `TestInstanceProfileName` parameter. The example policy on this page assumes that you do. The IAM role inside that instance profile must trust `ec2.amazonaws.com`. It must also have the permissions listed for `TestInstanceProfileName`.
If you leave `TestInstanceProfileName` empty, the automation creates an IAM role and instance profile for the test instance. It deletes them with the CloudFormation stack. In that case, the `AutomationAssumeRole` needs the following extra permissions. The example policy doesn't grant them. Scope them to `role/SetupIPMonitoringFromVPC-*` and `instance-profile/SetupIPMonitoringFromVPC-*`:
`iam:CreateRole`, `iam:GetRole`, `iam:TagRole`, and `iam:DeleteRole`
`iam:PutRolePolicy`, `iam:GetRolePolicy`, and `iam:DeleteRolePolicy`
`iam:AttachRolePolicy` and `iam:DetachRolePolicy`
`iam:CreateInstanceProfile`, `iam:GetInstanceProfile`, `iam:AddRoleToInstanceProfile`, `iam:RemoveRoleFromInstanceProfile`, and `iam:DeleteInstanceProfile`
`iam:PassRole` on `role/SetupIPMonitoringFromVPC-*`, with `iam:PassedToService` set to `ec2.amazonaws.com`
If you grant these permissions to an untrusted principal, that principal can create an IAM role with elevated permissions and use it. This results in privilege escalation in your AWS account. Grant them only to the `AutomationAssumeRole`. Make sure security guardrails are in place to prevent misuse of mutable IAM permissions.

 It is recommended that the user who runs the automation have the **AmazonSSMAutomationRole** IAM managed policy attached. In addition, the user must have the following policy attached to their user account, group, or role. The policy scopes the log group permissions to the default `CloudWatchLogGroupNamePrefix`. If you use a different prefix, update the log group resource. In the following example, replace {{111122223333}} with your AWS account ID, {{TestInstanceProfile}} with the name of the instance profile that you pass in `TestInstanceProfileName`, and {{TestInstanceRole}} with the name of the IAM role inside that instance profile:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadTestInstanceProfile",
            "Action": "iam:GetInstanceProfile",
            "Resource": "arn:aws:iam::{{111122223333}}:instance-profile/{{TestInstanceProfile}}",
            "Effect": "Allow"
        },
        {
            "Sid": "PassTestInstanceRole",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{TestInstanceRole}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "ActionsWithoutResourceLevelPermissions",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeInstanceTypes",
                "ec2:DescribeLaunchTemplates",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ssm:DescribeInstanceInformation",
                "ssm:ListCommands",
                "ssm:ListCommandInvocations"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Sid": "CloudFormationStack",
            "Action": [
                "cloudformation:CreateChangeSet",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStacks"
            ],
            "Resource": "arn:aws:cloudformation:*:{{111122223333}}:stack/AWSSupport-SetupIPMonitoringFromVPC-*",
            "Effect": "Allow"
        },
        {
            "Sid": "CloudFormationLanguageExtensions",
            "Action": "cloudformation:CreateChangeSet",
            "Resource": "arn:aws:cloudformation:*:aws:transform/LanguageExtensions",
            "Effect": "Allow"
        },
        {
            "Sid": "ReadAmazonLinuxAmiParameters",
            "Action": "ssm:GetParameters",
            "Resource": "arn:aws:ssm:*::parameter/aws/service/ami-amazon-linux-latest/*",
            "Effect": "Allow"
        },
        {
            "Sid": "CreateLaunchTemplate",
            "Action": "ec2:CreateLaunchTemplate",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
            "Effect": "Allow"
        },
        {
            "Sid": "CreateTaggedSecurityGroup",
            "Action": "ec2:CreateSecurityGroup",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:security-group/*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/AWSSupport-SetupIPMonitoringFromVPC-AutomationExecution": "false"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "CreateSecurityGroupInVpc",
            "Action": "ec2:CreateSecurityGroup",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:vpc/*",
            "Effect": "Allow"
        },
        {
            "Sid": "RunInstancesWithAmazonImage",
            "Action": "ec2:RunInstances",
            "Resource": "arn:aws:ec2:*::image/*",
            "Condition": {
                "StringEquals": {
                    "ec2:Owner": "amazon"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "RunInstancesResources",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
                "arn:aws:ec2:*:{{111122223333}}:network-interface/*",
                "arn:aws:ec2:*:{{111122223333}}:security-group/*",
                "arn:aws:ec2:*:{{111122223333}}:subnet/*",
                "arn:aws:ec2:*:{{111122223333}}:volume/*"
            ],
            "Effect": "Allow"
        },
        {
            "Sid": "RunTaggedInstance",
            "Action": "ec2:RunInstances",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:instance/*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/AWSSupport-SetupIPMonitoringFromVPC-AutomationExecution": "false"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "TagOnCreateOnly",
            "Action": "ec2:CreateTags",
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:instance/*",
                "arn:aws:ec2:*:{{111122223333}}:network-interface/*",
                "arn:aws:ec2:*:{{111122223333}}:security-group/*",
                "arn:aws:ec2:*:{{111122223333}}:volume/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": [
                        "CreateSecurityGroup",
                        "RunInstances"
                    ]
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "ManageTaggedResources",
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:DeleteSecurityGroup",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:TerminateInstances"
            ],
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:instance/*",
                "arn:aws:ec2:*:{{111122223333}}:security-group/*"
            ],
            "Condition": {
                "Null": {
                    "aws:ResourceTag/AWSSupport-SetupIPMonitoringFromVPC-AutomationExecution": "false"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "DeleteLaunchTemplateThroughCloudFormation",
            "Action": "ec2:DeleteLaunchTemplate",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": "cloudformation.amazonaws.com"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "RunShellScriptDocument",
            "Action": "ssm:SendCommand",
            "Resource": "arn:aws:ssm:*::document/AWS-RunShellScript",
            "Effect": "Allow"
        },
        {
            "Sid": "SendCommandToTaggedInstance",
            "Action": "ssm:SendCommand",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:instance/*",
            "Condition": {
                "Null": {
                    "ssm:resourceTag/AWSSupport-SetupIPMonitoringFromVPC-AutomationExecution": "false"
                }
            },
            "Effect": "Allow"
        },
        {
            "Sid": "TestResultLogGroups",
            "Action": [
                "logs:CreateLogGroup",
                "logs:DeleteLogGroup",
                "logs:PutMetricFilter",
                "logs:PutRetentionPolicy",
                "logs:TagResource"
            ],
            "Resource": "arn:aws:logs:*:{{111122223333}}:log-group:/AWSSupport-SetupIPMonitoringFromVPC*",
            "Effect": "Allow"
        },
        {
            "Sid": "TestResultDashboard",
            "Action": [
                "cloudwatch:DeleteDashboards",
                "cloudwatch:PutDashboard"
            ],
            "Resource": "arn:aws:cloudwatch::{{111122223333}}:dashboard/subnet-*",
            "Effect": "Allow"
        }
    ]
}
```

 **Document Steps**

1.  ** `aws:executeAwsApi` ** - describe the provided subnet to get the VPC ID and IPv6 CIDR block association state.

1.  ** `aws:executeScript` ** - validate the provided target IPs are syntactically correct IPv4 and/or IPv6 addresses, get the architecture of the selected instance type, and verify the subnet has an IPv6 pool association if any target IP is IPv6.

1.  ** `aws:createStack` ** - create a CloudFormation stack that provisions the test Amazon EC2 instance, IAM instance profile (if not provided), security group (if not provided), CloudWatch log groups, and CloudWatch dashboard.

   (Cleanup) If the step fails:

    ** `aws:executeScript` ** - describe the CloudFormation stack events to identify the failure reason.

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:waitForAwsResourceProperty` ** - wait for the CloudFormation stack to complete creation.

   (Cleanup) If the step fails:

    ** `aws:executeScript` ** - describe the CloudFormation stack events to identify the failure reason.

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:executeScript` ** - describe the CloudFormation stack resources to get the test instance ID, security group ID, IAM role, instance profile, and dashboard name.

   (Cleanup) If the step fails:

    ** `aws:executeScript` ** - describe the CloudFormation stack events to identify the failure reason.

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:waitForAwsResourceProperty` ** - wait for the test instance to become a managed instance.

   (Cleanup) If the step fails:

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:runCommand` ** - install the CloudWatch agent, `mtr`, and `traceroute` on the test instance.

   (Cleanup) If the step fails:

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:runCommand` ** - define the network test scripts (MTR, ping, tracepath, and traceroute) for each of the provided IPs.

   (Cleanup) If the step fails:

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:runCommand` ** - start the network tests and schedule subsequent executions using systemd timers that run every TestInterval minutes.

   (Cleanup) If the step fails:

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:runCommand` ** - configure the CloudWatch agent to push test results from `/home/ec2-user/logs/` to CloudWatch Logs.

   (Cleanup) If the step fails:

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:runCommand` ** - configure log rotation for the test results in `/home/ec2-user/logs/`.

1.  ** `aws:executeScript` ** - set the retention policy for all CloudWatch log groups created by the CloudFormation stack.

1.  ** `aws:executeScript` ** - create CloudWatch log group metric filters for ping latency and ping packet loss.

   (Cleanup) If the step fails:

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:executeScript` ** - update the CloudWatch dashboard to include widgets for ping latency and ping packet loss statistics.

   (Cleanup) If the step fails:

    ** `aws:executeAwsApi` ** - delete the CloudWatch dashboard, if it exists.

    ** `aws:deleteStack` ** - delete the CloudFormation stack and all associated resources.

1.  ** `aws:branch` ** - evaluate the SleepTime parameter. If set to `0`, the automation ends without deleting the stack.

1.  ** `aws:sleep` ** - wait for the specified SleepTime duration before deleting the CloudFormation stack.

1.  ** `aws:deleteStack` ** - delete the CloudFormation stack. Based on the RetainDashboardAndLogsOnDeletion parameter, the CloudWatch dashboard and log groups are either retained or deleted.

   (Cleanup) If the stack deletion fails:

    ** `aws:executeScript` ** - describe the CloudFormation stack events to identify the deletion failure reason.

 **Outputs**

updateCloudWatchDashboard.StackUrl - the URL of the CloudFormation stack.

updateCloudWatchDashboard.DashboardUrl - the URL of the CloudWatch dashboard.

updateCloudWatchDashboard.DashboardName - the name of the CloudWatch dashboard.

updateCloudWatchDashboard.LogGroups - the list of CloudWatch log groups created.

describeStackResources.HelperInstanceId - the test instance ID.

describeStackResources.StackName - the CloudFormation stack name.
