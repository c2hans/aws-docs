---
source_url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom-create.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Assign a Lambda function or webhook to an individual campaign using the Amazon Pinpoint API
<a name="channels-custom-create"></a>

To assign a Lambda function or webhook to an individual campaign, use the Amazon Pinpoint API to create or update a [Campaign](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns.html) object.

The `MessageConfiguration` object in the campaign must also contain a `CustomMessage` object. This object has one member: `Data`. The value of `Data` is a JSON string that contains the message payload that you want to send to the custom channel.

The campaign has to contain a `CustomDeliveryConfiguration` object. Within the `CustomDeliveryConfiguration` object, specify the following:
+ `EndpointTypes` – An array that contains all of the endpoint types that the custom channel campaign should be sent to. It can contain any or all of the following channel types:
  + `ADM`
  + `APNS`
  + `APNS_SANDBOX`
  + `APNS_VOIP`
  + `APNS_VOIP_SANDBOX`
  + `BAIDU`
  + `CUSTOM`
  + `EMAIL`
  + `GCM`
  + `SMS`
  + `VOICE`
+ `DeliveryUri` – The destination that endpoints are sent to. You can specify only one of the following:
  + The URL of the webhook that you want to send endpoint data to when the campaign runs.
  + The Amazon Resource Name (ARN) of a Lambda function that you want to execute when the campaign runs.

**Note**
The `Campaign` object can also contain a `Hook` object. This object is only used to create segments that are customized by a Lambda function when a campaign is executed. For more information, see [Customize Amazon Pinpoint segments using an AWS Lambda function](segments-dynamic.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
