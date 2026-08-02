---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-getconnectordefinitionversionresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetConnectorDefinitionVersionResponse
<a name="definitions-getconnectordefinitionversionresponse"></a>

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "Connectors": [
    {
      "Id": "string",
      "ConnectorArn": "string",
      "Parameters": {
        "additionalProperty0": "string",
        "additionalProperty1": "string",
        "additionalProperty2": "string"
      }
    }
  ]
},
"NextToken": "string"
}
```

GetConnectorDefinitionVersionResponse
Information about a connector definition version.
type: object

Arn
The ARN of the connector definition version.
type: string

Id
The ID of the connector definition version.
type: string

Version
The version of the connector definition version.
type: string

CreationTimestamp
The time, in milliseconds since the epoch, when the connector definition version was created.
type: string

Definition
Information about the connector definition version, which is a container for connectors.
type: object

Connectors
A list of references to connectors in this version, with their corresponding configuration settings.
type: array
items: [Connector](definitions-connector.md)

Connector
Information about a connector. Connectors run on the Greengrass core and contain built-in integration with local infrastructure, device protocols, AWS, and other cloud services.
type: object
required: ["Id", "ConnectorArn"]

Id
A descriptive or arbitrary ID for the connector. This value must be unique within the connector definition version. Maximum length is 128 characters with the pattern [a-zA-Z0-9:\_-]\+.
type: string

ConnectorArn
The ARN of the connector.
type: string

Parameters
The parameters or configuration used by the connector.
type: object
additionalProperties: An object with properties of type `string` that represent the connector configuration.

NextToken
The token for the next set of results, or `null` if there are no more results.
type: string
