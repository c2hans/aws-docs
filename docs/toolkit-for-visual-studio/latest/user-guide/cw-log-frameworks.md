---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/cw-log-frameworks.html
---

# Tutorial: Using Amazon Logging Frameworks with AWS Lambda to Create Application Logs
<a name="cw-log-frameworks"></a>

You can use Amazon CloudWatch Logs to monitor, store, and access your application’s logs. To get log data into CloudWatch Logs, use an AWS SDK or install the CloudWatch Logs agent to monitor certain log folders. CloudWatch Logs is integrated with several popular .NET logging frameworks, simplifying work flows.

To get started working with CloudWatch Logs and .NET logging frameworks, add the appropriate NuGet package and CloudWatch Logs output source to your application, then use your logging library as you normally would. This enables your application to log messages with your .NET framework, sending them to CloudWatch Logs, displaying your application’s log messages in the CloudWatch Logs console. You can also set up metrics and alarms from the CloudWatch Logs console, based on your application’s log messages.

Supported .NET logging frameworks include:
+ **NLog**: To view, see the [nuget.org NLog package](https://www.nuget.org/packages/AWS.Logger.NLog).
+ **Log4net**: To view, see the [nuget.org Log4net package](https://www.nuget.org/packages/AWS.Logger.NLog).
+ **ASP.NET Core logging Framework**: To view, see the [nuget.org ASP.NET Core logging Framework package](https://www.nuget.org/packages/AWS.Logger.AspNetCore/).

The following is an example of an `NLog.config` file that enables both CloudWatch Logs and the console as output for log messages by adding the `AWS.Logger.NLog` NuGet package, and AWS target into `NLog.config`.

```
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      throwExceptions="true">
  <targets>
    <target name="aws" type="AWSTarget" logGroup="NLog.ConfigExample" region="us-east-1"/>
    <target name="logfile" xsi:type="Console" layout="${callsite} ${message}" />
  </targets>
  <rules>
    <logger name="*" minlevel="Info" writeTo="logfile,aws" />
  </rules>
</nlog>
```

The logging plugins are all built on top of the AWS SDK for .NET and authenticate your AWS credentials in a process similar to the SDK. The following example details permissions required by the logging plugin credentials to access CloudWatch Logs:

**Note**
The AWS .NET logging plugins are an open source project. For additional information, samples, and instructions, see the [samples](https://github.com/aws/aws-logging-dotnet/tree/master/samples) and [instructions](https://github.com/aws/aws-logging-dotnet/blob/master/README.md) topics in the [AWS Logging .NET GitHub](https://github.com/aws/aws-logging-dotnet) repository.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups"
      ],
      "Resource": [
        "arn:aws:logs:*:*:*"
      ]
    }
  ]
}
```

------
