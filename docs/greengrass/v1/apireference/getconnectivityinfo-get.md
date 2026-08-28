---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectivityinfo-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetConnectivityInfo
<a name="getconnectivityinfo-get"></a>

Retrieves the connectivity information for a core.

URI: `GET /greengrass/things/{{ThingName}}/connectivityInfo`

Produces: application/json

## CLI:
<a name="getconnectivityinfo-get-cli"></a>

```
aws greengrass get-connectivity-info \
  --thing-name <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ThingName": "string"
}
```

## Parameters:
<a name="getconnectivityinfo-get-params"></a>

[**ThingName**](parameters-thingnameparam.md)
The thing name.
where used: path; required: true
type: string

## Responses:
<a name="getconnectivityinfo-get-resp"></a>

**200**
Success.
 [ GetConnectivityInfoResponse](definitions-getconnectivityinforesponse.md)

```
{
"message": "string",
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

Information about a Greengrass core's connectivity.
message
A message about the connectivity info request.
type: string
ConnectivityInfo
Connectivity info list.
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
