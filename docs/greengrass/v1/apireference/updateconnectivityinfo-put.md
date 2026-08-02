---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/updateconnectivityinfo-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UpdateConnectivityInfo
<a name="updateconnectivityinfo-put"></a>

Updates the connectivity information for the core. Client devices that belong to the group that has this core receive this information to find the location of the core and connect to it.

URI: `PUT /greengrass/things/{{ThingName}}/connectivityInfo`

Produces: application/json

## CLI:
<a name="updateconnectivityinfo-put-cli"></a>

```
aws greengrass update-connectivity-info \
  --thing-name <value> \
  [--connectivity-info <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ThingName": "string",
"ConnectivityInfo": [
  {
    "Id": "string",
    "HostAddress": "string",
    "PortNumber": "int32-integer",
    "Metadata": "string"
  }
]
}
```

## Parameters:
<a name="updateconnectivityinfo-put-params"></a>

[**ThingName**](parameters-thingnameparam.md)
The thing name.
where used: path; required: true
type: string

[**UpdateConnectivityInfoRequestBody**](parameters-updateconnectivityinforequestbody.md)
The connectivity information.
where used: body; required:

```
{
"ConnectivityInfo": [
  {
    "Id": "string",
    "HostAddress": "string",
    "PortNumber": 0x01,
    "Metadata": "string"
  }
]
}
```
schema:

Information required to update a Greengrass core's connectivity.
ConnectivityInfo
A list of connectivity info.
type: array
items: [ConnectivityInfo](definitions-connectivityinfo.md)

Information about a Greengrass core's connectivity.
required: ["Id", "HostAddress"]
Id
The ID of the connectivity information.
type: string
HostAddress
The endpoint for the Greengrass core. Can be an IP address or DNS address.
type: string
PortNumber
The port of the Greengrass core, usually 8883.
type: integer
format: int32
Metadata
Metadata for this endpoint.
type: string

## Responses:
<a name="updateconnectivityinfo-put-resp"></a>

**200**
Success.
 [ UpdateConnectivityInfoResponse](definitions-updateconnectivityinforesponse.md)

```
{
"message": "string",
"Version": "string"
}
```
message
A message about the connectivity info update request.
type: string
Version
The new version of the connectivity info.
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
