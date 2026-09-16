---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateWorkflow.html
---

# UpdateWorkflow
<a name="API_UpdateWorkflow"></a>

Updates an existing workflow.

## Request Syntax
<a name="API_UpdateWorkflow_RequestSyntax"></a>

```
{
   "DefaultRunProperties": {
      "{{string}}" : "{{string}}"
   },
   "Description": "{{string}}",
   "MaxConcurrentRuns": {{number}},
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWorkflow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultRunProperties](#API_UpdateWorkflow_RequestSyntax) **   <a name="Glue-UpdateWorkflow-request-DefaultRunProperties"></a>
A collection of properties to be used as part of each execution of the workflow.
Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_UpdateWorkflow_RequestSyntax) **   <a name="Glue-UpdateWorkflow-request-Description"></a>
The description of the workflow.
Type: String
Length Constraints: Maximum length of 120000.
Required: No

 ** [MaxConcurrentRuns](#API_UpdateWorkflow_RequestSyntax) **   <a name="Glue-UpdateWorkflow-request-MaxConcurrentRuns"></a>
You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
Type: Integer
Required: No

 ** [Name](#API_UpdateWorkflow_RequestSyntax) **   <a name="Glue-UpdateWorkflow-request-Name"></a>
Name of the workflow to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_UpdateWorkflow_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateWorkflow_ResponseSyntax) **   <a name="Glue-UpdateWorkflow-response-Name"></a>
The name of the workflow which was specified in input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_UpdateWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_UpdateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateWorkflow)
