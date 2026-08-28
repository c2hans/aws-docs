---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Service.html
---

# Service
<a name="API_Service"></a>

Represents a service in Resilience Hub. A service is the primary unit of resilience assessment.

## Contents
<a name="API_Service_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-Service-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-Service-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** accountId **   <a name="ngresiliencehub-Type-Service-accountId"></a>
The AWS account ID that owns the service.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** achievability **   <a name="ngresiliencehub-Type-Service-achievability"></a>
The achievability status of the service's resilience targets.
Type: [Achievability](API_Achievability.md) object
Required: No

 ** assessmentStatus **   <a name="ngresiliencehub-Type-Service-assessmentStatus"></a>
The current assessment status of the service.
Type: String
Valid Values: `NOT_STARTED | PENDING | IN_PROGRESS | FAILED | SUCCESS`
Required: No

 ** associatedSystems **   <a name="ngresiliencehub-Type-Service-associatedSystems"></a>
The systems associated with the service.
Type: Array of [AssociatedSystem](API_AssociatedSystem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** createdAt **   <a name="ngresiliencehub-Type-Service-createdAt"></a>
The timestamp when the service was created.
Type: Timestamp
Required: No

 ** dependencyDiscovery **   <a name="ngresiliencehub-Type-Service-dependencyDiscovery"></a>
The dependency discovery configuration for the service.
Type: [DependencyDiscoveryConfig](API_DependencyDiscoveryConfig.md) object
Required: No

 ** description **   <a name="ngresiliencehub-Type-Service-description"></a>
Resource description for services and policies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 615.
Required: No

 ** effectivePolicyValues **   <a name="ngresiliencehub-Type-Service-effectivePolicyValues"></a>
The effective policy values for the service.
Type: [EffectivePolicyValues](API_EffectivePolicyValues.md) object
Required: No

 ** estimatedAssessmentCost **   <a name="ngresiliencehub-Type-Service-estimatedAssessmentCost"></a>
The estimated cost of running an assessment on the service.
Type: [AssessmentCost](API_AssessmentCost.md) object
Required: No

 ** kmsKeyId **   <a name="ngresiliencehub-Type-Service-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** openFindingsCount **   <a name="ngresiliencehub-Type-Service-openFindingsCount"></a>
The number of open findings for the service.
Type: Integer
Required: No

 ** organizationId **   <a name="ngresiliencehub-Type-Service-organizationId"></a>
The AWS Organizations identifier for the service.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `o-[a-z0-9]{10,32}`
Required: No

 ** ouId **   <a name="ngresiliencehub-Type-Service-ouId"></a>
The organizational unit (OU) identifier for the service.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}`
Required: No

 ** permissionModel **   <a name="ngresiliencehub-Type-Service-permissionModel"></a>
The permission model for the service.
Type: [PermissionModel](API_PermissionModel.md) object
Required: No

 ** policyArn **   <a name="ngresiliencehub-Type-Service-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** regions **   <a name="ngresiliencehub-Type-Service-regions"></a>
The Regions where the service operates.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** reportConfiguration **   <a name="ngresiliencehub-Type-Service-reportConfiguration"></a>
Configuration for automatic report generation on a Service.
Type: [ServiceReportConfiguration](API_ServiceReportConfiguration.md) object
Required: No

 ** rerunAssessment **   <a name="ngresiliencehub-Type-Service-rerunAssessment"></a>
Indicates whether the assessment should be rerun.
Type: Boolean
Required: No

 ** resolvedFindingsCount **   <a name="ngresiliencehub-Type-Service-resolvedFindingsCount"></a>
The number of resolved findings for the service.
Type: Integer
Required: No

 ** resourceDiscovery **   <a name="ngresiliencehub-Type-Service-resourceDiscovery"></a>
The resource discovery status for the service.
Type: [ResourceDiscoveryStatus](API_ResourceDiscoveryStatus.md) object
Required: No

 ** tags **   <a name="ngresiliencehub-Type-Service-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-Service-updatedAt"></a>
The timestamp when the service was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
