---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ProtectedQueryInputParameters.html
---

# ProtectedQueryInputParameters
<a name="API_ProtectedQueryInputParameters"></a>

Provides information necessary to perform the protected query.

## Contents
<a name="API_ProtectedQueryInputParameters_Contents"></a>

 ** sqlParameters **   <a name="API-Type-ProtectedQueryInputParameters-sqlParameters"></a>
The parameters for the SQL type Protected Query.
Type: [ProtectedQuerySQLParameters](API_ProtectedQuerySQLParameters.md) object
Required: Yes

 ** computeConfiguration **   <a name="API-Type-ProtectedQueryInputParameters-computeConfiguration"></a>
Provides configuration information for the workers that will perform the protected query.
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** resultFormat **   <a name="API-Type-ProtectedQueryInputParameters-resultFormat"></a>
The format in which the query results should be returned. If not specified, defaults to `CSV`.
Type: String
Valid Values: `CSV | PARQUET`
Required: No

## See Also
<a name="API_ProtectedQueryInputParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ProtectedQueryInputParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ProtectedQueryInputParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ProtectedQueryInputParameters)
