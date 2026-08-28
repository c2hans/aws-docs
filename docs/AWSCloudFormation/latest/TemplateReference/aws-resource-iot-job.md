---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-job.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job
<a name="aws-resource-iot-job"></a>

Creates a job.

Requires permission to access the [CreateJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Syntax
<a name="aws-resource-iot-job-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-job-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::Job",
  "Properties" : {
      "[AbortConfig](#cfn-iot-job-abortconfig)" : {{AbortConfig}},
      "[Description](#cfn-iot-job-description)" : {{String}},
      "[DestinationPackageVersions](#cfn-iot-job-destinationpackageversions)" : {{[ String, ... ]}},
      "[Document](#cfn-iot-job-document)" : {{String}},
      "[DocumentParameters](#cfn-iot-job-documentparameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[DocumentSource](#cfn-iot-job-documentsource)" : {{String}},
      "[JobExecutionsRetryConfig](#cfn-iot-job-jobexecutionsretryconfig)" : {{JobExecutionsRetryConfig}},
      "[JobExecutionsRolloutConfig](#cfn-iot-job-jobexecutionsrolloutconfig)" : {{JobExecutionsRolloutConfig}},
      "[JobId](#cfn-iot-job-jobid)" : {{String}},
      "[JobTemplateArn](#cfn-iot-job-jobtemplatearn)" : {{String}},
      "[PresignedUrlConfig](#cfn-iot-job-presignedurlconfig)" : {{PresignedUrlConfig}},
      "[SchedulingConfig](#cfn-iot-job-schedulingconfig)" : {{SchedulingConfig}},
      "[Tags](#cfn-iot-job-tags)" : {{[ Tag, ... ]}},
      "[Targets](#cfn-iot-job-targets)" : {{[ String, ... ]}},
      "[TargetSelection](#cfn-iot-job-targetselection)" : {{String}},
      "[TimeoutConfig](#cfn-iot-job-timeoutconfig)" : {{TimeoutConfig}}
    }
}
```

### YAML
<a name="aws-resource-iot-job-syntax.yaml"></a>

```
Type: AWS::IoT::Job
Properties:
  [AbortConfig](#cfn-iot-job-abortconfig): {{
    AbortConfig}}
  [Description](#cfn-iot-job-description): {{String}}
  [DestinationPackageVersions](#cfn-iot-job-destinationpackageversions): {{
    - String}}
  [Document](#cfn-iot-job-document): {{String}}
  [DocumentParameters](#cfn-iot-job-documentparameters): {{
    {{Key}}: {{Value}}}}
  [DocumentSource](#cfn-iot-job-documentsource): {{String}}
  [JobExecutionsRetryConfig](#cfn-iot-job-jobexecutionsretryconfig): {{
    JobExecutionsRetryConfig}}
  [JobExecutionsRolloutConfig](#cfn-iot-job-jobexecutionsrolloutconfig): {{
    JobExecutionsRolloutConfig}}
  [JobId](#cfn-iot-job-jobid): {{String}}
  [JobTemplateArn](#cfn-iot-job-jobtemplatearn): {{String}}
  [PresignedUrlConfig](#cfn-iot-job-presignedurlconfig): {{
    PresignedUrlConfig}}
  [SchedulingConfig](#cfn-iot-job-schedulingconfig): {{
    SchedulingConfig}}
  [Tags](#cfn-iot-job-tags): {{
    - Tag}}
  [Targets](#cfn-iot-job-targets): {{
    - String}}
  [TargetSelection](#cfn-iot-job-targetselection): {{String}}
  [TimeoutConfig](#cfn-iot-job-timeoutconfig): {{
    TimeoutConfig}}
```

## Properties
<a name="aws-resource-iot-job-properties"></a>

`AbortConfig`  <a name="cfn-iot-job-abortconfig"></a>
Configuration for criteria to abort the job.
*Required*: No
*Type*: [AbortConfig](aws-properties-iot-job-abortconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iot-job-description"></a>
A short text description of the job.
*Required*: No
*Type*: String
*Pattern*: `^[^\p{C}]+$`
*Minimum*: `1`
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPackageVersions`  <a name="cfn-iot-job-destinationpackageversions"></a>
The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
**Note:**The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Document`  <a name="cfn-iot-job-document"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `32768`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DocumentParameters`  <a name="cfn-iot-job-documentparameters"></a>
A key-value map that pairs the patterns that need to be replaced in a managed template job document schema. You can use the description of each key as a guidance to specify the inputs during runtime when creating a job.
`documentParameters` can only be used when creating jobs from AWS managed templates. This parameter can't be used with custom job templates or to create jobs from them.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `30720`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DocumentSource`  <a name="cfn-iot-job-documentsource"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1350`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobExecutionsRetryConfig`  <a name="cfn-iot-job-jobexecutionsretryconfig"></a>
The configuration for the criteria to retry the job.
*Required*: No
*Type*: [JobExecutionsRetryConfig](aws-properties-iot-job-jobexecutionsretryconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobExecutionsRolloutConfig`  <a name="cfn-iot-job-jobexecutionsrolloutconfig"></a>
Allows you to create a staged rollout of a job.
*Required*: No
*Type*: [JobExecutionsRolloutConfig](aws-properties-iot-job-jobexecutionsrolloutconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobId`  <a name="cfn-iot-job-jobid"></a>
The unique identifier you assigned to this job when it was created.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobTemplateArn`  <a name="cfn-iot-job-jobtemplatearn"></a>
The ARN of the job template.
*Required*: No
*Type*: String
*Pattern*: `^arn:[!-~]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PresignedUrlConfig`  <a name="cfn-iot-job-presignedurlconfig"></a>
Configuration for pre-signed S3 URLs.
*Required*: No
*Type*: [PresignedUrlConfig](aws-properties-iot-job-presignedurlconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchedulingConfig`  <a name="cfn-iot-job-schedulingconfig"></a>
Property description not available.
*Required*: No
*Type*: [SchedulingConfig](aws-properties-iot-job-schedulingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iot-job-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-job-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-iot-job-targets"></a>
A list of IoT things and thing groups to which the job should be sent.
*Required*: Yes
*Type*: Array of String
*Maximum*: `2048`
*Minimum*: `0 | 1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetSelection`  <a name="cfn-iot-job-targetselection"></a>
Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group.
We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUOUS | SNAPSHOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutConfig`  <a name="cfn-iot-job-timeoutconfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
*Required*: No
*Type*: [TimeoutConfig](aws-properties-iot-job-timeoutconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-job-return-values"></a>

### Ref
<a name="aws-resource-iot-job-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iot-job-return-values-fn--getatt"></a>

####
<a name="aws-resource-iot-job-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time, in seconds since the epoch, when the job was created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
