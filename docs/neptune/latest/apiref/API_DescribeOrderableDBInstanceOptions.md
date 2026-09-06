---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribeOrderableDBInstanceOptions.html
---

# DescribeOrderableDBInstanceOptions
<a name="API_DescribeOrderableDBInstanceOptions"></a>

Returns a list of orderable DB instance options for the specified engine.

## Request Parameters
<a name="API_DescribeOrderableDBInstanceOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceClass **
The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.
Type: String
Required: No

 ** Engine **
The name of the engine to retrieve DB instance options for.
Type: String
Required: Yes

 ** EngineVersion **
The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.
Type: String
Required: No

 **Filters.Filter.N**
This parameter is not currently supported.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** LicenseModel **
The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.
Type: String
Required: No

 ** Marker **
 An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .
Type: String
Required: No

 ** MaxRecords **
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** Vpc **
The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.
Type: Boolean
Required: No

## Response Elements
<a name="API_DescribeOrderableDBInstanceOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
 An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .
Type: String

 **OrderableDBInstanceOptions.OrderableDBInstanceOption.N**
An [OrderableDBInstanceOption](API_OrderableDBInstanceOption.md) structure containing information about orderable options for the DB instance.
Type: Array of [OrderableDBInstanceOption](API_OrderableDBInstanceOption.md) objects

## Errors
<a name="API_DescribeOrderableDBInstanceOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeOrderableDBInstanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)
