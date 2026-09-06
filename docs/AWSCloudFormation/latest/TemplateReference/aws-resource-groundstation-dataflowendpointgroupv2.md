---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-groundstation-dataflowendpointgroupv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2
<a name="aws-resource-groundstation-dataflowendpointgroupv2"></a>

Creates a `DataflowEndpoint` group containing the specified list of Ground Station Agent based endpoints.

The `name` field in each endpoint is used in your mission profile `DataflowEndpointConfig` to specify which endpoints to use during a contact.

When a contact uses multiple `DataflowEndpointConfig` objects, each `Config` must match a `DataflowEndpoint` in the same group.

## Syntax
<a name="aws-resource-groundstation-dataflowendpointgroupv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-groundstation-dataflowendpointgroupv2-syntax.json"></a>

```
{
  "Type" : "AWS::GroundStation::DataflowEndpointGroupV2",
  "Properties" : {
      "[ContactPostPassDurationSeconds](#cfn-groundstation-dataflowendpointgroupv2-contactpostpassdurationseconds)" : {{Integer}},
      "[ContactPrePassDurationSeconds](#cfn-groundstation-dataflowendpointgroupv2-contactprepassdurationseconds)" : {{Integer}},
      "[Endpoints](#cfn-groundstation-dataflowendpointgroupv2-endpoints)" : {{[ CreateEndpointDetails, ... ]}},
      "[Tags](#cfn-groundstation-dataflowendpointgroupv2-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-groundstation-dataflowendpointgroupv2-syntax.yaml"></a>

```
Type: AWS::GroundStation::DataflowEndpointGroupV2
Properties:
  [ContactPostPassDurationSeconds](#cfn-groundstation-dataflowendpointgroupv2-contactpostpassdurationseconds): {{Integer}}
  [ContactPrePassDurationSeconds](#cfn-groundstation-dataflowendpointgroupv2-contactprepassdurationseconds): {{Integer}}
  [Endpoints](#cfn-groundstation-dataflowendpointgroupv2-endpoints): {{
    - CreateEndpointDetails}}
  [Tags](#cfn-groundstation-dataflowendpointgroupv2-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-groundstation-dataflowendpointgroupv2-properties"></a>

`ContactPostPassDurationSeconds`  <a name="cfn-groundstation-dataflowendpointgroupv2-contactpostpassdurationseconds"></a>
Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `480`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContactPrePassDurationSeconds`  <a name="cfn-groundstation-dataflowendpointgroupv2-contactprepassdurationseconds"></a>
Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `480`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Endpoints`  <a name="cfn-groundstation-dataflowendpointgroupv2-endpoints"></a>
List of endpoints for the dataflow endpoint group.
*Required*: No
*Type*: Array of [CreateEndpointDetails](aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-groundstation-dataflowendpointgroupv2-tags"></a>
Tags assigned to a resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-groundstation-dataflowendpointgroupv2-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-groundstation-dataflowendpointgroupv2-return-values"></a>

### Ref
<a name="aws-resource-groundstation-dataflowendpointgroupv2-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-groundstation-dataflowendpointgroupv2-return-values-fn--getatt"></a>

####
<a name="aws-resource-groundstation-dataflowendpointgroupv2-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`EndpointDetails`  <a name="EndpointDetails-fn::getatt"></a>
Information about the endpoint details.
