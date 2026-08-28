---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_EngineDefaults.html
---

# EngineDefaults
<a name="API_EngineDefaults"></a>

Contains the result of a successful invocation of the `DescribeEngineDefaultParameters` action.

## Contents
<a name="API_EngineDefaults_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBParameterGroupFamily **
Specifies the name of the DB parameter group family that the engine default parameters apply to.
Type: String
Required: No

 ** Marker **
An optional pagination token provided by a previous EngineDefaults request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .
Type: String
Required: No

 ** Parameters.Parameter.N **
Contains a list of engine default parameters.
Type: Array of [Parameter](API_Parameter.md) objects
Required: No

## See Also
<a name="API_EngineDefaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/EngineDefaults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/EngineDefaults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/EngineDefaults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
