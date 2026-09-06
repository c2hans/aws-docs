---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-cloudwatchalarmtemplategroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::CloudWatchAlarmTemplateGroup
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup"></a>

<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-description"></a>The `AWS::MediaLive::CloudWatchAlarmTemplateGroup` resource Property description not available. for MediaLive.

## Syntax
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::CloudWatchAlarmTemplateGroup",
  "Properties" : {
      "[Description](#cfn-medialive-cloudwatchalarmtemplategroup-description)" : {{String}},
      "[Name](#cfn-medialive-cloudwatchalarmtemplategroup-name)" : {{String}},
      "[Tags](#cfn-medialive-cloudwatchalarmtemplategroup-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-syntax.yaml"></a>

```
Type: AWS::MediaLive::CloudWatchAlarmTemplateGroup
Properties:
  [Description](#cfn-medialive-cloudwatchalarmtemplategroup-description): {{String}}
  [Name](#cfn-medialive-cloudwatchalarmtemplategroup-name): {{String}}
  [Tags](#cfn-medialive-cloudwatchalarmtemplategroup-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-properties"></a>

`Description`  <a name="cfn-medialive-cloudwatchalarmtemplategroup-description"></a>
A resource's optional description.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-cloudwatchalarmtemplategroup-name"></a>
A resource's name. Names must be unique within the scope of a resource type in a specific region.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-medialive-cloudwatchalarmtemplategroup-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-return-values"></a>

### Ref
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-cloudwatchalarmtemplategroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
A cloudwatch alarm template group's ARN (Amazon Resource Name)

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time of resource creation.

`Id`  <a name="Id-fn::getatt"></a>
A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>

`Identifier`  <a name="Identifier-fn::getatt"></a>
Property description not available.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The date and time of latest resource modification.
