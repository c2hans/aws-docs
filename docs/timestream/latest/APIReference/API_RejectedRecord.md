---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_RejectedRecord.html
---

# RejectedRecord
<a name="API_RejectedRecord"></a>

 Represents records that were not successfully inserted into Timestream due to data validation issues that must be resolved before reinserting time-series data into the system.

## Contents
<a name="API_RejectedRecord_Contents"></a>

 ** ExistingVersion **   <a name="timestream-Type-RejectedRecord-ExistingVersion"></a>
The existing version of the record. This value is populated in scenarios where an identical record exists with a higher version than the version in the write request.
Type: Long
Required: No

 ** Reason **   <a name="timestream-Type-RejectedRecord-Reason"></a>
 The reason why a record was not successfully inserted into Timestream. Possible causes of failure include:
+ Records with duplicate data where there are multiple records with the same dimensions, timestamps, and measure names but:
  + Measure values are different
  + Version is not present in the request, *or* the value of version in the new record is equal to or lower than the existing value

  If Timestream rejects data for this case, the `ExistingVersion` field in the `RejectedRecords` response will indicate the current record’s version. To force an update, you can resend the request with a version for the record set to a value greater than the `ExistingVersion`.
+  Records with timestamps that lie outside the retention duration of the memory store.
**Note**
When the retention window is updated, you will receive a `RejectedRecords` exception if you immediately try to ingest data within the new window. To avoid a `RejectedRecords` exception, wait until the duration of the new window to ingest new data. For further information, see [ Best Practices for Configuring Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices.html#configuration) and [the explanation of how storage works in Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html).
+  Records with dimensions or measures that exceed the Timestream defined limits.
 For more information, see [Access Management](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html) in the Timestream Developer Guide.
Type: String
Required: No

 ** RecordIndex **   <a name="timestream-Type-RejectedRecord-RecordIndex"></a>
 The index of the record in the input request for WriteRecords. Indexes begin with 0.
Type: Integer
Required: No

## See Also
<a name="API_RejectedRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/RejectedRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/RejectedRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/RejectedRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
