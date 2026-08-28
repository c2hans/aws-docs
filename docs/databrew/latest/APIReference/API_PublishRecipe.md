---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_PublishRecipe.html
---

# PublishRecipe
<a name="API_PublishRecipe"></a>

Publishes a new version of a DataBrew recipe.

## Request Syntax
<a name="API_PublishRecipe_RequestSyntax"></a>

```
POST /recipes/{{name}}/publishRecipe HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PublishRecipe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_PublishRecipe_RequestSyntax) **   <a name="databrew-PublishRecipe-request-uri-Name"></a>
The name of the recipe to be published.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_PublishRecipe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_PublishRecipe_RequestSyntax) **   <a name="databrew-PublishRecipe-request-Description"></a>
A description of the recipe to be published, for this version of the recipe.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_PublishRecipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_PublishRecipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_PublishRecipe_ResponseSyntax) **   <a name="databrew-PublishRecipe-response-Name"></a>
The name of the recipe that you published.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_PublishRecipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_PublishRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/PublishRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/PublishRecipe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
