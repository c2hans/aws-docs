---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-meteredproduct.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::MeteredProduct
<a name="aws-resource-deadline-meteredproduct"></a>

Adds a metered product.

## Syntax
<a name="aws-resource-deadline-meteredproduct-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-meteredproduct-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::MeteredProduct",
  "Properties" : {
      "[LicenseEndpointId](#cfn-deadline-meteredproduct-licenseendpointid)" : {{String}},
      "[ProductId](#cfn-deadline-meteredproduct-productid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-deadline-meteredproduct-syntax.yaml"></a>

```
Type: AWS::Deadline::MeteredProduct
Properties:
  [LicenseEndpointId](#cfn-deadline-meteredproduct-licenseendpointid): {{String}}
  [ProductId](#cfn-deadline-meteredproduct-productid): {{String}}
```

## Properties
<a name="aws-resource-deadline-meteredproduct-properties"></a>

`LicenseEndpointId`  <a name="cfn-deadline-meteredproduct-licenseendpointid"></a>
The Amazon EC2 identifier of the license endpoint.
*Required*: No
*Type*: String
*Pattern*: `^le-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProductId`  <a name="cfn-deadline-meteredproduct-productid"></a>
The product ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z]{1,32}-[.0-9a-z]{1,32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-deadline-meteredproduct-return-values"></a>

### Ref
<a name="aws-resource-deadline-meteredproduct-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the metered product.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-meteredproduct-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-meteredproduct-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the metered product.

`Family`  <a name="Family-fn::getatt"></a>
The family to which the metered product belongs.

`Port`  <a name="Port-fn::getatt"></a>
The port on which the metered product should run.

`Vendor`  <a name="Vendor-fn::getatt"></a>
The vendor.
