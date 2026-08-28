---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateScript.html
---

# CreateScript
<a name="API_CreateScript"></a>

Transforms a directed acyclic graph (DAG) into code.

## Request Syntax
<a name="API_CreateScript_RequestSyntax"></a>

```
{
   "DagEdges": [
      {
         "Source": "{{string}}",
         "Target": "{{string}}",
         "TargetParameter": "{{string}}"
      }
   ],
   "DagNodes": [
      {
         "Args": [
            {
               "Name": "{{string}}",
               "Param": {{boolean}},
               "Value": "{{string}}"
            }
         ],
         "Id": "{{string}}",
         "LineNumber": {{number}},
         "NodeType": "{{string}}"
      }
   ],
   "Language": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateScript_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DagEdges](#API_CreateScript_RequestSyntax) **   <a name="Glue-CreateScript-request-DagEdges"></a>
A list of the edges in the DAG.
Type: Array of [CodeGenEdge](API_CodeGenEdge.md) objects
Required: No

 ** [DagNodes](#API_CreateScript_RequestSyntax) **   <a name="Glue-CreateScript-request-DagNodes"></a>
A list of the nodes in the DAG.
Type: Array of [CodeGenNode](API_CodeGenNode.md) objects
Required: No

 ** [Language](#API_CreateScript_RequestSyntax) **   <a name="Glue-CreateScript-request-Language"></a>
The programming language of the resulting code from the DAG.
Type: String
Valid Values: `PYTHON | SCALA`
Required: No

## Response Syntax
<a name="API_CreateScript_ResponseSyntax"></a>

```
{
   "PythonScript": "string",
   "ScalaCode": "string"
}
```

## Response Elements
<a name="API_CreateScript_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PythonScript](#API_CreateScript_ResponseSyntax) **   <a name="Glue-CreateScript-response-PythonScript"></a>
The Python script generated from the DAG.
Type: String

 ** [ScalaCode](#API_CreateScript_ResponseSyntax) **   <a name="Glue-CreateScript-response-ScalaCode"></a>
The Scala code generated from the DAG.
Type: String

## Errors
<a name="API_CreateScript_Errors"></a>

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
<a name="API_CreateScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateScript)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateScript)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateScript)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateScript)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateScript)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateScript)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateScript)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateScript)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
