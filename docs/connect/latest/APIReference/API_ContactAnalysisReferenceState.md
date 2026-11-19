---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactAnalysisReferenceState.html
---

# ContactAnalysisReferenceState

The current processing state of conversational analytics for a contact, including the analysis status and, when applicable, the reason for that status.

## Contents
<a name="API_ContactAnalysisReferenceState_Contents"></a>

 ** Status **   <a name="connect-Type-ContactAnalysisReferenceState-Status"></a>
The status of conversational analytics processing for the contact. Valid values:
+  `REQUESTED` – Analysis has been requested for the contact and has not finished.
+  `COMPLETED` – Analysis finished successfully.
+  `FAILED` – Analysis did not finish successfully. See `StatusReason` for the cause.
Type: String
Required: No

 ** StatusReason **   <a name="connect-Type-ContactAnalysisReferenceState-StatusReason"></a>
The reason for the current analysis status. This value is populated only when the status is `FAILED`.
Type: String
Required: No

## See Also
<a name="API_ContactAnalysisReferenceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactAnalysisReferenceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactAnalysisReferenceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactAnalysisReferenceState)
