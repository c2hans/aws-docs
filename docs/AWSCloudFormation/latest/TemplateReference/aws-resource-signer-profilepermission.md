---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-signer-profilepermission.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Signer::ProfilePermission
<a name="aws-resource-signer-profilepermission"></a>

Adds cross-account permissions to a signing profile.

## Syntax
<a name="aws-resource-signer-profilepermission-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-signer-profilepermission-syntax.json"></a>

```
{
  "Type" : "AWS::Signer::ProfilePermission",
  "Properties" : {
      "[Action](#cfn-signer-profilepermission-action)" : {{String}},
      "[Principal](#cfn-signer-profilepermission-principal)" : {{String}},
      "[ProfileName](#cfn-signer-profilepermission-profilename)" : {{String}},
      "[ProfileVersion](#cfn-signer-profilepermission-profileversion)" : {{String}},
      "[StatementId](#cfn-signer-profilepermission-statementid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-signer-profilepermission-syntax.yaml"></a>

```
Type: AWS::Signer::ProfilePermission
Properties:
  [Action](#cfn-signer-profilepermission-action): {{String}}
  [Principal](#cfn-signer-profilepermission-principal): {{String}}
  [ProfileName](#cfn-signer-profilepermission-profilename): {{String}}
  [ProfileVersion](#cfn-signer-profilepermission-profileversion): {{String}}
  [StatementId](#cfn-signer-profilepermission-statementid): {{String}}
```

## Properties
<a name="aws-resource-signer-profilepermission-properties"></a>

`Action`  <a name="cfn-signer-profilepermission-action"></a>
The AWS Signer action permitted as part of cross-account permissions.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Principal`  <a name="cfn-signer-profilepermission-principal"></a>
The AWS principal receiving cross-account permissions. This may be an IAM role or another AWS account ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileName`  <a name="cfn-signer-profilepermission-profilename"></a>
The human-readable name of the signing profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z_]{2,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileVersion`  <a name="cfn-signer-profilepermission-profileversion"></a>
The version of the signing profile.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-zA-Z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StatementId`  <a name="cfn-signer-profilepermission-statementid"></a>
A unique identifier for the cross-account permission statement.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-signer-profilepermission-return-values"></a>

### Ref
<a name="aws-resource-signer-profilepermission-return-values-ref"></a>

The StatementId and ProfileName in the form StatementId\|ProfileName

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
