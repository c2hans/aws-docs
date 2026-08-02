---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlueConnectionInput.html
---

# GlueConnectionInput
<a name="API_GlueConnectionInput"></a>

The AWS Glue connecton input.

## Contents
<a name="API_GlueConnectionInput_Contents"></a>

 ** athenaProperties **   <a name="datazone-Type-GlueConnectionInput-athenaProperties"></a>
The Amazon Athena properties of the AWS Glue connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** authenticationConfiguration **   <a name="datazone-Type-GlueConnectionInput-authenticationConfiguration"></a>
The authentication configuration of the AWS Glue connection.
Type: [AuthenticationConfigurationInput](API_AuthenticationConfigurationInput.md) object
Required: No

 ** connectionProperties **   <a name="datazone-Type-GlueConnectionInput-connectionProperties"></a>
The connection properties of the AWS Glue connection.
Type: String to string map
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** connectionType **   <a name="datazone-Type-GlueConnectionInput-connectionType"></a>
The connection type of the AWS Glue connection.
Type: String
Valid Values: `SNOWFLAKE | BIGQUERY | DOCUMENTDB | DYNAMODB | MYSQL | OPENSEARCH | ORACLE | POSTGRESQL | REDSHIFT | SAPHANA | SQLSERVER | TERADATA | VERTICA`
Required: No

 ** description **   <a name="datazone-Type-GlueConnectionInput-description"></a>
The description of the AWS Glue connection.
Type: String
Required: No

 ** matchCriteria **   <a name="datazone-Type-GlueConnectionInput-matchCriteria"></a>
The match criteria of the AWS Glue connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Required: No

 ** name **   <a name="datazone-Type-GlueConnectionInput-name"></a>
The name of the AWS Glue connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** physicalConnectionRequirements **   <a name="datazone-Type-GlueConnectionInput-physicalConnectionRequirements"></a>
The physical connection requirements for the AWS Glue connection.
Type: [PhysicalConnectionRequirements](API_PhysicalConnectionRequirements.md) object
Required: No

 ** pythonProperties **   <a name="datazone-Type-GlueConnectionInput-pythonProperties"></a>
The Python properties of the AWS Glue connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** sparkProperties **   <a name="datazone-Type-GlueConnectionInput-sparkProperties"></a>
The Spark properties of the AWS Glue connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** validateCredentials **   <a name="datazone-Type-GlueConnectionInput-validateCredentials"></a>
Speciefies whether to validate credentials of the AWS Glue connection.
Type: Boolean
Required: No

 ** validateForComputeEnvironments **   <a name="datazone-Type-GlueConnectionInput-validateForComputeEnvironments"></a>
Speciefies whether to validate for compute environments of the AWS Glue connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `SPARK | ATHENA | PYTHON`
Required: No

## See Also
<a name="API_GlueConnectionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlueConnectionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlueConnectionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlueConnectionInput)
