---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartBlueprintRun.html
---

# StartBlueprintRun
<a name="API_StartBlueprintRun"></a>

Starts a new run of the specified blueprint.

## Request Syntax
<a name="API_StartBlueprintRun_RequestSyntax"></a>

```
{
   "BlueprintName": "{{string}}",
   "Parameters": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StartBlueprintRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlueprintName](#API_StartBlueprintRun_RequestSyntax) **   <a name="Glue-StartBlueprintRun-request-BlueprintName"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [Parameters](#API_StartBlueprintRun_RequestSyntax) **   <a name="Glue-StartBlueprintRun-request-Parameters"></a>
Specifies the parameters as a `BlueprintParameters` object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Required: No

 ** [RoleArn](#API_StartBlueprintRun_RequestSyntax) **   <a name="Glue-StartBlueprintRun-request-RoleArn"></a>
Specifies the IAM role used to create the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws[^:]*:iam::[0-9]*:role/.+`
Required: Yes

## Response Syntax
<a name="API_StartBlueprintRun_ResponseSyntax"></a>

```
{
   "RunId": "string"
}
```

## Response Elements
<a name="API_StartBlueprintRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RunId](#API_StartBlueprintRun_ResponseSyntax) **   <a name="Glue-StartBlueprintRun-response-RunId"></a>
The run ID for this blueprint run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartBlueprintRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IllegalBlueprintStateException **
The blueprint is in an invalid state to perform a requested operation.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartBlueprintRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartBlueprintRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartBlueprintRun)
