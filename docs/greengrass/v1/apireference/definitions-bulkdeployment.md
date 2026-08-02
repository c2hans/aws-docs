---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-bulkdeployment.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# BulkDeployment
<a name="definitions-bulkdeployment"></a>

```
{
"BulkDeploymentId": "string",
"BulkDeploymentArn": "string",
"CreatedAt": "string"
}
```

BulkDeployment
Information about a bulk deployment. You cannot start a new bulk deployment while another one is still running or in a non-terminal state.
type: object

BulkDeploymentId
The ID of the bulk deployment.
type: string

BulkDeploymentArn
The ARN of the bulk deployment.
type: string

CreatedAt
The time, in ISO format, when the deployment was created.
type: string
