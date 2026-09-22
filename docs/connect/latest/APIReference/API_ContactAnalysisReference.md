---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactAnalysisReference.html
---

# ContactAnalysisReference
<a name="API_ContactAnalysisReference"></a>

Information about a reference when the `referenceType` is `CONTACT_ANALYSIS`. Otherwise, null.

## Contents
<a name="API_ContactAnalysisReference_Contents"></a>

 ** AnalyticsMode **   <a name="connect-Type-ContactAnalysisReference-AnalyticsMode"></a>
The analytics mode of the contact analysis.
Type: String
Valid Values: `PostContact | RealTime | ContactLens | AutomatedInteraction`
Required: No

 ** Arn **   <a name="connect-Type-ContactAnalysisReference-Arn"></a>
The Amazon Resource Name (ARN) of the contact analysis reference.
Type: String
Required: No

 ** IsRedacted **   <a name="connect-Type-ContactAnalysisReference-IsRedacted"></a>
Indicates whether sensitive data has been redacted from the contact analysis.
Type: Boolean
Required: No

 ** Name **   <a name="connect-Type-ContactAnalysisReference-Name"></a>
Identifier of the contact analysis reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Status **   <a name="connect-Type-ContactAnalysisReference-Status"></a>
Status of the contact analysis reference type.
Type: String
Valid Values: `AVAILABLE | DELETED | APPROVED | REJECTED | PROCESSING | FAILED`
Required: No

 ** Value **   <a name="connect-Type-ContactAnalysisReference-Value"></a>
The location path of the contact analysis reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_ContactAnalysisReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactAnalysisReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactAnalysisReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactAnalysisReference)
