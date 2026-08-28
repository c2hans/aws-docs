---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-job.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Job
<a name="aws-resource-glue-job"></a>

The `AWS::Glue::Job` resource specifies an AWS Glue job in the data catalog. For more information, see [Adding Jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) and [Job Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job) in the *AWS Glue Developer Guide.*

## Syntax
<a name="aws-resource-glue-job-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-job-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::Job",
  "Properties" : {
      "[AllocatedCapacity](#cfn-glue-job-allocatedcapacity)" : {{Number}},
      "[Command](#cfn-glue-job-command)" : {{JobCommand}},
      "[Connections](#cfn-glue-job-connections)" : {{ConnectionsList}},
      "[DefaultArguments](#cfn-glue-job-defaultarguments)" : {{Json}},
      "[Description](#cfn-glue-job-description)" : {{String}},
      "[ExecutionClass](#cfn-glue-job-executionclass)" : {{String}},
      "[ExecutionProperty](#cfn-glue-job-executionproperty)" : {{ExecutionProperty}},
      "[GlueVersion](#cfn-glue-job-glueversion)" : {{String}},
      "[JobMode](#cfn-glue-job-jobmode)" : {{String}},
      "[JobRunQueuingEnabled](#cfn-glue-job-jobrunqueuingenabled)" : {{Boolean}},
      "[LogUri](#cfn-glue-job-loguri)" : {{String}},
      "[MaintenanceWindow](#cfn-glue-job-maintenancewindow)" : {{String}},
      "[MaxCapacity](#cfn-glue-job-maxcapacity)" : {{Number}},
      "[MaxRetries](#cfn-glue-job-maxretries)" : {{Number}},
      "[Name](#cfn-glue-job-name)" : {{String}},
      "[NonOverridableArguments](#cfn-glue-job-nonoverridablearguments)" : {{Json}},
      "[NotificationProperty](#cfn-glue-job-notificationproperty)" : {{NotificationProperty}},
      "[NumberOfWorkers](#cfn-glue-job-numberofworkers)" : {{Integer}},
      "[Role](#cfn-glue-job-role)" : {{String}},
      "[SecurityConfiguration](#cfn-glue-job-securityconfiguration)" : {{String}},
      "[Tags](#cfn-glue-job-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}},
      "[Timeout](#cfn-glue-job-timeout)" : {{Integer}},
      "[WorkerType](#cfn-glue-job-workertype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-glue-job-syntax.yaml"></a>

```
Type: AWS::Glue::Job
Properties:
  [AllocatedCapacity](#cfn-glue-job-allocatedcapacity): {{Number}}
  [Command](#cfn-glue-job-command): {{
    JobCommand}}
  [Connections](#cfn-glue-job-connections): {{
    ConnectionsList}}
  [DefaultArguments](#cfn-glue-job-defaultarguments): {{Json}}
  [Description](#cfn-glue-job-description): {{String}}
  [ExecutionClass](#cfn-glue-job-executionclass): {{String}}
  [ExecutionProperty](#cfn-glue-job-executionproperty): {{
    ExecutionProperty}}
  [GlueVersion](#cfn-glue-job-glueversion): {{String}}
  [JobMode](#cfn-glue-job-jobmode): {{String}}
  [JobRunQueuingEnabled](#cfn-glue-job-jobrunqueuingenabled): {{Boolean}}
  [LogUri](#cfn-glue-job-loguri): {{String}}
  [MaintenanceWindow](#cfn-glue-job-maintenancewindow): {{String}}
  [MaxCapacity](#cfn-glue-job-maxcapacity): {{Number}}
  [MaxRetries](#cfn-glue-job-maxretries): {{Number}}
  [Name](#cfn-glue-job-name): {{String}}
  [NonOverridableArguments](#cfn-glue-job-nonoverridablearguments): {{Json}}
  [NotificationProperty](#cfn-glue-job-notificationproperty): {{
    NotificationProperty}}
  [NumberOfWorkers](#cfn-glue-job-numberofworkers): {{Integer}}
  [Role](#cfn-glue-job-role): {{String}}
  [SecurityConfiguration](#cfn-glue-job-securityconfiguration): {{String}}
  [Tags](#cfn-glue-job-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
  [Timeout](#cfn-glue-job-timeout): {{Integer}}
  [WorkerType](#cfn-glue-job-workertype): {{String}}
```

## Properties
<a name="aws-resource-glue-job-properties"></a>

`AllocatedCapacity`  <a name="cfn-glue-job-allocatedcapacity"></a>
This parameter is no longer supported. Use `MaxCapacity` instead.
The number of capacity units that are allocated to this job.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Command`  <a name="cfn-glue-job-command"></a>
The code that executes a job.
*Required*: Yes
*Type*: [JobCommand](aws-properties-glue-job-jobcommand.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Connections`  <a name="cfn-glue-job-connections"></a>
The connections used for this job.
*Required*: No
*Type*: [ConnectionsList](aws-properties-glue-job-connectionslist.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultArguments`  <a name="cfn-glue-job-defaultarguments"></a>
The default arguments for this job, specified as name-value pairs.
You can specify arguments here that your own job-execution script consumes, in addition to arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see [Calling AWS Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) in the *AWS Glue Developer Guide*.
For information about the key-value pairs that AWS Glue consumes to set up your job, see [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) in the *AWS Glue Developer Guide*.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-glue-job-description"></a>
A description of the job.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionClass`  <a name="cfn-glue-job-executionclass"></a>
Indicates whether the job is run with a standard or flexible execution class. The standard execution class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.
The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.
Only jobs with AWS Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX`. The flexible execution class is available for Spark jobs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionProperty`  <a name="cfn-glue-job-executionproperty"></a>
The maximum number of concurrent runs that are allowed for this job.
*Required*: No
*Type*: [ExecutionProperty](aws-properties-glue-job-executionproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlueVersion`  <a name="cfn-glue-job-glueversion"></a>
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Jobs that are created without specifying a Glue version default to the latest Glue version available.
*Required*: No
*Type*: String
*Pattern*: `^(\w+\.)+\w+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobMode`  <a name="cfn-glue-job-jobmode"></a>
A mode that describes how a job was created. Valid values are:
+ `SCRIPT` - The job was created using the AWS Glue Studio script editor.
+ `VISUAL` - The job was created using the AWS Glue Studio visual editor.
+ `NOTEBOOK` - The job was created using an interactive sessions notebook.
When the `JobMode` field is missing or null, `SCRIPT` is assigned as the default value.
*Required*: No
*Type*: String
*Allowed values*: `SCRIPT | VISUAL | NOTEBOOK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobRunQueuingEnabled`  <a name="cfn-glue-job-jobrunqueuingenabled"></a>
Specifies whether job run queuing is enabled for the job runs for this job.
A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be considered for queueing.
If this field does not match the value set in the job run, then the value from the job run field will be used.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogUri`  <a name="cfn-glue-job-loguri"></a>
This field is reserved for future use.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceWindow`  <a name="cfn-glue-job-maintenancewindow"></a>
This field specifies a day of the week and hour for a maintenance window for streaming jobs. AWS Glue periodically performs maintenance activities. During these maintenance windows, AWS Glue will need to restart your streaming jobs.
AWS Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.
*Required*: No
*Type*: String
*Pattern*: `^(Sun|Mon|Tue|Wed|Thu|Fri|Sat):([01]?[0-9]|2[0-3])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCapacity`  <a name="cfn-glue-job-maxcapacity"></a>
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.
Do not set `Max Capacity` if using `WorkerType` and `NumberOfWorkers`.
The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job or an Apache Spark ETL job:
+ When you specify a Python shell job (`JobCommand.Name`="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
+ When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxRetries`  <a name="cfn-glue-job-maxretries"></a>
The maximum number of times to retry this job after a JobRun fails.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-job-name"></a>
The name you assign to this job definition.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NonOverridableArguments`  <a name="cfn-glue-job-nonoverridablearguments"></a>
Non-overridable arguments for this job, specified as name-value pairs.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationProperty`  <a name="cfn-glue-job-notificationproperty"></a>
Specifies configuration properties of a notification.
*Required*: No
*Type*: [NotificationProperty](aws-properties-glue-job-notificationproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfWorkers`  <a name="cfn-glue-job-numberofworkers"></a>
The number of workers of a defined `workerType` that are allocated when a job runs.
The maximum number of workers you can define are 299 for `G.1X`, and 149 for `G.2X`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-glue-job-role"></a>
The name or Amazon Resource Name (ARN) of the IAM role associated with this job.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityConfiguration`  <a name="cfn-glue-job-securityconfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this job.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-glue-job-tags"></a>
The tags to use with this job.
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-glue-job-timeout"></a>
The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkerType`  <a name="cfn-glue-job-workertype"></a>
The type of predefined worker that is allocated when a job runs.
AWS Glue provides multiple worker types to accommodate different workload requirements:
G Worker Types (General-purpose compute workers):
+ G.1X: 1 DPU (4 vCPUs, 16 GB memory, 94GB disk)
+ G.2X: 2 DPU (8 vCPUs, 32 GB memory, 138GB disk)
+ G.4X: 4 DPU (16 vCPUs, 64 GB memory, 256GB disk)
+ G.8X: 8 DPU (32 vCPUs, 128 GB memory, 512GB disk)
+ G.12X: 12 DPU (48 vCPUs, 192 GB memory, 768GB disk)
+ G.16X: 16 DPU (64 vCPUs, 256 GB memory, 1024GB disk)
R Worker Types (Memory-optimized workers):
+ R.1X: 1 M-DPU (4 vCPUs, 32 GB memory)
+ R.2X: 2 M-DPU (8 vCPUs, 64 GB memory)
+ R.4X: 4 M-DPU (16 vCPUs, 128 GB memory)
+ R.8X: 8 M-DPU (32 vCPUs, 256 GB memory)
*Required*: No
*Type*: String
*Allowed values*: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X | G.12X | G.16X | R.1X | R.2X | R.4X | R.8X`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-job-return-values"></a>

### Ref
<a name="aws-resource-glue-job-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the job name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-glue-job--examples"></a>

###
<a name="aws-resource-glue-job--examples--"></a>

The following example creates a job with an associated role. The ScriptLocation is an Amazon S3 location. The example provided below is a placeholder for your Amazon S3 location.

#### JSON
<a name="aws-resource-glue-job--examples----json"></a>

```
{
  "Description": "AWS Glue Job Test",
  "Resources": {
    "MyJobRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "glue.amazonaws.com"
                ]
              },
              "Action": [
                "sts:AssumeRole"
              ]
            }
          ]
        },
        "Path": "/",
        "Policies": [
          {
            "PolicyName": "root",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": "*",
                  "Resource": "*"
                }
              ]
            }
          }
        ]
      }
    },
    "MyJob": {
      "Type": "AWS::Glue::Job",
      "Properties": {
        "Command": {
          "Name": "glueetl",
          "ScriptLocation": "s3://<your-S3-script-uri>"
        },
        "DefaultArguments": {
          "--job-bookmark-option": "job-bookmark-enable"
        },
        "ExecutionProperty": {
          "MaxConcurrentRuns": 2
        },
        "MaxRetries": 0,
        "Name": "cf-job1",
        "Role": {
          "Ref": "MyJobRole"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-glue-job--examples----yaml"></a>

```
---
Description: "AWS Glue Job Test"
Resources:
  MyJobRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "glue.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Path: "/"
      Policies:
        -
          PolicyName: "root"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              -
                Effect: "Allow"
                Action: "*"
                Resource: "*"

  MyJob:
    Type: AWS::Glue::Job
    Properties:
      Command:
        Name: glueetl
        ScriptLocation: "s3://<your-S3-script-uri>"
      DefaultArguments:
        "--job-bookmark-option": "job-bookmark-enable"
      ExecutionProperty:
        MaxConcurrentRuns: 2
      MaxRetries: 0
      Name: cf-job1
      Role: !Ref MyJobRole
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
