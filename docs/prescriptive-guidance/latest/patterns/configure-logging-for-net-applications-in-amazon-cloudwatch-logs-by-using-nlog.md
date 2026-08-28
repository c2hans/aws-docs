---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog.html
---

# Configure logging for .NET applications in Amazon CloudWatch Logs by using NLog
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog"></a>

*Bibhuti Sahu and Rob Hill (AWS), Amazon Web Services*

## Summary
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-summary"></a>

This pattern describes how to use the NLog open-source logging framework to log .NET application usage and events in [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). In the CloudWatch console, you can view the application’s log messages in near real time. You can also set up [metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) and configure [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) to notify you if a metric threshold is exceeded. Using CloudWatch Application Insights, you can view automated or custom dashboards that show potential problems for the monitored applications. CloudWatch Application Insights is designed to help you quickly isolate ongoing issues with your applications and infrastructure.

To write log messages to CloudWatch Logs, you add the `AWS.Logger.NLog` NuGet package to the .NET project. Then, you update the `NLog.config` file to use CloudWatch Logs as a target.

## Prerequisites and limitations
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A .NET web or console application that:
  + Uses supported .NET Framework or .NET Core versions. For more information, see *Product versions*.
  + Uses NLog to send log data to Application Insights.
+ Permissions to create an IAM role for an AWS service. For more information, see [Service role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#id_roles_create_service-permissions).
+ Permissions to pass a role to an AWS service. For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).

**Product versions**
+ .NET Framework version 3.5 or later
+ .NET Core versions 1.0.1, 2.0.0, or later

## Architecture
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-architecture"></a>

**Target technology stack  **
+ NLog
+ Amazon CloudWatch Logs

**Target architecture**

![Architecture diagram of NLog writing log data for a .NET application to Amazon ClodWatch Logs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0ac9c3ad-2a28-415f-afc3-7fe3494b2b63/images/daea9f2f-7242-4ed2-843e-655d843dcfdf.png)

1. The .NET application writes log data to the NLog logging framework.

1. NLog writes the log data to CloudWatch Logs.

1. You use CloudWatch alarms and custom dashboards to monitor the .NET application.

## Tools
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-tools"></a>

**AWS services**
+ [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) helps you observe the health of your applications and underlying AWS resources.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) are a set of PowerShell modules that help you script operations on your AWS resources from the PowerShell command line.

**Other tools**
+ [Logger.NLog](https://www.nuget.org/packages/AWS.Logger.NLog) is an NLog target that records log data to CloudWatch Logs.
+ [NLog](https://nlog-project.org/) is an open-source logging framework for .NET platforms that helps you write log data to targets, such as databases, log files, or consoles.
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.
+ [Visual Studio](https://docs.microsoft.com/en-us/visualstudio/get-started/visual-studio-ide?view=vs-2022) is an integrated development environment (IDE) that includes compilers, code completion tools, graphical designers, and other features that support software development.

## Best practices
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-best-practices"></a>
+ Set a [retention policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) for the target log group. This must be done outside of the NLog configuration. By default, log data is stored in CloudWatch Logs indefinitely.
+ Adhere to the [Best practices for managing AWS access keys](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html).

## Epics
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-epics"></a>

### Set up access and tools
<a name="set-up-access-and-tools"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM policy. | Follow the instructions in [Creating policies using the JSON editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor) in the IAM documentation. Enter the following JSON policy, which has the least-privilege permissions necessary to allow CloudWatch Logs to read and write logs.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "logs:CreateLogGroup",<br />                "logs:CreateLogStream",<br />                "logs:GetLogEvents",<br />                "logs:PutLogEvents",<br />                "logs:DescribeLogGroups",<br />                "logs:DescribeLogStreams",<br />                "logs:PutRetentionPolicy"<br />            ],<br />            "Resource": [<br />                "*"<br />            ]<br />        }<br />    ]<br />}</pre> | AWS administrator, AWS DevOps |
| Create an IAM role. | Follow the instructions in [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the IAM documentation. Select the policy that you created previously. This is the role CloudWatch Logs assumes to perform logging actions. | AWS administrator, AWS DevOps |
| Set up AWS Tools for PowerShell. | 1. Follow the instructions for your operating system in [Installing the AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html).<br />2. Use the AWS Tools for PowerShell cmdlets to store your access key and secret key in a profile. For instructions, see [Managing Profiles](https://docs.aws.amazon.com/powershell/latest/userguide/specifying-your-aws-credentials.html#managing-profiles) in the AWS Tools for PowerShell documentation. | General AWS |

### Configure NLog
<a name="configure-nlog"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the NuGet package. | 1. In Visual Studio, choose **File**, and then choose **Open a project or solution**.<br />2. Choose the project where you want to install NLog.<br />3. In Visual Studio, choose **Tools**, **NuGet Package Manager**, **Package Manager Console**.<br />4. Install the `AWS.Logger.NLog` NuGet package by entering the following command.<pre>Install-Package AWS.Logger.NLog -Version 3.1.0</pre> | App developer |
| Configure the logging target. | 1. Open the `NLog.config` file.<br />2. For the target `type`, enter `AWSTarget`.<br />3. For the target `logGroup`, enter the name of the [log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) that you want to use. If the log group doesn't already exist, a new log group with the provided name is automatically created.<br />4. For the target `region`, enter the AWS Region where CloudWatch Logs is configured.<br />5. For the target `profile`, enter the name of the profile that you created previously to store to store the access key and secret key.<br />6. Save and close the `NLog.config` file.For a sample configuration file, see the [Additional information](#configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-additional) section of this pattern. When you run your application, NLog will write the log messages and send them to CloudWatch Logs. | App developer |

### Validate and monitor logs
<a name="validate-and-monitor-logs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate logging. | Follow the instructions in [View log data sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#ViewingLogData) in the CloudWatch Logs documentation. Validate that log events are being recorded for the .NET application. If log events are not being recorded, see the [Troubleshooting](#configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-troubleshooting) section in this pattern. | General AWS |
| Monitor the .NET application stack. | Configure monitoring in CloudWatch as needed for your use case. You can use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), [CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html), and [CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) to monitor your .NET workload. You can also configure [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) so that you can receive alerts, and you can create a custom [dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) for monitoring the workload from a single view. | General AWS |

## Troubleshooting
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Log data doesn’t appear in CloudWatch Logs. | Make sure that the IAM policy is attached to the IAM role that CloudWatch Logs assumes. For instructions, see the *Set up access and tools* section in the [Epics](#configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-epics) section. |

## Related resources
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-resources"></a>
+ [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) (CloudWatch Logs documentation)
+ [Amazon CloudWatch Logs and .NET Logging Frameworks](https://aws.amazon.com/blogs/developer/amazon-cloudwatch-logs-and-net-logging-frameworks/) (AWS blog post)

## Additional information
<a name="configure-logging-for-net-applications-in-amazon-cloudwatch-logs-by-using-nlog-additional"></a>

The following is a sample `NLog.config` file.

```
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <configSections>
    <section name="nlog" type="NLog.Config.ConfigSectionHandler, NLog" />
  </configSections>
  <startup>
    <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" />
  </startup>
  <nlog>
    <extensions>
      <add assembly="NLog.AWS.Logger" />
    </extensions>
    <targets>
      <target name="aws" type="AWSTarget" logGroup="NLog.TestGroup" region="us-east-1" profile="demo"/>
    </targets>
    <rules>
      <logger name="*" minlevel="Info" writeTo="aws" />
    </rules>
  </nlog>
</configuration>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
