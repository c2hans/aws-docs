---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-inputsecuritygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::InputSecurityGroup
<a name="aws-resource-medialive-inputsecuritygroup"></a>

The AWS::MediaLive::InputSecurityGroup is a MediaLive resource type that creates an input security group.

A MediaLive input security group is associated with a MediaLive input. The input security group is an "allow list" of IP addresses that controls whether an external IP address can push content to the associated MediaLive input.

## Syntax
<a name="aws-resource-medialive-inputsecuritygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-inputsecuritygroup-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::InputSecurityGroup",
  "Properties" : {
      "[Tags](#cfn-medialive-inputsecuritygroup-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}},
      "[WhitelistRules](#cfn-medialive-inputsecuritygroup-whitelistrules)" : {{[ InputWhitelistRuleCidr, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-medialive-inputsecuritygroup-syntax.yaml"></a>

```
Type: AWS::MediaLive::InputSecurityGroup
Properties:
  [Tags](#cfn-medialive-inputsecuritygroup-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
  [WhitelistRules](#cfn-medialive-inputsecuritygroup-whitelistrules): {{
    - InputWhitelistRuleCidr}}
```

## Properties
<a name="aws-resource-medialive-inputsecuritygroup-properties"></a>

`Tags`  <a name="cfn-medialive-inputsecuritygroup-tags"></a>
A collection of tags for this input security group. Each tag is a key-value pair.
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WhitelistRules`  <a name="cfn-medialive-inputsecuritygroup-whitelistrules"></a>
The list of IPv4 CIDR addresses to include in the input security group as "allowed" addresses.
*Required*: No
*Type*: Array of [InputWhitelistRuleCidr](aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-inputsecuritygroup-return-values"></a>

### Ref
<a name="aws-resource-medialive-inputsecuritygroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the input security group.

For example: `{ "Ref": "myInputSecurityGroup" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-medialive-inputsecuritygroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-inputsecuritygroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the MediaLive input security group. For example: arn:aws:medialive:us-west-1:111122223333:medialive:inputSecurityGroup:1234567

`Id`  <a name="Id-fn::getatt"></a>
The Id of the Input Security Group

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
