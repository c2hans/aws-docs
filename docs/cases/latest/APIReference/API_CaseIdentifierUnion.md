---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CaseIdentifierUnion.html
---

# CaseIdentifierUnion
<a name="API_connect-cases_CaseIdentifierUnion"></a>

Identifies a case by its case ID or its reference ID. Specify only one member.

## Contents
<a name="API_connect-cases_CaseIdentifierUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** caseId **   <a name="connect-Type-connect-cases_CaseIdentifierUnion-caseId"></a>
The unique identifier of the case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: No

 ** referenceId **   <a name="connect-Type-connect-cases_CaseIdentifierUnion-referenceId"></a>
The reference ID of the case. Reference IDs are unique within a domain, and uniqueness isn't case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: No

## See Also
<a name="API_connect-cases_CaseIdentifierUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseIdentifierUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseIdentifierUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseIdentifierUnion)
