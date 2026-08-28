---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ComplianceDrift.html
---

# ComplianceDrift
<a name="API_ComplianceDrift"></a>

Indicates the compliance drifts (recovery time objective (RTO) and recovery point objective (RPO)) that were detected for an assessed entity.

## Contents
<a name="API_ComplianceDrift_Contents"></a>

 ** actualReferenceId **   <a name="resiliencehub-Type-ComplianceDrift-actualReferenceId"></a>
Assessment identifier that is associated with this drift item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** actualValue **   <a name="resiliencehub-Type-ComplianceDrift-actualValue"></a>
Actual compliance value of the entity.
Type: String to [DisruptionCompliance](API_DisruptionCompliance.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** appId **   <a name="resiliencehub-Type-ComplianceDrift-appId"></a>
Identifier of your application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** appVersion **   <a name="resiliencehub-Type-ComplianceDrift-appVersion"></a>
Published version of your application on which drift was detected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** diffType **   <a name="resiliencehub-Type-ComplianceDrift-diffType"></a>
Difference type between actual and expected recovery point objective (RPO) and recovery time objective (RTO) values. Currently, AWS Resilience Hub supports only `NotEqual` difference type.
Type: String
Valid Values: `NotEqual | Added | Removed`
Required: No

 ** driftType **   <a name="resiliencehub-Type-ComplianceDrift-driftType"></a>
The type of drift detected. Currently, AWS Resilience Hub supports only **ApplicationCompliance** drift type.
Type: String
Valid Values: `ApplicationCompliance | AppComponentResiliencyComplianceStatus`
Required: No

 ** entityId **   <a name="resiliencehub-Type-ComplianceDrift-entityId"></a>
Identifier of an entity in which drift was detected. For compliance drift, the entity ID can be either application ID or the AppComponent ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** entityType **   <a name="resiliencehub-Type-ComplianceDrift-entityType"></a>
The type of entity in which drift was detected. For compliance drifts, AWS Resilience Hub supports `AWS::ResilienceHub::AppComponent` and `AWS::ResilienceHub::Application`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** expectedReferenceId **   <a name="resiliencehub-Type-ComplianceDrift-expectedReferenceId"></a>
Assessment identifier of a previous assessment of the same application version. AWS Resilience Hub uses the previous assessment (associated with the reference identifier) to compare the compliance with the current assessment to identify drifts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** expectedValue **   <a name="resiliencehub-Type-ComplianceDrift-expectedValue"></a>
The expected compliance value of an entity.
Type: String to [DisruptionCompliance](API_DisruptionCompliance.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

## See Also
<a name="API_ComplianceDrift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ComplianceDrift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ComplianceDrift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ComplianceDrift)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
