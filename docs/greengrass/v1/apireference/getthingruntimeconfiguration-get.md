---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getthingruntimeconfiguration-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetThingRuntimeConfiguration
<a name="getthingruntimeconfiguration-get"></a>

Retrieves the runtime configuration of a Greengrass core. Before you can retrieve the runtime configuration, you must use [UpdateThingRuntimeConfiguration](updatethingruntimeconfiguration-put.md) to create a runtime configuration for the core.

URI: `GET /greengrass/things/{ThingName}/runtimeconfig`

Produces: application/json

## CLI:
<a name="getthingruntimeconfiguration-get-cli"></a>

```
aws greengrass get-thing-runtime-configuration  \
    --thing-name <value> \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

cli-input-json format:

```
{
    "ThingName": ""
}
```

## Parameters:
<a name="getthingruntimeconfiguration-get-params"></a>

[ThingName](parameters-thingnameparam.md)
The thing name.
where used: path; required: true
type: string

## Responses:
<a name="getthingruntimeconfiguration-get-resp"></a>

**200**
200 response
 [ GetThingRuntimeConfigurationResponse](definitions-getthingruntimeconfigurationresponse.md)

```
{
  "RuntimeConfiguration": {
    "TelemetryConfiguration": {
      "Telemetry": "On|Off",
      "ConfigurationSyncStatus": "InSync|OutOfSync"
    }
  }
}
```
GetThingRuntimeConfigurationResponse
Information about the runtime configuration for a thing.
type: object
RuntimeConfiguration
The runtime configuration for a thing.
type: object
TelemetryConfiguration
The configuration setting to run telemetry.
type: object
required: ["Telemetry"]
Telemetry
The configuration setting to turn on or turn off telemetry.
type: string
enum: ["On", "Off"]
ConfigurationSyncStatus
The synchronization status of the device-reported configuration with the desired configuration.
type: string
enum: ["InSync", "OutOfSync"]

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
