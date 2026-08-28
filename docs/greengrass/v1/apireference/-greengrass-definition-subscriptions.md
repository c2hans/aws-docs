---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-subscriptions.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/subscriptions
<a name="-greengrass-definition-subscriptions"></a>

## GET
<a name="-greengrass-definition-subscriptions-get"></a>

 `GET /greengrass/definition/subscriptions`

Operation ID: [ListSubscriptionDefinitions](listsubscriptiondefinitions-get.md)

Retrieves a list of subscription definitions.

Produces: application/json

### Query Parameters
<a name="-greengrass-definition-subscriptions-get-query"></a>

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-definition-subscriptions-get-cli"></a>

```
aws greengrass list-subscription-definitions \
  [--max-results <value>] \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"MaxResults": "integer",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-definition-subscriptions-get-responses"></a>

**200** (ListSubscriptionDefinitionsResponse)

 [ ListDefinitionsResponse](definitions-listdefinitionsresponse.md)

```
{
"Definitions": [
  {
    "Name": "string",
    "Id": "string",
    "Arn": "string",
    "tags": {
      "additionalProperty0": "string",
      "additionalProperty1": "string",
      "additionalProperty2": "string"
    },
    "LastUpdatedTimestamp": "string",
    "CreationTimestamp": "string",
    "LatestVersion": "string",
    "LatestVersionArn": "string"
  }
],
"NextToken": "string"
}
```
ListDefinitionsResponse
A list of definitions.
type: object
Definitions
Information about a definition.
type: array
items: [DefinitionInformation](definitions-definitioninformation.md)
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
tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string
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
NextToken
The token for the next set of results, or `null` if there are no more results.
type: string

## POST
<a name="-greengrass-definition-subscriptions-post"></a>

 `POST /greengrass/definition/subscriptions`

Operation ID: [CreateSubscriptionDefinition](createsubscriptiondefinition-post.md)

Creates a subscription definition. You can provide the initial version of the subscription definition now or use `CreateSubscriptionDefinitionVersion` later.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-subscriptions-post-body"></a>

[**CreateSubscriptionDefinitionRequestBody**](parameters-createsubscriptiondefinitionrequestbody.md)

where used: body; required: true

```
{
"Name": "string",
"InitialVersion": {
  "Subscriptions": [
    {
      "Id": "string",
      "Source": "string",
      "Subject": "string",
      "Target": "string"
    }
  ]
},
"tags": {
  "keyName0": "string",
  "keyName1": "string",
  "keyName2": "string"
}
}
```
Name
The name of the subscription definition.
type: string
InitialVersion
Information about a subscription definition version.
type: object
Subscriptions
A list of subscriptions.
type: array
items: [Subscription](definitions-subscription.md)
Subscription
Information about a subscription.
type: object
required: ["Id", "Source", "Subject", "Target"]
Id
A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string
Source
The source of the subscription. Can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, 'cloud' (which represents AWS IoT), or 'GGShadowService'. If you specify a Lambda function, this ARN should match the ARN used to add the function to the Greengrass group.
type: string
Subject
The MQTT topic used to route the message.
type: string
Target
Where the message is sent. Can be a thing ARN, the ARN of a Lambda function alias (recommended) or version, a connector ARN, 'cloud' (which represents AWS IoT), or 'GGShadowService'. If you specify a Lambda function, this ARN should match the ARN used to add the function to the Greengrass group.
type: string
tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

### Header Parameters
<a name="-greengrass-definition-subscriptions-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### CLI
<a name="-greengrass-definition-subscriptions-post-cli"></a>

```
aws greengrass create-subscription-definition \
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
  "Subscriptions": [
    {
      "Id": "string",
      "Source": "string",
      "Subject": "string",
      "Target": "string"
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

### Responses
<a name="-greengrass-definition-subscriptions-post-responses"></a>

**200** (CreateSubscriptionDefinitionResponse)

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
