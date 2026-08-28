---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_FindingSummary.html
---

# FindingSummary
<a name="API_FindingSummary"></a>

Contains summary information about a finding.

## Contents
<a name="API_FindingSummary_Contents"></a>

 ** description **   <a name="ngresiliencehub-Type-FindingSummary-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** failureCategory **   <a name="ngresiliencehub-Type-FindingSummary-failureCategory"></a>
The failure category of the finding.
Type: String
Valid Values: `SHARED_FATE | EXCESSIVE_LOAD | EXCESSIVE_LATENCY | MISCONFIGURATION_AND_BUGS | SINGLE_POINT_OF_FAILURE`
Required: No

 ** findingId **   <a name="ngresiliencehub-Type-FindingSummary-findingId"></a>
The unique identifier of the finding.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** name **   <a name="ngresiliencehub-Type-FindingSummary-name"></a>
The name of the finding.
Type: String
Required: No

 ** policyComponent **   <a name="ngresiliencehub-Type-FindingSummary-policyComponent"></a>
The policy component associated with the finding.
Type: String
Valid Values: `AVAILABILITY_SLO | MULTI_AZ_DISASTER_RECOVERY | MULTI_REGION_DISASTER_RECOVERY | DATA_RECOVERY`
Required: No

 ** serviceArn **   <a name="ngresiliencehub-Type-FindingSummary-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** severity **   <a name="ngresiliencehub-Type-FindingSummary-severity"></a>
The severity of the finding.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** status **   <a name="ngresiliencehub-Type-FindingSummary-status"></a>
The current status of the finding.
Type: String
Valid Values: `OPEN | RESOLVED | IRRELEVANT`
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-FindingSummary-updatedAt"></a>
The timestamp when the finding was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_FindingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/FindingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/FindingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/FindingSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
