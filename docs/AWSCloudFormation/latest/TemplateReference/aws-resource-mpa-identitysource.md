---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mpa-identitysource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::IdentitySource
<a name="aws-resource-mpa-identitysource"></a>

Creates a new identity source. For more information, see [Identity Source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Syntax
<a name="aws-resource-mpa-identitysource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mpa-identitysource-syntax.json"></a>

```
{
  "Type" : "AWS::MPA::IdentitySource",
  "Properties" : {
      "[IdentitySourceParameters](#cfn-mpa-identitysource-identitysourceparameters)" : {{IdentitySourceParameters}},
      "[Tags](#cfn-mpa-identitysource-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mpa-identitysource-syntax.yaml"></a>

```
Type: AWS::MPA::IdentitySource
Properties:
  [IdentitySourceParameters](#cfn-mpa-identitysource-identitysourceparameters): {{
    IdentitySourceParameters}}
  [Tags](#cfn-mpa-identitysource-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mpa-identitysource-properties"></a>

`IdentitySourceParameters`  <a name="cfn-mpa-identitysource-identitysourceparameters"></a>
A ` IdentitySourceParameters` object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.
*Required*: Yes
*Type*: [IdentitySourceParameters](aws-properties-mpa-identitysource-identitysourceparameters.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mpa-identitysource-tags"></a>
Tags that you have added to the specified resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-mpa-identitysource-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mpa-identitysource-return-values"></a>

### Ref
<a name="aws-resource-mpa-identitysource-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mpa-identitysource-return-values-fn--getatt"></a>

####
<a name="aws-resource-mpa-identitysource-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Timestamp when the identity source was created.

`IdentitySourceArn`  <a name="IdentitySourceArn-fn::getatt"></a>
Amazon Resource Name (ARN) for the identity source.

`IdentitySourceParameters.IamIdentityCenter.ApprovalPortalUrl`  <a name="IdentitySourceParameters.IamIdentityCenter.ApprovalPortalUrl-fn::getatt"></a>
URL for the approval portal associated with the IAM Identity Center instance.

`IdentitySourceType`  <a name="IdentitySourceType-fn::getatt"></a>
The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.

`Status`  <a name="Status-fn::getatt"></a>
Status for the identity source. For example, if the identity source is `ACTIVE`.

`StatusCode`  <a name="StatusCode-fn::getatt"></a>
Status code of the identity source.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Message describing the status for the identity source.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
