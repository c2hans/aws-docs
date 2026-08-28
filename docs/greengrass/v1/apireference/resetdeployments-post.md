---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/resetdeployments-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ResetDeployments
<a name="resetdeployments-post"></a>

Resets a group's deployments.

URI: `POST /greengrass/groups/{{GroupId}}/deployments/$reset`

Produces: application/json

## CLI:
<a name="resetdeployments-post-cli"></a>

```
aws greengrass reset-deployments \
  --group-id <value> \
  [--force | --no-force] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"Force": "boolean",
"AmznClientToken": "string"
}
```

## Parameters:
<a name="resetdeployments-post-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**ResetDeploymentsRequestBody**](parameters-resetdeploymentsrequestbody.md)
Information required to reset deployments.
where used: body; required: true

```
{
"Force": true
}
```
schema:
ResetDeploymentsRequest
Information about a group reset request.
type: object
Force
If true, performs a best-effort only core reset.
type: boolean

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="resetdeployments-post-resp"></a>

**200**
Success. The group's deployments were reset.
 [ ResetDeploymentsResponse](definitions-resetdeploymentsresponse.md)

```
{
"DeploymentArn": "string",
"DeploymentId": "string"
}
```
ResetDeploymentsResponse
type: object
DeploymentArn
The ARN of the deployment.
type: string
DeploymentId
The ID of the deployment.
type: string

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
