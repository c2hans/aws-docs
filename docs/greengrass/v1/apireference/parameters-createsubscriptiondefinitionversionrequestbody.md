---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-createsubscriptiondefinitionversionrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateSubscriptionDefinitionVersionRequestBody
<a name="parameters-createsubscriptiondefinitionversionrequestbody"></a>

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

CreateSubscriptionDefinitionVersionRequestBody
in: body
required: true
schema: [SubscriptionDefinitionVersion](definitions-subscriptiondefinitionversion.md)

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
