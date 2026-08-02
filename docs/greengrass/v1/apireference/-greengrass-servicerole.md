---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-servicerole.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/servicerole
<a name="-greengrass-servicerole"></a>

## GET
<a name="-greengrass-servicerole-get"></a>

 `GET /greengrass/servicerole`

Operation ID: [GetServiceRoleForAccount](getserviceroleforaccount-get.md)

Produces: application/json

### CLI
<a name="-greengrass-servicerole-get-cli"></a>

```
aws greengrass get-service-role-for-account  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

### Responses
<a name="-greengrass-servicerole-get-responses"></a>

**200**
Success.
 [ GetServiceRoleForAccountResponse](definitions-getserviceroleforaccountresponse.md)

```
{
  "AssociatedAt": "string",
  "RoleArn": "string"
}
```
GetServiceRoleForAccountResponse
type: object
AssociatedAt
The time when the service role was associated with the account.
type: string
RoleArn
The ARN of the role associated with the account.
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

## PUT
<a name="-greengrass-servicerole-put"></a>

 `PUT /greengrass/servicerole`

Operation ID: [AssociateServiceRoleToAccount](associateserviceroletoaccount-put.md)

Associates a role with your account. AWS IoT Greengrass uses the role to access your Lambda functions and AWS IoT resources. A role is required for deployments to succeed. The role must have at least minimum permissions in the policy `AWSGreengrassResourceAccessRolePolicy`.

### Body Parameters
<a name="-greengrass-servicerole-put-body"></a>

[**AssociateServiceRoleToAccountRequestBody**](parameters-associateserviceroletoaccountrequestbody.md)

where used: body; required: true

```
{
"RoleArn": "string"
}
```
AssociateServiceRoleToAccountRequest
type: object
required: ["RoleArn"]
RoleArn
The ARN of the service role to associate with your account.
type: string

### CLI
<a name="-greengrass-servicerole-put-cli"></a>

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

### Responses
<a name="-greengrass-servicerole-put-responses"></a>

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

## DELETE
<a name="-greengrass-servicerole-delete"></a>

 `DELETE /greengrass/servicerole`

Operation ID: [DisassociateServiceRoleFromAccount](disassociateservicerolefromaccount-delete.md)

Disassociates the service role from your account. Without a service role, deployments do not work.

### CLI
<a name="-greengrass-servicerole-delete-cli"></a>

```
aws greengrass disassociate-service-role-from-account  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

### Responses
<a name="-greengrass-servicerole-delete-responses"></a>

**200**
Success.
 [ DisassociateServiceRoleFromAccountResponse](definitions-disassociateservicerolefromaccountresponse.md)

```
{
"DisassociatedAt": "string"
}
```
DisassociateServiceRoleFromAccountResponse
type: object
DisassociatedAt
The time when the service role was disassociated from the account.
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

## GET
<a name="-greengrass-servicerole-get"></a>

 `GET /greengrass/servicerole`

Operation ID: [GetServiceRoleForAccount](getserviceroleforaccount-get.md)

Retrieves the service role that is attached to your account.

### CLI
<a name="-greengrass-servicerole-get-cli"></a>

```
aws greengrass get-service-role-for-account  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

### Responses
<a name="-greengrass-servicerole-get-responses"></a>

**200**
Success.
 [ GetServiceRoleForAccountResponse](definitions-getserviceroleforaccountresponse.md)

```
{
"AssociatedAt": "string",
"RoleArn": "string"
}
```
GetServiceRoleForAccountResponse
type: object
AssociatedAt
The time when the service role was associated with the account.
type: string
RoleArn
The ARN of the role associated with the account.
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
