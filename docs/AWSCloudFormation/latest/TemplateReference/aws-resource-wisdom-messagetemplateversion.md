---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-messagetemplateversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplateVersion
<a name="aws-resource-wisdom-messagetemplateversion"></a>

Creates a new Amazon Q in Connect message template version from the current content and configuration of a message template. Versions are immutable and monotonically increasing. Once a version is created, you can reference a specific version of the message template by passing in `<messageTemplateArn>:<versionNumber>` as the message template identifier. An error is displayed if the supplied `messageTemplateContentSha256` is different from the `messageTemplateContentSha256` of the message template with `$LATEST` qualifier. If multiple `CreateMessageTemplateVersion` requests are made while the message template remains the same, only the first invocation creates a new version and the succeeding requests will return the same response as the first invocation.

## Syntax
<a name="aws-resource-wisdom-messagetemplateversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-messagetemplateversion-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::MessageTemplateVersion",
  "Properties" : {
      "[MessageTemplateArn](#cfn-wisdom-messagetemplateversion-messagetemplatearn)" : {{String}},
      "[MessageTemplateContentSha256](#cfn-wisdom-messagetemplateversion-messagetemplatecontentsha256)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-messagetemplateversion-syntax.yaml"></a>

```
Type: AWS::Wisdom::MessageTemplateVersion
Properties:
  [MessageTemplateArn](#cfn-wisdom-messagetemplateversion-messagetemplatearn): {{String}}
  [MessageTemplateContentSha256](#cfn-wisdom-messagetemplateversion-messagetemplatecontentsha256): {{String}}
```

## Properties
<a name="aws-resource-wisdom-messagetemplateversion-properties"></a>

`MessageTemplateArn`  <a name="cfn-wisdom-messagetemplateversion-messagetemplatearn"></a>
The Amazon Resource Name (ARN) of the message template.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MessageTemplateContentSha256`  <a name="cfn-wisdom-messagetemplateversion-messagetemplatecontentsha256"></a>
The content SHA256 of the message template.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-wisdom-messagetemplateversion-return-values"></a>

### Ref
<a name="aws-resource-wisdom-messagetemplateversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-messagetemplateversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-messagetemplateversion-return-values-fn--getatt-fn--getatt"></a>

`MessageTemplateVersionArn`  <a name="MessageTemplateVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Message Template Version.

`MessageTemplateVersionNumber`  <a name="MessageTemplateVersionNumber-fn::getatt"></a>
The version number for this Message Template Version.
