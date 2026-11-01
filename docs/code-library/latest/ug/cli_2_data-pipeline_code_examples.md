---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_data-pipeline_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Data Pipeline examples using AWS CLI
<a name="cli_2_data-pipeline_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Data Pipeline.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `activate-pipeline`
<a name="data-pipeline_ActivatePipeline_cli_2_topic"></a>

The following code example shows how to use `activate-pipeline`.

**AWS CLI**
**To activate a pipeline**
The following `activate-pipeline` example activates the specified pipeline.

```
aws datapipeline activate-pipeline \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```
This command produces no output.
To activate the pipeline at a specific date and time, use the following command.

```
aws datapipeline activate-pipeline \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}} \
    --start-timestamp {{2015-04-07T00:00:00Z}}
```
For more information, see [Working with pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-managing-pipeline.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [ActivatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/activate-pipeline.html) in *AWS CLI Command Reference*.

### `add-tags`
<a name="data-pipeline_AddTags_cli_2_topic"></a>

The following code example shows how to use `add-tags`.

**AWS CLI**
**To add a tag to a pipeline**
The following `add-tags` example adds the specified tag to the specified pipeline.

```
aws datapipeline add-tags \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}} \
    --tags {{key=environment,value=production}} {{key=owner,value=sales}}
```
This command produces no output.
To view the tags, use the describe-pipelines command. For example, the tags added in the example command appear as follows in the output for describe-pipelines:

```
{
    ...
        "tags": [
            {
                "value": "production",
                "key": "environment"
            },
            {
                "value": "sales",
                "key": "owner"
            }
        ]
    ...
}
```
For more information, see [Tagging Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-adding-tags.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [AddTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/add-tags.html) in *AWS CLI Command Reference*.

### `create-pipeline`
<a name="data-pipeline_CreatePipeline_cli_2_topic"></a>

The following code example shows how to use `create-pipeline`.

**AWS CLI**
**To create a pipeline**
The following `create-pipeline` example creates a pipeline.

```
aws datapipeline create-pipeline \
    --name {{my-pipeline}} \
    --unique-id {{my-pipeline-token}}
```
Output:

```
{
    "pipelineId": "df-00627471SOVYZEXAMPLE"
}
```
For more information, see [Creating a pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-creating-pipelines.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [CreatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/create-pipeline.html) in *AWS CLI Command Reference*.

### `deactivate-pipeline`
<a name="data-pipeline_DeactivatePipeline_cli_2_topic"></a>

The following code example shows how to use `deactivate-pipeline`.

**AWS CLI**
**To deactivate a pipeline**
The following `deactivate-pipeline` example deactivates the specified pipeline.

```
aws datapipeline deactivate-pipeline \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```
This command produces no output.
To deactivate the pipeline only after all running activities finish, use the following command.

```
aws datapipeline deactivate-pipeline \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}} \
    --no-cancel-active
```
For more information, see [Deactivating Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-deactivate-pipeline.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [DeactivatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/deactivate-pipeline.html) in *AWS CLI Command Reference*.

### `delete-pipeline`
<a name="data-pipeline_DeletePipeline_cli_2_topic"></a>

The following code example shows how to use `delete-pipeline`.

**AWS CLI**
**To delete a pipeline**
The following `delete-pipeline` example deletes the specified pipeline.

```
aws datapipeline delete-pipeline \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```
This command produces no output.
For more information, see [Deleting Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-delete-console.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [DeletePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/delete-pipeline.html) in *AWS CLI Command Reference*.

### `describe-pipelines`
<a name="data-pipeline_DescribePipelines_cli_2_topic"></a>

The following code example shows how to use `describe-pipelines`.

**AWS CLI**
**To describe your pipelines**
The following `describe-pipelines` example describes the specified pipeline.

```
aws datapipeline describe-pipelines \
    --pipeline-ids {{df-00627471SOVYZEXAMPLE}}
```
Output:

```
{
    "pipelineDescriptionList": [
        {
            "fields": [
                {
                    "stringValue": "PENDING",
                    "key": "@pipelineState"
                },
                {
                    "stringValue": "my-pipeline",
                    "key": "name"
                },
                {
                    "stringValue": "2015-04-07T16:05:58",
                    "key": "@creationTime"
                },
                {
                    "stringValue": "df-00627471SOVYZEXAMPLE",
                    "key": "@id"
                },
                {
                    "stringValue": "123456789012",
                    "key": "pipelineCreator"
                },
                {
                    "stringValue": "PIPELINE",
                    "key": "@sphere"
                },
                {
                    "stringValue": "123456789012",
                    "key": "@userId"
                },
                {
                    "stringValue": "123456789012",
                    "key": "@accountId"
                },
                {
                    "stringValue": "my-pipeline-token",
                    "key": "uniqueId"
                }
            ],
            "pipelineId": "df-00627471SOVYZEXAMPLE",
            "name": "my-pipeline",
            "tags": []
        }
    ]
}
```
For more information, see [Working with pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-managing-pipeline.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [DescribePipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-pipelines.html) in *AWS CLI Command Reference*.

### `get-pipeline-definition`
<a name="data-pipeline_GetPipelineDefinition_cli_2_topic"></a>

The following code example shows how to use `get-pipeline-definition`.

**AWS CLI**
**To get a pipeline definition**
The following `get-pipeline-definition` example gets the pipeline definition for the specified pipeline.

```
aws datapipeline get-pipeline-definition \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```
Output:

```
{
    "parameters": [
        {
            "type": "AWS::S3::ObjectKey",
            "id": "myS3OutputLoc",
            "description": "S3 output folder"
        },
        {
            "default": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data",
            "type": "AWS::S3::ObjectKey",
            "id": "myS3InputLoc",
            "description": "S3 input folder"
        },
        {
            "default": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt",
            "type": "String",
            "id": "myShellCmd",
            "description": "Shell command to run"
        }
    ],
    "objects": [
        {
            "type": "Ec2Resource",
            "terminateAfter": "20 Minutes",
            "instanceType": "t1.micro",
            "id": "EC2ResourceObj",
            "name": "EC2ResourceObj"
        },
        {
            "name": "Default",
            "failureAndRerunMode": "CASCADE",
            "resourceRole": "DataPipelineDefaultResourceRole",
            "schedule": {
                "ref": "DefaultSchedule"
            },
            "role": "DataPipelineDefaultRole",
            "scheduleType": "cron",
            "id": "Default"
        },
        {
            "directoryPath": "#{myS3OutputLoc}/#{format(@scheduledStartTime, 'YYYY-MM-dd-HH-mm-ss')}",
            "type": "S3DataNode",
            "id": "S3OutputLocation",
            "name": "S3OutputLocation"
        },
        {
            "directoryPath": "#{myS3InputLoc}",
            "type": "S3DataNode",
            "id": "S3InputLocation",
            "name": "S3InputLocation"
        },
        {
            "startAt": "FIRST_ACTIVATION_DATE_TIME",
            "name": "Every 15 minutes",
            "period": "15 minutes",
            "occurrences": "4",
            "type": "Schedule",
            "id": "DefaultSchedule"
        },
        {
            "name": "ShellCommandActivityObj",
            "command": "#{myShellCmd}",
            "output": {
                "ref": "S3OutputLocation"
            },
            "input": {
                "ref": "S3InputLocation"
            },
            "stage": "true",
            "type": "ShellCommandActivity",
            "id": "ShellCommandActivityObj",
            "runsOn": {
                "ref": "EC2ResourceObj"
            }
        }
    ],
    "values": {
        "myS3OutputLoc": "s3://amzn-s3-demo-bucket/",
        "myS3InputLoc": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data",
        "myShellCmd": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt"
    }
}
```
For more information, see [Pipeline definition file syntax](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-writing-pipeline-definition.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [GetPipelineDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/get-pipeline-definition.html) in *AWS CLI Command Reference*.

### `list-pipelines`
<a name="data-pipeline_ListPipelines_cli_2_topic"></a>

The following code example shows how to use `list-pipelines`.

**AWS CLI**
**To list your pipelines**
The following `list-pipelines` example lists your pipelines.

```
aws datapipeline list-pipelines
```
Output:

```
{
    "pipelineIdList": [
        {
            "id": "df-00627471SOVYZEXAMPLE",
            "name": "my-pipeline"
        },
        {
            "id": "df-09028963KNVMREXAMPLE",
            "name": "ImportDDB"
        },
        {
            "id": "df-0870198233ZYVEXAMPLE",
            "name": "CrossRegionDDB"
        },
        {
            "id": "df-00189603TB4MZEXAMPLE",
            "name": "CopyRedshift"
        }
    ]
}
```
For more information, see [Viewing Your Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-list-pipelines.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [ListPipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-pipelines.html) in *AWS CLI Command Reference*.

### `list-runs`
<a name="data-pipeline_ListRuns_cli_2_topic"></a>

The following code example shows how to use `list-runs`.

**AWS CLI**
**Example 1: To list your pipeline runs**
The following `list-runs` example lists the runs for the specified pipeline.

```
aws datapipeline list-runs \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}}
```
Output:

```
    Name                       Scheduled Start        Status                     ID                                              Started                Ended
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1.  EC2ResourceObj             2015-04-12T17:33:02    CREATING                   @EC2ResourceObj_2015-04-12T17:33:02             2015-04-12T17:33:10
2.  S3InputLocation            2015-04-12T17:33:02    FINISHED                   @S3InputLocation_2015-04-12T17:33:02            2015-04-12T17:33:09    2015-04-12T17:33:09
3.  S3OutputLocation           2015-04-12T17:33:02    WAITING_ON_DEPENDENCIES    @S3OutputLocation_2015-04-12T17:33:02           2015-04-12T17:33:09
4.  ShellCommandActivityObj    2015-04-12T17:33:02    WAITING_FOR_RUNNER         @ShellCommandActivityObj_2015-04-12T17:33:02    2015-04-12T17:33:09
```
For more information, see [Interpreting Pipeline Status Details](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-status.html) in the *AWS Data Pipeline Developer Guide*.
**Example 2: To list the pipeline runs between the specified dates**
The following `list-runs` example uses the `--start-interval` to specify the dates to include in the output.

```
aws datapipeline list-runs \
    --pipeline-id {{df-01434553B58A2SHZUKO5}} \
    --start-interval {{2017-10-07T00:00:00,2017-10-08T00:00:00}}
```
Output:

```
        Name                                                Scheduled Start      Status
        ID                                                  Started              Ended
----------------------------------------------------------------------------------------------------
    1.  EC2ResourceObj                                      2017-10-07T09:00:00  FINISHED
        @EC2ResourceObj_2017-10-07T09:00:00                 2017-10-07T09:00:05  2017-10-07T09:12:45

    2.  S3InputLocation                                     2017-10-07T09:00:00  FINISHED
        @S3InputLocation_2017-10-07T09:00:00                2017-10-07T09:01:10  2017-10-07T09:01:10

    3.  S3OutputLocation                                    2017-10-07T09:00:00  FINISHED
        @S3OutputLocation_2017-10-07T09:00:00               2017-10-07T09:01:10  2017-10-07T09:10:52

    4.  ShellCommandActivityObj                             2017-10-07T09:00:00  FINISHED
        @ShellCommandActivityObj_2017-10-07T09:00:00        2017-10-07T09:01:10  2017-10-07T09:10:52
```
For more information, see [Viewing Pipeline Instance Details](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-details-console.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [ListRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-runs.html) in *AWS CLI Command Reference*.

### `put-pipeline-definition`
<a name="data-pipeline_PutPipelineDefinition_cli_2_topic"></a>

The following code example shows how to use `put-pipeline-definition`.

**AWS CLI**
**To upload a pipeline definition**
The following `put-pipeline-definition` example uploads the specified pipeline definition to the specified pipeline.

```
aws datapipeline put-pipeline-definition \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}} \
    --pipeline-definition {{file://my-pipeline-definition.json}}
```
Contents of `my-pipeline-definition.json`:

```
{
    "parameters": [
        {
            "type": "AWS::S3::ObjectKey",
            "id": "myS3OutputLoc",
            "description": "S3 output folder"
        },
        {
            "default": "s3://amzn-s3-demo-bucket/pig-apache-logs/data",
            "type": "AWS::S3::ObjectKey",
            "id": "myS3InputLoc",
            "description": "S3 input folder"
        },
        {
            "default": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt",
            "type": "String",
            "id": "myShellCmd",
            "description": "Shell command to run"
        }
    ],
    "objects": [
        {
            "type": "Ec2Resource",
            "terminateAfter": "20 Minutes",
            "instanceType": "t1.micro",
            "id": "EC2ResourceObj",
            "name": "EC2ResourceObj"
        },
        {
            "name": "Default",
            "failureAndRerunMode": "CASCADE",
            "resourceRole": "DataPipelineDefaultResourceRole",
            "schedule": {
                "ref": "DefaultSchedule"
            },
            "role": "DataPipelineDefaultRole",
            "scheduleType": "cron",
            "id": "Default"
        },
        {
            "directoryPath": "#{myS3OutputLoc}/#{format(@scheduledStartTime, 'YYYY-MM-dd-HH-mm-ss')}",
            "type": "S3DataNode",
            "id": "S3OutputLocation",
            "name": "S3OutputLocation"
        },
        {
            "directoryPath": "#{myS3InputLoc}",
            "type": "S3DataNode",
            "id": "S3InputLocation",
            "name": "S3InputLocation"
        },
        {
            "startAt": "FIRST_ACTIVATION_DATE_TIME",
            "name": "Every 15 minutes",
            "period": "15 minutes",
            "occurrences": "4",
            "type": "Schedule",
            "id": "DefaultSchedule"
        },
        {
            "name": "ShellCommandActivityObj",
            "command": "#{myShellCmd}",
            "output": {
                "ref": "S3OutputLocation"
            },
            "input": {
                "ref": "S3InputLocation"
            },
            "stage": "true",
            "type": "ShellCommandActivity",
            "id": "ShellCommandActivityObj",
            "runsOn": {
                "ref": "EC2ResourceObj"
            }
        }
    ],
    "values": {
        "myS3OutputLoc": "s3://amzn-s3-demo-bucket/",
        "myS3InputLoc": "s3://amzn-s3-demo-bucket/pig-apache-logs/data",
        "myShellCmd": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt"
    }
}
```
Output:

```
{
    "validationErrors": [],
    "errored": false,
    "validationWarnings": []
}
```
For more information, see [Pipeline definition file syntax](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-writing-pipeline-definition.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [PutPipelineDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/put-pipeline-definition.html) in *AWS CLI Command Reference*.

### `remove-tags`
<a name="data-pipeline_RemoveTags_cli_2_topic"></a>

The following code example shows how to use `remove-tags`.

**AWS CLI**
**To remove a tag from a pipeline**
The following `remove-tags` example removes the specified tag from the specified pipeline.

```
aws datapipeline remove-tags \
    --pipeline-id {{df-00627471SOVYZEXAMPLE}} \
    --tag-keys {{environment}}
```
This command produces no output.
For more information, see [Tagging Your Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-adding-tags.html) in the *AWS Data Pipeline Developer Guide*.
+  For API details, see [RemoveTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/remove-tags.html) in *AWS CLI Command Reference*.
