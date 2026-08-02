---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataflowGraph.html
---

# GetDataflowGraph
<a name="API_GetDataflowGraph"></a>

Transforms a Python script into a directed acyclic graph (DAG).

## Request Syntax
<a name="API_GetDataflowGraph_RequestSyntax"></a>

```
{
   "PythonScript": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataflowGraph_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PythonScript](#API_GetDataflowGraph_RequestSyntax) **   <a name="Glue-GetDataflowGraph-request-PythonScript"></a>
The Python script to transform.
Type: String
Required: No

## Response Syntax
<a name="API_GetDataflowGraph_ResponseSyntax"></a>

```
{
   "DagEdges": [
      {
         "Source": "string",
         "Target": "string",
         "TargetParameter": "string"
      }
   ],
   "DagNodes": [
      {
         "Args": [
            {
               "Name": "string",
               "Param": boolean,
               "Value": "string"
            }
         ],
         "Id": "string",
         "LineNumber": number,
         "NodeType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetDataflowGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DagEdges](#API_GetDataflowGraph_ResponseSyntax) **   <a name="Glue-GetDataflowGraph-response-DagEdges"></a>
A list of the edges in the resulting DAG.
Type: Array of [CodeGenEdge](API_CodeGenEdge.md) objects

 ** [DagNodes](#API_GetDataflowGraph_ResponseSyntax) **   <a name="Glue-GetDataflowGraph-response-DagNodes"></a>
A list of the nodes in the resulting DAG.
Type: Array of [CodeGenNode](API_CodeGenNode.md) objects

## Errors
<a name="API_GetDataflowGraph_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetDataflowGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataflowGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataflowGraph)
