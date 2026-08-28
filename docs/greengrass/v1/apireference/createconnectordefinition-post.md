---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createconnectordefinition-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateConnectorDefinition
<a name="createconnectordefinition-post"></a>

Creates a connector definition. You can provide the initial version of the connector definition now or use `CreateConnectorDefinitionVersion` later.

URI: `POST /greengrass/definition/connectors`

Produces: application/json

## CLI:
<a name="createconnectordefinition-post-cli"></a>

```
aws greengrass create-connector-definition \
  [--name <value>] \
  [--initial-version <value>] \
  [--tags <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"Name": "string",
"InitialVersion": {
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
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
},
"AmznClientToken": "string"
}
```

## Parameters:
<a name="createconnectordefinition-post-params"></a>

[**CreateConnectorDefinitionRequestBody**](parameters-createconnectordefinitionrequestbody.md)

where used: body; required: true

```
{
"Name": "string",
"InitialVersion": {
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
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
}
}
```
schema:
Name
The name of the connector definition.
type: string
InitialVersion
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
tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to enforce the idempotency of this API.
where used: header; required: false
type: string

## Responses:
<a name="createconnectordefinition-post-resp"></a>

**200** (CreateConnectorDefinitionResponse)

 [ DefinitionInformation](definitions-definitioninformation.md)

```
{
"Name": "string",
"Id": "string",
"Arn": "string",
"LastUpdatedTimestamp": "string",
"CreationTimestamp": "string",
"LatestVersion": "string",
"LatestVersionArn": "string"
}
```
DefinitionInformation
Information about a definition.
type: object
Name
The name of the definition.
type: string
Id
The ID of the definition.
type: string
Arn
The ARN of the definition.
type: string
LastUpdatedTimestamp
The time, in milliseconds since the epoch, when the definition was last updated.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the definition was created.
type: string
LatestVersion
The ID of the latest version associated with the definition.
type: string
LatestVersionArn
The ARN of the latest version associated with the definition.
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
