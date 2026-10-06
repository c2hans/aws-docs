---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ScopeResult.html
---

# ScopeResult
<a name="API_ScopeResult"></a>

The outcome of scoping a CI/CD pentest job's code changes, including the decision and the reason for it.

## Contents
<a name="API_ScopeResult_Contents"></a>

 ** decision **   <a name="securityagent-Type-ScopeResult-decision"></a>
The scoping decision for the job's code changes.
Type: String
Valid Values: `IN_SCOPE | SCOPED_OUT | SCOPE_CONFLICT`
Required: Yes

 ** reason **   <a name="securityagent-Type-ScopeResult-reason"></a>
A human-readable explanation of the scoping decision.
Type: String
Required: Yes

## See Also
<a name="API_ScopeResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ScopeResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ScopeResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ScopeResult)
