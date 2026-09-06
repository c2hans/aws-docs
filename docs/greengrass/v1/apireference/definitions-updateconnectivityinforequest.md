---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-updateconnectivityinforequest.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UpdateConnectivityInfoRequest
<a name="definitions-updateconnectivityinforequest"></a>

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
