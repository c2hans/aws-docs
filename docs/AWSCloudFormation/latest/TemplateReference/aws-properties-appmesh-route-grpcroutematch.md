---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-grpcroutematch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route GrpcRouteMatch
<a name="aws-properties-appmesh-route-grpcroutematch"></a>

An object that represents the criteria for determining a request match.

## Syntax
<a name="aws-properties-appmesh-route-grpcroutematch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-grpcroutematch-syntax.json"></a>

```
{
  "[Metadata](#cfn-appmesh-route-grpcroutematch-metadata)" : {{[ GrpcRouteMetadata, ... ]}},
  "[MethodName](#cfn-appmesh-route-grpcroutematch-methodname)" : {{String}},
  "[Port](#cfn-appmesh-route-grpcroutematch-port)" : {{Integer}},
  "[ServiceName](#cfn-appmesh-route-grpcroutematch-servicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-route-grpcroutematch-syntax.yaml"></a>

```
  [Metadata](#cfn-appmesh-route-grpcroutematch-metadata): {{
    - GrpcRouteMetadata}}
  [MethodName](#cfn-appmesh-route-grpcroutematch-methodname): {{String}}
  [Port](#cfn-appmesh-route-grpcroutematch-port): {{Integer}}
  [ServiceName](#cfn-appmesh-route-grpcroutematch-servicename): {{String}}
```

## Properties
<a name="aws-properties-appmesh-route-grpcroutematch-properties"></a>

`Metadata`  <a name="cfn-appmesh-route-grpcroutematch-metadata"></a>
An object that represents the data to match from the request.
*Required*: No
*Type*: Array of [GrpcRouteMetadata](aws-properties-appmesh-route-grpcroutemetadata.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MethodName`  <a name="cfn-appmesh-route-grpcroutematch-methodname"></a>
The method name to match from the request. If you specify a name, you must also specify a `serviceName`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-appmesh-route-grpcroutematch-port"></a>
The port number to match on.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-appmesh-route-grpcroutematch-servicename"></a>
The fully qualified domain name for the service to match from the request.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
