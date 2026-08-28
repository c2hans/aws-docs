---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-managedblockchain-accessor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ManagedBlockchain::Accessor
<a name="aws-resource-managedblockchain-accessor"></a>

Creates a new accessor for use with Amazon Managed Blockchain service that supports token based access. The accessor contains information required for token based access.

## Syntax
<a name="aws-resource-managedblockchain-accessor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-managedblockchain-accessor-syntax.json"></a>

```
{
  "Type" : "AWS::ManagedBlockchain::Accessor",
  "Properties" : {
      "[AccessorType](#cfn-managedblockchain-accessor-accessortype)" : {{String}},
      "[NetworkType](#cfn-managedblockchain-accessor-networktype)" : {{String}},
      "[Tags](#cfn-managedblockchain-accessor-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-managedblockchain-accessor-syntax.yaml"></a>

```
Type: AWS::ManagedBlockchain::Accessor
Properties:
  [AccessorType](#cfn-managedblockchain-accessor-accessortype): {{String}}
  [NetworkType](#cfn-managedblockchain-accessor-networktype): {{String}}
  [Tags](#cfn-managedblockchain-accessor-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-managedblockchain-accessor-properties"></a>

`AccessorType`  <a name="cfn-managedblockchain-accessor-accessortype"></a>
The type of the accessor.
Currently, accessor type is restricted to `BILLING_TOKEN`.
*Required*: Yes
*Type*: String
*Allowed values*: `BILLING_TOKEN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-managedblockchain-accessor-networktype"></a>
The blockchain network that the `Accessor` token is created for.
We recommend using the appropriate `networkType` value for the blockchain network that you are creating the `Accessor` token for. You cannot use the value `ETHEREUM_MAINNET_AND_GOERLI` to specify a `networkType` for your Accessor token.
The default value of `ETHEREUM_MAINNET_AND_GOERLI` is only applied:
+ when the `CreateAccessor` action does not set a `networkType`.
+ to all existing `Accessor` tokens that were created before the `networkType` property was introduced.
*Required*: No
*Type*: String
*Allowed values*: `ETHEREUM_GOERLI | ETHEREUM_MAINNET | ETHEREUM_MAINNET_AND_GOERLI | POLYGON_MAINNET | POLYGON_MUMBAI`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-managedblockchain-accessor-tags"></a>
The tags assigned to the Accessor.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-managedblockchain-accessor-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-managedblockchain-accessor-return-values"></a>

### Ref
<a name="aws-resource-managedblockchain-accessor-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Accessor ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-managedblockchain-accessor-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-managedblockchain-accessor-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`BillingToken`  <a name="BillingToken-fn::getatt"></a>
The billing token is a property of the accessor. Use this token to make Ethereum API calls to your Ethereum node. The billing token is used to track your accessor object for billing Ethereum API requests made to your Ethereum nodes.

`CreationDate`  <a name="CreationDate-fn::getatt"></a>
The creation date and time of the accessor.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the accessor.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the accessor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
