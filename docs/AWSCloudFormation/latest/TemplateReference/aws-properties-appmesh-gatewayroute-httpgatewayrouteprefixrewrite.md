---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpGatewayRoutePrefixRewrite
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite"></a>

An object representing the beginning characters of the route to rewrite.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-syntax.json"></a>

```
{
  "[DefaultPrefix](#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix)" : {{String}},
  "[Value](#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-syntax.yaml"></a>

```
  [DefaultPrefix](#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix): {{String}}
  [Value](#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-properties"></a>

`DefaultPrefix`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix"></a>
The default prefix used to replace the incoming route prefix when rewritten.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value"></a>
The value used to replace the incoming route prefix when rewritten.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
