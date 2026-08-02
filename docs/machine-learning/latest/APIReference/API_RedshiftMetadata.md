---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RedshiftMetadata.html
---

# RedshiftMetadata
<a name="API_RedshiftMetadata"></a>

Describes the `DataSource` details specific to Amazon Redshift.

## Contents
<a name="API_RedshiftMetadata_Contents"></a>

 ** DatabaseUserName **   <a name="amazonml-Type-RedshiftMetadata-DatabaseUserName"></a>
A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the `RedshiftSelectSqlQuery` query. The username should be valid for an Amazon Redshift [USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** RedshiftDatabase **   <a name="amazonml-Type-RedshiftMetadata-RedshiftDatabase"></a>
Describes the database details required to connect to an Amazon Redshift database.
Type: [RedshiftDatabase](API_RedshiftDatabase.md) object
Required: No

 ** SelectSqlQuery **   <a name="amazonml-Type-RedshiftMetadata-SelectSqlQuery"></a>
 The SQL query that is specified during [CreateDataSourceFromRedshift](API_CreateDataSourceFromRedshift.md). Returns only if `Verbose` is true in GetDataSourceInput.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16777216.
Required: No

## See Also
<a name="API_RedshiftMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/RedshiftMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/RedshiftMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/RedshiftMetadata)
