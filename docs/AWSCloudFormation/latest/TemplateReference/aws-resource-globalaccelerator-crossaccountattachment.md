---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-globalaccelerator-crossaccountattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GlobalAccelerator::CrossAccountAttachment
<a name="aws-resource-globalaccelerator-crossaccountattachment"></a>

Create a cross-account attachment in AWS Global Accelerator. You create a cross-account attachment to specify the *principals* who have permission to work with *resources* in accelerators in their own account. You specify, in the same attachment, the resources that are shared.

A principal can be an AWS account number or the Amazon Resource Name (ARN) for an accelerator. For account numbers that are listed as principals, to work with a resource listed in the attachment, you must sign in to an account specified as a principal. Then, you can work with resources that are listed, with any of your accelerators. If an accelerator ARN is listed in the cross-account attachment as a principal, anyone with permission to make updates to the accelerator can work with resources that are listed in the attachment.

Specify each principal and resource separately. To specify two CIDR address pools, list them individually under `Resources`, and so on. For a command line operation, for example, you might use a statement like the following:

 ` "Resources": [{"Cidr": "169.254.60.0/24"},{"Cidr": "169.254.59.0/24"}]`

For more information, see [ Working with cross-account attachments and resources in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the *AWS Global Accelerator Developer Guide*.

## Syntax
<a name="aws-resource-globalaccelerator-crossaccountattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-globalaccelerator-crossaccountattachment-syntax.json"></a>

```
{
  "Type" : "AWS::GlobalAccelerator::CrossAccountAttachment",
  "Properties" : {
      "[Name](#cfn-globalaccelerator-crossaccountattachment-name)" : {{String}},
      "[Principals](#cfn-globalaccelerator-crossaccountattachment-principals)" : {{[ String, ... ]}},
      "[Resources](#cfn-globalaccelerator-crossaccountattachment-resources)" : {{[ Resource, ... ]}},
      "[Tags](#cfn-globalaccelerator-crossaccountattachment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-globalaccelerator-crossaccountattachment-syntax.yaml"></a>

```
Type: AWS::GlobalAccelerator::CrossAccountAttachment
Properties:
  [Name](#cfn-globalaccelerator-crossaccountattachment-name): {{String}}
  [Principals](#cfn-globalaccelerator-crossaccountattachment-principals): {{
    - String}}
  [Resources](#cfn-globalaccelerator-crossaccountattachment-resources): {{
    - Resource}}
  [Tags](#cfn-globalaccelerator-crossaccountattachment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-globalaccelerator-crossaccountattachment-properties"></a>

`Name`  <a name="cfn-globalaccelerator-crossaccountattachment-name"></a>
The name of the cross-account attachment.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{0,64}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principals`  <a name="cfn-globalaccelerator-crossaccountattachment-principals"></a>
The principals included in the cross-account attachment.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resources`  <a name="cfn-globalaccelerator-crossaccountattachment-resources"></a>
The resources included in the cross-account attachment.
*Required*: No
*Type*: Array of [Resource](aws-properties-globalaccelerator-crossaccountattachment-resource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-globalaccelerator-crossaccountattachment-tags"></a>
Add tags for a cross-account attachment.
For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html) in the *AWS Global Accelerator Developer Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-globalaccelerator-crossaccountattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-globalaccelerator-crossaccountattachment-return-values"></a>

### Ref
<a name="aws-resource-globalaccelerator-crossaccountattachment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the cross-account attachment.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-globalaccelerator-crossaccountattachment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-globalaccelerator-crossaccountattachment-return-values-fn--getatt-fn--getatt"></a>

`AttachmentArn`  <a name="AttachmentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the cross-account attachment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
