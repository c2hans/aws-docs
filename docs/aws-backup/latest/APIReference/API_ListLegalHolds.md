---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListLegalHolds.html
---

# ListLegalHolds
<a name="API_ListLegalHolds"></a>

This action returns metadata about active and previous legal holds.

## Request Syntax
<a name="API_ListLegalHolds_RequestSyntax"></a>

```
GET /legal-holds/?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLegalHolds_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListLegalHolds_RequestSyntax) **   <a name="Backup-ListLegalHolds-request-uri-MaxResults"></a>
The maximum number of resource list items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListLegalHolds_RequestSyntax) **   <a name="Backup-ListLegalHolds-request-uri-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListLegalHolds_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLegalHolds_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LegalHolds": [
      {
         "CancellationDate": number,
         "CreationDate": number,
         "Description": "string",
         "LegalHoldArn": "string",
         "LegalHoldId": "string",
         "Status": "string",
         "Title": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLegalHolds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LegalHolds](#API_ListLegalHolds_ResponseSyntax) **   <a name="Backup-ListLegalHolds-response-LegalHolds"></a>
This is an array of returned legal holds, both active and previous.
Type: Array of [LegalHold](API_LegalHold.md) objects

 ** [NextToken](#API_ListLegalHolds_ResponseSyntax) **   <a name="Backup-ListLegalHolds-response-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

## Errors
<a name="API_ListLegalHolds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListLegalHolds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListLegalHolds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListLegalHolds)
