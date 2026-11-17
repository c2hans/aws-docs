---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog.html
---

# Configure logging for .NET applications in Amazon CloudWatch Logs by using NLog
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog"></a>

*Bibhuti Sahu and Rob Hill (AWS), Amazon Web Services*

## Summary
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-summary"></a>

This pattern describes how to use the NLog open-source logging framework to send .NET application logs and events to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). In the [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) console, you can view log messages in near real time, create [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html), and configure [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) that notify you when a threshold is breached. With Amazon CloudWatch Application Insights, you can use automated or custom dashboards to help identify problems in your applications and infrastructure.

To write log messages to CloudWatch Logs, you add the AWS.Logger.NLog NuGet package to your .NET project and configure CloudWatch Logs as an NLog target. The application authenticates by using temporary credentials from an [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/) role instead of long-term access keys. A retention policy and encryption with [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/) help protect the log group.

## Prerequisites and limitations
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A .NET web or console application that targets a supported .NET version (see *Product versions*) and uses NLog for application logging.
+ Permissions to create IAM policies and roles, and to pass a role to an AWS service. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) and [Grant a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).
+ A compute environment that can use an IAM role, such as [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), or [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elastic-beanstalk/). For on-premises servers, use AWS Identity and Access Management Roles Anywhere. For local development, use an [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/) user.
+ (Optional) An AWS KMS customer managed key for log group encryption.

**Limitations**
+ You configure retention, encryption, and data protection settings on the log group, not through the NLog configuration.
+ CloudWatch Logs service quotas apply, such as the `PutLogEvents` API batch size and request rate. AWS.Logger.NLog automatically batches and retries requests.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Product versions**
+ .NET 10 (LTS)
+ .NET Framework 4.8 or 4.8.1 (Windows)
+ AWS.Logger.NLog 5.0.1 or later, and NLog 5.x or later
+ AWS Tools for PowerShell V5 (optional, for the setup commands)
+ Visual Studio 2022 or later, or the .NET CLI

## Architecture
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-architecture"></a>

**Target technology stack  **
+ NLog with the AWS.Logger.NLog target
+ Amazon CloudWatch Logs, encrypted with AWS KMS
+ IAM role that provides temporary credentials

**Target architecture**

![Architecture diagram of NLog writing log data for a .NET application to Amazon CloudWatch Logs.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0ac9c3ad-2a28-415f-afc3-7fe3494b2b63/images/daea9f2f-7242-4ed2-843e-655d843dcfdf.png)

1. The .NET application writes log events to the NLog framework.

1. The AWS.Logger.NLog target gets temporary credentials from the IAM role attached to the compute environment, through the AWS SDK for .NET default credential chain.

1. The target sends batched log events to a CloudWatch Logs log group that uses AWS KMS encryption.

1. You use metric filters, alarms, CloudWatch Logs Insights, and dashboards to monitor the application.

## Tools
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-tools"></a>

**AWS services**
+ [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) helps you observe the health of your applications and underlying AWS resources.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) are a set of PowerShell modules that help you script operations on your AWS resources from the PowerShell command line.

