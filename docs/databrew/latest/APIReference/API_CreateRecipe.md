---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CreateRecipe.html
---

# CreateRecipe
<a name="API_CreateRecipe"></a>

Creates a new DataBrew recipe.

## Request Syntax
<a name="API_CreateRecipe_RequestSyntax"></a>

```
POST /recipes HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Steps": [
      {
         "Action": {
            "Operation": "{{string}}",
            "Parameters": {
               "{{string}}" : "{{string}}"
            }
         },
         "ConditionExpressions": [
            {
               "Condition": "{{string}}",
               "TargetColumn": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRecipe_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRecipe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateRecipe_RequestSyntax) **   <a name="databrew-CreateRecipe-request-Name"></a>
A unique name for the recipe. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Steps](#API_CreateRecipe_RequestSyntax) **   <a name="databrew-CreateRecipe-request-Steps"></a>
An array containing the steps to be performed by the recipe. Each recipe step consists of one recipe action and (optionally) an array of condition expressions.
Type: Array of [RecipeStep](API_RecipeStep.md) objects
Required: Yes

 ** [Description](#API_CreateRecipe_RequestSyntax) **   <a name="databrew-CreateRecipe-request-Description"></a>
A description for the recipe.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Tags](#API_CreateRecipe_RequestSyntax) **   <a name="databrew-CreateRecipe-request-Tags"></a>
Metadata tags to apply to this recipe.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRecipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateRecipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateRecipe_ResponseSyntax) **   <a name="databrew-CreateRecipe-response-Name"></a>
The name of the recipe that you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateRecipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/CreateRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CreateRecipe)
