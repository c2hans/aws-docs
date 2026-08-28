---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContentEventStream.html
---

# SelectObjectContentEventStream
<a name="API_SelectObjectContentEventStream"></a>

The container for selecting objects from a content event stream.

## Contents
<a name="API_SelectObjectContentEventStream_Contents"></a>

 ** Cont **   <a name="AmazonS3-Type-SelectObjectContentEventStream-Cont"></a>
The Continuation Event.
Type: [ContinuationEvent](API_ContinuationEvent.md) data type
Required: No

 ** End **   <a name="AmazonS3-Type-SelectObjectContentEventStream-End"></a>
The End Event.
Type: [EndEvent](API_EndEvent.md) data type
Required: No

 ** Progress **   <a name="AmazonS3-Type-SelectObjectContentEventStream-Progress"></a>
The Progress Event.
Type: [ProgressEvent](API_ProgressEvent.md) data type
Required: No

 ** Records **   <a name="AmazonS3-Type-SelectObjectContentEventStream-Records"></a>
The Records Event.
Type: [RecordsEvent](API_RecordsEvent.md) data type
Required: No

 ** Stats **   <a name="AmazonS3-Type-SelectObjectContentEventStream-Stats"></a>
The Stats Event.
Type: [StatsEvent](API_StatsEvent.md) data type
Required: No

## See Also
<a name="API_SelectObjectContentEventStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SelectObjectContentEventStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SelectObjectContentEventStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SelectObjectContentEventStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
