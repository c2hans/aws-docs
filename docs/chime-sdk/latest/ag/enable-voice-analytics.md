---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/enable-voice-analytics.html
---

# Enabling voice analytics
<a name="enable-voice-analytics"></a>

**Important**
As a condition of using this feature, you acknowledge that the collection, use, storage, and retention of your caller’s biometric identifiers and biometric information (“biometric data”) in the form of a digital voice profile requires the caller’s informed consent via a written release. Such consent is required under various state laws, including biometrics laws in Illinois, Texas, Washington and other state privacy laws.
You must provide a written release to each caller through a process that clearly reflects each caller’s informed consent before using Amazon Chime SDK voice analytics service, as required under the terms of your agreement with AWS governing your use of the service.

**Note**
To enable voice analytics, you must have at least one Amazon Chime SDK Voice Connector and at least one Amazon Chime SDK call analytics configuration. For more information about creating Voice Connectors, see [Creating an Amazon Chime SDK Voice Connector](create-voicecon.md). For information about creating a call analytics configuration, see [Creating call analytics configurations](create-ca-config.md). For information about updating a configuration, see

The topics in this section explain how to enable Amazon Chime SDK voice analytics for Amazon Chime SDK Voice Connectors. Voice analytics uses machine learning to enable some or all of the following:
+ **Speaker search** – Converts a caller's voice into a vector *embedding*. It then compares the embedding to a database of known voice embeddings. If it finds a match or matches, it returns a ranked list of high-likelihood voice profile ID matches, along with a corresponding set of confidence scores.
**Note**
Speaker search is not designed for authentication or identity verification use cases, such as verifying the identity of a speaker with extremely high accuracy.
+ **Voice tone analysis** – Predicts the sentiment expressed in a speech signal based on a combined analysis of linguistic and tonal information.
**Note**
As a reminder, you must comply with all legal requirements when using voice tone analysis. This includes obtaining consent from the speaker as required by law, and not using the feature to make decisions about the speaker that would produce legal or similarly significant impacts, such as employment, housing, credit worthiness, or financial offers.

To enable voice analytics, administrators use the Amazon Chime SDK console to do the following:
+ Configure Voice Connectors to use one or more of the features listed above.
+ Create notification targets. Notification targets asynchronously receive voice analysis events, and you must have at least one target.
+ Create voice profile domains. Voice profile domains contain sets of *voice profiles*. In turn, a voice profile consists of a vector embedding of a caller's voice, plus a unique ID. By default, you can create 3 voice profile domains, and each domain can house 20,000 voice profiles. You can request an increase for both limits as needed.

Developers can use a set of APIs to do those same tasks. For more information, see [Using the Amazon Chime SDK PSTN voice analytics service](https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html), in the *Amazon Chime SDK Developer guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
