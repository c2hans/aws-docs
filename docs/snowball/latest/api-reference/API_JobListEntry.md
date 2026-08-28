---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobListEntry.html
---

# JobListEntry
<a name="API_JobListEntry"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Each `JobListEntry` object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of an export job.

## Contents
<a name="API_JobListEntry_Contents"></a>

 ** CreationDate **   <a name="Snowball-Type-JobListEntry-CreationDate"></a>
The creation date for this job.
Type: Timestamp
Required: No

 ** Description **   <a name="Snowball-Type-JobListEntry-Description"></a>
The optional description of this specific job, for example `Important Photos 2016-08-11`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** IsMaster **   <a name="Snowball-Type-JobListEntry-IsMaster"></a>
A value that indicates that this job is a main job. A main job represents a successful request to create an export job. Main jobs aren't associated with any Snowballs. Instead, each main job will have at least one job part, and each job part is associated with a Snowball. It might take some time before the job parts associated with a particular main job are listed, because they are created after the main job is created.
Type: Boolean
Required: No

 ** JobId **   <a name="Snowball-Type-JobListEntry-JobId"></a>
The automatically generated ID for a job, for example `JID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** JobState **   <a name="Snowball-Type-JobListEntry-JobState"></a>
The current state of this job.
Type: String
Valid Values: `New | PreparingAppliance | PreparingShipment | InTransitToCustomer | WithCustomer | InTransitToAWS | WithAWSSortingFacility | WithAWS | InProgress | Complete | Cancelled | Listing | Pending`
Required: No

 ** JobType **   <a name="Snowball-Type-JobListEntry-JobType"></a>
The type of job.
Type: String
Valid Values: `IMPORT | EXPORT | LOCAL_USE`
Required: No

 ** SnowballType **   <a name="Snowball-Type-JobListEntry-SnowballType"></a>
The type of device used with this job.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: No

## See Also
<a name="API_JobListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/JobListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/JobListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/JobListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
