---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/associateroletogroup-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# AssociateRoleToGroup
<a name="associateroletogroup-put"></a>

Associates a role with a group. Your Greengrass core uses the role to access AWS services. The role's permissions should allow Greengrass Lambda functions and connectors to perform actions against the cloud.

URI: `PUT /greengrass/groups/{{GroupId}}/role`

## CLI:
<a name="associateroletogroup-put-cli"></a>

```
aws greengrass associate-role-to-group \
  --group-id <value> \
  [--role-arn <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"RoleArn": "string"
}
```

## Parameters:
<a name="associateroletogroup-put-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**AssociateRoleToGroupRequestBody**](parameters-associateroletogrouprequestbody.md)

where used: body; required: true

```
{
"RoleArn": "string"
}
```
schema:
AssociateRoleToGroupRequest
type: object
required: ["RoleArn"]
RoleArn
The ARN of the role to associate with this group.
type: string

## Responses:
<a name="associateroletogroup-put-resp"></a>

**200**
Success.
 [ AssociateRoleToGroupResponse](definitions-associateroletogroupresponse.md)

```
{
"AssociatedAt": "string"
}
```
Group
type: object
AssociatedAt
The time, in milliseconds since the epoch, when the role ARN was associated with the group.
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
