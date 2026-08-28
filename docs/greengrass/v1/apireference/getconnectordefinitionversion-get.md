---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectordefinitionversion-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetConnectorDefinitionVersion
<a name="getconnectordefinitionversion-get"></a>

Retrieves information about a connector definition version, including the connectors that the version contains. Connectors are prebuilt modules that interact with local infrastructure, device protocols, AWS, and other cloud services.

URI: `GET /greengrass/definition/connectors/{{ConnectorDefinitionId}}/versions/{{ConnectorDefinitionVersionId}}`

Produces: application/json

## CLI:
<a name="getconnectordefinitionversion-get-cli"></a>

```
aws greengrass get-connector-definition-version \
  --connector-definition-id <value> \
  --connector-definition-version-id <value> \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ConnectorDefinitionId": "string",
"ConnectorDefinitionVersionId": "string",
"NextToken": "string"
}
```

## Parameters:
<a name="getconnectordefinitionversion-get-params"></a>

[**ConnectorDefinitionId**](parameters-connectordefinitionidparam.md)
The ID of the connector definition.
where used: path; required: true
type: string

[**ConnectorDefinitionVersionId**](parameters-connectordefinitionversionidparam.md)
The ID of the connector definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListConnectorDefinitionVersions` requests. If the version is the last one that was associated with a connector definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

## Responses:
<a name="getconnectordefinitionversion-get-resp"></a>

**200** (GetConnectorDefinitionVersionResponse)

 [ GetConnectorDefinitionVersionResponse](definitions-getconnectordefinitionversionresponse.md)

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
additionalProperties: The key-value pair for the resource tag. Type: string
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
