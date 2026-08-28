---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_FailedRemediationExceptionBatch.html
---

# FailedRemediationExceptionBatch
<a name="API_FailedRemediationExceptionBatch"></a>

List of each of the failed remediation exceptions with specific reasons.

## Contents
<a name="API_FailedRemediationExceptionBatch_Contents"></a>

 ** FailedItems **   <a name="config-Type-FailedRemediationExceptionBatch-FailedItems"></a>
Returns remediation exception resource key object of the failed items.
Type: Array of [RemediationException](API_RemediationException.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** FailureMessage **   <a name="config-Type-FailedRemediationExceptionBatch-FailureMessage"></a>
Returns a failure message. For example, the auto-remediation has failed.
Type: String
Required: No

## See Also
<a name="API_FailedRemediationExceptionBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/FailedRemediationExceptionBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/FailedRemediationExceptionBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/FailedRemediationExceptionBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
