---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_ListDataViews.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# ListDataViews
<a name="API_ListDataViews"></a>

Lists all available Dataviews for a Dataset.

## Request Syntax
<a name="API_ListDataViews_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}/dataviewsv2?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataViews_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_ListDataViews_RequestSyntax) **   <a name="finspace-ListDataViews-request-uri-datasetId"></a>
The unique identifier of the Dataset for which to retrieve Dataviews.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

 ** [maxResults](#API_ListDataViews_RequestSyntax) **   <a name="finspace-ListDataViews-request-uri-maxResults"></a>
The maximum number of results per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDataViews_RequestSyntax) **   <a name="finspace-ListDataViews-request-uri-nextToken"></a>
A token that indicates where a results page should begin.

## Request Body
<a name="API_ListDataViews_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataViews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataViews": [
      {
         "asOfTimestamp": number,
         "autoUpdate": boolean,
         "createTime": number,
         "datasetId": "string",
         "dataViewArn": "string",
         "dataViewId": "string",
         "destinationTypeProperties": {
            "destinationType": "string",
            "s3DestinationExportFileFormat": "string",
            "s3DestinationExportFileFormatOptions": {
               "string" : "string"
            }
         },
         "errorInfo": {
            "errorCategory": "string",
            "errorMessage": "string"
         },
         "lastModifiedTime": number,
         "partitionColumns": [ "string" ],
         "sortColumns": [ "string" ],
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataViews](#API_ListDataViews_ResponseSyntax) **   <a name="finspace-ListDataViews-response-dataViews"></a>
A list of Dataviews.
Type: Array of [DataViewSummary](API_DataViewSummary.md) objects

 ** [nextToken](#API_ListDataViews_ResponseSyntax) **   <a name="finspace-ListDataViews-response-nextToken"></a>
A token that indicates where a results page should begin.
Type: String

## Errors
<a name="API_ListDataViews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDataViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/ListDataViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/ListDataViews)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
