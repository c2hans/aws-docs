---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribePendingMaintenanceActions.html
---

# DescribePendingMaintenanceActions
<a name="API_DescribePendingMaintenanceActions"></a>

Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.

## Request Parameters
<a name="API_DescribePendingMaintenanceActions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**
A filter that specifies one or more resources to return pending maintenance actions for.
Supported filters:
+  `db-cluster-id` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.
+  `db-instance-id` - Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** Marker **
 An optional pagination token provided by a previous `DescribePendingMaintenanceActions` request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** ResourceIdentifier **
The ARN of a resource to return pending maintenance actions for.
Type: String
Required: No

## Response Elements
<a name="API_DescribePendingMaintenanceActions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
 An optional pagination token provided by a previous `DescribePendingMaintenanceActions` request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by `MaxRecords`.
Type: String

 **PendingMaintenanceActions.ResourcePendingMaintenanceActions.N**
A list of the pending maintenance actions for the resource.
Type: Array of [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) objects

## Errors
<a name="API_DescribePendingMaintenanceActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The specified resource ID was not found.
HTTP Status Code: 404

## See Also
<a name="API_DescribePendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribePendingMaintenanceActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribePendingMaintenanceActions)
