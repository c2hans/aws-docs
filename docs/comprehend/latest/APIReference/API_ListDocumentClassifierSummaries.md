---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDocumentClassifierSummaries.html
---

# ListDocumentClassifierSummaries
<a name="API_ListDocumentClassifierSummaries"></a>

Gets a list of summaries of the document classifiers that you have created

## Request Syntax
<a name="API_ListDocumentClassifierSummaries_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDocumentClassifierSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDocumentClassifierSummaries_RequestSyntax) **   <a name="comprehend-ListDocumentClassifierSummaries-request-MaxResults"></a>
The maximum number of results to return on each page. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListDocumentClassifierSummaries_RequestSyntax) **   <a name="comprehend-ListDocumentClassifierSummaries-request-NextToken"></a>
Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListDocumentClassifierSummaries_ResponseSyntax"></a>

```
{
   "DocumentClassifierSummariesList": [
      {
         "DocumentClassifierName": "string",
         "LatestVersionCreatedAt": number,
         "LatestVersionName": "string",
         "LatestVersionStatus": "string",
         "NumberOfVersions": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDocumentClassifierSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentClassifierSummariesList](#API_ListDocumentClassifierSummaries_ResponseSyntax) **   <a name="comprehend-ListDocumentClassifierSummaries-response-DocumentClassifierSummariesList"></a>
The list of summaries of document classifiers.
Type: Array of [DocumentClassifierSummary](API_DocumentClassifierSummary.md) objects

 ** [NextToken](#API_ListDocumentClassifierSummaries_ResponseSyntax) **   <a name="comprehend-ListDocumentClassifierSummaries-response-NextToken"></a>
Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListDocumentClassifierSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is invalid.
 ** Detail **
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** TooManyRequestsException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 400

## See Also
<a name="API_ListDocumentClassifierSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ListDocumentClassifierSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ListDocumentClassifierSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
