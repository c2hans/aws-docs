---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DeleteRecipeVersion.html
---

# DeleteRecipeVersion
<a name="API_DeleteRecipeVersion"></a>

Deletes a single version of a DataBrew recipe.

## Request Syntax
<a name="API_DeleteRecipeVersion_RequestSyntax"></a>

```
DELETE /recipes/{{name}}/recipeVersion/{{recipeVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRecipeVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteRecipeVersion_RequestSyntax) **   <a name="databrew-DeleteRecipeVersion-request-uri-Name"></a>
The name of the recipe.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [recipeVersion](#API_DeleteRecipeVersion_RequestSyntax) **   <a name="databrew-DeleteRecipeVersion-request-uri-RecipeVersion"></a>
The version of the recipe to be deleted. You can specify a numeric versions (`X.Y`) or `LATEST_WORKING`. `LATEST_PUBLISHED` is not supported.
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: Yes

## Request Body
<a name="API_DeleteRecipeVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRecipeVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string",
   "RecipeVersion": "string"
}
```

## Response Elements
<a name="API_DeleteRecipeVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DeleteRecipeVersion_ResponseSyntax) **   <a name="databrew-DeleteRecipeVersion-response-Name"></a>
The name of the recipe that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [RecipeVersion](#API_DeleteRecipeVersion_ResponseSyntax) **   <a name="databrew-DeleteRecipeVersion-response-RecipeVersion"></a>
The version of the recipe that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.

## Errors
<a name="API_DeleteRecipeVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRecipeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DeleteRecipeVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DeleteRecipeVersion)
