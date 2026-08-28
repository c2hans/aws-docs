---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createconnectordefinitionversion-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateConnectorDefinitionVersion
<a name="createconnectordefinitionversion-post"></a>

Creates a version of a connector definition that has already been defined.

URI: `POST /greengrass/definition/connectors/{{ConnectorDefinitionId}}/versions`

Produces: application/json

## CLI:
<a name="createconnectordefinitionversion-post-cli"></a>

```
aws greengrass create-connector-definition-version \
  --connector-definition-id <value> \
  [--connectors <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ConnectorDefinitionId": "string",
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
],
"AmznClientToken": "string"
}
```

## Parameters:
<a name="createconnectordefinitionversion-post-params"></a>

[**ConnectorDefinitionId**](parameters-connectordefinitionidparam.md)
The ID of the connector definition.
where used: path; required: true
type: string

[**CreateConnectorDefinitionVersionRequestBody**](parameters-createconnectordefinitionversionrequestbody.md)

where used: body; required: true

```
{
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
}
```
schema:
ConnectorDefinitionVersion
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

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to enforce the idempotency of this API.
where used: header; required: false
type: string

## Responses:
<a name="createconnectordefinitionversion-post-resp"></a>

**200** (CreateConnectorDefinitionVersionResponse)

 [ VersionInformation](definitions-versioninformation.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string"
}
```
VersionInformation
Information about a version.
type: object
Arn
The ARN of the version.
type: string
Id
The ID of the parent definition that the version is associated with.
type: string
Version
The ID of the version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the version was created.
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
