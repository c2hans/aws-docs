---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-viewversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::ViewVersion
<a name="aws-resource-connect-viewversion"></a>

Creates a version for the specified customer-managed view within the specified instance.

## Syntax
<a name="aws-resource-connect-viewversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-viewversion-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::ViewVersion",
  "Properties" : {
      "[VersionDescription](#cfn-connect-viewversion-versiondescription)" : {{String}},
      "[ViewArn](#cfn-connect-viewversion-viewarn)" : {{String}},
      "[ViewContentSha256](#cfn-connect-viewversion-viewcontentsha256)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-viewversion-syntax.yaml"></a>

```
Type: AWS::Connect::ViewVersion
Properties:
  [VersionDescription](#cfn-connect-viewversion-versiondescription): {{String}}
  [ViewArn](#cfn-connect-viewversion-viewarn): {{String}}
  [ViewContentSha256](#cfn-connect-viewversion-viewcontentsha256): {{String}}
```

## Properties
<a name="aws-resource-connect-viewversion-properties"></a>

`VersionDescription`  <a name="cfn-connect-viewversion-versiondescription"></a>
The description of the view version.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewArn`  <a name="cfn-connect-viewversion-viewarn"></a>
The unqualified Amazon Resource Name (ARN) of the view.
For example:

```
arn:<partition>:connect:<region>:<accountId>:instance/00000000-0000-0000-0000-000000000000/view/00000000-0000-0000-0000-000000000000
```
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/view/[-:a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ViewContentSha256`  <a name="cfn-connect-viewversion-viewcontentsha256"></a>
Indicates the checksum value of the latest published view content.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-viewversion-return-values"></a>

### Ref
<a name="aws-resource-connect-viewversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-viewversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-viewversion-return-values-fn--getatt-fn--getatt"></a>

`Version`  <a name="Version-fn::getatt"></a>
Current version of the view.

`ViewVersionArn`  <a name="ViewVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the view version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
