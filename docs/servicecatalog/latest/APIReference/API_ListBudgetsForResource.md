---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListBudgetsForResource.html
---

# ListBudgetsForResource
<a name="API_ListBudgetsForResource"></a>

Lists all the budgets associated to the specified resource.

## Request Syntax
<a name="API_ListBudgetsForResource_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBudgetsForResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListBudgetsForResource_RequestSyntax) **   <a name="servicecatalog-ListBudgetsForResource-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PageSize](#API_ListBudgetsForResource_RequestSyntax) **   <a name="servicecatalog-ListBudgetsForResource-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListBudgetsForResource_RequestSyntax) **   <a name="servicecatalog-ListBudgetsForResource-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [ResourceId](#API_ListBudgetsForResource_RequestSyntax) **   <a name="servicecatalog-ListBudgetsForResource-request-ResourceId"></a>
The resource identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListBudgetsForResource_ResponseSyntax"></a>

```
{
   "Budgets": [
      {
         "BudgetName": "string"
      }
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_ListBudgetsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Budgets](#API_ListBudgetsForResource_ResponseSyntax) **   <a name="servicecatalog-ListBudgetsForResource-response-Budgets"></a>
Information about the associated budgets.
Type: Array of [BudgetDetail](API_BudgetDetail.md) objects

 ** [NextPageToken](#API_ListBudgetsForResource_ResponseSyntax) **   <a name="servicecatalog-ListBudgetsForResource-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

## Errors
<a name="API_ListBudgetsForResource_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListBudgetsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListBudgetsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListBudgetsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
