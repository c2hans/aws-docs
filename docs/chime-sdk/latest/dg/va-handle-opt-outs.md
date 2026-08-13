---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-handle-opt-outs.html
---

# Handling opt outs for speaker search for the Amazon Chime SDK
<a name="va-handle-opt-outs"></a>

You can handle opt outs for end users and entire organizations. Opting out has the following effects:
+ After you opt out, voice analytics will not use any new enrollment audio for model training, and it will not use any enrollment audio collected and stored prior to your opting out.
+ After you opt out, voice analytics will store and use enrollment audio in order to provide the speaker search service.

**Warning**
The following opt-out actions are irreversible. You can't recover deleted data.

**Handling end user opt-outs**
When end users want to opt out of speaker search, call the [DeleteVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceProfile.html) API. This action removes the voice profile, plus the voice embeddings and enrollment audio.

To delete a group of voice embeddings, call the [DeleteVoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceProfileDomain.html) API to remove the domain. This action deletes *all* the voice profiles in a domain.

**Handling opt-out at the organizational level**
To handle opt outs for an entire organization, use an AWS Organizations opt-out policy. Use the `chimesdkvoiceanalytics` service name. For information about the policies, see [ AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.

**Note**
To use an opt-out policy, your AWS accounts must be centrally managed by AWS Organizations. If you haven't already created an organization for your AWS accounts, see [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.
