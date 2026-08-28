---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-things-thingname-runtimeconfig.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/things/ThingName/runtimeconfig
<a name="-greengrass-things-thingname-runtimeconfig"></a>

## GET
<a name="-greengrass-things-thingname-runtimeconfig-get"></a>

 `GET /greengrass/things/{ThingName}/runtimeconfig`

Operation ID: [GetThingRuntimeConfiguration](getthingruntimeconfiguration-get.md)

Produces: application/json

### CLI
<a name="-greengrass-things-thingname-runtimeconfig-get-cli"></a>

```
aws greengrass get-thing-runtime-configuration  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

### Responses
<a name="-greengrass-things-thingname-runtimeconfig-get-responses"></a>

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
The runtime configuration for a thing.
type: object
RuntimeConfiguration
Runtime configuration for a thing.
type: object
TelemetryConfiguration
The configuration setting for running telemetry.
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

## PUT
<a name="-greengrass-things-thingname-runtimeconfig-put"></a>

 `PUT /greengrass/things/{ThingName}/runtimeconfig`

Operation ID: [UpdateThingRuntimeConfiguration](updatethingruntimeconfiguration-put.md)

Produces: application/json

### CLI
<a name="-greengrass-things-thingname-runtimeconfig-put-cli"></a>

```
aws greengrass update-thing-runtime-configuration \
    [--telemetry-configuration <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

cli-input-json format:

```
{
  "TelemetryConfiguration": {
    "Telemetry": "On|Off"
  }
}
```

### Responses
<a name="-greengrass-things-thingname-runtimeconfig-put-responses"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
