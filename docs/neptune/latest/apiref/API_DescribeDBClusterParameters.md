---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribeDBClusterParameters.html
---

# DescribeDBClusterParameters
<a name="API_DescribeDBClusterParameters"></a>

Returns the detailed parameter list for a particular DB cluster parameter group.

## Request Parameters
<a name="API_DescribeDBClusterParameters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **
The name of a specific DB cluster parameter group to return parameter details for.
Constraints:
+ If supplied, must match the name of an existing DBClusterParameterGroup.
Type: String
Required: Yes

 **Filters.Filter.N**
This parameter is not currently supported.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** Marker **
 An optional pagination token provided by a previous `DescribeDBClusterParameters` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** Source **
 A value that indicates to return only parameters for a specific source. Parameter sources can be `engine`, `service`, or `customer`.
Type: String
Required: No

## Response Elements
<a name="API_DescribeDBClusterParameters_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
 An optional pagination token provided by a previous DescribeDBClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .
Type: String

 **Parameters.Parameter.N**
Provides a list of parameters for the DB cluster parameter group.
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_DescribeDBClusterParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **
 *DBParameterGroupName* does not refer to an existing DB parameter group.
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusterParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribeDBClusterParameters)
