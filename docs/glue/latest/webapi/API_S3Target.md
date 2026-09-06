---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3Target.html
---

# S3Target
<a name="API_S3Target"></a>

Specifies a data store in Amazon Simple Storage Service (Amazon S3).

## Contents
<a name="API_S3Target_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-S3Target-ConnectionName"></a>
The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).
Type: String
Required: No

 ** DlqEventQueueArn **   <a name="Glue-Type-S3Target-DlqEventQueueArn"></a>
A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue`.
Type: String
Required: No

 ** EventQueueArn **   <a name="Glue-Type-S3Target-EventQueueArn"></a>
A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs`.
Type: String
Required: No

 ** Exclusions **   <a name="Glue-Type-S3Target-Exclusions"></a>
A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
Type: Array of strings
Required: No

 ** Path **   <a name="Glue-Type-S3Target-Path"></a>
The path to the Amazon S3 target.
Type: String
Required: No

 ** SampleSize **   <a name="Glue-Type-S3Target-SampleSize"></a>
Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249.
Type: Integer
Required: No

## See Also
<a name="API_S3Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3Target)
