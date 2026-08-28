---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-devices-devicedefinitionid-versions.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/devices/DeviceDefinitionId/versions
<a name="-greengrass-definition-devices-devicedefinitionid-versions"></a>

## POST
<a name="-greengrass-definition-devices-devicedefinitionid-versions-post"></a>

 `POST /greengrass/definition/devices/{{DeviceDefinitionId}}/versions`

Operation ID: [CreateDeviceDefinitionVersion](createdevicedefinitionversion-post.md)

Creates a version of a device definition that has already been defined.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-post-body"></a>

[**CreateDeviceDefinitionVersionRequestBody**](parameters-createdevicedefinitionversionrequestbody.md)

where used: body; required: true

```
{
"Devices": [
  {
    "Id": "string",
    "ThingArn": "string",
    "CertificateArn": "string",
    "SyncShadow": true
  }
]
}
```
DeviceDefinitionVersion
Information about a device definition version.
type: object
Devices
A list of devices in the definition version.
type: array
items: [Device](definitions-device.md)
Device
Information about a device.
type: object
required: ["Id", "ThingArn", "CertificateArn"]
Id
A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string
ThingArn
The thing ARN of the device.
type: string
CertificateArn
The ARN of the certificate associated with the device.
type: string
SyncShadow
If true, the device's local shadow is synced with the cloud automatically.
type: boolean

### Header Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### Path Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-post-path"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-devices-devicedefinitionid-versions-post-cli"></a>

```
aws greengrass create-device-definition-version \
  --device-definition-id <value> \
  [--devices <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"DeviceDefinitionId": "string",
"Devices": [
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
<a name="-greengrass-definition-devices-devicedefinitionid-versions-post-responses"></a>

**200** (CreateDeviceDefinitionVersionResponse)

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
<a name="-greengrass-definition-devices-devicedefinitionid-versions-get"></a>

 `GET /greengrass/definition/devices/{{DeviceDefinitionId}}/versions`

Operation ID: [ListDeviceDefinitionVersions](listdevicedefinitionversions-get.md)

Lists the versions of a device definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-get-path"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

### CLI
<a name="-greengrass-definition-devices-devicedefinitionid-versions-get-cli"></a>

```
aws greengrass list-device-definition-versions \
  --device-definition-id <value> \
  [--next-token <value>] \
  [--max-results <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"DeviceDefinitionId": "string",
"NextToken": "string",
"MaxResults": "integer"
}
```

### Responses
<a name="-greengrass-definition-devices-devicedefinitionid-versions-get-responses"></a>

**200** (ListDeviceDefinitionVersionsResponse)

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
