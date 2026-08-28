---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_FleetSummary.html
---

# FleetSummary
<a name="API_FleetSummary"></a>

The details of a fleet.

## Contents
<a name="API_FleetSummary_Contents"></a>

 ** configuration **   <a name="deadlinecloud-Type-FleetSummary-configuration"></a>
The configuration details for the fleet.
Type: [FleetConfiguration](API_FleetConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="deadlinecloud-Type-FleetSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-FleetSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** displayName **   <a name="deadlinecloud-Type-FleetSummary-displayName"></a>
The display name of the fleet summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-FleetSummary-farmId"></a>
The farm ID.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-FleetSummary-fleetId"></a>
The fleet ID.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** maxWorkerCount **   <a name="deadlinecloud-Type-FleetSummary-maxWorkerCount"></a>
The maximum number of workers specified in the fleet.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** minWorkerCount **   <a name="deadlinecloud-Type-FleetSummary-minWorkerCount"></a>
The minimum number of workers in the fleet.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** status **   <a name="deadlinecloud-Type-FleetSummary-status"></a>
The status of the fleet.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | SUSPENDED`
Required: Yes

 ** workerCount **   <a name="deadlinecloud-Type-FleetSummary-workerCount"></a>
The number of workers in the fleet summary.
Type: Integer
Required: Yes

 ** autoScalingStatus **   <a name="deadlinecloud-Type-FleetSummary-autoScalingStatus"></a>
The AWS Auto Scaling status of a fleet.
Type: String
Valid Values: `GROWING | STEADY | SHRINKING`
Required: No

 ** statusMessage **   <a name="deadlinecloud-Type-FleetSummary-statusMessage"></a>
A message that communicates a suspended status of the fleet.
Type: String
Required: No

 ** targetWorkerCount **   <a name="deadlinecloud-Type-FleetSummary-targetWorkerCount"></a>
The target number of workers in a fleet.
Type: Integer
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-FleetSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-FleetSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_FleetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
