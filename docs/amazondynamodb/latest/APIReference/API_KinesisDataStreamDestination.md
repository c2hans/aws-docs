---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KinesisDataStreamDestination.html
---

# KinesisDataStreamDestination
<a name="API_KinesisDataStreamDestination"></a>

Describes a Kinesis data stream destination.

## Contents
<a name="API_KinesisDataStreamDestination_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApproximateCreationDateTimePrecision **   <a name="DDB-Type-KinesisDataStreamDestination-ApproximateCreationDateTimePrecision"></a>
The precision of the Kinesis data stream timestamp. The values are either `MILLISECOND` or `MICROSECOND`.
Type: String
Valid Values: `MILLISECOND | MICROSECOND`
Required: No

 ** DestinationStatus **   <a name="DDB-Type-KinesisDataStreamDestination-DestinationStatus"></a>
The current status of replication.
Type: String
Valid Values: `ENABLING | ACTIVE | DISABLING | DISABLED | ENABLE_FAILED | UPDATING`
Required: No

 ** DestinationStatusDescription **   <a name="DDB-Type-KinesisDataStreamDestination-DestinationStatusDescription"></a>
The human-readable string that corresponds to the replica status.
Type: String
Required: No

 ** StreamArn **   <a name="DDB-Type-KinesisDataStreamDestination-StreamArn"></a>
The ARN for a specific Kinesis data stream.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

## See Also
<a name="API_KinesisDataStreamDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/KinesisDataStreamDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/KinesisDataStreamDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/KinesisDataStreamDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
