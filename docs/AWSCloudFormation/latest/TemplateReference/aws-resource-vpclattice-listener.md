---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-listener.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Listener
<a name="aws-resource-vpclattice-listener"></a>

Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see [Listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html) in the *Amazon VPC Lattice User Guide*.

## Syntax
<a name="aws-resource-vpclattice-listener-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-listener-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::Listener",
  "Properties" : {
      "[DefaultAction](#cfn-vpclattice-listener-defaultaction)" : {{DefaultAction}},
      "[Name](#cfn-vpclattice-listener-name)" : {{String}},
      "[Port](#cfn-vpclattice-listener-port)" : {{Integer}},
      "[Protocol](#cfn-vpclattice-listener-protocol)" : {{String}},
      "[ServiceIdentifier](#cfn-vpclattice-listener-serviceidentifier)" : {{String}},
      "[Tags](#cfn-vpclattice-listener-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-listener-syntax.yaml"></a>

```
Type: AWS::VpcLattice::Listener
Properties:
  [DefaultAction](#cfn-vpclattice-listener-defaultaction): {{
    DefaultAction}}
  [Name](#cfn-vpclattice-listener-name): {{String}}
  [Port](#cfn-vpclattice-listener-port): {{Integer}}
  [Protocol](#cfn-vpclattice-listener-protocol): {{String}}
  [ServiceIdentifier](#cfn-vpclattice-listener-serviceidentifier): {{String}}
  [Tags](#cfn-vpclattice-listener-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-vpclattice-listener-properties"></a>

`DefaultAction`  <a name="cfn-vpclattice-listener-defaultaction"></a>
The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.
*Required*: Yes
*Type*: [DefaultAction](aws-properties-vpclattice-listener-defaultaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-vpclattice-listener-name"></a>
The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
*Required*: No
*Type*: String
*Pattern*: `^(?!listener-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-vpclattice-listener-port"></a>
The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-vpclattice-listener-protocol"></a>
The listener protocol.
*Required*: Yes
*Type*: String
*Allowed values*: `HTTP | HTTPS | TLS_PASSTHROUGH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceIdentifier`  <a name="cfn-vpclattice-listener-serviceidentifier"></a>
The ID or ARN of the service.
*Required*: No
*Type*: String
*Pattern*: `^((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))$`
*Minimum*: `21`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-vpclattice-listener-tags"></a>
The tags for the listener.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-listener-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-vpclattice-listener-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-listener-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the listener.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-listener-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-listener-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the listener.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the listener.

`ServiceArn`  <a name="ServiceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service.

`ServiceId`  <a name="ServiceId-fn::getatt"></a>
The ID of the service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
