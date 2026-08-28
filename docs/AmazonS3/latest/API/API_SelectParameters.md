---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectParameters.html
---

# SelectParameters
<a name="API_SelectParameters"></a>

**Important**
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Describes the parameters for Select job types.

Learn [How to optimize querying your data in Amazon S3](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/) using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), [S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html), or client-side filtering.

## Contents
<a name="API_SelectParameters_Contents"></a>

 ** Expression **   <a name="AmazonS3-Type-SelectParameters-Expression"></a>
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)
The expression that is used to query the object.
Type: String
Required: Yes

 ** ExpressionType **   <a name="AmazonS3-Type-SelectParameters-ExpressionType"></a>
The type of the provided expression (for example, SQL).
Type: String
Valid Values: `SQL`
Required: Yes

 ** InputSerialization **   <a name="AmazonS3-Type-SelectParameters-InputSerialization"></a>
Describes the serialization format of the object.
Type: [InputSerialization](API_InputSerialization.md) data type
Required: Yes

 ** OutputSerialization **   <a name="AmazonS3-Type-SelectParameters-OutputSerialization"></a>
Describes how the results of the Select job are serialized.
Type: [OutputSerialization](API_OutputSerialization.md) data type
Required: Yes

## See Also
<a name="API_SelectParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SelectParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SelectParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SelectParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
