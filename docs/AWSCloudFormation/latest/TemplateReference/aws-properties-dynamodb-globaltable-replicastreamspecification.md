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
  "[ResourcePolicy](#cfn-dynamodb-globaltable-replicastreamspecification-resourcepolicy)" : {{ResourcePolicy}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-replicastreamspecification-syntax.yaml"></a>

```
  [ResourcePolicy](#cfn-dynamodb-globaltable-replicastreamspecification-resourcepolicy): {{
    ResourcePolicy}}
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
