---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_TargetDomainSummary.html
---

# TargetDomainSummary
<a name="API_TargetDomainSummary"></a>

Contains summary information about a target domain.

## Contents
<a name="API_TargetDomainSummary_Contents"></a>

 ** domainName **   <a name="securityagent-Type-TargetDomainSummary-domainName"></a>
The domain name of the target domain.
Type: String
Required: Yes

 ** targetDomainId **   <a name="securityagent-Type-TargetDomainSummary-targetDomainId"></a>
The unique identifier of the target domain.
Type: String
Required: Yes

 ** verificationStatus **   <a name="securityagent-Type-TargetDomainSummary-verificationStatus"></a>
The current verification status of the target domain.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED | UNREACHABLE`
Required: No

## See Also
<a name="API_TargetDomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/TargetDomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/TargetDomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/TargetDomainSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
