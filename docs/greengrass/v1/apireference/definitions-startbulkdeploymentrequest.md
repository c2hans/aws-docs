---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-startbulkdeploymentrequest.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# StartBulkDeploymentRequest
<a name="definitions-startbulkdeploymentrequest"></a>

```
{
"InputFileUri": "string",
"ExecutionRoleArn": "string",
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
}
}
```

StartBulkDeploymentRequest
Information about a bulk deployment. You cannot start a new bulk deployment while another one is still running or in a non-terminal state.
type: object
required: ["InputFileUri", "ExecutionRoleArn"]

InputFileUri
The URI of the input file in the S3 bucket. The execution role must have `getObject` permissions on this bucket to access the input file. The input file is a JSON-serialized, line-delimited file with UTF-8 encoding that provides a list of group and version IDs and the deployment type. This file must be less than 100 MB. Currently, AWS IoT Greengrass supports only `NewDeployment` deployment types.

```
{"GroupId":"{{groupId1}}", "GroupVersionId":"{{groupVersionId1}}", "DeploymentType":"NewDeployment"}
{"GroupId":"{{groupId2}}", "GroupVersionId":"{{groupVersionId2}}", "DeploymentType":"NewDeployment"}
{"GroupId":"{{groupId3}}", "GroupVersionId":"{{groupVersionId3}}", "DeploymentType":"NewDeployment"}
...
```
For more information, including the input file format, see [Create Bulk Deployments For Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html).
type: string

ExecutionRoleArn
The ARN of the execution role to associate with the bulk deployment operation. This IAM role must allow the `greengrass:CreateDeployment` action for all group versions that are listed in the input file. This IAM role must have access to the S3 bucket that contains the input file.
type: string

tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
