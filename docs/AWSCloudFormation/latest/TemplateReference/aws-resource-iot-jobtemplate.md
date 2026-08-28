---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-jobtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::JobTemplate
<a name="aws-resource-iot-jobtemplate"></a>

Represents a job template.

## Syntax
<a name="aws-resource-iot-jobtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-jobtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::JobTemplate",
  "Properties" : {
      "[AbortConfig](#cfn-iot-jobtemplate-abortconfig)" : {{AbortConfig}},
      "[Description](#cfn-iot-jobtemplate-description)" : {{String}},
      "[DestinationPackageVersions](#cfn-iot-jobtemplate-destinationpackageversions)" : {{[ String, ... ]}},
      "[Document](#cfn-iot-jobtemplate-document)" : {{String}},
      "[DocumentSource](#cfn-iot-jobtemplate-documentsource)" : {{String}},
      "[JobArn](#cfn-iot-jobtemplate-jobarn)" : {{String}},
      "[JobExecutionsRetryConfig](#cfn-iot-jobtemplate-jobexecutionsretryconfig)" : {{JobExecutionsRetryConfig}},
      "[JobExecutionsRolloutConfig](#cfn-iot-jobtemplate-jobexecutionsrolloutconfig)" : {{JobExecutionsRolloutConfig}},
      "[JobTemplateId](#cfn-iot-jobtemplate-jobtemplateid)" : {{String}},
      "[MaintenanceWindows](#cfn-iot-jobtemplate-maintenancewindows)" : {{[ MaintenanceWindow, ... ]}},
      "[PresignedUrlConfig](#cfn-iot-jobtemplate-presignedurlconfig)" : {{PresignedUrlConfig}},
      "[Tags](#cfn-iot-jobtemplate-tags)" : {{[ Tag, ... ]}},
      "[TimeoutConfig](#cfn-iot-jobtemplate-timeoutconfig)" : {{TimeoutConfig}}
    }
}
```

### YAML
<a name="aws-resource-iot-jobtemplate-syntax.yaml"></a>

```
Type: AWS::IoT::JobTemplate
Properties:
  [AbortConfig](#cfn-iot-jobtemplate-abortconfig): {{
    AbortConfig}}
  [Description](#cfn-iot-jobtemplate-description): {{String}}
  [DestinationPackageVersions](#cfn-iot-jobtemplate-destinationpackageversions): {{
    - String}}
  [Document](#cfn-iot-jobtemplate-document): {{String}}
  [DocumentSource](#cfn-iot-jobtemplate-documentsource): {{String}}
  [JobArn](#cfn-iot-jobtemplate-jobarn): {{String}}
  [JobExecutionsRetryConfig](#cfn-iot-jobtemplate-jobexecutionsretryconfig): {{
    JobExecutionsRetryConfig}}
  [JobExecutionsRolloutConfig](#cfn-iot-jobtemplate-jobexecutionsrolloutconfig): {{
    JobExecutionsRolloutConfig}}
  [JobTemplateId](#cfn-iot-jobtemplate-jobtemplateid): {{String}}
  [MaintenanceWindows](#cfn-iot-jobtemplate-maintenancewindows): {{
    - MaintenanceWindow}}
  [PresignedUrlConfig](#cfn-iot-jobtemplate-presignedurlconfig): {{
    PresignedUrlConfig}}
  [Tags](#cfn-iot-jobtemplate-tags): {{
    - Tag}}
  [TimeoutConfig](#cfn-iot-jobtemplate-timeoutconfig): {{
    TimeoutConfig}}
```

## Properties
<a name="aws-resource-iot-jobtemplate-properties"></a>

`AbortConfig`  <a name="cfn-iot-jobtemplate-abortconfig"></a>
The criteria that determine when and how a job abort takes place.
*Required*: No
*Type*: [AbortConfig](aws-properties-iot-jobtemplate-abortconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-iot-jobtemplate-description"></a>
A description of the job template.
*Required*: Yes
*Type*: String
*Pattern*: `[^\p{C}]+`
*Maximum*: `2028`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationPackageVersions`  <a name="cfn-iot-jobtemplate-destinationpackageversions"></a>
The package version Amazon Resource Names (ARNs) that are installed on the device’s reserved named shadow (`$package`) when the job successfully completes.
**Note:** Up to 25 package version ARNS are allowed.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Document`  <a name="cfn-iot-jobtemplate-document"></a>
The job document.
Required if you don't specify a value for `documentSource`.
*Required*: No
*Type*: String
*Maximum*: `32768`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DocumentSource`  <a name="cfn-iot-jobtemplate-documentsource"></a>
An S3 link, or S3 object URL, to the job document. The link is an Amazon S3 object URL and is required if you don't specify a value for `document`.
For example, `--document-source https://s3.region-code.amazonaws.com/example-firmware/device-firmware.1.0`
For more information, see [Methods for accessing a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1350`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobArn`  <a name="cfn-iot-jobtemplate-jobarn"></a>
The ARN of the job to use as the basis for the job template.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobExecutionsRetryConfig`  <a name="cfn-iot-jobtemplate-jobexecutionsretryconfig"></a>
Allows you to create the criteria to retry a job.
*Required*: No
*Type*: [JobExecutionsRetryConfig](aws-properties-iot-jobtemplate-jobexecutionsretryconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobExecutionsRolloutConfig`  <a name="cfn-iot-jobtemplate-jobexecutionsrolloutconfig"></a>
Allows you to create a staged rollout of a job.
*Required*: No
*Type*: [JobExecutionsRolloutConfig](aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobTemplateId`  <a name="cfn-iot-jobtemplate-jobtemplateid"></a>
A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, "-", and "\_" are valid for use here.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_-]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceWindows`  <a name="cfn-iot-jobtemplate-maintenancewindows"></a>
An optional configuration within the SchedulingConfig to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.
*Required*: No
*Type*: Array of [MaintenanceWindow](aws-properties-iot-jobtemplate-maintenancewindow.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PresignedUrlConfig`  <a name="cfn-iot-jobtemplate-presignedurlconfig"></a>
Configuration for pre-signed S3 URLs.
*Required*: No
*Type*: [PresignedUrlConfig](aws-properties-iot-jobtemplate-presignedurlconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iot-jobtemplate-tags"></a>
Metadata that can be used to manage the job template.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-jobtemplate-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutConfig`  <a name="cfn-iot-jobtemplate-timeoutconfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
*Required*: No
*Type*: [TimeoutConfig](aws-properties-iot-jobtemplate-timeoutconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iot-jobtemplate-return-values"></a>

### Ref
<a name="aws-resource-iot-jobtemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the job template Id. For example:

 `{ "Ref": "MyJobTemplate-12345" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-jobtemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iot-jobtemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the job to use as the basis for the job template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
