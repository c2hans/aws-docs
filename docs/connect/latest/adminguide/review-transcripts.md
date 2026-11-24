---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/review-transcripts.html
---

# Review analyzed conversations using conversational analytics

By using Connect Customer conversational analytics, you can review the transcript and identify what part of the contact is of interest. You won't need to listen to an entire call or read an entire chat transcript to find out what's interesting about it. You can focus on specific parts of the audio or transcript. Both are highlighted for you wherever there are points of interest.

For example, you might scan the transcript of the contact and see a red sentiment emoji for a customer turn, which indicates the customer is expressing a negative sentiment. You can choose the timestamp and jump to that portion of audio recording or chat interaction.

The following image shows an example of a voice contact.

![An analysis of a voice contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-category-hit.png)

The following image shows an example of a chat contact. **System Message** applies to chat, where the participant might be a Lex bot or prompt.

![An analysis of a chat contact.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-category-hit-chat.png)

**To review analyzed conversations**

1. Log in to Connect Customer with a user account that has **Contact search** and **conversational analytics - conversational analytics** permissions in the security profile.

1. In Connect Customer, choose **Analytics and optimization**, **Contact search**.

1. Use the filters on the page to narrow your search for a contact. For date, you can search up to 14 days at a time. For more information about searching for contacts, see [Search for completed and in-progress contacts](contact-search.md).

1. Choose the contact ID to view the contact details for the contact.

1. In the **Recording** and **Transcript** sections of the **Contact details** page, review what was spoken or written, when, and their sentiment.

   If a contact has more than one language, the transcript shows each segment in its language. For post-call analytics, if the language of a segment doesn't support redaction, conversational analytics redacts the entire segment. The redacted transcript shows the language code of the segment, for example, `[Content Removed - ko-KR redaction is not supported]`.

   The following image shows the transcript of a contact with more than one language.
![The Recording and Transcript sections of the Contact details page for a contact with more than one language. The transcript shows one customer turn in English. Conversational analytics removed the content of two customer turns because their language doesn't support redaction.](https://docs.aws.amazon.com/connect/latest/adminguide/images/review-transcripts-multi-language-redaction.png)

1. For calls, if desired, choose the play prompt to listen to the recording. Or, choose the relevant part of the recording to listen to the portion you're interested in.

1. For chats, if desired, use the graph to navigate to the portion of the transcript you're interested in.
