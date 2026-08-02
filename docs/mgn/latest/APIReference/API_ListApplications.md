---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Retrieves all applications or multiple applications by ID.

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
POST /ListApplications HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "filters": {
      "applicationIDs": [ "{{string}}" ],
      "isArchived": {{boolean}},
      "waveIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListApplications_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_ListApplications_RequestSyntax) **   <a name="mgn-ListApplications-request-accountID"></a>
Applications list Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [filters](#API_ListApplications_RequestSyntax) **   <a name="mgn-ListApplications-request-filters"></a>
Applications list filters.
Type: [ListApplicationsRequestFilters](API_ListApplicationsRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListApplications_RequestSyntax) **   <a name="mgn-ListApplications-request-maxResults"></a>
Maximum results to return when listing applications.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="mgn-ListApplications-request-nextToken"></a>
Request next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "applicationAggregatedStatus": {
            "healthStatus": "string",
            "lastUpdateDateTime": "string",
            "progressStatus": "string",
            "totalSourceServers": number
         },
         "applicationID": "string",
         "arn": "string",
         "creationDateTime": "string",
         "description": "string",
         "isArchived": boolean,
         "lastModifiedDateTime": "string",
         "name": "string",
         "tags": {
            "string" : "string"
         },
         "waveID": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListApplications_ResponseSyntax) **   <a name="mgn-ListApplications-response-items"></a>
Applications list.
Type: Array of [Application](API_Application.md) objects

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="mgn-ListApplications-response-nextToken"></a>
Response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListApplications)
