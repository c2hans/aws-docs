---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/listgroupcertificateauthorities-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListGroupCertificateAuthorities
<a name="listgroupcertificateauthorities-get"></a>

Retrieves the current CAs for a group.

URI: `GET /greengrass/groups/{{GroupId}}/certificateauthorities`

Produces: application/json

## CLI:
<a name="listgroupcertificateauthorities-get-cli"></a>

```
aws greengrass list-group-certificate-authorities \
  --group-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string"
}
```

## Parameters:
<a name="listgroupcertificateauthorities-get-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

## Responses:
<a name="listgroupcertificateauthorities-get-resp"></a>

**200**
Success. The response body contains the PKI configuration.
 [ ListGroupCertificateAuthoritiesResponse](definitions-listgroupcertificateauthoritiesresponse.md)

```
{
"GroupCertificateAuthorities": [
  {
    "GroupCertificateAuthorityId": "string",
    "GroupCertificateAuthorityArn": "string"
  }
]
}
```
ListGroupCertificateAuthoritiesResponse
type: object
GroupCertificateAuthorities
A list of certificate authorities associated with the group.
type: array
items: [GroupCertificateAuthorityProperties](definitions-groupcertificateauthorityproperties.md)
Group Certificate Authority Properties
Information about a certificate authority for a group.
type: object
GroupCertificateAuthorityId
The ID of the certificate authority for the group.
type: string
GroupCertificateAuthorityArn
The ARN of the certificate authority for the group.
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
