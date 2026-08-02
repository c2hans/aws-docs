---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/devices/DeviceDefinitionId/versions/DeviceDefinitionVersionId
<a name="-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid"></a>

## GET
<a name="-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid-get"></a>

 `GET /greengrass/definition/devices/{{DeviceDefinitionId}}/versions/{{DeviceDefinitionVersionId}}`

Operation ID: [GetDeviceDefinitionVersion](getdevicedefinitionversion-get.md)

Retrieves information about a device definition version.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid-get-path"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

[**DeviceDefinitionVersionId**](parameters-devicedefinitionversionidparam.md)
The ID of the device definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListDeviceDefinitionVersions` requests. If the version is the last one that was associated with a device definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid-get-cli"></a>

```
aws greengrass get-device-definition-version \
  --device-definition-id <value> \
  --device-definition-version-id <value> \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"DeviceDefinitionId": "string",
"DeviceDefinitionVersionId": "string",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-definition-devices-devicedefinitionid-versions-devicedefinitionversionid-get-responses"></a>

**200** (GetDeviceDefinitionVersionResponse)

 [ GetDeviceDefinitionVersionResponse](definitions-getdevicedefinitionversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "Devices": [
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
GetDeviceDefinitionVersionResponse
type: object
Arn
The ARN of the device definition version.
type: string
Id
The ID of the device definition version.
type: string
Version
The version of the device definition version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the device definition version was created.
type: string
Definition
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
