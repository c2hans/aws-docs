---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_AgreementSummary.html
---

# AgreementSummary
<a name="API_AgreementSummary"></a>

Summary for agreement resource.

## Contents
<a name="API_AgreementSummary_Contents"></a>

 ** acceptanceTerms **   <a name="artifact-Type-AgreementSummary-acceptanceTerms"></a>
Terms required to accept the agreement resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** arn **   <a name="artifact-Type-AgreementSummary-arn"></a>
ARN of the agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** description **   <a name="artifact-Type-AgreementSummary-description"></a>
Description of the agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** id **   <a name="artifact-Type-AgreementSummary-id"></a>
Identifier of the agreement resource.
Type: String
Pattern: `agreement-[a-zA-Z0-9]{16}`
Required: No

 ** name **   <a name="artifact-Type-AgreementSummary-name"></a>
Name of the agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** revisionId **   <a name="artifact-Type-AgreementSummary-revisionId"></a>
Revision Id of the agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** subjects **   <a name="artifact-Type-AgreementSummary-subjects"></a>
Subjects of the agreement resource.
Type: Array of strings
Valid Values: `ACCOUNT | ORGANIZATION`
Required: No

 ** terminateTerms **   <a name="artifact-Type-AgreementSummary-terminateTerms"></a>
Terms required to terminate the agreement resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

## See Also
<a name="API_AgreementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/AgreementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/AgreementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/AgreementSummary)
