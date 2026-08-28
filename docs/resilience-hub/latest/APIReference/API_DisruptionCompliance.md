---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DisruptionCompliance.html
---

# DisruptionCompliance
<a name="API_DisruptionCompliance"></a>

Defines the compliance against the resiliency policy for a disruption.

## Contents
<a name="API_DisruptionCompliance_Contents"></a>

 ** complianceStatus **   <a name="resiliencehub-Type-DisruptionCompliance-complianceStatus"></a>
The current status of compliance for the resiliency policy.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotApplicable | MissingPolicy`
Required: Yes

 ** achievableRpoInSecs **   <a name="resiliencehub-Type-DisruptionCompliance-achievableRpoInSecs"></a>
The Recovery Point Objective (RPO) that is achievable, in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** achievableRtoInSecs **   <a name="resiliencehub-Type-DisruptionCompliance-achievableRtoInSecs"></a>
The Recovery Time Objective (RTO) that is achievable, in seconds
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** currentRpoInSecs **   <a name="resiliencehub-Type-DisruptionCompliance-currentRpoInSecs"></a>
The current RPO, in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** currentRtoInSecs **   <a name="resiliencehub-Type-DisruptionCompliance-currentRtoInSecs"></a>
The current RTO, in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** message **   <a name="resiliencehub-Type-DisruptionCompliance-message"></a>
The disruption compliance message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** rpoDescription **   <a name="resiliencehub-Type-DisruptionCompliance-rpoDescription"></a>
The RPO description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** rpoReferenceId **   <a name="resiliencehub-Type-DisruptionCompliance-rpoReferenceId"></a>
Reference identifier of the RPO .
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** rtoDescription **   <a name="resiliencehub-Type-DisruptionCompliance-rtoDescription"></a>
The RTO description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** rtoReferenceId **   <a name="resiliencehub-Type-DisruptionCompliance-rtoReferenceId"></a>
Reference identifier of the RTO.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_DisruptionCompliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/DisruptionCompliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/DisruptionCompliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/DisruptionCompliance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
