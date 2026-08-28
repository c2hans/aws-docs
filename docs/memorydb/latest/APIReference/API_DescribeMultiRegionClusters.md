---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeMultiRegionClusters.html
---

# DescribeMultiRegionClusters
<a name="API_DescribeMultiRegionClusters"></a>

Returns details about one or more multi-Region clusters.

## Request Syntax
<a name="API_DescribeMultiRegionClusters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MultiRegionClusterName": "{{string}}",
   "NextToken": "{{string}}",
   "ShowClusterDetails": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeMultiRegionClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeMultiRegionClusters_RequestSyntax) **   <a name="MemoryDB-DescribeMultiRegionClusters-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Required: No

 ** [MultiRegionClusterName](#API_DescribeMultiRegionClusters_RequestSyntax) **   <a name="MemoryDB-DescribeMultiRegionClusters-request-MultiRegionClusterName"></a>
The name of a specific multi-Region cluster to describe.
Type: String
Required: No

 ** [NextToken](#API_DescribeMultiRegionClusters_RequestSyntax) **   <a name="MemoryDB-DescribeMultiRegionClusters-request-NextToken"></a>
A token to specify where to start paginating.
Type: String
Required: No

 ** [ShowClusterDetails](#API_DescribeMultiRegionClusters_RequestSyntax) **   <a name="MemoryDB-DescribeMultiRegionClusters-request-ShowClusterDetails"></a>
Details about the multi-Region cluster.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeMultiRegionClusters_ResponseSyntax"></a>

```
{
   "MultiRegionClusters": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeMultiRegionClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MultiRegionClusters](#API_DescribeMultiRegionClusters_ResponseSyntax) **   <a name="MemoryDB-DescribeMultiRegionClusters-response-MultiRegionClusters"></a>
A list of multi-Region clusters.
Type: Array of [MultiRegionCluster](API_MultiRegionCluster.md) objects

 ** [NextToken](#API_DescribeMultiRegionClusters_ResponseSyntax) **   <a name="MemoryDB-DescribeMultiRegionClusters-response-NextToken"></a>
A token to use to retrieve the next page of results.
Type: String

## Errors
<a name="API_DescribeMultiRegionClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** MultiRegionClusterNotFoundFault **
The specified multi-Region cluster does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMultiRegionClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeMultiRegionClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeMultiRegionClusters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
