---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-integrationresourceproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::IntegrationResourceProperty
<a name="aws-resource-glue-integrationresourceproperty"></a>

The `AWS::Glue::IntegrationResourceProperty` resource type can be used to setup `ResourceProperty` of the AWS Glue connection (for the SaaS source), DynamoDB Database (for DynamoDB source), or AWS Glue database ARN (for the target). ResourceProperty is used to define the properties requires to setup the integration, including the role to access the connection or database, KMS keys, event bus for event notifications and VPC connection. To set both source and target properties the same API needs to be invoked twice, once with the AWS Glue connection ARN as ResourceArn with SourceProcessingProperties and next, with the AWS Glue database ARN as ResourceArn with TargetProcessingProperties respectively.

## Syntax
<a name="aws-resource-glue-integrationresourceproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-integrationresourceproperty-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::IntegrationResourceProperty",
  "Properties" : {
      "[ResourceArn](#cfn-glue-integrationresourceproperty-resourcearn)" : {{String}},
      "[SourceProcessingProperties](#cfn-glue-integrationresourceproperty-sourceprocessingproperties)" : {{SourceProcessingProperties}},
      "[Tags](#cfn-glue-integrationresourceproperty-tags)" : {{[ Tag, ... ]}},
      "[TargetProcessingProperties](#cfn-glue-integrationresourceproperty-targetprocessingproperties)" : {{TargetProcessingProperties}}
    }
}
```

### YAML
<a name="aws-resource-glue-integrationresourceproperty-syntax.yaml"></a>

```
Type: AWS::Glue::IntegrationResourceProperty
Properties:
  [ResourceArn](#cfn-glue-integrationresourceproperty-resourcearn): {{String}}
  [SourceProcessingProperties](#cfn-glue-integrationresourceproperty-sourceprocessingproperties): {{
    SourceProcessingProperties}}
  [Tags](#cfn-glue-integrationresourceproperty-tags): {{
    - Tag}}
  [TargetProcessingProperties](#cfn-glue-integrationresourceproperty-targetprocessingproperties): {{
    TargetProcessingProperties}}
```

## Properties
<a name="aws-resource-glue-integrationresourceproperty-properties"></a>

`ResourceArn`  <a name="cfn-glue-integrationresourceproperty-resourcearn"></a>
The connection ARN of the source, or the database ARN of the target.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:.*:.*:[0-9]+:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceProcessingProperties`  <a name="cfn-glue-integrationresourceproperty-sourceprocessingproperties"></a>
The resource properties associated with the integration source.
*Required*: No
*Type*: [SourceProcessingProperties](aws-properties-glue-integrationresourceproperty-sourceprocessingproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-glue-integrationresourceproperty-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-integrationresourceproperty-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetProcessingProperties`  <a name="cfn-glue-integrationresourceproperty-targetprocessingproperties"></a>
The structure used to define the resource properties associated with the integration target.
*Required*: No
*Type*: [TargetProcessingProperties](aws-properties-glue-integrationresourceproperty-targetprocessingproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-integrationresourceproperty-return-values"></a>

### Ref
<a name="aws-resource-glue-integrationresourceproperty-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns The resource property arn.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-glue-integrationresourceproperty-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-glue-integrationresourceproperty-return-values-fn--getatt-fn--getatt"></a>

`ResourcePropertyArn`  <a name="ResourcePropertyArn-fn::getatt"></a>
Property description not available.
