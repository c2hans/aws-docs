---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedNodeTypeUpdates.html
---

# ListAllowedNodeTypeUpdates
<a name="API_ListAllowedNodeTypeUpdates"></a>

Lists all available node types that you can scale to from your cluster's current node type. When you use the UpdateCluster operation to scale your cluster, the value of the NodeType parameter must be one of the node types returned by this operation.

## Request Syntax
<a name="API_ListAllowedNodeTypeUpdates_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAllowedNodeTypeUpdates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_ListAllowedNodeTypeUpdates_RequestSyntax) **   <a name="MemoryDB-ListAllowedNodeTypeUpdates-request-ClusterName"></a>
The name of the cluster you want to scale. MemoryDB uses the cluster name to identify the current node type being used by this cluster, and from that to create a list of node types you can scale up to.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListAllowedNodeTypeUpdates_ResponseSyntax"></a>

```
{
   "ScaleDownNodeTypes": [ "string" ],
   "ScaleUpNodeTypes": [ "string" ]
}
```

## Response Elements
<a name="API_ListAllowedNodeTypeUpdates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScaleDownNodeTypes](#API_ListAllowedNodeTypeUpdates_ResponseSyntax) **   <a name="MemoryDB-ListAllowedNodeTypeUpdates-response-ScaleDownNodeTypes"></a>
A list node types which you can use to scale down your cluster.
Type: Array of strings

 ** [ScaleUpNodeTypes](#API_ListAllowedNodeTypeUpdates_ResponseSyntax) **   <a name="MemoryDB-ListAllowedNodeTypeUpdates-response-ScaleUpNodeTypes"></a>
A list node types which you can use to scale up your cluster.
Type: Array of strings

## Errors
<a name="API_ListAllowedNodeTypeUpdates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_ListAllowedNodeTypeUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ListAllowedNodeTypeUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
