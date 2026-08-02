---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-groups-groupid-certificateauthorities-configuration-expiry.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/groups/GroupId/certificateauthorities/configuration/expiry
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry"></a>

## GET
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-get"></a>

 `GET /greengrass/groups/{{GroupId}}/certificateauthorities/configuration/expiry`

Operation ID: [GetGroupCertificateConfiguration](getgroupcertificateconfiguration-get.md)

Retrieves the current configuration for the CA used by the group.

Produces: application/json

### Path Parameters
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-get-path"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-get-cli"></a>

```
aws greengrass get-group-certificate-configuration \
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

### Responses
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-get-responses"></a>

**200**
Success. The response body contains the PKI configuration.
 [ GroupCertificateConfiguration](definitions-groupcertificateconfiguration.md)

```
{
"GroupId": "string",
"CertificateAuthorityExpiryInMilliseconds": "string",
"CertificateExpiryInMilliseconds": "string"
}
```
GroupCertificateConfiguration
Information about a group certificate configuration.
type: object
GroupId
The ID of the group certificate configuration.
type: string
CertificateAuthorityExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate authority expires.
type: string
CertificateExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate expires.
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

## PUT
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-put"></a>

 `PUT /greengrass/groups/{{GroupId}}/certificateauthorities/configuration/expiry`

Operation ID: [UpdateGroupCertificateConfiguration](updategroupcertificateconfiguration-put.md)

Updates the certificate expiry time for a group.

Produces: application/json

### Body Parameters
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-put-body"></a>

[**UpdateGroupCertificateConfigurationRequestBody**](parameters-updategroupcertificateconfigurationrequestbody.md)

where used: body; required: true

```
{
"CertificateExpiryInMilliseconds": "string"
}
```
updateGroupCertificateConfigurationRequest
type: object
required: ["CertificateExpiryInMilliseconds"]
CertificateExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate expires.
type: string

### Path Parameters
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-put-path"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-put-cli"></a>

```
aws greengrass update-group-certificate-configuration \
  --group-id <value> \
  [--certificate-expiry-in-milliseconds <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"CertificateExpiryInMilliseconds": "string"
}
```

### Responses
<a name="-greengrass-groups-groupid-certificateauthorities-configuration-expiry-put-responses"></a>

**200**
Success. The response body contains the PKI configuration.
 [ GroupCertificateConfiguration](definitions-groupcertificateconfiguration.md)

```
{
"GroupId": "string",
"CertificateAuthorityExpiryInMilliseconds": "string",
"CertificateExpiryInMilliseconds": "string"
}
```
GroupCertificateConfiguration
Information about a group certificate configuration.
type: object
GroupId
The ID of the group certificate configuration.
type: string
CertificateAuthorityExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate authority expires.
type: string
CertificateExpiryInMilliseconds
The amount of time, in milliseconds, before the certificate expires.
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
