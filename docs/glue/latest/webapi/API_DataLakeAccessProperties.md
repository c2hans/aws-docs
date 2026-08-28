---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataLakeAccessProperties.html
---

# DataLakeAccessProperties
<a name="API_DataLakeAccessProperties"></a>

Input properties to configure data lake access for your catalog resource in the AWS Glue Data Catalog.

## Contents
<a name="API_DataLakeAccessProperties_Contents"></a>

 ** CatalogType **   <a name="Glue-Type-DataLakeAccessProperties-CatalogType"></a>
Specifies a federated catalog type for the native catalog resource. The currently supported type is `aws:redshift`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DataLakeAccess **   <a name="Glue-Type-DataLakeAccessProperties-DataLakeAccess"></a>
Turns on or off data lake access for Apache Spark applications that access Amazon Redshift databases in the Data Catalog from any non-Redshift engine, such as Amazon Athena, Amazon EMR, or AWS Glue ETL.
Type: Boolean
Required: No

 ** DataTransferRole **   <a name="Glue-Type-DataLakeAccessProperties-DataTransferRole"></a>
A role that will be assumed by AWS Glue for transferring data into/out of the staging bucket during a query.
Type: String
Pattern: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`
Required: No

 ** KmsKey **   <a name="Glue-Type-DataLakeAccessProperties-KmsKey"></a>
An encryption key that will be used for the staging bucket that will be created along with the catalog.
Type: String
Required: No

## See Also
<a name="API_DataLakeAccessProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataLakeAccessProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataLakeAccessProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataLakeAccessProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
