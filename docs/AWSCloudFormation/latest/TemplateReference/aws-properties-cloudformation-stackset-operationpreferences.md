---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stackset-operationpreferences.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet OperationPreferences
<a name="aws-properties-cloudformation-stackset-operationpreferences"></a>

The user-specified preferences for how CloudFormation performs a StackSet operation. For more information on maximum concurrent accounts and failure tolerance, see [StackSet operation options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-properties-cloudformation-stackset-operationpreferences-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stackset-operationpreferences-syntax.json"></a>

```
{
  "[ConcurrencyMode](#cfn-cloudformation-stackset-operationpreferences-concurrencymode)" : {{String}},
  "[FailureToleranceCount](#cfn-cloudformation-stackset-operationpreferences-failuretolerancecount)" : {{Integer}},
  "[FailureTolerancePercentage](#cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage)" : {{Integer}},
  "[MaxConcurrentCount](#cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount)" : {{Integer}},
  "[MaxConcurrentPercentage](#cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage)" : {{Integer}},
  "[RegionConcurrencyType](#cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype)" : {{String}},
  "[RegionOrder](#cfn-cloudformation-stackset-operationpreferences-regionorder)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-stackset-operationpreferences-syntax.yaml"></a>

```
  [ConcurrencyMode](#cfn-cloudformation-stackset-operationpreferences-concurrencymode): {{String}}
  [FailureToleranceCount](#cfn-cloudformation-stackset-operationpreferences-failuretolerancecount): {{Integer}}
  [FailureTolerancePercentage](#cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage): {{Integer}}
  [MaxConcurrentCount](#cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount): {{Integer}}
  [MaxConcurrentPercentage](#cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage): {{Integer}}
  [RegionConcurrencyType](#cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype): {{String}}
  [RegionOrder](#cfn-cloudformation-stackset-operationpreferences-regionorder): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-stackset-operationpreferences-properties"></a>

`ConcurrencyMode`  <a name="cfn-cloudformation-stackset-operationpreferences-concurrencymode"></a>
Specifies how the concurrency level behaves during the operation execution.
+ `STRICT_FAILURE_TOLERANCE`: This option dynamically lowers the concurrency level to ensure the number of failed accounts never exceeds the value of `FailureToleranceCount` \+1. The initial actual concurrency is set to the lower of either the value of the `MaxConcurrentCount`, or the value of `FailureToleranceCount` \+1. The actual concurrency is then reduced proportionally by the number of failures. This is the default behavior.

  If failure tolerance or Maximum concurrent accounts are set to percentages, the behavior is similar.
+ `SOFT_FAILURE_TOLERANCE`: This option decouples `FailureToleranceCount` from the actual concurrency. This allows StackSet operations to run at the concurrency level set by the `MaxConcurrentCount` value, or `MaxConcurrentPercentage`, regardless of the number of failures.
*Required*: No
*Type*: String
*Allowed values*: `STRICT_FAILURE_TOLERANCE | SOFT_FAILURE_TOLERANCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureToleranceCount`  <a name="cfn-cloudformation-stackset-operationpreferences-failuretolerancecount"></a>
The number of accounts per Region this operation can fail in before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.
Conditional: You must specify either `FailureToleranceCount` or `FailureTolerancePercentage` (but not both).
*Required*: Conditional
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureTolerancePercentage`  <a name="cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage"></a>
The percentage of accounts per Region this stack operation can fail in before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.
When calculating the number of accounts based on the specified percentage, CloudFormation rounds *down* to the next whole number.
Conditional: You must specify either `FailureToleranceCount` or `FailureTolerancePercentage`, but not both.
*Required*: Conditional
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxConcurrentCount`  <a name="cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount"></a>
The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `FailureToleranceCount`. `MaxConcurrentCount` is at most one more than the `FailureToleranceCount`.
Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
Conditional: You must specify either `MaxConcurrentCount` or `MaxConcurrentPercentage`, but not both.
*Required*: Conditional
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxConcurrentPercentage`  <a name="cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage"></a>
The maximum percentage of accounts in which to perform this operation at one time.
When calculating the number of accounts based on the specified percentage, CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
Conditional: You must specify either `MaxConcurrentCount` or `MaxConcurrentPercentage`, but not both.
*Required*: Conditional
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionConcurrencyType`  <a name="cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype"></a>
The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.
*Required*: No
*Type*: String
*Allowed values*: `SEQUENTIAL | PARALLEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionOrder`  <a name="cfn-cloudformation-stackset-operationpreferences-regionorder"></a>
The order of the Regions where you want to perform the stack operation.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
