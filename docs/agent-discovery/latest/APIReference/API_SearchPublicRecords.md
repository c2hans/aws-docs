---
source_url: https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_SearchPublicRecords.html
---

# SearchPublicRecords

Searches public records for agents, tools, skills, and other resources. Results combine keyword and semantic ranking and are returned most relevant first. Only the public descriptors of each record are returned.

## Request Syntax
<a name="API_SearchPublicRecords_RequestSyntax"></a>

```
POST /records/search HTTP/1.1
Content-type: application/json

{
   "filters": {{JSON value}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "query": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchPublicRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchPublicRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchPublicRecords_RequestSyntax) **   <a name="agentdiscovery-SearchPublicRecords-request-filters"></a>
A structured filter that narrows the results. Each condition applies an operator to a field: `$eq`, `$ne`, or `$in`. The `identifier` field also supports `$prefix`. To combine conditions, use a single `$and` or `$or` key whose value is an array of single-condition objects. Conditions can't be nested further.
You can filter on `identifier`, `domain`, `recordType`, `descriptorType`, `provenance`, and `recordVersion`. For example, `{"recordType": {"$eq": "AGENT"}}` returns only agents.
A filter can have at most 10 conditions. `$in` takes 1 to 25 values, and each value is a string of 1 to 512 characters. An empty filter (`{}`) is not valid.
Type: JSON value
Required: No

 ** [maxResults](#API_SearchPublicRecords_RequestSyntax) **   <a name="agentdiscovery-SearchPublicRecords-request-maxResults"></a>
The maximum number of records to return in one page of results. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_SearchPublicRecords_RequestSyntax) **   <a name="agentdiscovery-SearchPublicRecords-request-nextToken"></a>
The token returned by a previous request to get the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [query](#API_SearchPublicRecords_RequestSyntax) **   <a name="agentdiscovery-SearchPublicRecords-request-query"></a>
A natural language query that describes what you are looking for. The query is used for both keyword and semantic ranking.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_SearchPublicRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "records": [
      {
         "createdAt": number,
         "description": "string",
         "descriptors": {
            "string" : {
               "additionalData": {
                  "string" : "DescriptorEntry"
               },
               "data": "string",
               "source": {
                  "fromUrl": {
                     "url": "string"
                  }
               },
               "version": "string"
            }
         },
         "displayName": "string",
         "domain": "string",
         "identifier": { ... },
         "recordType": "string",
         "recordVersion": "string",
         "trustManifests": [
            {
               "contributor": "string",
               "provenance": [
                  {
                     "relation": "string",
                     "sourceId": "string"
                  }
               ]
            }
         ],
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_SearchPublicRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchPublicRecords_ResponseSyntax) **   <a name="agentdiscovery-SearchPublicRecords-response-nextToken"></a>
The token to pass in a later request to get the next page of results. This value is absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [records](#API_SearchPublicRecords_ResponseSyntax) **   <a name="agentdiscovery-SearchPublicRecords-response-records"></a>
The records that match the search, most relevant first.
Type: Array of [PublicRecord](API_PublicRecord.md) objects

## Errors
<a name="API_SearchPublicRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request failed because of an internal error. Retrying the same request is not likely to succeed.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because the request rate is too high. Reduce the request rate and try again.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints of the operation.
HTTP Status Code: 400

## See Also
<a name="API_SearchPublicRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-discovery-2022-07-26/SearchPublicRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-discovery-2022-07-26/SearchPublicRecords)
