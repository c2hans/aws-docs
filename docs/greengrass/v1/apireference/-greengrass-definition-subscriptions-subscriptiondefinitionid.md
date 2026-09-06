---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-subscriptions-subscriptiondefinitionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/subscriptions/SubscriptionDefinitionId
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid"></a>

## GET
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-get"></a>

 `GET /greengrass/definition/subscriptions/{{SubscriptionDefinitionId}}`

Operation ID: [GetSubscriptionDefinition](getsubscriptiondefinition-get.md)

Retrieves information about a subscription definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-get-path"></a>

[**SubscriptionDefinitionId**](parameters-subscriptiondefinitionidparam.md)
The ID of the subscription definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-get-cli"></a>

```
aws greengrass get-subscription-definition \
  --subscription-definition-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"SubscriptionDefinitionId": "string"
}
```

### Responses
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-get-responses"></a>

**200** (GetSubscriptionDefinitionResponse)

 [ DefinitionInformation](definitions-definitioninformation.md)

```
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

## DELETE
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-delete"></a>

 `DELETE /greengrass/definition/subscriptions/{{SubscriptionDefinitionId}}`

Operation ID: [DeleteSubscriptionDefinition](deletesubscriptiondefinition-delete.md)

Deletes a subscription definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-delete-path"></a>

[**SubscriptionDefinitionId**](parameters-subscriptiondefinitionidparam.md)
The ID of the subscription definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-delete-cli"></a>

```
aws greengrass delete-subscription-definition \
  --subscription-definition-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"SubscriptionDefinitionId": "string"
}
```

### Responses
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-delete-responses"></a>

**200**
Success.
 [ Empty](definitions-empty.md)

```
{
}
```
Empty Schema
Empty
type: object

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

## PUT
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-put"></a>

 `PUT /greengrass/definition/subscriptions/{{SubscriptionDefinitionId}}`

Operation ID: [UpdateSubscriptionDefinition](updatesubscriptiondefinition-put.md)

Updates the name of a subscription definition. To update the list of available subscriptions, use `CreateSubscriptionDefinitionVersion`.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-put-body"></a>

[**UpdateDefinitionRequestBody**](parameters-updatedefinitionrequestbody.md)

where used: body; required: true

```
{
"Name": "string"
}
```
Name
The name of the definition.
required: true
type: string

### Path Parameters
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-put-path"></a>

[**SubscriptionDefinitionId**](parameters-subscriptiondefinitionidparam.md)
The ID of the subscription definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-put-cli"></a>

```
aws greengrass update-subscription-definition \
  --subscription-definition-id <value> \
  [--name <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"SubscriptionDefinitionId": "string",
"Name": "string"
}
```

### Responses
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-put-responses"></a>

**200**
Success.
 [ Empty](definitions-empty.md)

```
{
}
```
Empty Schema
Empty
type: object

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
