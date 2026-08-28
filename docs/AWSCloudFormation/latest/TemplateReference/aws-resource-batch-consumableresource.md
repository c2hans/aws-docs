---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-consumableresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ConsumableResource
<a name="aws-resource-batch-consumableresource"></a>

The `AWS::Batch::ConsumableResource` resource specifies the parameters for an AWS Batch consumable resource. For more information, see [Resource-aware scheduling](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling.html) in the * AWS Batch User Guide *.

## Syntax
<a name="aws-resource-batch-consumableresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-batch-consumableresource-syntax.json"></a>

```
{
  "Type" : "AWS::Batch::ConsumableResource",
  "Properties" : {
      "[ConsumableResourceName](#cfn-batch-consumableresource-consumableresourcename)" : {{String}},
      "[ResourceType](#cfn-batch-consumableresource-resourcetype)" : {{String}},
      "[Tags](#cfn-batch-consumableresource-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TotalQuantity](#cfn-batch-consumableresource-totalquantity)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-batch-consumableresource-syntax.yaml"></a>

```
Type: AWS::Batch::ConsumableResource
Properties:
  [ConsumableResourceName](#cfn-batch-consumableresource-consumableresourcename): {{String}}
  [ResourceType](#cfn-batch-consumableresource-resourcetype): {{String}}
  [Tags](#cfn-batch-consumableresource-tags): {{
    {{Key}}: {{Value}}}}
  [TotalQuantity](#cfn-batch-consumableresource-totalquantity): {{Integer}}
```

## Properties
<a name="aws-resource-batch-consumableresource-properties"></a>

`ConsumableResourceName`  <a name="cfn-batch-consumableresource-consumableresourcename"></a>
The name of the consumable resource.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceType`  <a name="cfn-batch-consumableresource-resourcetype"></a>
Indicates whether the resource is available to be re-used after a job completes. Can be one of:
+  `REPLENISHABLE`
+  `NON_REPLENISHABLE`
*Required*: Yes
*Type*: String
*Allowed values*: `REPLENISHABLE | NON_REPLENISHABLE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-batch-consumableresource-tags"></a>
The tags that you apply to the consumable resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalQuantity`  <a name="cfn-batch-consumableresource-totalquantity"></a>
The total amount of the consumable resource that is available.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-batch-consumableresource-return-values"></a>

### Ref
<a name="aws-resource-batch-consumableresource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the consumable resource ARN, such as `arn:aws:batch:us-east-1:555555555555:consumable-resource/Resource`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-batch-consumableresource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-batch-consumableresource-return-values-fn--getatt-fn--getatt"></a>

`AvailableQuantity`  <a name="AvailableQuantity-fn::getatt"></a>
The amount of the consumable resource that is currently available to use.

`ConsumableResourceArn`  <a name="ConsumableResourceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the consumable resource.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp (in milliseconds) for when the consumable resource was created.

`InUseQuantity`  <a name="InUseQuantity-fn::getatt"></a>
The amount of the consumable resource that is currently in use.

## See also
<a name="aws-resource-batch-consumableresource--seealso"></a>
+ [Resource-aware scheduling](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling.html) in the * AWS Batch User Guide *.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
