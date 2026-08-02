---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckDescription.html
---

# TrustedAdvisorCheckDescription
<a name="API_TrustedAdvisorCheckDescription"></a>

The description and metadata for a Trusted Advisor check.

## Contents
<a name="API_TrustedAdvisorCheckDescription_Contents"></a>

 ** category **   <a name="AWSSupport-Type-TrustedAdvisorCheckDescription-category"></a>
The category of the Trusted Advisor check.
Type: String

 ** description **   <a name="AWSSupport-Type-TrustedAdvisorCheckDescription-description"></a>
The description of the Trusted Advisor check, which includes the alert criteria and recommended operations (contains HTML markup).
Type: String

 ** id **   <a name="AWSSupport-Type-TrustedAdvisorCheckDescription-id"></a>
The unique identifier for the Trusted Advisor check.
Type: String

 ** metadata **   <a name="AWSSupport-Type-TrustedAdvisorCheckDescription-metadata"></a>
The column headings for the data returned by the Trusted Advisor check. The order of the headings corresponds to the order of the data in the **Metadata** element of the [TrustedAdvisorResourceDetail](API_TrustedAdvisorResourceDetail.md) for the check. **Metadata** contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.
Type: Array of strings

 ** name **   <a name="AWSSupport-Type-TrustedAdvisorCheckDescription-name"></a>
The display name for the Trusted Advisor check.
Type: String

## See Also
<a name="API_TrustedAdvisorCheckDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/TrustedAdvisorCheckDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/TrustedAdvisorCheckDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/TrustedAdvisorCheckDescription)
