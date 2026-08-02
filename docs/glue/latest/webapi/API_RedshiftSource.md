---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RedshiftSource.html
---

# RedshiftSource
<a name="API_RedshiftSource"></a>

Specifies an Amazon Redshift data store.

## Contents
<a name="API_RedshiftSource_Contents"></a>

 ** Database **   <a name="Glue-Type-RedshiftSource-Database"></a>
The database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-RedshiftSource-Name"></a>
The name of the Amazon Redshift data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-RedshiftSource-Table"></a>
The database table to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** RedshiftTmpDir **   <a name="Glue-Type-RedshiftSource-RedshiftTmpDir"></a>
The Amazon S3 path where temporary data can be staged when copying out of the database.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** TmpDirIAMRole **   <a name="Glue-Type-RedshiftSource-TmpDirIAMRole"></a>
The IAM role with permissions.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_RedshiftSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RedshiftSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RedshiftSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RedshiftSource)
