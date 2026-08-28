---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_EngineDefaults.html
---

# EngineDefaults
<a name="API_EngineDefaults"></a>

Contains the result of a successful invocation of the `DescribeEngineDefaultClusterParameters` operation.

## Contents
<a name="API_EngineDefaults_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBParameterGroupFamily **
The name of the cluster parameter group family to return the engine parameter information for.
Type: String
Required: No

 ** Marker **
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** Parameters.Parameter.N **
The parameters of a particular cluster parameter group family.
Type: Array of [Parameter](API_Parameter.md) objects
Required: No

## See Also
<a name="API_EngineDefaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/EngineDefaults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/EngineDefaults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/EngineDefaults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
