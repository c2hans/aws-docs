---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigatewayv2-portalproduct.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::PortalProduct
<a name="aws-resource-apigatewayv2-portalproduct"></a>

Creates a new portal product.

## Syntax
<a name="aws-resource-apigatewayv2-portalproduct-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigatewayv2-portalproduct-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGatewayV2::PortalProduct",
  "Properties" : {
      "[Description](#cfn-apigatewayv2-portalproduct-description)" : {{String}},
      "[DisplayName](#cfn-apigatewayv2-portalproduct-displayname)" : {{String}},
      "[Tags](#cfn-apigatewayv2-portalproduct-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-apigatewayv2-portalproduct-syntax.yaml"></a>

```
Type: AWS::ApiGatewayV2::PortalProduct
Properties:
  [Description](#cfn-apigatewayv2-portalproduct-description): {{String}}
  [DisplayName](#cfn-apigatewayv2-portalproduct-displayname): {{String}}
  [Tags](#cfn-apigatewayv2-portalproduct-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-apigatewayv2-portalproduct-properties"></a>

`Description`  <a name="cfn-apigatewayv2-portalproduct-description"></a>
A description of the portal product.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-apigatewayv2-portalproduct-displayname"></a>
The name of the portal product as it appears in a published portal.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-apigatewayv2-portalproduct-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-apigatewayv2-portalproduct-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-apigatewayv2-portalproduct-return-values"></a>

### Ref
<a name="aws-resource-apigatewayv2-portalproduct-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-apigatewayv2-portalproduct-return-values-fn--getatt"></a>

####
<a name="aws-resource-apigatewayv2-portalproduct-return-values-fn--getatt-fn--getatt"></a>

`LastModified`  <a name="LastModified-fn::getatt"></a>
The timestamp when the portal product was last modified.

`PortalProductArn`  <a name="PortalProductArn-fn::getatt"></a>
The ARN of the portal product.

`PortalProductId`  <a name="PortalProductId-fn::getatt"></a>
The portal product identifier.
