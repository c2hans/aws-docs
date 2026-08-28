---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceSummary.html
---

# ServiceSummary
<a name="API_ServiceSummary"></a>

Contains summary information about a service.

## Contents
<a name="API_ServiceSummary_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-ServiceSummary-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-ServiceSummary-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** accountId **   <a name="ngresiliencehub-Type-ServiceSummary-accountId"></a>
Displayed only if caller has access.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** achievability **   <a name="ngresiliencehub-Type-ServiceSummary-achievability"></a>
The achievability status of the service's resilience targets.
Type: [Achievability](API_Achievability.md) object
Required: No

 ** assessmentStatus **   <a name="ngresiliencehub-Type-ServiceSummary-assessmentStatus"></a>
The current assessment status of the service.
Type: String
Valid Values: `NOT_STARTED | PENDING | IN_PROGRESS | FAILED | SUCCESS`
Required: No

 ** associatedSystems **   <a name="ngresiliencehub-Type-ServiceSummary-associatedSystems"></a>
The systems associated with the service.
Type: Array of [AssociatedSystem](API_AssociatedSystem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** createdAt **   <a name="ngresiliencehub-Type-ServiceSummary-createdAt"></a>
The timestamp when the service was created.
Type: Timestamp
Required: No

 ** dependencyDiscovery **   <a name="ngresiliencehub-Type-ServiceSummary-dependencyDiscovery"></a>
The dependency discovery configuration.
Type: [DependencyDiscoveryConfig](API_DependencyDiscoveryConfig.md) object
Required: No

 ** openFindingsCount **   <a name="ngresiliencehub-Type-ServiceSummary-openFindingsCount"></a>
The number of open findings.
Type: Integer
Required: No

 ** organizationId **   <a name="ngresiliencehub-Type-ServiceSummary-organizationId"></a>
Displayed only if caller has access.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `o-[a-z0-9]{10,32}`
Required: No

 ** ouId **   <a name="ngresiliencehub-Type-ServiceSummary-ouId"></a>
Displayed only if caller has access.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}`
Required: No

 ** policyArn **   <a name="ngresiliencehub-Type-ServiceSummary-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** regions **   <a name="ngresiliencehub-Type-ServiceSummary-regions"></a>
The Regions where the service operates.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** resolvedFindingsCount **   <a name="ngresiliencehub-Type-ServiceSummary-resolvedFindingsCount"></a>
The number of resolved findings.
Type: Integer
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-ServiceSummary-updatedAt"></a>
The timestamp when the service was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
