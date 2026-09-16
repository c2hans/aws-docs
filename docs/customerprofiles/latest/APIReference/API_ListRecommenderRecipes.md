---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderRecipes.html
---

# ListRecommenderRecipes
<a name="API_connect-customer-profiles_ListRecommenderRecipes"></a>

Returns a list of available recommender recipes that can be used to create recommenders.

## Request Syntax
<a name="API_connect-customer-profiles_ListRecommenderRecipes_RequestSyntax"></a>

```
GET /recommender-recipes?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListRecommenderRecipes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_connect-customer-profiles_ListRecommenderRecipes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderRecipes-request-uri-MaxResults"></a>
The maximum number of recommender recipes to return in the response. The default value is 100.
Valid Range: Minimum value of 10. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListRecommenderRecipes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderRecipes-request-uri-NextToken"></a>
A token received from a previous ListRecommenderRecipes call to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListRecommenderRecipes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListRecommenderRecipes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecommenderRecipes": [
      {
         "description": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListRecommenderRecipes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_connect-customer-profiles_ListRecommenderRecipes_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderRecipes-response-NextToken"></a>
A token to retrieve the next page of results. Null if there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [RecommenderRecipes](#API_connect-customer-profiles_ListRecommenderRecipes_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderRecipes-response-RecommenderRecipes"></a>
A list of available recommender recipes and their properties.
Type: Array of [RecommenderRecipe](API_connect-customer-profiles_RecommenderRecipe.md) objects

## Errors
<a name="API_connect-customer-profiles_ListRecommenderRecipes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_ListRecommenderRecipes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListRecommenderRecipes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListRecommenderRecipes)
