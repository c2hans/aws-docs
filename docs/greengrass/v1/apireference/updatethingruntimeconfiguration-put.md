---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/updatethingruntimeconfiguration-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UpdateThingRuntimeConfiguration
<a name="updatethingruntimeconfiguration-put"></a>

Updates the runtime configuration of a Greengrass core to turn on or turn off telemetry.

URI: `PUT /greengrass/things/{ThingName}/runtimeconfig`

produces: application/json

## CLI:
<a name="updatethingruntimeconfiguration-put-cli"></a>

```
aws greengrass update-thing-runtime-configuration \
    --thing-name <value> \
    [--telemetry-configuration <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

cli-input-json format:

```
{
  "TelemetryConfiguration": {
    "Telemetry": "On|Off"
  },
  "ThingName": ""
}
```

## Parameters:
<a name="updatethingruntimeconfiguration-put-params"></a>

[RuntimeConfigurationUpdateRequestBody](parameters-runtimeconfigurationupdaterequestbody.md)
The configuration settings to run telemetry.
where used: body; required: true

```
{
  "TelemetryConfiguration": {
    "Telemetry": "On|Off"
  }
}
```
schema:
RuntimeConfigurationUpdate
Information about the runtime configuration for a thing.
type: object
TelemetryConfiguration
The configuration settings to run telemetry.
type: object
required: ["Telemetry"]
Telemetry
The configuration setting to turn on or turn off telemetry.
type: string
enum: ["On", "Off"]

[ThingName](parameters-thingnameparam.md)
The thing name.
where used: path; required: true
type: string

## Responses:
<a name="updatethingruntimeconfiguration-put-resp"></a>

**200**
200 response
 [ Empty](definitions-empty.md)

```
{
}
```
Empty Schema
Empty
type: object

**400**
400 response
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
500 response
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
