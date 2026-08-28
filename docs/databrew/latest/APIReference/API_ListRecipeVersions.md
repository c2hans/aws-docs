---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ListRecipeVersions.html
---

# ListRecipeVersions
<a name="API_ListRecipeVersions"></a>

Lists the versions of a particular DataBrew recipe, except for `LATEST_WORKING`.

## Request Syntax
<a name="API_ListRecipeVersions_RequestSyntax"></a>

```
GET /recipeVersions?maxResults={{MaxResults}}&name={{Name}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecipeVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListRecipeVersions_RequestSyntax) **   <a name="databrew-ListRecipeVersions-request-uri-MaxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Name](#API_ListRecipeVersions_RequestSyntax) **   <a name="databrew-ListRecipeVersions-request-uri-Name"></a>
The name of the recipe for which to return version information.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [NextToken](#API_ListRecipeVersions_RequestSyntax) **   <a name="databrew-ListRecipeVersions-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body
<a name="API_ListRecipeVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecipeVersions_ResponseSyntax"></a>

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
<a name="API_ListRecipeVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Recipes](#API_ListRecipeVersions_ResponseSyntax) **   <a name="databrew-ListRecipeVersions-response-Recipes"></a>
A list of versions for the specified recipe.
Type: Array of [Recipe](API_Recipe.md) objects

 ** [NextToken](#API_ListRecipeVersions_ResponseSyntax) **   <a name="databrew-ListRecipeVersions-response-NextToken"></a>
A token that you can use in a subsequent call to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListRecipeVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListRecipeVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/ListRecipeVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ListRecipeVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
