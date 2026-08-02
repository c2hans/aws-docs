---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createsubscriptiondefinitionversion-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateSubscriptionDefinitionVersion
<a name="createsubscriptiondefinitionversion-post"></a>

Creates a version of a subscription definition that has already been defined.

URI: `POST /greengrass/definition/subscriptions/{{SubscriptionDefinitionId}}/versions`

Produces: application/json

## CLI:
<a name="createsubscriptiondefinitionversion-post-cli"></a>

```
aws greengrass create-subscription-definition-version \
  --subscription-definition-id <value> \
  [--subscriptions <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"SubscriptionDefinitionId": "string",
"Subscriptions": [
  {
    "Id": "string",
    "Source": "string",
    "Subject": "string",
    "Target": "string"
  }
],
"AmznClientToken": "string"
}
```

## Parameters:
<a name="createsubscriptiondefinitionversion-post-params"></a>

[**SubscriptionDefinitionId**](parameters-subscriptiondefinitionidparam.md)
The ID of the subscription definition.
where used: path; required: true
type: string

[**CreateSubscriptionDefinitionVersionRequestBody**](parameters-createsubscriptiondefinitionversionrequestbody.md)

where used: body; required: true

```
{
"Subscriptions": [
  {
    "Id": "string",
    "Source": "string",
    "Subject": "string",
    "Target": "string"
  }
]
}
```
schema:
SubscriptionDefinitionVersion
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

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="createsubscriptiondefinitionversion-post-resp"></a>

**200** (CreateSubscriptionDefinitionVersionResponse)

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
