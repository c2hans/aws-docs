---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSDatabaseCredentials.html
---

# RDSDatabaseCredentials
<a name="API_RDSDatabaseCredentials"></a>

The database credentials to connect to a database on an RDS DB instance.

## Contents
<a name="API_RDSDatabaseCredentials_Contents"></a>

 ** Password **   <a name="amazonml-Type-RDSDatabaseCredentials-Password"></a>
The password to be used by Amazon ML to connect to a database on an RDS DB instance. The password should have sufficient permissions to execute the `RDSSelectQuery` query.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 128.
Required: Yes

 ** Username **   <a name="amazonml-Type-RDSDatabaseCredentials-Username"></a>
The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an `RDSSelectSqlQuery` query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_RDSDatabaseCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/RDSDatabaseCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/RDSDatabaseCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/RDSDatabaseCredentials)
