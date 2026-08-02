---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getserviceroleforaccount-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetServiceRoleForAccount
<a name="getserviceroleforaccount-get"></a>

Retrieves the service role that is attached to your account.

URI: `GET /greengrass/servicerole`

## CLI:
<a name="getserviceroleforaccount-get-cli"></a>

```
aws greengrass get-service-role-for-account  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

## Responses:
<a name="getserviceroleforaccount-get-resp"></a>

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
