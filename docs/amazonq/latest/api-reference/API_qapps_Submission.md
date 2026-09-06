---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_Submission.html
---

# Submission
<a name="API_qapps_Submission"></a>

A record created when a user submits a form card.

## Contents
<a name="API_qapps_Submission_Contents"></a>

 ** submissionId **   <a name="qbusiness-Type-qapps_Submission-submissionId"></a>
The unique identifier of the submission.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

 ** timestamp **   <a name="qbusiness-Type-qapps_Submission-timestamp"></a>
The date and time when the card is submitted.
Type: Timestamp
Required: No

 ** value **   <a name="qbusiness-Type-qapps_Submission-value"></a>
The data submitted by the user.
Type: JSON value
Required: No

## See Also
<a name="API_qapps_Submission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/Submission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/Submission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/Submission)
