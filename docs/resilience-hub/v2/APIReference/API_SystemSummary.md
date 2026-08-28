---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SystemSummary.html
---

# SystemSummary
<a name="API_SystemSummary"></a>

Contains summary information about a system.

## Contents
<a name="API_SystemSummary_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-SystemSummary-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** systemId **   <a name="ngresiliencehub-Type-SystemSummary-systemId"></a>
System ID for cross-account use without exposing account structure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-SystemSummary-createdAt"></a>
The timestamp when the system was created.
Type: Timestamp
Required: No

 ** organizationId **   <a name="ngresiliencehub-Type-SystemSummary-organizationId"></a>
Displayed only if caller has access.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `o-[a-z0-9]{10,32}`
Required: No

 ** ouId **   <a name="ngresiliencehub-Type-SystemSummary-ouId"></a>
Displayed only if caller has access.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}`
Required: No

 ** servicesCount **   <a name="ngresiliencehub-Type-SystemSummary-servicesCount"></a>
The number of services in the system.
Type: Integer
Required: No

 ** systemArn **   <a name="ngresiliencehub-Type-SystemSummary-systemArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-SystemSummary-updatedAt"></a>
The timestamp when the system was last updated.
Type: Timestamp
Required: No

 ** userJourneysCount **   <a name="ngresiliencehub-Type-SystemSummary-userJourneysCount"></a>
The number of user journeys in the system.
Type: Integer
Required: No

## See Also
<a name="API_SystemSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SystemSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SystemSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SystemSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
