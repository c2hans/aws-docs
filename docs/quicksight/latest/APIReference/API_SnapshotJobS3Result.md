---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotJobS3Result.html
---

# SnapshotJobS3Result
<a name="API_SnapshotJobS3Result"></a>

The Amazon S3 result from the snapshot job. The result includes the `DestinationConfiguration` and the Amazon S3 Uri. If an error occured during the job, the result returns information on the error.

## Contents
<a name="API_SnapshotJobS3Result_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorInfo **   <a name="QS-Type-SnapshotJobS3Result-ErrorInfo"></a>
An array of error records that describe any failures that occur while the dashboard snapshot job runs.
Type: Array of [SnapshotJobResultErrorInfo](API_SnapshotJobResultErrorInfo.md) objects
Required: No

 ** S3DestinationConfiguration **   <a name="QS-Type-SnapshotJobS3Result-S3DestinationConfiguration"></a>
A list of Amazon S3 bucket configurations that are provided when you make a `StartDashboardSnapshotJob` API call.
Type: [SnapshotS3DestinationConfiguration](API_SnapshotS3DestinationConfiguration.md) object
Required: No

 ** S3Uri **   <a name="QS-Type-SnapshotJobS3Result-S3Uri"></a>
The Amazon S3 Uri.
Type: String
Pattern: `^(https|s3)://([^/]+)/?(.*)$`
Required: No

## See Also
<a name="API_SnapshotJobS3Result_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotJobS3Result)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotJobS3Result)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotJobS3Result)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
