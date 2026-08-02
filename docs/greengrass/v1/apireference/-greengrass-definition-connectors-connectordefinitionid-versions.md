---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-connectors-connectordefinitionid-versions.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/connectors/ConnectorDefinitionId/versions
<a name="-greengrass-definition-connectors-connectordefinitionid-versions"></a>

## GET
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-get"></a>

 `GET /greengrass/definition/connectors/{{ConnectorDefinitionId}}/versions`

Operation ID: [ListConnectorDefinitionVersions](listconnectordefinitionversions-get.md)

Lists the versions of a connector definition, which are containers for connectors. Connectors run on the Greengrass core and contain built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-get-path"></a>

[**ConnectorDefinitionId**](parameters-connectordefinitionidparam.md)
The ID of the connector definition.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

### CLI
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-get-cli"></a>

```
aws greengrass list-connector-definition-versions \
  --connector-definition-id <value> \
  [--next-token <value>] \
  [--max-results <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ConnectorDefinitionId": "string",
"NextToken": "string",
"MaxResults": "integer"
}
```

### Responses
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-get-responses"></a>

**200** (ListConnectorDefinitionVersionsResponse)

 [ ListVersionsResponse](definitions-listversionsresponse.md)

```
{
"Versions": [
  {
    "Arn": "string",
    "Id": "string",
    "Version": "string",
    "CreationTimestamp": "string"
  }
],
"NextToken": "string"
}
```
ListVersionsResponse
A list of versions.
type: object
Versions
Information about a version.
type: array
items: [VersionInformation](definitions-versioninformation.md)
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

## POST
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-post"></a>

 `POST /greengrass/definition/connectors/{{ConnectorDefinitionId}}/versions`

Operation ID: [CreateConnectorDefinitionVersion](createconnectordefinitionversion-post.md)

Creates a version of a connector definition that has already been defined.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-post-body"></a>

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

### Header Parameters
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to enforce the idempotency of this API.
where used: header; required: false
type: string

### Path Parameters
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-post-path"></a>

[**ConnectorDefinitionId**](parameters-connectordefinitionidparam.md)
The ID of the connector definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-post-cli"></a>

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

### Responses
<a name="-greengrass-definition-connectors-connectordefinitionid-versions-post-responses"></a>

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
