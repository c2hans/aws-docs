---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-multiregionendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MultiRegionEndpoint
<a name="aws-resource-ses-multiregionendpoint"></a>

Creates a multi-region endpoint (global-endpoint).

The primary region is going to be the AWS-Region where the operation is executed. The secondary region has to be provided in request's parameters. From the data flow standpoint there is no difference between primary and secondary regions - sending traffic is divided between the two. The primary region is the region where the resource has been created and where it can be managed.

## Syntax
<a name="aws-resource-ses-multiregionendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-multiregionendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MultiRegionEndpoint",
  "Properties" : {
      "[Details](#cfn-ses-multiregionendpoint-details)" : {{Details}},
      "[EndpointName](#cfn-ses-multiregionendpoint-endpointname)" : {{String}},
      "[Tags](#cfn-ses-multiregionendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-multiregionendpoint-syntax.yaml"></a>

```
Type: AWS::SES::MultiRegionEndpoint
Properties:
  [Details](#cfn-ses-multiregionendpoint-details): {{
    Details}}
  [EndpointName](#cfn-ses-multiregionendpoint-endpointname): {{String}}
  [Tags](#cfn-ses-multiregionendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-multiregionendpoint-properties"></a>

`Details`  <a name="cfn-ses-multiregionendpoint-details"></a>
Contains details of a multi-region endpoint (global-endpoint) being created.
*Required*: Yes
*Type*: [Details](aws-properties-ses-multiregionendpoint-details.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointName`  <a name="cfn-ses-multiregionendpoint-endpointname"></a>
The name of the multi-region endpoint (global-endpoint).
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ses-multiregionendpoint-tags"></a>
An array of objects that define the tags (keys and values) to associate with the multi-region endpoint (global-endpoint).
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-multiregionendpoint-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-multiregionendpoint-return-values"></a>

### Ref
<a name="aws-resource-ses-multiregionendpoint-return-values-ref"></a>
