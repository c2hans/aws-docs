---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataLakeAccessPropertiesOutput.html
---

# DataLakeAccessPropertiesOutput
<a name="API_DataLakeAccessPropertiesOutput"></a>

The output properties of the data lake access configuration for your catalog resource in the AWS Glue Data Catalog.

## Contents
<a name="API_DataLakeAccessPropertiesOutput_Contents"></a>

 ** CatalogType **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-CatalogType"></a>
Specifies a federated catalog type for the native catalog resource. The currently supported type is `aws:redshift`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DataLakeAccess **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-DataLakeAccess"></a>
Turns on or off data lake access for Apache Spark applications that access Amazon Redshift databases in the Data Catalog.
Type: Boolean
Required: No

 ** DataTransferRole **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-DataTransferRole"></a>
A role that will be assumed by AWS Glue for transferring data into/out of the staging bucket during a query.
Type: String
Pattern: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`
Required: No

 ** KmsKey **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-KmsKey"></a>
An encryption key that will be used for the staging bucket that will be created along with the catalog.
Type: String
Required: No

 ** ManagedWorkgroupName **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-ManagedWorkgroupName"></a>
The managed Redshift Serverless compute name that is created for your catalog resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ManagedWorkgroupStatus **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-ManagedWorkgroupStatus"></a>
The managed Redshift Serverless compute status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RedshiftDatabaseName **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-RedshiftDatabaseName"></a>
The default Redshift database resource name in the managed compute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StatusMessage **   <a name="Glue-Type-DataLakeAccessPropertiesOutput-StatusMessage"></a>
A message that gives more detailed information about the managed workgroup status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DataLakeAccessPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataLakeAccessPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataLakeAccessPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataLakeAccessPropertiesOutput)
