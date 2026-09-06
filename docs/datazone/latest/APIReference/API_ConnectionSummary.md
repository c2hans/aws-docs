---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ConnectionSummary.html
---

# ConnectionSummary
<a name="API_ConnectionSummary"></a>

The summary of a connection.

## Contents
<a name="API_ConnectionSummary_Contents"></a>

 ** connectionId **   <a name="datazone-Type-ConnectionSummary-connectionId"></a>
The ID of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** domainId **   <a name="datazone-Type-ConnectionSummary-domainId"></a>
The domain ID of a connection.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** domainUnitId **   <a name="datazone-Type-ConnectionSummary-domainUnitId"></a>
The domain unit ID of a connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: Yes

 ** name **   <a name="datazone-Type-ConnectionSummary-name"></a>
The connection name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** physicalEndpoints **   <a name="datazone-Type-ConnectionSummary-physicalEndpoints"></a>
The connection physical endpoints.
Type: Array of [PhysicalEndpoint](API_PhysicalEndpoint.md) objects
Required: Yes

 ** type **   <a name="datazone-Type-ConnectionSummary-type"></a>
The connection type.
Type: String
Valid Values: `ATHENA | BIGQUERY | DATABRICKS | DOCUMENTDB | DYNAMODB | HYPERPOD | IAM | MYSQL | OPENSEARCH | ORACLE | POSTGRESQL | REDSHIFT | S3 | SAPHANA | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | VERTICA | WORKFLOWS_MWAA | AMAZON_Q | MLFLOW | VPC | GIT`
Required: Yes

 ** configurations **   <a name="datazone-Type-ConnectionSummary-configurations"></a>
The configurations of a connection summary.
Type: Array of [Configuration](API_Configuration.md) objects
Required: No

 ** environmentId **   <a name="datazone-Type-ConnectionSummary-environmentId"></a>
The environment ID of a connection.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** projectId **   <a name="datazone-Type-ConnectionSummary-projectId"></a>
The connection project ID.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** props **   <a name="datazone-Type-ConnectionSummary-props"></a>
The connection props.
Type: [ConnectionPropertiesOutput](API_ConnectionPropertiesOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** scope **   <a name="datazone-Type-ConnectionSummary-scope"></a>
The scope of the connection.
Type: String
Valid Values: `DOMAIN | PROJECT`
Required: No

## See Also
<a name="API_ConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ConnectionSummary)
