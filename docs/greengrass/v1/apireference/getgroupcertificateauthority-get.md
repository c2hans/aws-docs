---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupcertificateauthority-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetGroupCertificateAuthority
<a name="getgroupcertificateauthority-get"></a>

Retreives the CA associated with a group. Returns the public key of the CA.

URI: `GET /greengrass/groups/{{GroupId}}/certificateauthorities/{{CertificateAuthorityId}}`

Produces: application/json

## CLI:
<a name="getgroupcertificateauthority-get-cli"></a>

```
aws greengrass get-group-certificate-authority \
  --group-id <value> \
  --certificate-authority-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"CertificateAuthorityId": "string"
}
```

## Parameters:
<a name="getgroupcertificateauthority-get-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**CertificateAuthorityId**](parameters-certificateauthorityidparam.md)
The ID of the certificate authority.
where used: path; required: true
type: string

## Responses:
<a name="getgroupcertificateauthority-get-resp"></a>

**200**
Success. The response body contains the PKI configuration.
 [ GetGroupCertificateAuthorityResponse](definitions-getgroupcertificateauthorityresponse.md)

```
{
"PemEncodedCertificate": "string",
"GroupCertificateAuthorityArn": "string",
"GroupCertificateAuthorityId": "string"
}
```
GetGroupCertificateAuthorityResponse
Information about a certificate authority for a group.
type: object
PemEncodedCertificate
The PEM encoded certificate for the group.
type: string
GroupCertificateAuthorityArn
The ARN of the certificate authority for the group.
type: string
GroupCertificateAuthorityId
The ID of the certificate authority for the group.
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
