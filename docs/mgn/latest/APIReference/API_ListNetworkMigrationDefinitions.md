---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationDefinitions.html
---

# ListNetworkMigrationDefinitions
<a name="API_ListNetworkMigrationDefinitions"></a>

Lists all network migration definitions in the account, with optional filtering.

## Request Syntax
<a name="API_ListNetworkMigrationDefinitions_RequestSyntax"></a>

```
POST /network-migration/ListNetworkMigrationDefinitions HTTP/1.1
Content-type: application/json

{
   "filters": {
      "networkMigrationDefinitionIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListNetworkMigrationDefinitions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListNetworkMigrationDefinitions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListNetworkMigrationDefinitions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationDefinitions-request-filters"></a>
Filters to apply when listing network migration definitions.
Type: [ListNetworkMigrationDefinitionsRequestFilters](API_ListNetworkMigrationDefinitionsRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListNetworkMigrationDefinitions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationDefinitions-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListNetworkMigrationDefinitions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationDefinitions-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListNetworkMigrationDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "name": "string",
         "networkMigrationDefinitionID": "string",
         "scopeTags": {
            "string" : "string"
         },
         "sourceEnvironment": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNetworkMigrationDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListNetworkMigrationDefinitions_ResponseSyntax) **   <a name="mgn-ListNetworkMigrationDefinitions-response-items"></a>
A list of network migration definition summaries.
Type: Array of [NetworkMigrationDefinitionSummary](API_NetworkMigrationDefinitionSummary.md) objects

 ** [nextToken](#API_ListNetworkMigrationDefinitions_ResponseSyntax) **   <a name="mgn-ListNetworkMigrationDefinitions-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListNetworkMigrationDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operating denied due to a file permission or access check error.
HTTP Status Code: 403

## See Also
<a name="API_ListNetworkMigrationDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListNetworkMigrationDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListNetworkMigrationDefinitions)
