---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-schedulerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application SchedulerConfiguration
<a name="aws-properties-emrserverless-application-schedulerconfiguration"></a>

The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.

## Syntax
<a name="aws-properties-emrserverless-application-schedulerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-schedulerconfiguration-syntax.json"></a>

```
{
  "[MaxConcurrentRuns](#cfn-emrserverless-application-schedulerconfiguration-maxconcurrentruns)" : {{Integer}},
  "[QueueTimeoutMinutes](#cfn-emrserverless-application-schedulerconfiguration-queuetimeoutminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-schedulerconfiguration-syntax.yaml"></a>

```
  [MaxConcurrentRuns](#cfn-emrserverless-application-schedulerconfiguration-maxconcurrentruns): {{Integer}}
  [QueueTimeoutMinutes](#cfn-emrserverless-application-schedulerconfiguration-queuetimeoutminutes): {{Integer}}
```

## Properties
<a name="aws-properties-emrserverless-application-schedulerconfiguration-properties"></a>

`MaxConcurrentRuns`  <a name="cfn-emrserverless-application-schedulerconfiguration-maxconcurrentruns"></a>
The maximum concurrent job runs on this application. If scheduler configuration is enabled on your application, the default value is 15. The valid range is 1 to 1000.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`QueueTimeoutMinutes`  <a name="cfn-emrserverless-application-schedulerconfiguration-queuetimeoutminutes"></a>
The maximum duration in minutes for the job in QUEUED state. If scheduler configuration is enabled on your application, the default value is 360 minutes (6 hours). The valid range is from 15 to 720.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
