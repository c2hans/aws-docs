---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-voice-profile-domains.html
---

# Managing voice profile domains
<a name="manage-voice-profile-domains"></a>

Amazon Chime SDK speaker search creates *voice profiles*, vector maps of a caller's voice. A voice profile domain represents a collection of voice profiles. You must create a voice profile domain before developers can call the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_StartSpeakerSearchTask.html) API.

**Important**
The speaker search feature involves the creation of a voice embedding, which can be used to compare the voice of a caller against previously stored voice data. The collection, use, storage, and retention of biometric identifiers and biometric information in the form of a digital embedding may require the caller’s informed consent via a written release. Such consent is required under various state laws, including biometrics laws in Illinois, Texas, Washington and other state privacy laws. Before using the speaker search feature, you must provide all notices, and obtain all consents as required by applicable law, and under the [AWS service terms](https://aws.amazon.com/service-terms/) governing your use of the feature.
You must provide a written release to each caller through a process that clearly reflects each caller’s informed consent before using Amazon Chime SDK voice analytics service, as required under the terms of your agreement with AWS governing your use of the service.

The following topics explain how to create and manage voice profile domains.

**Topics**
+ [Creating voice profile domains](create-vp-domain.md)
+ [Editing voice profile domains](edit-vp-domain.md)
+ [Deleting voice profile domains](delete-vp-domain.md)
+ [Using tags with voice profile domains](vp-domain-tags.md)
+ [Understanding the voice analytics consent notice](va-consent-notice.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
