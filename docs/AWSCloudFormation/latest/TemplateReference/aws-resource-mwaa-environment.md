---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mwaa-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAA::Environment
<a name="aws-resource-mwaa-environment"></a>

The `AWS::MWAA::Environment` resource creates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

## Syntax
<a name="aws-resource-mwaa-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mwaa-environment-syntax.json"></a>

```
{
  "Type" : "AWS::MWAA::Environment",
  "Properties" : {
      "[AirflowConfigurationOptions](#cfn-mwaa-environment-airflowconfigurationoptions)" : {{Json}},
      "[AirflowVersion](#cfn-mwaa-environment-airflowversion)" : {{String}},
      "[DagS3Path](#cfn-mwaa-environment-dags3path)" : {{String}},
      "[EndpointManagement](#cfn-mwaa-environment-endpointmanagement)" : {{String}},
      "[EnvironmentClass](#cfn-mwaa-environment-environmentclass)" : {{String}},
      "[ExecutionRoleArn](#cfn-mwaa-environment-executionrolearn)" : {{String}},
      "[KmsKey](#cfn-mwaa-environment-kmskey)" : {{String}},
      "[LoggingConfiguration](#cfn-mwaa-environment-loggingconfiguration)" : {{LoggingConfiguration}},
      "[MaxWebservers](#cfn-mwaa-environment-maxwebservers)" : {{Integer}},
      "[MaxWorkers](#cfn-mwaa-environment-maxworkers)" : {{Integer}},
      "[MinWebservers](#cfn-mwaa-environment-minwebservers)" : {{Integer}},
      "[MinWorkers](#cfn-mwaa-environment-minworkers)" : {{Integer}},
      "[Name](#cfn-mwaa-environment-name)" : {{String}},
      "[NetworkConfiguration](#cfn-mwaa-environment-networkconfiguration)" : {{NetworkConfiguration}},
      "[PluginsS3ObjectVersion](#cfn-mwaa-environment-pluginss3objectversion)" : {{String}},
      "[PluginsS3Path](#cfn-mwaa-environment-pluginss3path)" : {{String}},
      "[RequirementsS3ObjectVersion](#cfn-mwaa-environment-requirementss3objectversion)" : {{String}},
      "[RequirementsS3Path](#cfn-mwaa-environment-requirementss3path)" : {{String}},
      "[Schedulers](#cfn-mwaa-environment-schedulers)" : {{Integer}},
      "[SourceBucketArn](#cfn-mwaa-environment-sourcebucketarn)" : {{String}},
      "[StartupScriptS3ObjectVersion](#cfn-mwaa-environment-startupscripts3objectversion)" : {{String}},
      "[StartupScriptS3Path](#cfn-mwaa-environment-startupscripts3path)" : {{String}},
      "[Tags](#cfn-mwaa-environment-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}},
      "[WebserverAccessMode](#cfn-mwaa-environment-webserveraccessmode)" : {{String}},
      "[WeeklyMaintenanceWindowStart](#cfn-mwaa-environment-weeklymaintenancewindowstart)" : {{String}},
      "[WorkerReplacementStrategy](#cfn-mwaa-environment-workerreplacementstrategy)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mwaa-environment-syntax.yaml"></a>

```
Type: AWS::MWAA::Environment
Properties:
  [AirflowConfigurationOptions](#cfn-mwaa-environment-airflowconfigurationoptions): {{Json}}
  [AirflowVersion](#cfn-mwaa-environment-airflowversion): {{String}}
  [DagS3Path](#cfn-mwaa-environment-dags3path): {{String}}
  [EndpointManagement](#cfn-mwaa-environment-endpointmanagement): {{String}}
  [EnvironmentClass](#cfn-mwaa-environment-environmentclass): {{String}}
  [ExecutionRoleArn](#cfn-mwaa-environment-executionrolearn): {{String}}
  [KmsKey](#cfn-mwaa-environment-kmskey): {{String}}
  [LoggingConfiguration](#cfn-mwaa-environment-loggingconfiguration): {{
    LoggingConfiguration}}
  [MaxWebservers](#cfn-mwaa-environment-maxwebservers): {{Integer}}
  [MaxWorkers](#cfn-mwaa-environment-maxworkers): {{Integer}}
  [MinWebservers](#cfn-mwaa-environment-minwebservers): {{Integer}}
  [MinWorkers](#cfn-mwaa-environment-minworkers): {{Integer}}
  [Name](#cfn-mwaa-environment-name): {{String}}
  [NetworkConfiguration](#cfn-mwaa-environment-networkconfiguration): {{
    NetworkConfiguration}}
  [PluginsS3ObjectVersion](#cfn-mwaa-environment-pluginss3objectversion): {{String}}
  [PluginsS3Path](#cfn-mwaa-environment-pluginss3path): {{String}}
  [RequirementsS3ObjectVersion](#cfn-mwaa-environment-requirementss3objectversion): {{String}}
  [RequirementsS3Path](#cfn-mwaa-environment-requirementss3path): {{String}}
  [Schedulers](#cfn-mwaa-environment-schedulers): {{Integer}}
  [SourceBucketArn](#cfn-mwaa-environment-sourcebucketarn): {{String}}
  [StartupScriptS3ObjectVersion](#cfn-mwaa-environment-startupscripts3objectversion): {{String}}
  [StartupScriptS3Path](#cfn-mwaa-environment-startupscripts3path): {{String}}
  [Tags](#cfn-mwaa-environment-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
  [WebserverAccessMode](#cfn-mwaa-environment-webserveraccessmode): {{String}}
  [WeeklyMaintenanceWindowStart](#cfn-mwaa-environment-weeklymaintenancewindowstart): {{String}}
  [WorkerReplacementStrategy](#cfn-mwaa-environment-workerreplacementstrategy): {{String}}
```

## Properties
<a name="aws-resource-mwaa-environment-properties"></a>

`AirflowConfigurationOptions`  <a name="cfn-mwaa-environment-airflowconfigurationoptions"></a>
A list of key-value pairs containing the Airflow configuration options for your environment. For example, `core.default_timezone: utc`. To learn more, see [Apache Airflow configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html).
*Required*: No
*Type*: Json
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`AirflowVersion`  <a name="cfn-mwaa-environment-airflowversion"></a>
The version of Apache Airflow to use for the environment. If no value is specified, defaults to the latest version.
If you specify a newer version number for an existing environment, the version update requires some service interruption before taking effect.
*Allowed Values*: `2.7.2` \| `2.8.1` \| `2.9.2` \| `2.10.1` \| `2.10.3` \| `3.0.6` \| `3.2.1` (latest)
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z.]+$`
*Maximum*: `32`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DagS3Path`  <a name="cfn-mwaa-environment-dags3path"></a>
The relative path to the DAGs folder on your Amazon S3 bucket. For example, `dags`. To learn more, see [Adding or updating DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EndpointManagement`  <a name="cfn-mwaa-environment-endpointmanagement"></a>
Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA. If set to `SERVICE`, Amazon MWAA will create and manage the required VPC endpoints in your VPC. If set to `CUSTOMER`, you must create, and manage, the VPC endpoints in your VPC.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOMER | SERVICE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentClass`  <a name="cfn-mwaa-environment-environmentclass"></a>
The environment class type. Valid values: `mw1.micro`, `mw1.small`, `mw1.medium`, `mw1.large`, `mw1.1large`, and `mw1.2large`. To learn more, see [Amazon MWAA environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ExecutionRoleArn`  <a name="cfn-mwaa-environment-executionrolearn"></a>
The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, `arn:aws:iam::123456789:role/my-execution-role`. To learn more, see [Amazon MWAA Execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b)(-[a-z]+)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Maximum*: `1224`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`KmsKey`  <a name="cfn-mwaa-environment-kmskey"></a>
The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment. You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).
*Required*: No
*Type*: String
*Pattern*: `^(((arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b)(-[a-z]+)?:kms:[a-z]{2}-[a-z]+-\d:\d+:)?key\/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}|(arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):kms:[a-z]{2}-[a-z]+-\d:\d+:)?alias/.+)$`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfiguration`  <a name="cfn-mwaa-environment-loggingconfiguration"></a>
The Apache Airflow logs being sent to CloudWatch Logs: `DagProcessingLogs`, `SchedulerLogs`, `TaskLogs`, `WebserverLogs`, `WorkerLogs`.
*Required*: No
*Type*: [LoggingConfiguration](aws-properties-mwaa-environment-loggingconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`MaxWebservers`  <a name="cfn-mwaa-environment-maxwebservers"></a>
The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in `MaxWebservers`. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinWebservers`.
Valid values: For environments larger than mw1.micro, accepts values from `2` to `5`. Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`MaxWorkers`  <a name="cfn-mwaa-environment-maxworkers"></a>
The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the `MaxWorkers` field. For example, `20`. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in `MinWorkers`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`MinWebservers`  <a name="cfn-mwaa-environment-minwebservers"></a>
The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinWebservers`.
Valid values: For environments larger than mw1.micro, accepts values from `2` to `5`. Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`MinWorkers`  <a name="cfn-mwaa-environment-minworkers"></a>
The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the `MaxWorkers` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the `MinWorkers` field. For example, `2`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Name`  <a name="cfn-mwaa-environment-name"></a>
The name of your Amazon MWAA environment.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][0-9a-zA-Z\-_]*$`
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfiguration`  <a name="cfn-mwaa-environment-networkconfiguration"></a>
The VPC networking components used to secure and enable network traffic between the AWS resources for your environment. To learn more, see [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html).
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-mwaa-environment-networkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PluginsS3ObjectVersion`  <a name="cfn-mwaa-environment-pluginss3objectversion"></a>
The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html).
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PluginsS3Path`  <a name="cfn-mwaa-environment-pluginss3path"></a>
The relative path to the `plugins.zip` file on your Amazon S3 bucket. For example, `plugins.zip`. To learn more, see [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`RequirementsS3ObjectVersion`  <a name="cfn-mwaa-environment-requirementss3objectversion"></a>
The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html).
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`RequirementsS3Path`  <a name="cfn-mwaa-environment-requirementss3path"></a>
The relative path to the `requirements.txt` file on your Amazon S3 bucket. For example, `requirements.txt`. To learn more, see [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Schedulers`  <a name="cfn-mwaa-environment-schedulers"></a>
The number of schedulers that you want to run in your environment. Valid values:
+ **v2** - For environments larger than mw1.micro, accepts values from 2 to 5. Defaults to 2 for all environment sizes except mw1.micro, which defaults to 1.
+ **v1** - Accepts 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SourceBucketArn`  <a name="cfn-mwaa-environment-sourcebucketarn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, `arn:aws:s3:::my-airflow-bucket-unique-name`. To learn more, see [Create an Amazon S3 bucket for Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b)(-[a-z]+)?:s3:::[a-z0-9.\-]+$`
*Minimum*: `1`
*Maximum*: `1224`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`StartupScriptS3ObjectVersion`  <a name="cfn-mwaa-environment-startupscripts3objectversion"></a>
The version of the startup shell script in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file every time you update the script.
 Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:
 `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`
 For more information, see [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html).
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`StartupScriptS3Path`  <a name="cfn-mwaa-environment-startupscripts3path"></a>
The relative path to the startup shell script in your Amazon S3 bucket. For example, `s3://mwaa-environment/startup.sh`.
 Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, see [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `1024`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-mwaa-environment-tags"></a>
The key-value tag pairs associated to your environment. For example, `"Environment": "Staging"`. To learn more, see [Tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
If you specify new tags for an existing environment, the update requires service interruption before taking effect.
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`WebserverAccessMode`  <a name="cfn-mwaa-environment-webserveraccessmode"></a>
The Apache Airflow *Web server* access mode. To learn more, see [Apache Airflow access modes](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html). Valid values: `PRIVATE_ONLY`, `PUBLIC_ONLY`, or `PUBLIC_AND_PRIVATE`.
*Required*: No
*Type*: String
*Allowed values*: `PRIVATE_ONLY | PUBLIC_ONLY | PUBLIC_AND_PRIVATE`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`WeeklyMaintenanceWindowStart`  <a name="cfn-mwaa-environment-weeklymaintenancewindowstart"></a>
The day and time of the week to start weekly maintenance updates of your environment in the following format: `DAY:HH:MM`. For example: `TUE:03:30`. You can specify a start time in 30 minute increments only. Supported input includes the following:
+ MON\|TUE\|WED\|THU\|FRI\|SAT\|SUN:([01]\\\\d\|2[0-3]):(00\|30)
*Required*: No
*Type*: String
*Pattern*: `(MON|TUE|WED|THU|FRI|SAT|SUN):([01]\d|2[0-3]):(00|30)`
*Maximum*: `9`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`WorkerReplacementStrategy`  <a name="cfn-mwaa-environment-workerreplacementstrategy"></a>
The worker replacement strategy for your Amazon MWAA environment.
*Required*: No
*Type*: String
*Allowed values*: `FORCED | GRACEFUL`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-mwaa-environment-return-values"></a>

### Ref
<a name="aws-resource-mwaa-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the environment details.

### Fn::GetAtt
<a name="aws-resource-mwaa-environment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mwaa-environment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN for the Amazon MWAA environment.

`CeleryExecutorQueue`  <a name="CeleryExecutorQueue-fn::getatt"></a>
The queue ARN for the environment's [Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html). Amazon MWAA uses a Celery Executor to distribute tasks across multiple workers. When you create an environment in a shared VPC, you must provide access to the Celery Executor queue from your VPC.

`DatabaseVpcEndpointService`  <a name="DatabaseVpcEndpointService-fn::getatt"></a>
The VPC endpoint for the environment's Amazon RDS database.

`LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn`  <a name="LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn-fn::getatt"></a>
The ARN for the CloudWatch Logs group where the Apache Airflow DAG processing logs are published.

`LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn`  <a name="LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn-fn::getatt"></a>
The ARN for the CloudWatch Logs group where the Apache Airflow Scheduler logs are published.

`LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn`  <a name="LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn-fn::getatt"></a>
The ARN for the CloudWatch Logs group where the Apache Airflow task logs are published.

`LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn`  <a name="LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn-fn::getatt"></a>
The ARN for the CloudWatch Logs group where the Apache Airflow Web server logs are published.

`LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn`  <a name="LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn-fn::getatt"></a>
The ARN for the CloudWatch Logs group where the Apache Airflow Worker logs are published.

`WebserverUrl`  <a name="WebserverUrl-fn::getatt"></a>
The URL of your Apache Airflow UI.

`WebserverVpcEndpointService`  <a name="WebserverVpcEndpointService-fn::getatt"></a>
The VPC endpoint for the environment's web server.

## Examples
<a name="aws-resource-mwaa-environment--examples"></a>

**Topics**
+ [Create a MWAA environment - JSON](#aws-resource-mwaa-environment--examples--Create_a_MWAA_environment_-_JSON)
+ [Create a MWAA environment - YAML](#aws-resource-mwaa-environment--examples--Create_a_MWAA_environment_-_YAML)

### Create a MWAA environment - JSON
<a name="aws-resource-mwaa-environment--examples--Create_a_MWAA_environment_-_JSON"></a>

The following example shows how to create a MWAA environment:

#### JSON
<a name="aws-resource-mwaa-environment--examples--Create_a_MWAA_environment_-_JSON--json"></a>

```
{
    "Environment": {
        "Type": "AWS::MWAA::Environment",
        "Properties": {
            "Name": "my-airflow-environment",
            "AirflowConfigurationOptions": {
                "logging.logging_level": "INFO",
                "core.default_timezone": "utc"
            },
            "Tags": {
                "Environment": "Staging",
                "Team": "Analytics"
            },
            "NetworkConfiguration": {
                "SubnetIds": [
                    "subnet-123456",
                    "subnet-789011"
                ],
                "SecurityGroupIds": [
                    "sg-0101010"
                ]
            },
            "LoggingConfiguration": {
                "DagProcessingLogs": {
                    "Enabled": true,
                    "LogLevel": "INFO"
                },
                "SchedulerLogs": {
                    "Enabled": false,
                    "LogLevel": "INFO"
                },
                "TaskLogs": {
                    "Enabled": true,
                    "LogLevel": "INFO"
                },
                "WebserverLogs": {
                    "Enabled": false,
                    "LogLevel": "INFO"
                },
                "WorkerLogs": {
                    "Enabled": false,
                    "LogLevel": "INFO"
                }
            },
            "SourceBucketArn": "arn:aws:s3:::my-dags-bucket",
            "ExecutionRoleArn": "arn:aws:iam::012345678900:role/service-role/my-execution-role",
            "MaxWorkers": 1,
            "DagS3Path": "dags",
            "EnvironmentClass": "mw1.small"
        }
    }
}
```

### Create a MWAA environment - YAML
<a name="aws-resource-mwaa-environment--examples--Create_a_MWAA_environment_-_YAML"></a>

The following example shows how to create a MWAA environment:

#### YAML
<a name="aws-resource-mwaa-environment--examples--Create_a_MWAA_environment_-_YAML--yaml"></a>

```
Environment:
    Properties:
      AirflowConfigurationOptions:
        core.default_timezone: utc
        logging.logging_level: INFO
      DagS3Path: dags
      EnvironmentClass: mw1.small
      ExecutionRoleArn: "arn:aws:iam::012345678900:role/service-role/my-execution-role"
      LoggingConfiguration:
        DagProcessingLogs:
          Enabled: true
          LogLevel: INFO
        SchedulerLogs:
          Enabled: false
          LogLevel: INFO
        TaskLogs:
          Enabled: true
          LogLevel: INFO
        WebserverLogs:
          Enabled: false
          LogLevel: INFO
        WorkerLogs:
          Enabled: false
          LogLevel: INFO
      MaxWorkers: 1
      Name: my-airflow-environment
      NetworkConfiguration:
        SecurityGroupIds:
          - sg-0101010
        SubnetIds:
          - subnet-123456
          - subnet-789011
      SourceBucketArn: "arn:aws:s3:::my-dags-bucket"
      Tags:
        Environment: Staging
        Team: Analytics
    Type: "AWS::MWAA::Environment"
```
