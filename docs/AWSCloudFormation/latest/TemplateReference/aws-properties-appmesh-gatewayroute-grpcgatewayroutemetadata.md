---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute GrpcGatewayRouteMetadata
<a name="aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata"></a>

An object representing the metadata of the gateway route.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata-syntax.json"></a>

```
{
  "[Invert](#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert)" : {{Boolean}},
  "[Match](#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match)" : {{GatewayRouteMetadataMatch}},
  "[Name](#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata-syntax.yaml"></a>

```
  [Invert](#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert): {{Boolean}}
  [Match](#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match): {{
    GatewayRouteMetadataMatch}}
  [Name](#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata-properties"></a>

`Invert`  <a name="cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match"></a>
The criteria for determining a metadata match.
*Required*: No
*Type*: [GatewayRouteMetadataMatch](aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name"></a>
A name for the gateway route metadata.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
