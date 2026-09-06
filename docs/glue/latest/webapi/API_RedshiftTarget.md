---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RedshiftTarget.html
---

# RedshiftTarget
<a name="API_RedshiftTarget"></a>

Specifies a target that uses Amazon Redshift.

## Contents
<a name="API_RedshiftTarget_Contents"></a>

 ** Database **   <a name="Glue-Type-RedshiftTarget-Database"></a>
The name of the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-RedshiftTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-RedshiftTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-RedshiftTarget-Table"></a>
The name of the table in the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** RedshiftTmpDir **   <a name="Glue-Type-RedshiftTarget-RedshiftTmpDir"></a>
The Amazon S3 path where temporary data can be staged when copying out of the database.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** TmpDirIAMRole **   <a name="Glue-Type-RedshiftTarget-TmpDirIAMRole"></a>
The IAM role with permissions.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** UpsertRedshiftOptions **   <a name="Glue-Type-RedshiftTarget-UpsertRedshiftOptions"></a>
The set of options to configure an upsert operation when writing to a Redshift target.
Type: [UpsertRedshiftTargetOptions](API_UpsertRedshiftTargetOptions.md) object
Required: No

## See Also
<a name="API_RedshiftTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RedshiftTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RedshiftTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RedshiftTarget)
