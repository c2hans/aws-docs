---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetBlueprints.html
---

# BatchGetBlueprints
<a name="API_BatchGetBlueprints"></a>

Retrieves information about a list of blueprints.

## Request Syntax
<a name="API_BatchGetBlueprints_RequestSyntax"></a>

```
{
   "IncludeBlueprint": {{boolean}},
   "IncludeParameterSpec": {{boolean}},
   "Names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetBlueprints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludeBlueprint](#API_BatchGetBlueprints_RequestSyntax) **   <a name="Glue-BatchGetBlueprints-request-IncludeBlueprint"></a>
Specifies whether or not to include the blueprint in the response.
Type: Boolean
Required: No

 ** [IncludeParameterSpec](#API_BatchGetBlueprints_RequestSyntax) **   <a name="Glue-BatchGetBlueprints-request-IncludeParameterSpec"></a>
Specifies whether or not to include the parameters, as a JSON string, for the blueprint in the response.
Type: Boolean
Required: No

 ** [Names](#API_BatchGetBlueprints_RequestSyntax) **   <a name="Glue-BatchGetBlueprints-request-Names"></a>
A list of blueprint names.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_BatchGetBlueprints_ResponseSyntax"></a>

```
{
   "Blueprints": [
      {
         "BlueprintLocation": "string",
         "BlueprintServiceLocation": "string",
         "CreatedOn": number,
         "Description": "string",
         "ErrorMessage": "string",
         "LastActiveDefinition": {
            "BlueprintLocation": "string",
            "BlueprintServiceLocation": "string",
            "Description": "string",
            "LastModifiedOn": number,
            "ParameterSpec": "string"
         },
         "LastModifiedOn": number,
         "Name": "string",
         "ParameterSpec": "string",
         "Status": "string"
      }
   ],
   "MissingBlueprints": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetBlueprints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Blueprints](#API_BatchGetBlueprints_ResponseSyntax) **   <a name="Glue-BatchGetBlueprints-response-Blueprints"></a>
Returns a list of blueprint as a `Blueprints` object.
Type: Array of [Blueprint](API_Blueprint.md) objects

 ** [MissingBlueprints](#API_BatchGetBlueprints_ResponseSyntax) **   <a name="Glue-BatchGetBlueprints-response-MissingBlueprints"></a>
Returns a list of `BlueprintNames` that were not found.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`

## Errors
<a name="API_BatchGetBlueprints_Errors"></a>

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
<a name="API_BatchGetBlueprints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetBlueprints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetBlueprints)
