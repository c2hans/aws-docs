---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatches.html
---

# ListBuildBatches
<a name="API_ListBuildBatches"></a>

Retrieves the identifiers of your build batches in the current region.

## Request Syntax
<a name="API_ListBuildBatches_RequestSyntax"></a>

```
{
   "filter": {
      "status": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBuildBatches_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [filter](#API_ListBuildBatches_RequestSyntax) **   <a name="CodeBuild-ListBuildBatches-request-filter"></a>
A `BuildBatchFilter` object that specifies the filters for the search.
Type: [BuildBatchFilter](API_BuildBatchFilter.md) object
Required: No

 ** [maxResults](#API_ListBuildBatches_RequestSyntax) **   <a name="CodeBuild-ListBuildBatches-request-maxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListBuildBatches_RequestSyntax) **   <a name="CodeBuild-ListBuildBatches-request-nextToken"></a>
The `nextToken` value returned from a previous call to `ListBuildBatches`. This specifies the next item to return. To return the beginning of the list, exclude this parameter.
Type: String
Required: No

 ** [sortOrder](#API_ListBuildBatches_RequestSyntax) **   <a name="CodeBuild-ListBuildBatches-request-sortOrder"></a>
Specifies the sort order of the returned items. Valid values include:
+  `ASCENDING`: List the batch build identifiers in ascending order by identifier.
+  `DESCENDING`: List the batch build identifiers in descending order by identifier.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListBuildBatches_ResponseSyntax"></a>

```
{
   "ids": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBuildBatches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ids](#API_ListBuildBatches_ResponseSyntax) **   <a name="CodeBuild-ListBuildBatches-response-ids"></a>
An array of strings that contains the batch build identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

 ** [nextToken](#API_ListBuildBatches_ResponseSyntax) **   <a name="CodeBuild-ListBuildBatches-response-nextToken"></a>
If there are more items to return, this contains a token that is passed to a subsequent call to `ListBuildBatches` to retrieve the next set of items.
Type: String

## Errors
<a name="API_ListBuildBatches_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListBuildBatches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListBuildBatches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListBuildBatches)
