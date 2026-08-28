---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-productsubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ProductSubscription
<a name="aws-resource-securityhub-productsubscription"></a>

The `AWS::SecurityHub::ProductSubscription` resource creates a subscription to a third-party product that generates findings that you want to receive in AWS Security Hub CSPM. For a list of integrations to third-party products, see [Available third-party partner product integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html) in the *AWS Security Hub CSPM User Guide*.

To change a product subscription, remove the current product subscription resource, and then create a new one.

Tags aren't supported for this resource.

## Syntax
<a name="aws-resource-securityhub-productsubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-productsubscription-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::ProductSubscription",
  "Properties" : {
      "[ProductArn](#cfn-securityhub-productsubscription-productarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-productsubscription-syntax.yaml"></a>

```
Type: AWS::SecurityHub::ProductSubscription
Properties:
  [ProductArn](#cfn-securityhub-productsubscription-productarn): {{String}}
```

## Properties
<a name="aws-resource-securityhub-productsubscription-properties"></a>

`ProductArn`  <a name="cfn-securityhub-productsubscription-productarn"></a>
The ARN of the product to enable the integration for.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws\S*:securityhub:\S*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securityhub-productsubscription-return-values"></a>

### Ref
<a name="aws-resource-securityhub-productsubscription-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of your subscription to the product to enable integrations for. For example, `arn:aws:securityhub:us-east-1:123456789012:product-subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-productsubscription-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-productsubscription-return-values-fn--getatt-fn--getatt"></a>

`ProductSubscriptionArn`  <a name="ProductSubscriptionArn-fn::getatt"></a>
The ARN of your subscription to the product to enable integrations for.

## Examples
<a name="aws-resource-securityhub-productsubscription--examples"></a>

### Creating a Security Hub CSPM product subscription
<a name="aws-resource-securityhub-productsubscription--examples--Creating_a_product_subscription"></a>

The following example creates a Security Hub CSPM product subscription to the specified third-party product.

#### JSON
<a name="aws-resource-securityhub-productsubscription--examples--Creating_a_product_subscription--json"></a>

```
{
	"Description": "Example template to create a Security Hub product subscription",
	"Resources": {
		"SecurityHubProductSubscription": {
			"Type": "AWS::SecurityHub::ProductSubscription",
			"Properties": {
				"ProductArn": {
					"Fn::Sub": "arn:${AWS::Partition}:securityhub:${AWS::Region}::product/aws/example"
				}
			}
		}
	}
}
```

#### YAML
<a name="aws-resource-securityhub-productsubscription--examples--Creating_a_product_subscription--yaml"></a>

```
Description: Example template to create a Security Hub product subscription
Resources:
  SecurityHubProductSubscription:
    Type: 'AWS::SecurityHub::ProductSubscription'
    Properties:
      ProductArn: !Sub 'arn:${AWS::Partition}:securityhub:${AWS::Region}::product/aws/example'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
