---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CaseIdentifier.html
---

# CaseIdentifier
<a name="API_connect-cases_CaseIdentifier"></a>

The identifiers of a case that a batch operation returns.

## Contents
<a name="API_connect-cases_CaseIdentifier_Contents"></a>

 ** caseId **   <a name="connect-Type-connect-cases_CaseIdentifier-caseId"></a>
The unique identifier of the case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: No

 ** referenceId **   <a name="connect-Type-connect-cases_CaseIdentifier-referenceId"></a>
The reference ID of the case. Cases created before reference IDs were available don't have one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: No

 ** referenceNumber **   <a name="connect-Type-connect-cases_CaseIdentifier-referenceNumber"></a>
The reference number of the case. Reference numbers aren't guaranteed to be unique. `BatchUpdateCase` and `BatchCreateRelatedItem` don't return this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: No

## See Also
<a name="API_connect-cases_CaseIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseIdentifier)
