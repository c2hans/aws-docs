---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_OnFailure.html
---

# OnFailure
<a name="API_OnFailure"></a>

A destination for events that failed processing. For more information, see [Adding a destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations).

## Contents
<a name="API_OnFailure_Contents"></a>

 ** Destination **   <a name="lambda-Type-OnFailure-Destination"></a>
The Amazon Resource Name (ARN) of the destination resource.
To retain records of failed invocations from [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html), [DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html), [self-managed Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/kafka-on-failure.html), or [Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/kafka-on-failure.html), you can configure an Amazon SNS topic, Amazon SQS queue, Amazon S3 bucket, or Kafka topic as the destination.
Amazon SNS destinations have a message size limit of 256 KB. If the combined size of the function request and response payload exceeds the limit, Lambda will drop the payload when sending `OnFailure` event to the destination. For details on this behavior, refer to [Retaining records of asynchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html).
To retain records of failed invocations from [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html), [DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html), [self-managed Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-smaa-onfailure-destination) or [Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-onfailure-destination), you can configure an Amazon SNS topic, Amazon SQS queue, or Amazon S3 bucket as the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `$|kafka://([^.]([a-zA-Z0-9\-_.]{0,248}))|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

## See Also
<a name="API_OnFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/OnFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/OnFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/OnFailure)
