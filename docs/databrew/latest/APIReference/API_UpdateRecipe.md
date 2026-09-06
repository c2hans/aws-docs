---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateRecipe.html
---

# UpdateRecipe
<a name="API_UpdateRecipe"></a>

Modifies the definition of the `LATEST_WORKING` version of a DataBrew recipe.

## Request Syntax
<a name="API_UpdateRecipe_RequestSyntax"></a>

```
PUT /recipes/{{name}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
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
   ]
}
```

## URI Request Parameters
<a name="API_UpdateRecipe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateRecipe_RequestSyntax) **   <a name="databrew-UpdateRecipe-request-uri-Name"></a>
The name of the recipe to be updated.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_UpdateRecipe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateRecipe_RequestSyntax) **   <a name="databrew-UpdateRecipe-request-Description"></a>
A description of the recipe.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Steps](#API_UpdateRecipe_RequestSyntax) **   <a name="databrew-UpdateRecipe-request-Steps"></a>
One or more steps to be performed by the recipe. Each step consists of an action, and the conditions under which the action should succeed.
Type: Array of [RecipeStep](API_RecipeStep.md) objects
Required: No

## Response Syntax
<a name="API_UpdateRecipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateRecipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateRecipe_ResponseSyntax) **   <a name="databrew-UpdateRecipe-response-Name"></a>
The name of the recipe that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_UpdateRecipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateRecipe)
