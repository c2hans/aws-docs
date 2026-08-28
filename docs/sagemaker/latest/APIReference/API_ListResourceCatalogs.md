---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListResourceCatalogs.html
---

# ListResourceCatalogs
<a name="API_ListResourceCatalogs"></a>

 Lists Amazon SageMaker Catalogs based on given filters and orders. The maximum number of `ResourceCatalog`s viewable is 1000.

## Request Syntax
<a name="API_ListResourceCatalogs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceCatalogs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-CreationTimeAfter"></a>
 Use this parameter to search for `ResourceCatalog`s created after a specific date and time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-CreationTimeBefore"></a>
 Use this parameter to search for `ResourceCatalog`s created before a specific date and time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-MaxResults"></a>
 The maximum number of results returned by `ListResourceCatalogs`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-NameContains"></a>
 A string that partially matches one or more `ResourceCatalog`s names. Filters `ResourceCatalog` by name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [NextToken](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-NextToken"></a>
 A token to resume pagination of `ListResourceCatalogs` results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-SortBy"></a>
 The value on which the resource catalog list is sorted.
Type: String
Valid Values: `CreationTime`
Required: No

 ** [SortOrder](#API_ListResourceCatalogs_RequestSyntax) **   <a name="sagemaker-ListResourceCatalogs-request-SortOrder"></a>
 The order in which the resource catalogs are listed.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListResourceCatalogs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceCatalogs": [
      {
         "CreationTime": number,
         "Description": "string",
         "ResourceCatalogArn": "string",
         "ResourceCatalogName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceCatalogs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceCatalogs_ResponseSyntax) **   <a name="sagemaker-ListResourceCatalogs-response-NextToken"></a>
 A token to resume pagination of `ListResourceCatalogs` results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [ResourceCatalogs](#API_ListResourceCatalogs_ResponseSyntax) **   <a name="sagemaker-ListResourceCatalogs-response-ResourceCatalogs"></a>
 A list of the requested `ResourceCatalog`s.
Type: Array of [ResourceCatalog](API_ResourceCatalog.md) objects

## Errors
<a name="API_ListResourceCatalogs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListResourceCatalogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListResourceCatalogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListResourceCatalogs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
