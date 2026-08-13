---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptune-dbclusterparametergroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Neptune::DBClusterParameterGroup
<a name="aws-resource-neptune-dbclusterparametergroup"></a>

The `AWS::Neptune::DBClusterParameterGroup` resource creates a new Amazon Neptune DB cluster parameter group.

**Note**
Applying a parameter group to a DB cluster might require instances to reboot, resulting in a database outage while the instances reboot.

**Note**
If you provide a custom `DBClusterParameterGroup` that you associate with the `DBCluster`, it is best to specify an `EngineVersion` property in the `DBCluster`. That `EngineVersion` needs to be compatible with the value of the `Family` property in the `DBClusterParameterGroup`.

## Syntax
<a name="aws-resource-neptune-dbclusterparametergroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptune-dbclusterparametergroup-syntax.json"></a>

```
{
  "Type" : "AWS::Neptune::DBClusterParameterGroup",
  "Properties" : {
      "[Description](#cfn-neptune-dbclusterparametergroup-description)" : {{String}},
      "[Family](#cfn-neptune-dbclusterparametergroup-family)" : {{String}},
      "[Name](#cfn-neptune-dbclusterparametergroup-name)" : {{String}},
      "[Parameters](#cfn-neptune-dbclusterparametergroup-parameters)" : {{Json}},
      "[Tags](#cfn-neptune-dbclusterparametergroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-neptune-dbclusterparametergroup-syntax.yaml"></a>

```
Type: AWS::Neptune::DBClusterParameterGroup
Properties:
  [Description](#cfn-neptune-dbclusterparametergroup-description): {{String}}
  [Family](#cfn-neptune-dbclusterparametergroup-family): {{String}}
  [Name](#cfn-neptune-dbclusterparametergroup-name): {{String}}
  [Parameters](#cfn-neptune-dbclusterparametergroup-parameters): {{Json}}
  [Tags](#cfn-neptune-dbclusterparametergroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-neptune-dbclusterparametergroup-properties"></a>

`Description`  <a name="cfn-neptune-dbclusterparametergroup-description"></a>
Provides the customer-specified description for this DB cluster parameter group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Family`  <a name="cfn-neptune-dbclusterparametergroup-family"></a>
Must be `neptune1` for engine versions prior to [1.2.0.0](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.2.0.0.html), or `neptune1.2` for engine version `1.2.0.0` and higher.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-neptune-dbclusterparametergroup-name"></a>
Provides the name of the DB cluster parameter group.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-neptune-dbclusterparametergroup-parameters"></a>
The parameters to set for this DB cluster parameter group.
The parameters are expressed as a JSON object consisting of key-value pairs.
If you update the parameters, some interruption may occur depending on which parameters you update.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-neptune-dbclusterparametergroup-tags"></a>
The tags that you want to attach to this parameter group.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptune-dbclusterparametergroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-neptune-dbclusterparametergroup-return-values"></a>

### Ref
<a name="aws-resource-neptune-dbclusterparametergroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
