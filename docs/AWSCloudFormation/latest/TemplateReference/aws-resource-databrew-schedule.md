---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-databrew-schedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Schedule
<a name="aws-resource-databrew-schedule"></a>

Specifies a new schedule for one or more AWS Glue DataBrew jobs. Jobs can be run at a specific date and time, or at regular intervals.

## Syntax
<a name="aws-resource-databrew-schedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-databrew-schedule-syntax.json"></a>

```
{
  "Type" : "AWS::DataBrew::Schedule",
  "Properties" : {
      "[CronExpression](#cfn-databrew-schedule-cronexpression)" : {{String}},
      "[JobNames](#cfn-databrew-schedule-jobnames)" : {{[ String, ... ]}},
      "[Name](#cfn-databrew-schedule-name)" : {{String}},
      "[Tags](#cfn-databrew-schedule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-databrew-schedule-syntax.yaml"></a>

```
Type: AWS::DataBrew::Schedule
Properties:
  [CronExpression](#cfn-databrew-schedule-cronexpression): {{String}}
  [JobNames](#cfn-databrew-schedule-jobnames): {{
    - String}}
  [Name](#cfn-databrew-schedule-name): {{String}}
  [Tags](#cfn-databrew-schedule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-databrew-schedule-properties"></a>

`CronExpression`  <a name="cfn-databrew-schedule-cronexpression"></a>
The dates and times when the job is to run. For more information, see [Working with cron expressions for recipe jobs](https://docs.aws.amazon.com/databrew/latest/dg/jobs.recipe.html#jobs.cron) in the *AWS Glue DataBrew Developer Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobNames`  <a name="cfn-databrew-schedule-jobnames"></a>
A list of jobs to be run, according to the schedule.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-databrew-schedule-name"></a>
The name of the schedule.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-databrew-schedule-tags"></a>
Metadata tags that have been applied to the schedule.
*Required*: No
*Type*: Array of [Tag](aws-properties-databrew-schedule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-databrew-schedule-return-values"></a>

### Ref
<a name="aws-resource-databrew-schedule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "mySchedule" }`

For an AWS Glue DataBrew schedule named `mySchedule`, `Ref` returns the name of the schedule.

## Examples
<a name="aws-resource-databrew-schedule--examples"></a>

### Creating schedules
<a name="aws-resource-databrew-schedule--examples--Creating_schedules"></a>

The following examples create new DataBrew schedules.

#### YAML
<a name="aws-resource-databrew-schedule--examples--Creating_schedules--yaml"></a>

```
Resources:
  TestDataBrewSchedule:
    Type: AWS::DataBrew::Schedule
    Properties:
      JobNames: ["job-name"]
      Name: schedule-name
      CronExpression: "cron(0 0/1 ? * * *)"
      Tags: [{Key: key00AtCreate, Value: value001AtCreate}]
```

#### JSON
<a name="aws-resource-databrew-schedule--examples--Creating_schedules--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "This CloudFormation template specifies a DataBrew Schedule",
    "Resources": {
        "MyDataBrewSchedule": {
            "Type": "AWS::DataBrew::Schedule",
            "Properties": {
                "JobNames": ["job-test"],
                "Name": "cf-test-schedule1",
                "CronExpression": "cron(0 0/1 ? * * *)"
            },
            "Tags": [
                    {
                        "Key": "key00AtCreate",
                        "Value": "value001AtCreate"
                    }
                ]
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
