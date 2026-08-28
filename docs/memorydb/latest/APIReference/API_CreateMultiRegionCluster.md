---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateMultiRegionCluster.html
---

# CreateMultiRegionCluster
<a name="API_CreateMultiRegionCluster"></a>

Creates a new multi-Region cluster.

## Request Syntax
<a name="API_CreateMultiRegionCluster_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Engine": "{{string}}",
   "EngineVersion": "{{string}}",
   "MultiRegionClusterNameSuffix": "{{string}}",
   "MultiRegionParameterGroupName": "{{string}}",
   "NodeType": "{{string}}",
   "NumShards": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TLSEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateMultiRegionCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-Description"></a>
A description for the multi-Region cluster.
Type: String
Required: No

 ** [Engine](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-Engine"></a>
The name of the engine to be used for the multi-Region cluster.
Type: String
Required: No

 ** [EngineVersion](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-EngineVersion"></a>
The version of the engine to be used for the multi-Region cluster.
Type: String
Required: No

 ** [MultiRegionClusterNameSuffix](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-MultiRegionClusterNameSuffix"></a>
A suffix to be added to the Multi-Region cluster name. Amazon MemoryDB automatically applies a prefix to the Multi-Region cluster Name when it is created. Each Amazon Region has its own prefix. For instance, a Multi-Region cluster Name created in the US-West-1 region will begin with "virxk", along with the suffix name you provide. The suffix guarantees uniqueness of the Multi-Region cluster name across multiple regions. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** [MultiRegionParameterGroupName](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-MultiRegionParameterGroupName"></a>
The name of the multi-Region parameter group to be associated with the cluster.
Type: String
Required: No

 ** [NodeType](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-NodeType"></a>
The node type to be used for the multi-Region cluster.
Type: String
Required: Yes

 ** [NumShards](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-NumShards"></a>
The number of shards for the multi-Region cluster.
Type: Integer
Required: No

 ** [Tags](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-Tags"></a>
A list of tags to be applied to the multi-Region cluster.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [TLSEnabled](#API_CreateMultiRegionCluster_RequestSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-request-TLSEnabled"></a>
Whether to enable TLS encryption for the multi-Region cluster.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateMultiRegionCluster_ResponseSyntax"></a>

```
{
   "MultiRegionCluster": {
      "ARN": "string",
      "Clusters": [
         {
            "ARN": "string",
            "ClusterName": "string",
            "Region": "string",
            "Status": "string"
         }
      ],
      "Description": "string",
      "Engine": "string",
      "EngineVersion": "string",
      "MultiRegionClusterName": "string",
      "MultiRegionParameterGroupName": "string",
      "NodeType": "string",
      "NumberOfShards": number,
      "Status": "string",
      "TLSEnabled": boolean
   }
}
```

## Response Elements
<a name="API_CreateMultiRegionCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MultiRegionCluster](#API_CreateMultiRegionCluster_ResponseSyntax) **   <a name="MemoryDB-CreateMultiRegionCluster-response-MultiRegionCluster"></a>
Details about the newly created multi-Region cluster.
Type: [MultiRegionCluster](API_MultiRegionCluster.md) object

## Errors
<a name="API_CreateMultiRegionCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterQuotaForCustomerExceededFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** MultiRegionClusterAlreadyExistsFault **
A multi-Region cluster with the specified name already exists.
HTTP Status Code: 400

 ** MultiRegionParameterGroupNotFoundFault **
The specified multi-Region parameter group does not exist.
HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_CreateMultiRegionCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateMultiRegionCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateMultiRegionCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
