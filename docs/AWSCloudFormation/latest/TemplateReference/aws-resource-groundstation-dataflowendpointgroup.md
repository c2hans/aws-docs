---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-groundstation-dataflowendpointgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup
<a name="aws-resource-groundstation-dataflowendpointgroup"></a>

Creates a Dataflow Endpoint Group request.

 Dataflow endpoint groups contain a list of endpoints. When the name of a dataflow endpoint group is specified in a mission profile, the Ground Station service will connect to the endpoints and flow data during a contact.

 For more information about dataflow endpoint groups, see [Dataflow Endpoint Groups](https://docs.aws.amazon.com/ground-station/latest/ug/dataflowendpointgroups.html).

## Syntax
<a name="aws-resource-groundstation-dataflowendpointgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-groundstation-dataflowendpointgroup-syntax.json"></a>

```
{
  "Type" : "AWS::GroundStation::DataflowEndpointGroup",
  "Properties" : {
      "[ContactPostPassDurationSeconds](#cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds)" : {{Integer}},
      "[ContactPrePassDurationSeconds](#cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds)" : {{Integer}},
      "[EndpointDetails](#cfn-groundstation-dataflowendpointgroup-endpointdetails)" : {{[ EndpointDetails, ... ]}},
      "[Tags](#cfn-groundstation-dataflowendpointgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-groundstation-dataflowendpointgroup-syntax.yaml"></a>

```
Type: AWS::GroundStation::DataflowEndpointGroup
Properties:
  [ContactPostPassDurationSeconds](#cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds): {{Integer}}
  [ContactPrePassDurationSeconds](#cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds): {{Integer}}
  [EndpointDetails](#cfn-groundstation-dataflowendpointgroup-endpointdetails): {{
    - EndpointDetails}}
  [Tags](#cfn-groundstation-dataflowendpointgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-groundstation-dataflowendpointgroup-properties"></a>

`ContactPostPassDurationSeconds`  <a name="cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds"></a>
 Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a `POSTPASS` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the `POSTPASS` state.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `480`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContactPrePassDurationSeconds`  <a name="cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds"></a>
 Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a `PREPASS` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the `PREPASS` state.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `480`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointDetails`  <a name="cfn-groundstation-dataflowendpointgroup-endpointdetails"></a>
 List of Endpoint Details, containing address and port for each endpoint. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix AWS Ground Station Agent endpoints with Dataflow endpoints in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type.
*Required*: Yes
*Type*: [Array](aws-properties-groundstation-dataflowendpointgroup-endpointdetails.md) of [EndpointDetails](aws-properties-groundstation-dataflowendpointgroup-endpointdetails.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-groundstation-dataflowendpointgroup-tags"></a>
 Tags assigned to a resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-groundstation-dataflowendpointgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-groundstation-dataflowendpointgroup-return-values"></a>

### Ref
<a name="aws-resource-groundstation-dataflowendpointgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the dataflow endpoint group. For example:

 `{ "Ref": "DataflowEndpointGroup" }`

 For the Ground Station dataflow endpoint group, `Ref` returns the ARN of the dataflow endpoint group.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-groundstation-dataflowendpointgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-groundstation-dataflowendpointgroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the dataflow endpoint group, such as `arn:aws:groundstation:us-east-2:012345678910:dataflow-endpoint-group/9940bf3b-d2ba-427e-9906-842b5e5d2296`.

`Id`  <a name="Id-fn::getatt"></a>
 UUID of a dataflow endpoint group.

## Examples
<a name="aws-resource-groundstation-dataflowendpointgroup--examples"></a>

### Create a DataflowEndpointGroup
<a name="aws-resource-groundstation-dataflowendpointgroup--examples--Create_a_DataflowEndpointGroup"></a>

The following example creates a Ground Station `DataflowEndpointGroup`

#### JSON
<a name="aws-resource-groundstation-dataflowendpointgroup--examples--Create_a_DataflowEndpointGroup--json"></a>

```
{
  "Resources": {
    "myDataflowEndpointGroup": {
      "Type": "AWS::GroundStation::DataflowEndpointGroup",
      "Properties": {
        "EndpointDetails": [
          {
            "SecurityDetails": {
              "SubnetIds": [
                "subnet-6782e71e"
              ],
              "SecurityGroupIds": [
                "sg-6979fe18"
              ],
              "RoleArn": "arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEBQ4PI"
            },
            "Endpoint": {
              "Name": "myEndpoint",
              "Address": {
                "Name": "172.10.0.2",
                "Port": 44720
              },
              "Mtu": 1500
            }
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-groundstation-dataflowendpointgroup--examples--Create_a_DataflowEndpointGroup--yaml"></a>

```
Resources:
  myDataflowEndpointGroup:
    Type: AWS::GroundStation::DataflowEndpointGroup
    Properties:
      EndpointDetails:
        - SecurityDetails:
            SubnetIds:
              - subnet-12345678
            SecurityGroupIds:
              - sg-87654321
            RoleArn: arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEABCDE
      Endpoint:
        Name: myEndpoint
        Address:
          Name: 172.10.0.2
          Port: 44720
        Mtu: 1500
```
