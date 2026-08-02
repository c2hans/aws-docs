---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/stopbulkdeployment-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# StopBulkDeployment
<a name="stopbulkdeployment-put"></a>

Stops the execution of a bulk deployment. This action returns a status of `Stopping` until the deployment is stopped. You cannot start a new bulk deployment while a previous deployment is in the `Stopping` state. This action doesn't roll back completed deployments or cancel pending deployments.

URI: `PUT /greengrass/bulk/deployments/{{BulkDeploymentId}}/$stop`

Produces: application/json

## CLI:
<a name="stopbulkdeployment-put-cli"></a>

```
aws greengrass stop-bulk-deployment \
  --bulk-deployment-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"BulkDeploymentId": "string"
}
```

## Parameters:
<a name="stopbulkdeployment-put-params"></a>

[**BulkDeploymentId**](parameters-bulkdeploymentidparam.md)
The ID of the bulk deployment.
where used: path; required: true
type: string

## Responses:
<a name="stopbulkdeployment-put-resp"></a>

**200**
Success. The bulk deployment is being stopped.

**400**
Invalid request.
 [ GeneralError](definitions-generalerror.md)

```
{
"Message": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GeneralError
General error information.
type: object
required: ["Message"]
Message
A message that contains information about the error.
type: string
ErrorDetails
A list of error details.
type: array
items: [ErrorDetail](definitions-errordetail.md)
ErrorDetail
Details about the error.
type: object
DetailedErrorCode
A detailed error code.
type: string
DetailedErrorMessage
A detailed error message.
type: string
