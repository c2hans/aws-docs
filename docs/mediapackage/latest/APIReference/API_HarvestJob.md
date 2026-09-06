---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_HarvestJob.html
---

# HarvestJob
<a name="API_HarvestJob"></a>

Represents a harvest job resource in MediaPackage v2, which is used to export content from an origin endpoint to an S3 bucket.

## Contents
<a name="API_HarvestJob_Contents"></a>

 ** Arn **   <a name="mediapackage-Type-HarvestJob-Arn"></a>
The Amazon Resource Name (ARN) of the harvest job.
Type: String
Required: Yes

 ** ChannelGroupName **   <a name="mediapackage-Type-HarvestJob-ChannelGroupName"></a>
The name of the channel group containing the channel associated with this harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ChannelName **   <a name="mediapackage-Type-HarvestJob-ChannelName"></a>
The name of the channel associated with this harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** CreatedAt **   <a name="mediapackage-Type-HarvestJob-CreatedAt"></a>
The date and time when the harvest job was created.
Type: Timestamp
Required: Yes

 ** Destination **   <a name="mediapackage-Type-HarvestJob-Destination"></a>
The S3 destination where the harvested content will be placed.
Type: [Destination](API_Destination.md) object
Required: Yes

 ** HarvestedManifests **   <a name="mediapackage-Type-HarvestJob-HarvestedManifests"></a>
A list of manifests that are being or have been harvested.
Type: [HarvestedManifests](API_HarvestedManifests.md) object
Required: Yes

 ** HarvestJobName **   <a name="mediapackage-Type-HarvestJob-HarvestJobName"></a>
The name of the harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ModifiedAt **   <a name="mediapackage-Type-HarvestJob-ModifiedAt"></a>
The date and time when the harvest job was last modified.
Type: Timestamp
Required: Yes

 ** OriginEndpointName **   <a name="mediapackage-Type-HarvestJob-OriginEndpointName"></a>
The name of the origin endpoint associated with this harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ScheduleConfiguration **   <a name="mediapackage-Type-HarvestJob-ScheduleConfiguration"></a>
The configuration for when the harvest job is scheduled to run.
Type: [HarvesterScheduleConfiguration](API_HarvesterScheduleConfiguration.md) object
Required: Yes

 ** Status **   <a name="mediapackage-Type-HarvestJob-Status"></a>
The current status of the harvest job (e.g., QUEUED, IN\_PROGRESS, CANCELLED, COMPLETED, FAILED).
Type: String
Valid Values: `QUEUED | IN_PROGRESS | CANCELLED | COMPLETED | FAILED`
Required: Yes

 ** Description **   <a name="mediapackage-Type-HarvestJob-Description"></a>
An optional description of the harvest job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ErrorMessage **   <a name="mediapackage-Type-HarvestJob-ErrorMessage"></a>
An error message if the harvest job encountered any issues.
Type: String
Required: No

 ** ETag **   <a name="mediapackage-Type-HarvestJob-ETag"></a>
The current version of the harvest job. Used for concurrency control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_HarvestJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/HarvestJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/HarvestJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/HarvestJob)
