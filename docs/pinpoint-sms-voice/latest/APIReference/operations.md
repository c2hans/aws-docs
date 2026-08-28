---
source_url: https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/operations.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Operations
<a name="operations"></a>

The Amazon Pinpoint SMS and Voice REST API includes the following operations.
+ [CreateConfigurationSet](v1-sms-voice-configuration-sets.md#CreateConfigurationSet)

  Creates a new configuration set. After you create the configuration set, you can add one or more event destinations to it.
+ [CreateConfigurationSetEventDestination](v1-sms-voice-configuration-sets-configurationsetname-event-destinations.md#CreateConfigurationSetEventDestination)

  Creates a new event destination in a configuration set.
+ [DeleteConfigurationSet](v1-sms-voice-configuration-sets-configurationsetname.md#DeleteConfigurationSet)

  Deletes an existing configuration set.
+ [DeleteConfigurationSetEventDestination](v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.md#DeleteConfigurationSetEventDestination)

  Deletes an event destination from a configuration set.
+ [GetConfigurationSetEventDestinations](v1-sms-voice-configuration-sets-configurationsetname-event-destinations.md#GetConfigurationSetEventDestinations)

  Retrieves information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination.
+ [ListConfigurationSets](v1-sms-voice-configuration-sets.md#ListConfigurationSets)

  Retrieves a list of configuration sets that are associated with your account in the current AWS Region.
+ [SendVoiceMessage](v1-sms-voice-voice-message.md#SendVoiceMessage)

  Creates a new voice message and sends it to a recipient's phone number.
+ [UpdateConfigurationSetEventDestination](v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.md#UpdateConfigurationSetEventDestination)

  Updates an event destination in a configuration set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint SMS and Voice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
