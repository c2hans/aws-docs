---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-cores-coredefinitionid-versions.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/cores/CoreDefinitionId/versions
<a name="-greengrass-definition-cores-coredefinitionid-versions"></a>

## POST
<a name="-greengrass-definition-cores-coredefinitionid-versions-post"></a>

 `POST /greengrass/definition/cores/{{CoreDefinitionId}}/versions`

Operation ID: [CreateCoreDefinitionVersion](createcoredefinitionversion-post.md)

Creates a version of a core definition that has already been defined. Greengrass groups must each contain exactly one Greengrass core.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-cores-coredefinitionid-versions-post-body"></a>

[**CreateCoreDefinitionVersionRequestBody**](parameters-createcoredefinitionversionrequestbody.md)

where used: body; required: true

```
{
"Cores": [
  {
    "Id": "string",
    "ThingArn": "string",
    "CertificateArn": "string",
    "SyncShadow": true
  }
]
}
```
CoreDefinitionVersion
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

### Header Parameters
<a name="-greengrass-definition-cores-coredefinitionid-versions-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### Path Parameters
<a name="-greengrass-definition-cores-coredefinitionid-versions-post-path"></a>

[**CoreDefinitionId**](parameters-coredefinitionidparam.md)
The ID of the core definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-cores-coredefinitionid-versions-post-cli"></a>

```
aws greengrass create-core-definition-version \
  --core-definition-id <value> \
  [--cores <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"CoreDefinitionId": "string",
"Cores": [
  {
    "Id": "string",
    "ThingArn": "string",
    "CertificateArn": "string",
    "SyncShadow": "boolean"
  }
],
"AmznClientToken": "string"
}
```

### Responses
<a name="-greengrass-definition-cores-coredefinitionid-versions-post-responses"></a>

**200** (CreateCoreDefinitionVersionResponse)

 [ VersionInformation](definitions-versioninformation.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string"
}
```
VersionInformation
Information about a version.
type: object
Arn
The ARN of the version.
type: string
Id
The ID of the parent definition that the version is associated with.
type: string
Version
The ID of the version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the version was created.
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

## GET
<a name="-greengrass-definition-cores-coredefinitionid-versions-get"></a>

 `GET /greengrass/definition/cores/{{CoreDefinitionId}}/versions`

Operation ID: [ListCoreDefinitionVersions](listcoredefinitionversions-get.md)

Lists the versions of a core definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-cores-coredefinitionid-versions-get-path"></a>

[**CoreDefinitionId**](parameters-coredefinitionidparam.md)
The ID of the core definition.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-cores-coredefinitionid-versions-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

### CLI
<a name="-greengrass-definition-cores-coredefinitionid-versions-get-cli"></a>

```
aws greengrass list-core-definition-versions \
  --core-definition-id <value> \
  [--next-token <value>] \
  [--max-results <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"CoreDefinitionId": "string",
"NextToken": "string",
"MaxResults": "integer"
}
```

### Responses
<a name="-greengrass-definition-cores-coredefinitionid-versions-get-responses"></a>

**200** (ListCoreDefinitionVersionsResponse)

 [ ListVersionsResponse](definitions-listversionsresponse.md)

```
{
"Versions": [
  {
    "Arn": "string",
    "Id": "string",
    "Version": "string",
    "CreationTimestamp": "string"
  }
],
"NextToken": "string"
}
```
ListVersionsResponse
A list of versions.
type: object
Versions
Information about a version.
type: array
items: [VersionInformation](definitions-versioninformation.md)
VersionInformation
Information about a version.
type: object
Arn
The ARN of the version.
type: string
Id
The ID of the parent definition that the version is associated with.
type: string
Version
The ID of the version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the version was created.
type: string
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
