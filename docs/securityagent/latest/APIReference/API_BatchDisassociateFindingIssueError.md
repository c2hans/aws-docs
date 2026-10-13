---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchDisassociateFindingIssueError.html
---

# BatchDisassociateFindingIssueError
<a name="API_BatchDisassociateFindingIssueError"></a>

A finding that failed to disassociate, with the cause of the failure.

## Contents
<a name="API_BatchDisassociateFindingIssueError_Contents"></a>

 ** code **   <a name="securityagent-Type-BatchDisassociateFindingIssueError-code"></a>
The machine-readable failure category.
Type: String
Valid Values: `CLIENT_ERROR | INTERNAL_ERROR | STOPPED_BY_USER`
Required: Yes

 ** findingId **   <a name="securityagent-Type-BatchDisassociateFindingIssueError-findingId"></a>
The identifier of the finding that failed to disassociate.
Type: String
Required: Yes

 ** message **   <a name="securityagent-Type-BatchDisassociateFindingIssueError-message"></a>
A customer-facing explanation of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: Yes

## See Also
<a name="API_BatchDisassociateFindingIssueError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchDisassociateFindingIssueError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchDisassociateFindingIssueError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchDisassociateFindingIssueError)
