---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/listsubscriptiondefinitions-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListSubscriptionDefinitions
<a name="listsubscriptiondefinitions-get"></a>

Retrieves a list of subscription definitions.

URI: `GET /greengrass/definition/subscriptions`

Produces: application/json

## CLI:
<a name="listsubscriptiondefinitions-get-cli"></a>

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

## Parameters:
<a name="listsubscriptiondefinitions-get-params"></a>

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

## Responses:
<a name="listsubscriptiondefinitions-get-resp"></a>

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
