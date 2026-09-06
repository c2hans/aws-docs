---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute GatewayRouteHostnameRewrite
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite"></a>

An object representing the gateway route host name to rewrite.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite-syntax.json"></a>

```
{
  "[DefaultTargetHostname](#cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite-syntax.yaml"></a>

```
  [DefaultTargetHostname](#cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite-properties"></a>

`DefaultTargetHostname`  <a name="cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname"></a>
The default target host name to write to.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