**Other tools**
+ [AWS.Logger.NLog](https://www.nuget.org/packages/AWS.Logger.NLog) is an NLog target that records log data to CloudWatch Logs.
+ [NLog](https://nlog-project.org/) is an open-source logging framework for .NET platforms that helps you write log data to targets such as databases, log files, or consoles.
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.
+ [Visual Studio](https://learn.microsoft.com/en-us/visualstudio/get-started/visual-studio-ide) is an integrated development environment (IDE) that includes compilers, code completion tools, graphical designers, and other features that support software development.

## Best practices
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-best-practices"></a>
+ **Use temporary credentials.** Attach an IAM role to the compute resource. Don’t embed access keys in code or in NLog.config. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).
+ **Apply least privilege.** Grant only the write actions that the logger needs, scoped to the Amazon Resource Name (ARN) of the specific log group.
+ **Set a retention policy.** By default, CloudWatch Logs keeps log data indefinitely. Set retention on the log group, outside of the NLog configuration.
+ **Encrypt log data.** Associate an AWS KMS customer managed key with the log group. For more information, see [Encrypt log data in CloudWatch Logs using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).
+ **Protect sensitive data.** Don’t log secrets, tokens, or personal data. Add a [data protection policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) to detect and mask sensitive data.
+ **Use private connectivity.** For workloads in private subnets, use an interface endpoint in [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/) (Amazon VPC) for CloudWatch Logs (`com.amazonaws.<region>.logs`).
+ **Set log levels for production.** Set the minimum log level to Info or higher in production to help control cost and reduce noise.

## Epics
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-epics"></a>

### Set up access and tools
<a name="set-up-access-and-tools"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the log group and IAM policy. | Create the log group in advance so that you can apply retention and encryption and scope IAM permissions to it. Use [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html) to run the following commands:<pre>New-CWLLogGroup -LogGroupName "NLog.TestGroup" `<br />  -KmsKeyId "arn:aws:kms:<region>:111122223333:key/<key-id>"<br /><br />Write-CWLRetentionPolicy -LogGroupName "NLog.TestGroup" -RetentionInDays 90</pre><br />Then follow the instructions in [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html). Use the least-privilege policy in the *Additional information* section. It allows only the write actions that the logger needs, on the specific log group. | AWS administrator, AWS DevOps |
| Create an IAM role for the compute environment. | Follow the instructions in [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). Choose the service that runs your application (for example, Amazon EC2 or an [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) task), and attach the policy that you created. The application’s compute resource, not CloudWatch Logs, assumes this role. A sample trust policy is in the *Additional information* section. | AWS administrator, AWS DevOps |
| Attach the role to the application. | + For Amazon EC2, attach the role as an instance profile.<br />+ For Amazon ECS, set the role as the task role in the task definition.<br />+ For [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/), use Amazon EKS Pod Identity or IAM roles for service accounts (IRSA).<br />+ For AWS Lambda, use the function’s execution role.<br />+ For on-premises servers, use AWS Identity and Access Management Roles Anywhere.<br />+ (Local development only) Install [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html), and sign in with IAM Identity Center to get short-term credentials. Don’t store long-term access keys. For more information, see [Configure tool authentication](https://docs.aws.amazon.com/powershell/latest/userguide/specifying-your-aws-credentials.html). | AWS administrator, AWS DevOps |

### Configure NLog
<a name="configure-nlog"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the NuGet package. | From the project directory, run the following command:<pre>dotnet add package AWS.Logger.NLog --version 5.0.1</pre><br />Alternatively, in the Visual Studio Package Manager Console (**Tools**, **NuGet Package Manager**, **Package Manager Console**), run the following command:<pre>Install-Package AWS.Logger.NLog -Version 5.0.1</pre> | App developer |
| Configure the logging target. | + Open the NLog.config file (or the NLog section of appsettings.json).<br />+ For the target type, enter `AWSTarget`.<br />+ For `logGroup`, enter the name of the log group that you created.<br />+ For `region`, enter the AWS Region of the log group.<br />+ When the application runs on AWS, don’t set a profile, access key, or secret key. The target uses the IAM role automatically.For sample configurations, see the *Additional information* section. When you run your application, NLog writes the log messages and sends them to CloudWatch Logs. | App developer |

### Validate and monitor logs
<a name="validate-and-monitor-logs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate logging. | Run the application, and then follow the instructions in [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) to view log events for the .NET application. If no events appear, see the *Troubleshooting* section. | General AWS |
| Monitor the .NET application stack. | Use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), [CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html), and [CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) to monitor your .NET workload. Configure [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to receive alerts, and create a [dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) to view your key metrics and logs in one place.<br />(Optional) To mask personal data and credentials, add a data protection policy to the log group. For instructions, see [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html). | General AWS |

## Troubleshooting
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Log data doesn’t appear in CloudWatch Logs. | Confirm that the IAM policy is attached to the role that the application’s compute resource uses (instance profile, task role, or execution role), and that the `logGroup` and `region` values in NLog.config match the log group. |
| AccessDeniedException appears in the NLog internal log. | Check that the Amazon Resource Name (ARN) in the `Resource` element of the IAM policy matches the log group name, Region, and account. If the log group is encrypted, check that the AWS KMS key policy allows the CloudWatch Logs service principal for that Region (`logs.<region>.amazonaws.com`). |
| The application can’t find AWS credentials. | When running on AWS, verify that the IAM role is attached to the compute resource (instance profile, task role, or execution role). For local development, sign in again with IAM Identity Center to refresh the session. Don’t use long-term access keys as a workaround. |
| The application writes logs to an unexpected AWS Region. | Set the `AWS_REGION` environment variable for the application, or add the `region` attribute to the `AWSTarget`. If neither is set, the AWS SDK for .NET uses the Region from the shared config profile or from Amazon EC2 instance metadata. |
| You need to diagnose NLog target errors. | On the `nlog` element, set `internalLogLevel="Warn"` and `internalLogFile` to a file path. Then review the file for exceptions from the AWS target. Turn off internal logging after you finish troubleshooting. |

## Related resources
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-resources"></a>
+ [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) (CloudWatch Logs documentation)
+ [Encrypt log data in CloudWatch Logs using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html) (CloudWatch Logs documentation)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)
+ [Amazon CloudWatch Logs and .NET Logging Frameworks](https://aws.amazon.com/blogs/developer/amazon-cloudwatch-logs-and-net-logging-frameworks/) (AWS blog post)

## Additional information
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-additional"></a>

**Least-privilege IAM policy**

Replace the Region, account ID, and log group name with your own values. If you create the log group in advance (recommended), you can remove `logs:CreateLogGroup`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "WriteAppLogs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": [
        "arn:aws:logs:<region>:111122223333:log-group:NLog.TestGroup",
        "arn:aws:logs:<region>:111122223333:log-group:NLog.TestGroup:log-stream:*"
      ]
    },
    {
      "Sid": "DescribeGroups",
      "Effect": "Allow",
      "Action": "logs:DescribeLogGroups",
      "Resource": "arn:aws:logs:<region>:111122223333:log-group:*"
    }
  ]
}
```

**Sample trust policy (Amazon EC2)**

For Amazon ECS, use `ecs-tasks.amazonaws.com`. For AWS Lambda, use `lambda.amazonaws.com`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "ec2.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Sample NLog.config (.NET 10)**

```
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      internalLogLevel="Warn" internalLogFile="logs/nlog-internal.log">
  <extensions>
    <add assembly="NLog.AWS.Logger" />
  </extensions>
  <targets>
    <target name="aws" type="AWSTarget" logGroup="NLog.TestGroup" />
  </targets>
  <rules>
    <logger name="*" minlevel="Info" writeTo="aws" />
  </rules>
</nlog>
```

**Sample app.config (.NET Framework 4.8)**

```
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <configSections>
    <section name="nlog" type="NLog.Config.ConfigSectionHandler, NLog" />
  </configSections>
  <startup>
    <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.8" />
  </startup>
  <nlog>
    <extensions>
      <add assembly="NLog.AWS.Logger" />
    </extensions>
    <targets>
      <target name="aws" type="AWSTarget" logGroup="NLog.TestGroup" />
    </targets>
    <rules>
      <logger name="*" minlevel="Info" writeTo="aws" />
    </rules>
  </nlog>
</configuration>
```

This sample omits the `region` attribute so that the AWS SDK for .NET resolves the Region from the environment: the `AWS_REGION` environment variable, the shared config profile, or Amazon EC2 instance or Amazon ECS task metadata. To set it explicitly, add `region="<your-aws-region>"` to the target. Replace `<region>` and the account ID in the Amazon Resource Names (ARNs) in the IAM policy with your own values.
