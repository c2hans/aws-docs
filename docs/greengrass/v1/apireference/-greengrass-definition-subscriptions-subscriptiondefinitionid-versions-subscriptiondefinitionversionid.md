---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/subscriptions/SubscriptionDefinitionId/versions/SubscriptionDefinitionVersionId
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid"></a>

## GET
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid-get"></a>

 `GET /greengrass/definition/subscriptions/{{SubscriptionDefinitionId}}/versions/{{SubscriptionDefinitionVersionId}}`

Operation ID: [GetSubscriptionDefinitionVersion](getsubscriptiondefinitionversion-get.md)

Retrieves information about a subscription definition version.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid-get-path"></a>

[**SubscriptionDefinitionId**](parameters-subscriptiondefinitionidparam.md)
The ID of the subscription definition.
where used: path; required: true
type: string

[**SubscriptionDefinitionVersionId**](parameters-subscriptiondefinitionversionidparam.md)
The ID of the subscription definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListSubscriptionDefinitionVersions` requests. If the version is the last one that was associated with a subscription definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid-get-cli"></a>

```
aws greengrass get-subscription-definition-version \
  --subscription-definition-id <value> \
  --subscription-definition-version-id <value> \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"SubscriptionDefinitionId": "string",
"SubscriptionDefinitionVersionId": "string",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-definition-subscriptions-subscriptiondefinitionid-versions-subscriptiondefinitionversionid-get-responses"></a>

**200** (GetSubscriptionDefinitionVersionResponse)

 [ GetSubscriptionDefinitionVersionResponse](definitions-getsubscriptiondefinitionversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "Subscriptions": [
    {
      "Id": "string",
      "Source": "string",
      "Subject": "string",
      "Target": "string"
    }
  ]
},
"NextToken": "string"
}
```
GetSubscriptionDefinitionVersionResponse
Information about a subscription definition version.
type: object
Arn
The ARN of the subscription definition version.
type: string
Id
The ID of the subscription definition version.
type: string
Version
The version of the subscription definition version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the subscription definition version was created.
type: string
Definition
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
