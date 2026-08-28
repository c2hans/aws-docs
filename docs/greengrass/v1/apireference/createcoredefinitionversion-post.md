---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createcoredefinitionversion-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateCoreDefinitionVersion
<a name="createcoredefinitionversion-post"></a>

Creates a version of a core definition that has already been defined. Greengrass groups must each contain exactly one Greengrass core.

URI: `POST /greengrass/definition/cores/{{CoreDefinitionId}}/versions`

Produces: application/json

## CLI:
<a name="createcoredefinitionversion-post-cli"></a>

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

## Parameters:
<a name="createcoredefinitionversion-post-params"></a>

[**CoreDefinitionId**](parameters-coredefinitionidparam.md)
The ID of the core definition.
where used: path; required: true
type: string

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
schema:
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

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="createcoredefinitionversion-post-resp"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
