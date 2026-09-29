---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-datasetintegration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::DatasetIntegration
<a name="aws-resource-observabilityadmin-datasetintegration"></a>

Creates a dataset integration for the caller's account in the current region and returns its ARN.

To use this operation, you must have permission to access the dataset integration resources through the IAM role specified in the `RoleArn` parameter.

If a dataset integration already exists for the account, this operation fails with a `ConflictException`.

## Syntax
<a name="aws-resource-observabilityadmin-datasetintegration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-datasetintegration-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::DatasetIntegration",
  "Properties" : {
      "[RoleArn](#cfn-observabilityadmin-datasetintegration-rolearn)" : {{String}},
      "[Tags](#cfn-observabilityadmin-datasetintegration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-datasetintegration-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::DatasetIntegration
Properties:
  [RoleArn](#cfn-observabilityadmin-datasetintegration-rolearn): {{String}}
  [Tags](#cfn-observabilityadmin-datasetintegration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-observabilityadmin-datasetintegration-properties"></a>

`RoleArn`  <a name="cfn-observabilityadmin-datasetintegration-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the dataset integration.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-observabilityadmin-datasetintegration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-datasetintegration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-observabilityadmin-datasetintegration-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-datasetintegration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-datasetintegration-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-datasetintegration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dataset integration.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the dataset integration was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the dataset integration was last updated.
