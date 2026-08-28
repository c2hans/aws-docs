---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-task.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task
<a name="aws-resource-datasync-task"></a>

The `AWS::DataSync::Task` resource specifies a task. A task is a set of two locations (source and destination) and a set of `Options` that you use to control the behavior of a task. If you don't specify `Options` when you create a task, AWS DataSync populates them with service defaults.

## Syntax
<a name="aws-resource-datasync-task-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-task-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::Task",
  "Properties" : {
      "[CloudWatchLogGroupArn](#cfn-datasync-task-cloudwatchloggrouparn)" : {{String}},
      "[DestinationLocationArn](#cfn-datasync-task-destinationlocationarn)" : {{String}},
      "[Excludes](#cfn-datasync-task-excludes)" : {{[ FilterRule, ... ]}},
      "[Includes](#cfn-datasync-task-includes)" : {{[ FilterRule, ... ]}},
      "[ManifestConfig](#cfn-datasync-task-manifestconfig)" : {{ManifestConfig}},
      "[Name](#cfn-datasync-task-name)" : {{String}},
      "[Options](#cfn-datasync-task-options)" : {{Options}},
      "[Schedule](#cfn-datasync-task-schedule)" : {{TaskSchedule}},
      "[SourceLocationArn](#cfn-datasync-task-sourcelocationarn)" : {{String}},
      "[Tags](#cfn-datasync-task-tags)" : {{[ Tag, ... ]}},
      "[TaskMode](#cfn-datasync-task-taskmode)" : {{String}},
      "[TaskReportConfig](#cfn-datasync-task-taskreportconfig)" : {{TaskReportConfig}}
    }
}
```

### YAML
<a name="aws-resource-datasync-task-syntax.yaml"></a>

```
Type: AWS::DataSync::Task
Properties:
  [CloudWatchLogGroupArn](#cfn-datasync-task-cloudwatchloggrouparn): {{String}}
  [DestinationLocationArn](#cfn-datasync-task-destinationlocationarn): {{String}}
  [Excludes](#cfn-datasync-task-excludes): {{
    - FilterRule}}
  [Includes](#cfn-datasync-task-includes): {{
    - FilterRule}}
  [ManifestConfig](#cfn-datasync-task-manifestconfig): {{
    ManifestConfig}}
  [Name](#cfn-datasync-task-name): {{String}}
  [Options](#cfn-datasync-task-options): {{
    Options}}
  [Schedule](#cfn-datasync-task-schedule): {{
    TaskSchedule}}
  [SourceLocationArn](#cfn-datasync-task-sourcelocationarn): {{String}}
  [Tags](#cfn-datasync-task-tags): {{
    - Tag}}
  [TaskMode](#cfn-datasync-task-taskmode): {{String}}
  [TaskReportConfig](#cfn-datasync-task-taskreportconfig): {{
    TaskReportConfig}}
