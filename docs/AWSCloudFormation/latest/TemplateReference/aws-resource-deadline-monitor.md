---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-monitor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Monitor
<a name="aws-resource-deadline-monitor"></a>

Creates an AWS Deadline Cloud monitor that you can use to view your farms, queues, and fleets. After you submit a job, you can track the progress of the tasks and steps that make up the job, and then download the job's results.

## Syntax
<a name="aws-resource-deadline-monitor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-monitor-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Monitor",
  "Properties" : {
      "[DisplayName](#cfn-deadline-monitor-displayname)" : {{String}},
      "[IdentityCenterInstanceArn](#cfn-deadline-monitor-identitycenterinstancearn)" : {{String}},
      "[IdentityCenterRegion](#cfn-deadline-monitor-identitycenterregion)" : {{String}},
      "[RoleArn](#cfn-deadline-monitor-rolearn)" : {{String}},
      "[Subdomain](#cfn-deadline-monitor-subdomain)" : {{String}},
      "[Tags](#cfn-deadline-monitor-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-deadline-monitor-syntax.yaml"></a>

```
Type: AWS::Deadline::Monitor
Properties:
  [DisplayName](#cfn-deadline-monitor-displayname): {{String}}
  [IdentityCenterInstanceArn](#cfn-deadline-monitor-identitycenterinstancearn): {{String}}
  [IdentityCenterRegion](#cfn-deadline-monitor-identitycenterregion): {{String}}
  [RoleArn](#cfn-deadline-monitor-rolearn): {{String}}
  [Subdomain](#cfn-deadline-monitor-subdomain): {{String}}
  [Tags](#cfn-deadline-monitor-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-deadline-monitor-properties"></a>

`DisplayName`  <a name="cfn-deadline-monitor-displayname"></a>
The name of the monitor that displays on the Deadline Cloud console.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityCenterInstanceArn`  <a name="cfn-deadline-monitor-identitycenterinstancearn"></a>
The Amazon Resource Name of the IAM Identity Center instance responsible for authenticating monitor users.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterRegion`  <a name="cfn-deadline-monitor-identitycenterregion"></a>
The Region where IAM Identity Center is enabled.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-deadline-monitor-rolearn"></a>
The Amazon Resource Name of the IAM role for the monitor. Users of the monitor use this role to access Deadline Cloud resources.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdomain`  <a name="cfn-deadline-monitor-subdomain"></a>
The subdomain used for the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-]{1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-deadline-monitor-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-monitor-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-monitor-return-values"></a>

### Ref
<a name="aws-resource-deadline-monitor-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-deadline-monitor-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-monitor-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the monitor.

`IdentityCenterApplicationArn`  <a name="IdentityCenterApplicationArn-fn::getatt"></a>
The Amazon Resource Name that the IAM Identity Center assigned to the monitor when it was created.

`MonitorId`  <a name="MonitorId-fn::getatt"></a>
The unique identifier for the monitor.

`Url`  <a name="Url-fn::getatt"></a>
The complete URL of the monitor. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.
