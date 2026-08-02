---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListConnectors.html
---

# ListConnectors
<a name="API_ListConnectors"></a>

List Connectors.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
POST /ListConnectors HTTP/1.1
Content-type: application/json

{
   "filters": {
      "connectorIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListConnectors_RequestSyntax) **   <a name="mgn-ListConnectors-request-filters"></a>
List Connectors Request filters.
Type: [ListConnectorsRequestFilters](API_ListConnectorsRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListConnectors_RequestSyntax) **   <a name="mgn-ListConnectors-request-maxResults"></a>
List Connectors Request max results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListConnectors_RequestSyntax) **   <a name="mgn-ListConnectors-request-nextToken"></a>
List Connectors Request next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "connectorID": "string",
         "name": "string",
         "ssmCommandConfig": {
            "cloudWatchLogGroupName": "string",
            "cloudWatchOutputEnabled": boolean,
            "outputS3BucketName": "string",
            "s3OutputEnabled": boolean
         },
         "ssmInstanceID": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListConnectors_ResponseSyntax) **   <a name="mgn-ListConnectors-response-items"></a>
List connectors response items.
Type: Array of [Connector](API_Connector.md) objects

 ** [nextToken](#API_ListConnectors_ResponseSyntax) **   <a name="mgn-ListConnectors-response-nextToken"></a>
List connectors response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListConnectors)
