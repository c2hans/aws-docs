---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotfleetwise-vehicle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Vehicle
<a name="aws-resource-iotfleetwise-vehicle"></a>

 Creates a vehicle, which is an instance of a vehicle model (model manifest). Vehicles created from the same vehicle model consist of the same signals inherited from the vehicle model.

**Note**
 If you have an existing AWS IoT thing, you can use AWS IoT FleetWise to create a vehicle and collect data from your thing.

For more information, see [Vehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicles.html) in the *AWS IoT FleetWise Developer Guide*.

## Syntax
<a name="aws-resource-iotfleetwise-vehicle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotfleetwise-vehicle-syntax.json"></a>

```
{
  "Type" : "AWS::IoTFleetWise::Vehicle",
  "Properties" : {
      "[AssociationBehavior](#cfn-iotfleetwise-vehicle-associationbehavior)" : {{String}},
      "[Attributes](#cfn-iotfleetwise-vehicle-attributes)" : {{{{{Key}}: {{Value}}, ...}}},
      "[DecoderManifestArn](#cfn-iotfleetwise-vehicle-decodermanifestarn)" : {{String}},
      "[ModelManifestArn](#cfn-iotfleetwise-vehicle-modelmanifestarn)" : {{String}},
      "[Name](#cfn-iotfleetwise-vehicle-name)" : {{String}},
      "[StateTemplates](#cfn-iotfleetwise-vehicle-statetemplates)" : {{[ StateTemplateAssociation, ... ]}},
      "[Tags](#cfn-iotfleetwise-vehicle-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotfleetwise-vehicle-syntax.yaml"></a>

```
Type: AWS::IoTFleetWise::Vehicle
Properties:
  [AssociationBehavior](#cfn-iotfleetwise-vehicle-associationbehavior): {{String}}
  [Attributes](#cfn-iotfleetwise-vehicle-attributes): {{
    {{Key}}: {{Value}}}}
  [DecoderManifestArn](#cfn-iotfleetwise-vehicle-decodermanifestarn): {{String}}
  [ModelManifestArn](#cfn-iotfleetwise-vehicle-modelmanifestarn): {{String}}
  [Name](#cfn-iotfleetwise-vehicle-name): {{String}}
  [StateTemplates](#cfn-iotfleetwise-vehicle-statetemplates): {{
    - StateTemplateAssociation}}
  [Tags](#cfn-iotfleetwise-vehicle-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotfleetwise-vehicle-properties"></a>

`AssociationBehavior`  <a name="cfn-iotfleetwise-vehicle-associationbehavior"></a>
 An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.
*Required*: No
*Type*: String
*Allowed values*: `CreateIotThing | ValidateIotThingExists`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attributes`  <a name="cfn-iotfleetwise-vehicle-attributes"></a>
 Static information about a vehicle in a key-value pair. For example: `"engine Type"` : `"v6"`
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecoderManifestArn`  <a name="cfn-iotfleetwise-vehicle-decodermanifestarn"></a>
The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelManifestArn`  <a name="cfn-iotfleetwise-vehicle-modelmanifestarn"></a>
The Amazon Resource Name (ARN) of the vehicle model (model manifest) to create the vehicle from.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotfleetwise-vehicle-name"></a>
The unique ID of the vehicle.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z\d\-_:]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StateTemplates`  <a name="cfn-iotfleetwise-vehicle-statetemplates"></a>
Associate state templates to track the state of the vehicle. State templates determine which signal updates the vehicle sends to the cloud.
*Required*: No
*Type*: Array of [StateTemplateAssociation](aws-properties-iotfleetwise-vehicle-statetemplateassociation.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotfleetwise-vehicle-tags"></a>
 Metadata which can be used to manage the vehicle.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotfleetwise-vehicle-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotfleetwise-vehicle-return-values"></a>

### Ref
<a name="aws-resource-iotfleetwise-vehicle-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iotfleetwise-vehicle-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotfleetwise-vehicle-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the vehicle.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time).

`LastModificationTime`  <a name="LastModificationTime-fn::getatt"></a>
The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
