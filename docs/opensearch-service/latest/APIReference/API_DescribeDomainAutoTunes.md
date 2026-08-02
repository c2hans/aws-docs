---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainAutoTunes.html
---

# DescribeDomainAutoTunes
<a name="API_DescribeDomainAutoTunes"></a>

Returns the list of optimizations that Auto-Tune has made to an Amazon OpenSearch Service domain. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html).

## Request Syntax
<a name="API_DescribeDomainAutoTunes_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/autoTunes?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainAutoTunes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDomainAutoTunes_RequestSyntax) **   <a name="opensearchservice-DescribeDomainAutoTunes-request-uri-DomainName"></a>
Name of the domain that you want Auto-Tune details about.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [MaxResults](#API_DescribeDomainAutoTunes_RequestSyntax) **   <a name="opensearchservice-DescribeDomainAutoTunes-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_DescribeDomainAutoTunes_RequestSyntax) **   <a name="opensearchservice-DescribeDomainAutoTunes-request-uri-NextToken"></a>
If your initial `DescribeDomainAutoTunes` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `DescribeDomainAutoTunes` operations, which returns results in the next page.

## Request Body
<a name="API_DescribeDomainAutoTunes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainAutoTunes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AutoTunes": [
      {
         "AutoTuneDetails": {
            "ScheduledAutoTuneDetails": {
               "Action": "string",
               "ActionType": "string",
               "Date": number,
               "Severity": "string"
            }
         },
         "AutoTuneType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDomainAutoTunes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoTunes](#API_DescribeDomainAutoTunes_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainAutoTunes-response-AutoTunes"></a>
The list of setting adjustments that Auto-Tune has made to the domain.
Type: Array of [AutoTune](API_AutoTune.md) objects

 ** [NextToken](#API_DescribeDomainAutoTunes_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainAutoTunes-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_DescribeDomainAutoTunes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDomainAutoTunes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomainAutoTunes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomainAutoTunes)
