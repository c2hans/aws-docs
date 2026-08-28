---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesweb-sessionlogger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::SessionLogger
<a name="aws-resource-workspacesweb-sessionlogger"></a>

The session logger resource.

## Syntax
<a name="aws-resource-workspacesweb-sessionlogger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesweb-sessionlogger-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesWeb::SessionLogger",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-workspacesweb-sessionlogger-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[CustomerManagedKey](#cfn-workspacesweb-sessionlogger-customermanagedkey)" : {{String}},
      "[DisplayName](#cfn-workspacesweb-sessionlogger-displayname)" : {{String}},
      "[EventFilter](#cfn-workspacesweb-sessionlogger-eventfilter)" : {{EventFilter}},
      "[LogConfiguration](#cfn-workspacesweb-sessionlogger-logconfiguration)" : {{LogConfiguration}},
      "[Tags](#cfn-workspacesweb-sessionlogger-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-workspacesweb-sessionlogger-syntax.yaml"></a>

```
Type: AWS::WorkSpacesWeb::SessionLogger
Properties:
  [AdditionalEncryptionContext](#cfn-workspacesweb-sessionlogger-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [CustomerManagedKey](#cfn-workspacesweb-sessionlogger-customermanagedkey): {{String}}
  [DisplayName](#cfn-workspacesweb-sessionlogger-displayname): {{String}}
  [EventFilter](#cfn-workspacesweb-sessionlogger-eventfilter): {{
    EventFilter}}
  [LogConfiguration](#cfn-workspacesweb-sessionlogger-logconfiguration): {{
    LogConfiguration}}
  [Tags](#cfn-workspacesweb-sessionlogger-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-workspacesweb-sessionlogger-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-workspacesweb-sessionlogger-additionalencryptioncontext"></a>
The additional encryption context of the session logger.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomerManagedKey`  <a name="cfn-workspacesweb-sessionlogger-customermanagedkey"></a>
The custom managed key of the session logger.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisplayName`  <a name="cfn-workspacesweb-sessionlogger-displayname"></a>
The human-readable display name.
*Required*: No
*Type*: String
*Pattern*: `^[ _\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventFilter`  <a name="cfn-workspacesweb-sessionlogger-eventfilter"></a>
The filter that specifies which events to monitor.
*Required*: Yes
*Type*: [EventFilter](aws-properties-workspacesweb-sessionlogger-eventfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-workspacesweb-sessionlogger-logconfiguration"></a>
The configuration that specifies where logs are fowarded.
*Required*: Yes
*Type*: [LogConfiguration](aws-properties-workspacesweb-sessionlogger-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-workspacesweb-sessionlogger-tags"></a>
The tags of the session logger.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesweb-sessionlogger-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesweb-sessionlogger-return-values"></a>

### Ref
<a name="aws-resource-workspacesweb-sessionlogger-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-workspacesweb-sessionlogger-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspacesweb-sessionlogger-return-values-fn--getatt-fn--getatt"></a>

`AssociatedPortalArns`  <a name="AssociatedPortalArns-fn::getatt"></a>
The associated portal ARN.

`CreationDate`  <a name="CreationDate-fn::getatt"></a>
The date the session logger resource was created.

`SessionLoggerArn`  <a name="SessionLoggerArn-fn::getatt"></a>
The ARN of the session logger resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
