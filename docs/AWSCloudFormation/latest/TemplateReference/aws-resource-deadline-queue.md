---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-queue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue
<a name="aws-resource-deadline-queue"></a>

Creates a queue to coordinate the order in which jobs run on a farm. A queue can also specify where to pull resources and indicate where to output completed jobs.

## Syntax
<a name="aws-resource-deadline-queue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-queue-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Queue",
  "Properties" : {
      "[AllowedStorageProfileIds](#cfn-deadline-queue-allowedstorageprofileids)" : {{[ String, ... ]}},
      "[DefaultBudgetAction](#cfn-deadline-queue-defaultbudgetaction)" : {{String}},
      "[Description](#cfn-deadline-queue-description)" : {{String}},
      "[DisplayName](#cfn-deadline-queue-displayname)" : {{String}},
      "[FarmId](#cfn-deadline-queue-farmid)" : {{String}},
      "[JobAttachmentSettings](#cfn-deadline-queue-jobattachmentsettings)" : {{JobAttachmentSettings}},
      "[JobRunAsUser](#cfn-deadline-queue-jobrunasuser)" : {{JobRunAsUser}},
      "[RequiredFileSystemLocationNames](#cfn-deadline-queue-requiredfilesystemlocationnames)" : {{[ String, ... ]}},
      "[RoleArn](#cfn-deadline-queue-rolearn)" : {{String}},
      "[SchedulingConfiguration](#cfn-deadline-queue-schedulingconfiguration)" : {{SchedulingConfiguration}},
      "[Tags](#cfn-deadline-queue-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-deadline-queue-syntax.yaml"></a>

```
Type: AWS::Deadline::Queue
Properties:
  [AllowedStorageProfileIds](#cfn-deadline-queue-allowedstorageprofileids): {{
    - String}}
  [DefaultBudgetAction](#cfn-deadline-queue-defaultbudgetaction): {{String}}
  [Description](#cfn-deadline-queue-description): {{String}}
  [DisplayName](#cfn-deadline-queue-displayname): {{String}}
  [FarmId](#cfn-deadline-queue-farmid): {{String}}
  [JobAttachmentSettings](#cfn-deadline-queue-jobattachmentsettings): {{
    JobAttachmentSettings}}
  [JobRunAsUser](#cfn-deadline-queue-jobrunasuser): {{
    JobRunAsUser}}
  [RequiredFileSystemLocationNames](#cfn-deadline-queue-requiredfilesystemlocationnames): {{
    - String}}
  [RoleArn](#cfn-deadline-queue-rolearn): {{String}}
  [SchedulingConfiguration](#cfn-deadline-queue-schedulingconfiguration): {{
    SchedulingConfiguration}}
  [Tags](#cfn-deadline-queue-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-deadline-queue-properties"></a>

`AllowedStorageProfileIds`  <a name="cfn-deadline-queue-allowedstorageprofileids"></a>
The identifiers of the storage profiles that this queue can use to share assets between workers using different operating systems.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultBudgetAction`  <a name="cfn-deadline-queue-defaultbudgetaction"></a>
The default action taken on a queue summary if a budget wasn't configured.
*Required*: No
*Type*: String
*Allowed values*: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-deadline-queue-description"></a>
A description of the queue that helps identify what the queue is used for.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-deadline-queue-displayname"></a>
The display name of the queue summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FarmId`  <a name="cfn-deadline-queue-farmid"></a>
The farm ID.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobAttachmentSettings`  <a name="cfn-deadline-queue-jobattachmentsettings"></a>
The job attachment settings. These are the Amazon S3 bucket name and the Amazon S3 prefix.
*Required*: No
*Type*: [JobAttachmentSettings](aws-properties-deadline-queue-jobattachmentsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobRunAsUser`  <a name="cfn-deadline-queue-jobrunasuser"></a>
Identifies the user for a job.
*Required*: No
*Type*: [JobRunAsUser](aws-properties-deadline-queue-jobrunasuser.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequiredFileSystemLocationNames`  <a name="cfn-deadline-queue-requiredfilesystemlocationnames"></a>
The file system location that the queue uses.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `64 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-deadline-queue-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that workers use when running jobs in this queue.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchedulingConfiguration`  <a name="cfn-deadline-queue-schedulingconfiguration"></a>
The scheduling configuration for a queue. Defines the strategy used to assign workers to jobs.
*Required*: No
*Type*: [SchedulingConfiguration](aws-properties-deadline-queue-schedulingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-deadline-queue-tags"></a>
The tags to add to your queue. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-queue-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-queue-return-values"></a>

### Ref
<a name="aws-resource-deadline-queue-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the specified queue.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-queue-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-queue-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the queue.

`QueueId`  <a name="QueueId-fn::getatt"></a>
The queue ID.
