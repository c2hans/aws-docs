---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SourceDescription.html
---

# SourceDescription
<a name="API_SourceDescription"></a>

Details about a Kinesis data stream used as the source for a Firehose stream.

## Contents
<a name="API_SourceDescription_Contents"></a>

 ** DatabaseSourceDescription **   <a name="Firehose-Type-SourceDescription-DatabaseSourceDescription"></a>
Details about a database used as the source for a Firehose stream.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseSourceDescription](API_DatabaseSourceDescription.md) object
Required: No

 ** DirectPutSourceDescription **   <a name="Firehose-Type-SourceDescription-DirectPutSourceDescription"></a>
Details about Direct PUT used as the source for a Firehose stream.
Type: [DirectPutSourceDescription](API_DirectPutSourceDescription.md) object
Required: No

 ** KinesisStreamSourceDescription **   <a name="Firehose-Type-SourceDescription-KinesisStreamSourceDescription"></a>
The [KinesisStreamSourceDescription](API_KinesisStreamSourceDescription.md) value for the source Kinesis data stream.
Type: [KinesisStreamSourceDescription](API_KinesisStreamSourceDescription.md) object
Required: No

 ** MSKSourceDescription **   <a name="Firehose-Type-SourceDescription-MSKSourceDescription"></a>
The configuration description for the Amazon MSK cluster to be used as the source for a delivery stream.
Type: [MSKSourceDescription](API_MSKSourceDescription.md) object
Required: No

## See Also
<a name="API_SourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SourceDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
