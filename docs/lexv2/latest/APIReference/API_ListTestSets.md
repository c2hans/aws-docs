---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestSets.html
---

# ListTestSets
<a name="API_ListTestSets"></a>

The list of the test sets

## Request Syntax
<a name="API_ListTestSets_RequestSyntax"></a>

```
POST /testsets HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListTestSets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTestSets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTestSets_RequestSyntax) **   <a name="lexv2-ListTestSets-request-maxResults"></a>
The maximum number of test sets to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestSets_RequestSyntax) **   <a name="lexv2-ListTestSets-request-nextToken"></a>
If the response from the ListTestSets operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.
Type: String
Required: No

 ** [sortBy](#API_ListTestSets_RequestSyntax) **   <a name="lexv2-ListTestSets-request-sortBy"></a>
The sort order for the list of test sets.
Type: [TestSetSortBy](API_TestSetSortBy.md) object
Required: No

## Response Syntax
<a name="API_ListTestSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "testSets": [
      {
         "creationDateTime": number,
         "description": "string",
         "lastUpdatedDateTime": number,
         "modality": "string",
         "numTurns": number,
         "roleArn": "string",
         "status": "string",
         "storageLocation": {
            "kmsKeyArn": "string",
            "s3BucketName": "string",
            "s3Path": "string"
         },
         "testSetId": "string",
         "testSetName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTestSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTestSets_ResponseSyntax) **   <a name="lexv2-ListTestSets-response-nextToken"></a>
A token that indicates whether there are more results to return in a response to the ListTestSets operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListTestSets operation request to get the next page of results.
Type: String

 ** [testSets](#API_ListTestSets_ResponseSyntax) **   <a name="lexv2-ListTestSets-response-testSets"></a>
The selected test sets in a list of test sets.
Type: Array of [TestSetSummary](API_TestSetSummary.md) objects

## Errors
<a name="API_ListTestSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListTestSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListTestSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListTestSets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
