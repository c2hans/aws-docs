---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Finding.html
---

# Finding
<a name="API_Finding"></a>

Represents a resilience finding from a failure mode assessment.

## Contents
<a name="API_Finding_Contents"></a>

 ** comment **   <a name="ngresiliencehub-Type-Finding-comment"></a>
A user-provided comment about the finding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** description **   <a name="ngresiliencehub-Type-Finding-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** failureCategory **   <a name="ngresiliencehub-Type-Finding-failureCategory"></a>
The failure category of the finding.
Type: String
Valid Values: `SHARED_FATE | EXCESSIVE_LOAD | EXCESSIVE_LATENCY | MISCONFIGURATION_AND_BUGS | SINGLE_POINT_OF_FAILURE`
Required: No

 ** findingId **   <a name="ngresiliencehub-Type-Finding-findingId"></a>
The unique identifier of the finding.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** infrastructureAndCodeRecommendations **   <a name="ngresiliencehub-Type-Finding-infrastructureAndCodeRecommendations"></a>
Infrastructure and code recommendations to address the finding.
Type: Array of [InfrastructureAndCodeRecommendation](API_InfrastructureAndCodeRecommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** name **   <a name="ngresiliencehub-Type-Finding-name"></a>
The name of the finding.
Type: String
Required: No

 ** observabilityRecommendations **   <a name="ngresiliencehub-Type-Finding-observabilityRecommendations"></a>
Observability recommendations to address the finding.
Type: Array of [ObservabilityRecommendation](API_ObservabilityRecommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** policyComponent **   <a name="ngresiliencehub-Type-Finding-policyComponent"></a>
The policy component associated with the finding.
Type: String
Valid Values: `AVAILABILITY_SLO | MULTI_AZ_DISASTER_RECOVERY | MULTI_REGION_DISASTER_RECOVERY | DATA_RECOVERY`
Required: No

 ** reasoning **   <a name="ngresiliencehub-Type-Finding-reasoning"></a>
The reasoning behind the finding.
Type: String
Required: No

 ** serviceFunctions **   <a name="ngresiliencehub-Type-Finding-serviceFunctions"></a>
The service functions associated with the finding.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: No

 ** severity **   <a name="ngresiliencehub-Type-Finding-severity"></a>
The severity of the finding.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** status **   <a name="ngresiliencehub-Type-Finding-status"></a>
The current status of the finding.
Type: String
Valid Values: `OPEN | RESOLVED | IRRELEVANT`
Required: No

 ** testingRecommendations **   <a name="ngresiliencehub-Type-Finding-testingRecommendations"></a>
Testing recommendations to address the finding.
Type: Array of [TestingRecommendation](API_TestingRecommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-Finding-updatedAt"></a>
The timestamp when the finding was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Finding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Finding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Finding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
