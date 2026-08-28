---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Complaint.html
---

# Complaint
<a name="API_Complaint"></a>

Information about a `Complaint` event.

## Contents
<a name="API_Complaint_Contents"></a>

 ** ComplaintFeedbackType **   <a name="SES-Type-Complaint-ComplaintFeedbackType"></a>
 The value of the `Feedback-Type` field from the feedback report received from the ISP.
Type: String
Required: No

 ** ComplaintSubType **   <a name="SES-Type-Complaint-ComplaintSubType"></a>
 Can either be `null` or `OnAccountSuppressionList`. If the value is `OnAccountSuppressionList`, SES accepted the message, but didn't attempt to send it because it was on the account-level suppression list.
Type: String
Required: No

## See Also
<a name="API_Complaint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Complaint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Complaint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Complaint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
