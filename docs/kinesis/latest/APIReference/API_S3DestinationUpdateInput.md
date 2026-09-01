---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3DestinationUpdateInput.html
---

# S3DestinationUpdateInput
<a name="API_S3DestinationUpdateInput"></a>

The updated configuration for a general purpose Amazon S3 destination. Used in [UpdateChannel](API_UpdateChannel.md). Only `DataFreshnessInSeconds` can be updated.

## Contents
<a name="API_S3DestinationUpdateInput_Contents"></a>

 ** DataFreshnessInSeconds **   <a name="Streams-Type-S3DestinationUpdateInput-DataFreshnessInSeconds"></a>
The maximum age, in seconds, of undelivered data before the channel delivers it to the destination.
Type: Integer
Required: Yes

## See Also
<a name="API_S3DestinationUpdateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3DestinationUpdateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3DestinationUpdateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3DestinationUpdateInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
