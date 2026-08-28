---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_IngestionStatus.html
---

# IngestionStatus
<a name="API_IngestionStatus"></a>

A table showing information about the most recent successful and failed attempts to ingest events.

## Contents
<a name="API_IngestionStatus_Contents"></a>

 ** LatestIngestionAttemptEventID **   <a name="awscloudtrail-Type-IngestionStatus-LatestIngestionAttemptEventID"></a>
The event ID of the most recent attempt to ingest events.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9\-]+$`
Required: No

 ** LatestIngestionAttemptTime **   <a name="awscloudtrail-Type-IngestionStatus-LatestIngestionAttemptTime"></a>
The time stamp of the most recent attempt to ingest events on the channel.
Type: Timestamp
Required: No

 ** LatestIngestionErrorCode **   <a name="awscloudtrail-Type-IngestionStatus-LatestIngestionErrorCode"></a>
The error code for the most recent failure to ingest events.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** LatestIngestionSuccessEventID **   <a name="awscloudtrail-Type-IngestionStatus-LatestIngestionSuccessEventID"></a>
The event ID of the most recent successful ingestion of events.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9\-]+$`
Required: No

 ** LatestIngestionSuccessTime **   <a name="awscloudtrail-Type-IngestionStatus-LatestIngestionSuccessTime"></a>
The time stamp of the most recent successful ingestion of events for the channel.
Type: Timestamp
Required: No

## See Also
<a name="API_IngestionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/IngestionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/IngestionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/IngestionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
