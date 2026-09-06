---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ListRecipes.html
---

# ListRecipes
<a name="API_ListRecipes"></a>

Lists all of the DataBrew recipes that are defined.

## Request Syntax
<a name="API_ListRecipes_RequestSyntax"></a>

```
GET /recipes?maxResults={{MaxResults}}&nextToken={{NextToken}}&recipeVersion={{RecipeVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecipes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListRecipes_RequestSyntax) **   <a name="databrew-ListRecipes-request-uri-MaxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListRecipes_RequestSyntax) **   <a name="databrew-ListRecipes-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [RecipeVersion](#API_ListRecipes_RequestSyntax) **   <a name="databrew-ListRecipes-request-uri-RecipeVersion"></a>
Return only those recipes with a version identifier of `LATEST_WORKING` or `LATEST_PUBLISHED`. If `RecipeVersion` is omitted, `ListRecipes` returns all of the `LATEST_PUBLISHED` recipe versions.
Valid values: `LATEST_WORKING` \| `LATEST_PUBLISHED`
Length Constraints: Minimum length of 1. Maximum length of 16.

## Request Body
<a name="API_ListRecipes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecipes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Recipes": [
      {
         "CreateDate": number,
         "CreatedBy": "string",
         "Description": "string",
         "LastModifiedBy": "string",
         "LastModifiedDate": number,
         "Name": "string",
         "ProjectName": "string",
         "PublishedBy": "string",
         "PublishedDate": number,
         "RecipeVersion": "string",
         "ResourceArn": "string",
         "Steps": [
            {
               "Action": {
                  "Operation": "string",
                  "Parameters": {
                     "string" : "string"
                  }
               },
               "ConditionExpressions": [
                  {
                     "Condition": "string",
                     "TargetColumn": "string",
                     "Value": "string"
                  }
               ]
            }
         ],
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListRecipes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Recipes](#API_ListRecipes_ResponseSyntax) **   <a name="databrew-ListRecipes-response-Recipes"></a>
A list of recipes that are defined.
Type: Array of [Recipe](API_Recipe.md) objects

 ** [NextToken](#API_ListRecipes_ResponseSyntax) **   <a name="databrew-ListRecipes-response-NextToken"></a>
A token that you can use in a subsequent call to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListRecipes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListRecipes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/ListRecipes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ListRecipes)
