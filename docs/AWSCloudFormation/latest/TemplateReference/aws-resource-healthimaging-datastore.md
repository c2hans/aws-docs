---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-healthimaging-datastore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthImaging::Datastore
<a name="aws-resource-healthimaging-datastore"></a>

Create a data store.

## Syntax
<a name="aws-resource-healthimaging-datastore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-healthimaging-datastore-syntax.json"></a>

```
{
  "Type" : "AWS::HealthImaging::Datastore",
  "Properties" : {
      "[DatastoreName](#cfn-healthimaging-datastore-datastorename)" : {{String}},
      "[KmsKeyArn](#cfn-healthimaging-datastore-kmskeyarn)" : {{String}},
      "[Tags](#cfn-healthimaging-datastore-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-healthimaging-datastore-syntax.yaml"></a>

```
Type: AWS::HealthImaging::Datastore
Properties:
  [DatastoreName](#cfn-healthimaging-datastore-datastorename): {{String}}
  [KmsKeyArn](#cfn-healthimaging-datastore-kmskeyarn): {{String}}
  [Tags](#cfn-healthimaging-datastore-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-healthimaging-datastore-properties"></a>

`DatastoreName`  <a name="cfn-healthimaging-datastore-datastorename"></a>
The data store name.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9._/#-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-healthimaging-datastore-kmskeyarn"></a>
The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-healthimaging-datastore-tags"></a>
The tags provided when creating a data store.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-healthimaging-datastore-return-values"></a>

### Ref
<a name="aws-resource-healthimaging-datastore-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

### Fn::GetAtt
<a name="aws-resource-healthimaging-datastore-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-healthimaging-datastore-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the data store was created.

`DatastoreArn`  <a name="DatastoreArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the data store.

`DatastoreId`  <a name="DatastoreId-fn::getatt"></a>
The data store identifier.

`DatastoreStatus`  <a name="DatastoreStatus-fn::getatt"></a>
The data store status.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the data store was last updated.
