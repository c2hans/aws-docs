---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/doc-history.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Document history
<a name="doc-history"></a>

The following table describes the important changes to the documentation since the last release of Amazon Pinpoint.
+ **API version:** 2016-12-01 (latest)
+ **Latest documentation update:** April 4, 2024

| Change | API Version | Description | Date Changed |
| --- | --- | --- | --- |
| End of support notice | 2016-12-01 | **End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging. | May 20, 2025 |
| Changed feature | 2016-12-01 | Added support for email headers. | May 7, 2024 |
| Changed feature | 2016-12-01 | Updated the RawContent samples for push notifications. | April 4, 2024 |
| Changed feature | 2016-12-01 | Added support for Token Credentials when authenticating with GCM. | July 28, 2023 |
| Changed feature | 2016-12-01 | Added support for journey maximum number of messages that can be sent to an endpoint in a given timeframe. | June 26, 2023 |
| New feature | 2016-12-01 | Added support for journey run metrics. | April 25, 2023 |
| Changed feature | 2016-12-01 | Updated support for Tags in UpdateCampaign, UpdateSegment, UpdateEmailTemplate, UpdateInAppTemplate, UpdatePushTemplate, UpdateSmsTemplate and UpdateVoiceTemplate . | April 18, 2023 |
| New feature | 2016-12-01 | Added support for sending and validating OTP messages. | November 26, 2021 |
| New feature | 2016-12-01 | Added support for sending in-app messages. | November 1, 2021 |
| Changed feature | 2016-12-01 | Enhanced support for sending campaigns through custom channels: added CustomDeliveryConfiguration and CampaignCustomMessage objects; and, deprecated the Delivery value for the CampaignHook object, which was part of a public beta release. | April 23, 2020 |
| New sample | 2016-12-01 | Added examples of RawContent objects that contain sample data. | April 2, 2020 |
| New feature | 2016-12-01 | Added support for integrating recommender models with email, push notification, and SMS message templates. | March 4, 2020 |
| New sample | 2016-12-01 | Added an example of a JourneyResponse object that contains sample data. | January 20, 2020 |
| New feature | 2016-12-01 | Added versioning support for all types of message templates. | December 20, 2019 |
| New feature | 2016-12-01 | Added support for using and managing message templates for messages that are sent through the voice channel. Also added support for specifying default values for message variables in all types of message templates. | November 18, 2019 |
| New feature | 2016-12-01 | Added support for using and managing journeys, and querying analytics data for journeys. | October 31, 2019 |
| New feature | 2016-12-01 | Added support for using and managing message templates for messages that are sent through the email or SMS channel, or a push notification channel. | October 7, 2019 |
| New feature | 2016-12-01 | Added support for querying analytics data for a subset of metrics that apply to applications (projects) and campaigns. | July 24, 2019 |
| New feature | 2016-12-01 | Added support for deleting custom attributes from applications (projects). | May 15, 2019 |
| New feature | 2016-12-01 | Added support for tagging applications (projects), campaigns, and segments. | February 27, 2019 |
| New feature | 2016-12-01 | Added support for recording events and associating them with endpoints. | August 7, 2018 |
| Deprecated feature | 2016-12-01 | Removed the external ID key (ExternalId property) requirement for streaming events and importing endpoint definitions. | October 26, 2017 |
| New feature | 2016-12-01 | Added channels for the Amazon Device Messaging (ADM) and Baidu Cloud Push services. | September 27, 2017 |
| New feature | 2016-12-01 | Added support for streaming events to Amazon Data Firehose and Amazon Kinesis Data Streams. | March 24, 2017 |
| General availability | 2016-12-01 | This release introduces Amazon Pinpoint and the Amazon Pinpoint API. | December 1, 2016 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
