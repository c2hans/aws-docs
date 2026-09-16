---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListConnections.html
---

# ListConnections
<a name="API_ListConnections"></a>

Retrieves a list of connections from the account.

## Request Syntax
<a name="API_ListConnections_RequestSyntax"></a>

```
{
   "ConnectionState": "{{string}}",
   "Limit": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionState](#API_ListConnections_RequestSyntax) **   <a name="eventbridge-ListConnections-request-ConnectionState"></a>
The state of the connection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AUTHORIZED | DEAUTHORIZED | AUTHORIZING | DEAUTHORIZING | ACTIVE | FAILED_CONNECTIVITY`
Required: No

 ** [Limit](#API_ListConnections_RequestSyntax) **   <a name="eventbridge-ListConnections-request-Limit"></a>
The maximum number of connections to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListConnections_RequestSyntax) **   <a name="eventbridge-ListConnections-request-NamePrefix"></a>
A name prefix to filter results returned. Only connections with a name that starts with the prefix are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListConnections_RequestSyntax) **   <a name="eventbridge-ListConnections-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListConnections_ResponseSyntax"></a>

```
{
   "Connections": [
      {
         "AuthorizationType": "string",
         "ConnectionArn": "string",
         "ConnectionState": "string",
         "CreationTime": number,
         "LastAuthorizedTime": number,
         "LastModifiedTime": number,
         "Name": "string",
         "StateReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connections](#API_ListConnections_ResponseSyntax) **   <a name="eventbridge-ListConnections-response-Connections"></a>
An array of connections objects that include details about the connections.
Type: Array of [Connection](API_Connection.md) objects

 ** [NextToken](#API_ListConnections_ResponseSyntax) **   <a name="eventbridge-ListConnections-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## See Also
<a name="API_ListConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListConnections)
