---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListTagOptions.html
---

# ListTagOptions
<a name="API_ListTagOptions"></a>

Lists the specified TagOptions or all TagOptions.

## Request Syntax
<a name="API_ListTagOptions_RequestSyntax"></a>

```
{
   "Filters": {
      "Active": {{boolean}},
      "Key": "{{string}}",
      "Value": "{{string}}"
   },
   "PageSize": {{number}},
   "PageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagOptions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListTagOptions_RequestSyntax) **   <a name="servicecatalog-ListTagOptions-request-Filters"></a>
The search filters. If no search filters are specified, the output includes all TagOptions.
Type: [ListTagOptionsFilters](API_ListTagOptionsFilters.md) object
Required: No

 ** [PageSize](#API_ListTagOptions_RequestSyntax) **   <a name="servicecatalog-ListTagOptions-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListTagOptions_RequestSyntax) **   <a name="servicecatalog-ListTagOptions-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

## Response Syntax
<a name="API_ListTagOptions_ResponseSyntax"></a>

```
{
   "PageToken": "string",
   "TagOptionDetails": [
      {
         "Active": boolean,
         "Id": "string",
         "Key": "string",
         "Owner": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PageToken](#API_ListTagOptions_ResponseSyntax) **   <a name="servicecatalog-ListTagOptions-response-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [TagOptionDetails](#API_ListTagOptions_ResponseSyntax) **   <a name="servicecatalog-ListTagOptions-response-TagOptionDetails"></a>
Information about the TagOptions.
Type: Array of [TagOptionDetail](API_TagOptionDetail.md) objects

## Errors
<a name="API_ListTagOptions_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** TagOptionNotMigratedException **
An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the AWS Management Console to perform the migration process before retrying the operation.
HTTP Status Code: 400

## See Also
<a name="API_ListTagOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListTagOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListTagOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
