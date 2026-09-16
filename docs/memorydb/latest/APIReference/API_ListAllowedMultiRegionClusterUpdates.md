---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedMultiRegionClusterUpdates.html
---

# ListAllowedMultiRegionClusterUpdates
<a name="API_ListAllowedMultiRegionClusterUpdates"></a>

Lists the allowed updates for a multi-Region cluster.

## Request Syntax
<a name="API_ListAllowedMultiRegionClusterUpdates_RequestSyntax"></a>

```
{
   "MultiRegionClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAllowedMultiRegionClusterUpdates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MultiRegionClusterName](#API_ListAllowedMultiRegionClusterUpdates_RequestSyntax) **   <a name="MemoryDB-ListAllowedMultiRegionClusterUpdates-request-MultiRegionClusterName"></a>
The name of the multi-Region cluster.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListAllowedMultiRegionClusterUpdates_ResponseSyntax"></a>

```
{
   "ScaleDownNodeTypes": [ "string" ],
   "ScaleUpNodeTypes": [ "string" ]
}
```

## Response Elements
<a name="API_ListAllowedMultiRegionClusterUpdates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScaleDownNodeTypes](#API_ListAllowedMultiRegionClusterUpdates_ResponseSyntax) **   <a name="MemoryDB-ListAllowedMultiRegionClusterUpdates-response-ScaleDownNodeTypes"></a>
The node types that the cluster can be scaled down to.
Type: Array of strings

 ** [ScaleUpNodeTypes](#API_ListAllowedMultiRegionClusterUpdates_ResponseSyntax) **   <a name="MemoryDB-ListAllowedMultiRegionClusterUpdates-response-ScaleUpNodeTypes"></a>
The node types that the cluster can be scaled up to.
Type: Array of strings

## Errors
<a name="API_ListAllowedMultiRegionClusterUpdates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** MultiRegionClusterNotFoundFault **
The specified multi-Region cluster does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ListAllowedMultiRegionClusterUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ListAllowedMultiRegionClusterUpdates)
