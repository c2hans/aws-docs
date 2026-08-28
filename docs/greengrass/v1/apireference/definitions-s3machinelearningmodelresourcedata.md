---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-s3machinelearningmodelresourcedata.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# S3MachineLearningModelResourceData
<a name="definitions-s3machinelearningmodelresourcedata"></a>

```
{
"S3Uri": "string",
"DestinationPath": "string",
"OwnerSetting": {
  "GroupOwner": "string",
  "GroupPermission": "ro|rw"
}
}
```

S3MachineLearningModelResourceData
Attributes that define an Amazon S3 machine learning resource.
type: object

S3Uri
The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format.
type: string

DestinationPath
The absolute local path of the resource inside the Lambda environment.
type: string

OwnerSetting
The owner setting for the downloaded machine learning resource.
type: object
required: ["GroupOwner", "GroupPermission"]

GroupOwner
The group owner of the resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
type: string

GroupPermission
The permissions that the group owner has to the resource. Valid values are `rw` (read-write) or `ro` (read-only).
type: string
enum: ["ro", "rw"]

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
