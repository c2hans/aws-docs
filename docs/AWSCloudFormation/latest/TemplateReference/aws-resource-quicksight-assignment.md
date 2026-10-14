---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-assignment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Assignment
<a name="aws-resource-quicksight-assignment"></a>

Creates an assignment with one specified IAM policy, identified by its Amazon Resource Name (ARN). This policy assignment is attached to the specified groups or users of Amazon Quick Sight. Assignment names are unique per AWS account. To avoid overwriting rules in other namespaces, use assignment names that are unique.

## Syntax
<a name="aws-resource-quicksight-assignment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-assignment-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Assignment",
  "Properties" : {
      "[AssignmentName](#cfn-quicksight-assignment-assignmentname)" : {{String}},
      "[AssignmentStatus](#cfn-quicksight-assignment-assignmentstatus)" : {{String}},
      "[Identities](#cfn-quicksight-assignment-identities)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Namespace](#cfn-quicksight-assignment-namespace)" : {{String}},
      "[PolicyArn](#cfn-quicksight-assignment-policyarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-assignment-syntax.yaml"></a>

```
Type: AWS::QuickSight::Assignment
Properties:
  [AssignmentName](#cfn-quicksight-assignment-assignmentname): {{String}}
  [AssignmentStatus](#cfn-quicksight-assignment-assignmentstatus): {{String}}
  [Identities](#cfn-quicksight-assignment-identities): {{
    {{Key}}: {{Value}}}}
  [Namespace](#cfn-quicksight-assignment-namespace): {{String}}
  [PolicyArn](#cfn-quicksight-assignment-policyarn): {{String}}
```

## Properties
<a name="aws-resource-quicksight-assignment-properties"></a>

`AssignmentName`  <a name="cfn-quicksight-assignment-assignmentname"></a>
Assignment name.
*Required*: Yes
*Type*: String
*Pattern*: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AssignmentStatus`  <a name="cfn-quicksight-assignment-assignmentstatus"></a>
Assignment status.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DRAFT | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identities`  <a name="cfn-quicksight-assignment-identities"></a>
Identities.
*Required*: No
*Type*: Object of Array
*Pattern*: `[\u0020-\u00FF]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-quicksight-assignment-namespace"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]*$`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyArn`  <a name="cfn-quicksight-assignment-policyarn"></a>
The Amazon Resource Name (ARN) for the IAM policy.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-assignment-return-values"></a>

### Ref
<a name="aws-resource-quicksight-assignment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-assignment-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-assignment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`AssignmentId`  <a name="AssignmentId-fn::getatt"></a>
Assignment ID.