```

## Properties
<a name="aws-resource-datasync-task-properties"></a>

`CloudWatchLogGroupArn`  <a name="cfn-datasync-task-cloudwatchloggrouparn"></a>
Specifies the Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task.
For Enhanced mode tasks, you don't need to specify anything. DataSync automatically sends logs to a CloudWatch log group named `/aws/datasync`.
For more information, see [Monitoring data transfers with CloudWatch Logs](https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):logs:[a-z\-0-9]*:[0-9]{12}:log-group:([^:\*]*)(:\*)?$`
*Maximum*: `562`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationLocationArn`  <a name="cfn-datasync-task-destinationlocationarn"></a>
The Amazon Resource Name (ARN) of an AWS storage resource's location.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Excludes`  <a name="cfn-datasync-task-excludes"></a>
Specifies exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).
*Required*: No
*Type*: Array of [FilterRule](aws-properties-datasync-task-filterrule.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Includes`  <a name="cfn-datasync-task-includes"></a>
Specifies include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see [Specifying what DataSync transfers by using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html).
*Required*: No
*Type*: Array of [FilterRule](aws-properties-datasync-task-filterrule.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestConfig`  <a name="cfn-datasync-task-manifestconfig"></a>
The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).
*Required*: No
*Type*: [ManifestConfig](aws-properties-datasync-task-manifestconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datasync-task-name"></a>
Specifies the name of your task.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:@/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-datasync-task-options"></a>
Specifies your task's settings, such as preserving file metadata, verifying data integrity, among other options.
*Required*: No
*Type*: [Options](aws-properties-datasync-task-options.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-datasync-task-schedule"></a>
Specifies a schedule for when you want your task to run. For more information, see [Scheduling your task](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html).
*Required*: No
*Type*: [TaskSchedule](aws-properties-datasync-task-taskschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLocationArn`  <a name="cfn-datasync-task-sourcelocationarn"></a>
Specifies the ARN of your transfer's source location.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-datasync-task-tags"></a>
Specifies the tags that you want to apply to your task.
*Tags* are key-value pairs that help you manage, filter, and search for your DataSync resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-task-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskMode`  <a name="cfn-datasync-task-taskmode"></a>
The task mode that you're using. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).
*Required*: No
*Type*: String
*Allowed values*: `BASIC | ENHANCED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TaskReportConfig`  <a name="cfn-datasync-task-taskreportconfig"></a>
The configuration of your task report, which provides detailed information about your DataSync transfer. For more information, see [Monitoring your DataSync transfers with task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).
*Required*: No
*Type*: [TaskReportConfig](aws-properties-datasync-task-taskreportconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-task-return-values"></a>

### Ref
<a name="aws-resource-datasync-task-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:task/task-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-task-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-task-return-values-fn--getatt-fn--getatt"></a>

`DestinationNetworkInterfaceArns`  <a name="DestinationNetworkInterfaceArns-fn::getatt"></a>
The ARNs of the destination elastic network interfaces (ENIs) that were created for your subnet.

`SourceNetworkInterfaceArns`  <a name="SourceNetworkInterfaceArns-fn::getatt"></a>
The ARNs of the source ENIs that were created for your subnet.

`Status`  <a name="Status-fn::getatt"></a>
The status of the task that was described.

`TaskArn`  <a name="TaskArn-fn::getatt"></a>
The ARN of the task.

## Examples
<a name="aws-resource-datasync-task--examples"></a>

**Topics**
+ [Creating an Enhanced mode task](#aws-resource-datasync-task--examples--Creating_an_Enhanced_mode_task)
+ [Creating a Basic mode task](#aws-resource-datasync-task--examples--Creating_a_Basic_mode_task)

### Creating an Enhanced mode task
<a name="aws-resource-datasync-task--examples--Creating_an_Enhanced_mode_task"></a>

The following examples create an Enhanced mode task. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).

#### JSON
<a name="aws-resource-datasync-task--examples--Creating_an_Enhanced_mode_task--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Creates a DataSync task that uses Enhanced mode",
    "Resources": {
        "Task": {
            "Type": "AWS::DataSync::Task",
            "Properties": {
                "SourceLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3",
                "DestinationLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2",
                "Name": "My-Enhanced-mode-task",
                "TaskMode": "ENHANCED",
                "Options": {
                    "TransferMode": "CHANGED",
                    "VerifyMode": "ONLY_FILES_TRANSFERRED",
                    "ObjectTags": "PRESERVE",
                    "LogLevel": "TRANSFER"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-task--examples--Creating_an_Enhanced_mode_task--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Creates a DataSync task that uses Enhanced mode
Resources:
  Task:
    Type: AWS::DataSync::Task
    Properties:
      SourceLocationArn: arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3
      DestinationLocationArn: arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2
      Name: My-Enhanced-mode-task
      TaskMode: ENHANCED
      Options:
        TransferMode: CHANGED
        VerifyMode: ONLY_FILES_TRANSFERRED
        ObjectTags: PRESERVE
        LogLevel: TRANSFER
```

### Creating a Basic mode task
<a name="aws-resource-datasync-task--examples--Creating_a_Basic_mode_task"></a>

The following examples create a Basic mode task. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).

#### JSON
<a name="aws-resource-datasync-task--examples--Creating_a_Basic_mode_task--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Creates a DataSync task that uses Basic mode",
    "Resources": {
        "Task": {
            "Type": "AWS::DataSync::Task",
            "Properties": {
                "SourceLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3",
                "DestinationLocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2",
                "Name": "My-Basic-mode-task",
                "TaskMode": "BASIC",
                "Options": {
                    "TransferMode": "CHANGED",
                    "VerifyMode": "POINT_IN_TIME_CONSISTENT",
                    "LogLevel": "TRANSFER"
                },
                "CloudWatchLogGroupArn": "arn:aws:logs:us-east-2:111222333444:log-group:/my-log-group-name:*"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-task--examples--Creating_a_Basic_mode_task--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Creates a DataSync task that uses Basic mode
Resources:
  Task:
    Type: AWS::DataSync::Task
    Properties:
      SourceLocationArn: arn:aws:datasync:us-east-2:111222333444:location/loc-1111aaaa2222bbbb3
      DestinationLocationArn: arn:aws:datasync:us-east-2:111222333444:location/loc-0000zzzz1111yyyy2
      Name: My-Basic-mode-task
      TaskMode: BASIC
      Options:
        TransferMode: CHANGED
        VerifyMode: POINT_IN_TIME_CONSISTENT
        LogLevel: TRANSFER
      CloudWatchLogGroupArn: arn:aws:logs:us-east-2:111222333444:log-group:/my-log-group-name:*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
