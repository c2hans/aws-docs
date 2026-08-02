---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogTarget.html
---

# CatalogTarget
<a name="API_CatalogTarget"></a>

Specifies an AWS Glue Data Catalog target.

## Contents
<a name="API_CatalogTarget_Contents"></a>

 ** DatabaseName **   <a name="Glue-Type-CatalogTarget-DatabaseName"></a>
The name of the database to be synchronized.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Tables **   <a name="Glue-Type-CatalogTarget-Tables"></a>
A list of the tables to be synchronized.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** ConnectionName **   <a name="Glue-Type-CatalogTarget-ConnectionName"></a>
The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a `Catalog` connection type paired with a `NETWORK` Connection type.
Type: String
Required: No

 ** DlqEventQueueArn **   <a name="Glue-Type-CatalogTarget-DlqEventQueueArn"></a>
A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue`.
Type: String
Required: No

 ** EventQueueArn **   <a name="Glue-Type-CatalogTarget-EventQueueArn"></a>
A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs`.
Type: String
Required: No

## See Also
<a name="API_CatalogTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogTarget)
