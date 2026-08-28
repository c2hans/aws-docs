---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListWaves.html
---

# ListWaves
<a name="API_ListWaves"></a>

Retrieves all waves or multiple waves by ID.

## Request Syntax
<a name="API_ListWaves_RequestSyntax"></a>

```
POST /ListWaves HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "filters": {
      "isArchived": {{boolean}},
      "waveIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWaves_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWaves_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_ListWaves_RequestSyntax) **   <a name="mgn-ListWaves-request-accountID"></a>
Request account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [filters](#API_ListWaves_RequestSyntax) **   <a name="mgn-ListWaves-request-filters"></a>
Waves list filters.
Type: [ListWavesRequestFilters](API_ListWavesRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListWaves_RequestSyntax) **   <a name="mgn-ListWaves-request-maxResults"></a>
Maximum results to return when listing waves.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListWaves_RequestSyntax) **   <a name="mgn-ListWaves-request-nextToken"></a>
Request next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListWaves_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "creationDateTime": "string",
         "description": "string",
         "isArchived": boolean,
         "lastModifiedDateTime": "string",
         "name": "string",
         "tags": {
            "string" : "string"
         },
         "waveAggregatedStatus": {
            "healthStatus": "string",
            "lastUpdateDateTime": "string",
            "progressStatus": "string",
            "replicationStartedDateTime": "string",
            "totalApplications": number
         },
         "waveID": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWaves_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListWaves_ResponseSyntax) **   <a name="mgn-ListWaves-response-items"></a>
Waves list.
Type: Array of [Wave](API_Wave.md) objects

 ** [nextToken](#API_ListWaves_ResponseSyntax) **   <a name="mgn-ListWaves-response-nextToken"></a>
Response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListWaves_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

## See Also
<a name="API_ListWaves_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListWaves)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListWaves)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListWaves)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListWaves)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListWaves)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListWaves)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListWaves)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListWaves)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListWaves)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListWaves)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
