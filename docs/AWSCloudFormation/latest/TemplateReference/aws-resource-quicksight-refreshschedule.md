---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-refreshschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::RefreshSchedule
<a name="aws-resource-quicksight-refreshschedule"></a>

Creates a refresh schedule for a dataset in Quick.

## Syntax
<a name="aws-resource-quicksight-refreshschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-refreshschedule-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::RefreshSchedule",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-refreshschedule-awsaccountid)" : {{String}},
      "[DataSetId](#cfn-quicksight-refreshschedule-datasetid)" : {{String}},
      "[Schedule](#cfn-quicksight-refreshschedule-schedule)" : {{RefreshScheduleMap}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-refreshschedule-syntax.yaml"></a>

```
Type: AWS::QuickSight::RefreshSchedule
Properties:
  [AwsAccountId](#cfn-quicksight-refreshschedule-awsaccountid): {{String}}
  [DataSetId](#cfn-quicksight-refreshschedule-datasetid): {{String}}
  [Schedule](#cfn-quicksight-refreshschedule-schedule): {{
    RefreshScheduleMap}}
```

## Properties
<a name="aws-resource-quicksight-refreshschedule-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-refreshschedule-awsaccountid"></a>
The AWS account ID of the account that you are creating a schedule in.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSetId`  <a name="cfn-quicksight-refreshschedule-datasetid"></a>
The ID of the dataset that you are creating a refresh schedule for.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schedule`  <a name="cfn-quicksight-refreshschedule-schedule"></a>
The refresh schedule of a dataset.
*Required*: No
*Type*: [RefreshScheduleMap](aws-properties-quicksight-refreshschedule-refreshschedulemap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-refreshschedule-return-values"></a>

### Ref
<a name="aws-resource-quicksight-refreshschedule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-refreshschedule-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-refreshschedule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the refresh schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
