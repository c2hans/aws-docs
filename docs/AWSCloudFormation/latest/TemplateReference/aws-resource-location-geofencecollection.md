---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-geofencecollection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::GeofenceCollection
<a name="aws-resource-location-geofencecollection"></a>

The `AWS::Location::GeofenceCollection` resource specifies the ability to detect and act when a tracked device enters or exits a defined geographical boundary known as a geofence.

## Syntax
<a name="aws-resource-location-geofencecollection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-location-geofencecollection-syntax.json"></a>

```
{
  "Type" : "AWS::Location::GeofenceCollection",
  "Properties" : {
      "[CollectionName](#cfn-location-geofencecollection-collectionname)" : {{String}},
      "[Description](#cfn-location-geofencecollection-description)" : {{String}},
      "[KmsKeyId](#cfn-location-geofencecollection-kmskeyid)" : {{String}},
      "[Tags](#cfn-location-geofencecollection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-location-geofencecollection-syntax.yaml"></a>

```
Type: AWS::Location::GeofenceCollection
Properties:
  [CollectionName](#cfn-location-geofencecollection-collectionname): {{String}}
  [Description](#cfn-location-geofencecollection-description): {{String}}
  [KmsKeyId](#cfn-location-geofencecollection-kmskeyid): {{String}}
  [Tags](#cfn-location-geofencecollection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-location-geofencecollection-properties"></a>

`CollectionName`  <a name="cfn-location-geofencecollection-collectionname"></a>
A custom name for the geofence collection.
Requirements:
+ Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique geofence collection name.
+ No spaces allowed. For example, `ExampleGeofenceCollection`.
*Required*: Yes
*Type*: String
*Pattern*: `^[-._\w]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-location-geofencecollection-description"></a>
An optional description for the geofence collection.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-location-geofencecollection-kmskeyid"></a>
A key identifier for an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html). Enter a key ID, key ARN, alias name, or alias ARN.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-location-geofencecollection-tags"></a>
Applies one or more tags to the geofence collection. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.
Format: `"key" : "value"`
Restrictions:
+ Maximum 50 tags per resource
+ Each resource tag must be unique with a maximum of one value.
+ Maximum key length: 128 Unicode characters in UTF-8
+ Maximum value length: 256 Unicode characters in UTF-8
+ Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: \+ - = . \_ : / @.
+ Cannot use "aws:" as a prefix for a key.
*Required*: No
*Type*: Array of [Tag](aws-properties-location-geofencecollection-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-location-geofencecollection-return-values"></a>

### Ref
<a name="aws-resource-location-geofencecollection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `GeofenceCollection` name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-location-geofencecollection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-location-geofencecollection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`

`CollectionArn`  <a name="CollectionArn-fn::getatt"></a>
Synonym for `Arn`. The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS.
+ Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The timestamp for when the geofence collection resource was created in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
The timestamp for when the geofence collection resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
