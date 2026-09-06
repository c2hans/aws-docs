---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/cores/CoreDefinitionId/versions/CoreDefinitionVersionId
<a name="-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid"></a>

## GET
<a name="-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid-get"></a>

 `GET /greengrass/definition/cores/{{CoreDefinitionId}}/versions/{{CoreDefinitionVersionId}}`

Operation ID: [GetCoreDefinitionVersion](getcoredefinitionversion-get.md)

Retrieves information about a core definition version.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid-get-path"></a>

[**CoreDefinitionId**](parameters-coredefinitionidparam.md)
The ID of the core definition.
where used: path; required: true
type: string

[**CoreDefinitionVersionId**](parameters-coredefinitionversionidparam.md)
The ID of the core definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListCoreDefinitionVersions` requests. If the version is the last one that was associated with a core definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid-get-cli"></a>

```
aws greengrass get-core-definition-version \
  --core-definition-id <value> \
  --core-definition-version-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"CoreDefinitionId": "string",
"CoreDefinitionVersionId": "string"
}
```

### Responses
<a name="-greengrass-definition-cores-coredefinitionid-versions-coredefinitionversionid-get-responses"></a>

**200**
Success.
 [ GetCoreDefinitionVersionResponse](definitions-getcoredefinitionversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "Cores": [
    {
      "Id": "string",
      "ThingArn": "string",
      "CertificateArn": "string",
      "SyncShadow": true
    }
  ]
},
"NextToken": "string"
}
```
GetCoreDefinitionVersionResponse
type: object
Arn
The ARN of the core definition version.
type: string
Id
The ID of the core definition version.
type: string
Version
The version of the core definition version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the core definition version was created.
type: string
Definition
Information about a core definition version.
type: object
Cores
A list of cores in the core definition version.
type: array
items: [Core](definitions-core.md)
Core
Information about a core.
type: object
required: ["Id", "ThingArn", "CertificateArn"]
Id
A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string
ThingArn
The ARN of the thing that is the core.
type: string
CertificateArn
The ARN of the certificate associated with the core.
type: string
SyncShadow
If true, the core's local shadow is synced with the cloud automatically.
type: boolean
NextToken
The token for the next set of results, or `null` if there are no more results.
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
