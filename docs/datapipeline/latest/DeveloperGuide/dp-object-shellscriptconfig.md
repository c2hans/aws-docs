---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-shellscriptconfig.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# ShellScriptConfig
<a name="dp-object-shellscriptconfig"></a>

Use with an Activity to run a shell script for preActivityTaskConfig and postActivityTaskConfig. This object is available for [HadoopActivity](dp-object-hadoopactivity.md), [HiveActivity](dp-object-hiveactivity.md), [HiveCopyActivity](dp-object-hivecopyactivity.md), and [PigActivity](dp-object-pigactivity.md). You specify an S3 URI and a list of arguments for the script.

## Example
<a name="shellscriptconfig-example"></a>

A ShellScriptConfig with arguments:

```
{
   "id" : "ShellScriptConfig_1”,
   "name" : “prescript”,
   "type" : "ShellScriptConfig",
   "scriptUri": “s3://my-bucket/shell-cleanup.sh”,
   "scriptArgument" : ["arg1","arg2"]
 }
```

## Syntax
<a name="shellscriptconfig-syntax"></a>

This object includes the following fields.

| Optional Fields | Description | Slot Type |
| --- | --- | --- |
| parent | Parent of the current object from which slots are inherited. | Reference Object, for example, "parent":{"ref":"myBaseObjectId"} |
| scriptArgument | A list of arguments to use with the shell script. | String |
| scriptUri | The script URI in Amazon S3 that should be downloaded and run. | String |

| Runtime Fields | Description | Slot Type |
| --- | --- | --- |
| @version | Pipeline version that the object was created with. | String |

| System Fields | Description | Slot Type |
| --- | --- | --- |
| @error | Error describing the ill-formed object. | String |
| @pipelineId | ID of the pipeline to which this object belongs. | String |
| @sphere | The sphere of an object denotes its place in the lifecycle: Component Objects give rise to Instance Objects, which execute Attempt Objects. | String |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
