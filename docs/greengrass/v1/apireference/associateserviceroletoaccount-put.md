---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/associateserviceroletoaccount-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# AssociateServiceRoleToAccount
<a name="associateserviceroletoaccount-put"></a>

Associates a role with your account. AWS IoT Greengrass uses the role to access your Lambda functions and AWS IoT resources. A role is required for deployments to succeed. The role must have at least minimum permissions in the policy `AWSGreengrassResourceAccessRolePolicy`.

URI: `PUT /greengrass/servicerole`

## CLI:
<a name="associateserviceroletoaccount-put-cli"></a>

```
aws greengrass associate-service-role-to-account \
  [--role-arn <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"RoleArn": "string"
}
```

## Parameters:
<a name="associateserviceroletoaccount-put-params"></a>

[**AssociateServiceRoleToAccountRequestBody**](parameters-associateserviceroletoaccountrequestbody.md)

where used: body; required: true

```
{
"RoleArn": "string"
}
```
schema:
AssociateServiceRoleToAccountRequest
type: object
required: ["RoleArn"]
RoleArn
The ARN of the service role to associate with your account.
type: string

## Responses:
<a name="associateserviceroletoaccount-put-resp"></a>

**200**
Success.
 [ AssociateServiceRoleToAccountResponse](definitions-associateserviceroletoaccountresponse.md)

```
{
"AssociatedAt": "string"
}
```
AssociateServiceRoleToAccountResponse
type: object
AssociatedAt
The time when the service role was associated with the account.
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

**500**
Server error.
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
