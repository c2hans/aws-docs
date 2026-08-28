---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DisasterRecoverySource.html
---

# DisasterRecoverySource
<a name="API_DisasterRecoverySource"></a>

Contains the effective disaster recovery approach value for a service.

## Contents
<a name="API_DisasterRecoverySource_Contents"></a>

 ** policyName **   <a name="ngresiliencehub-Type-DisasterRecoverySource-policyName"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** source **   <a name="ngresiliencehub-Type-DisasterRecoverySource-source"></a>
Indicates whether the value comes from the service's own account or a cross-account policy.
Type: String
Valid Values: `SELF | CROSS_ACCOUNT`
Required: No

 ** value **   <a name="ngresiliencehub-Type-DisasterRecoverySource-value"></a>
The disaster recovery approach value.
Type: String
Required: No

## See Also
<a name="API_DisasterRecoverySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DisasterRecoverySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DisasterRecoverySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DisasterRecoverySource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
