---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicastreamspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable ReplicaStreamSpecification
<a name="aws-properties-dynamodb-globaltable-replicastreamspecification"></a>

Represents the DynamoDB Streams configuration for a global table replica.

## Syntax
<a name="aws-properties-dynamodb-globaltable-replicastreamspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-replicastreamspecification-syntax.json"></a>

```
{
  "[ResourcePolicy](#cfn-dynamodb-globaltable-replicastreamspecification-resourcepolicy)" : {{ResourcePolicy}},
  "[Tags](#cfn-dynamodb-globaltable-replicastreamspecification-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-replicastreamspecification-syntax.yaml"></a>

```
  [ResourcePolicy](#cfn-dynamodb-globaltable-replicastreamspecification-resourcepolicy): {{
    ResourcePolicy}}
  [Tags](#cfn-dynamodb-globaltable-replicastreamspecification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-replicastreamspecification-properties"></a>

`ResourcePolicy`  <a name="cfn-dynamodb-globaltable-replicastreamspecification-resourcepolicy"></a>
A resource-based policy document that contains the permissions for the specified stream of a DynamoDB global table replica. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource.
In a CloudFormation template, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to DynamoDB. For more information about resource-based policies, see [Using resource-based policies for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html) and [Resource-based policy examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-examples.html).
You can update the `ResourcePolicy` property if you've specified more than one table using the [AWS::DynamoDB::GlobalTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html) resource.
*Required*: No
*Type*: [ResourcePolicy](aws-properties-dynamodb-globaltable-resourcepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dynamodb-globaltable-replicastreamspecification-tags"></a>
Specifies the tags to apply to the DynamoDB stream for this global table replica. Stream tags are independent of table and replica tags.
For an overview on tagging DynamoDB resources, see [Tagging for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html) in the *Amazon DynamoDB Developer Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-dynamodb-globaltable-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
