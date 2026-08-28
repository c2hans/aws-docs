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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
