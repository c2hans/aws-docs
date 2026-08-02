---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetBlueprintRuns.html
---

# GetBlueprintRuns
<a name="API_GetBlueprintRuns"></a>

Retrieves the details of blueprint runs for a specified blueprint.

## Request Syntax
<a name="API_GetBlueprintRuns_RequestSyntax"></a>

```
{
   "BlueprintName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBlueprintRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlueprintName](#API_GetBlueprintRuns_RequestSyntax) **   <a name="Glue-GetBlueprintRuns-request-BlueprintName"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [MaxResults](#API_GetBlueprintRuns_RequestSyntax) **   <a name="Glue-GetBlueprintRuns-request-MaxResults"></a>
The maximum size of a list to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetBlueprintRuns_RequestSyntax) **   <a name="Glue-GetBlueprintRuns-request-NextToken"></a>
A continuation token, if this is a continuation request.
Type: String
Required: No

## Response Syntax
<a name="API_GetBlueprintRuns_ResponseSyntax"></a>

```
{
   "BlueprintRuns": [
      {
         "BlueprintName": "string",
         "CompletedOn": number,
         "ErrorMessage": "string",
         "Parameters": "string",
         "RoleArn": "string",
         "RollbackErrorMessage": "string",
         "RunId": "string",
         "StartedOn": number,
         "State": "string",
         "WorkflowName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetBlueprintRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlueprintRuns](#API_GetBlueprintRuns_ResponseSyntax) **   <a name="Glue-GetBlueprintRuns-response-BlueprintRuns"></a>
Returns a list of `BlueprintRun` objects.
Type: Array of [BlueprintRun](API_BlueprintRun.md) objects

 ** [NextToken](#API_GetBlueprintRuns_ResponseSyntax) **   <a name="Glue-GetBlueprintRuns-response-NextToken"></a>
A continuation token, if not all blueprint runs have been returned.
Type: String

## Errors
<a name="API_GetBlueprintRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetBlueprintRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetBlueprintRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetBlueprintRuns)
