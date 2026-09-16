---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListRelays.html
---

# ListRelays
<a name="API_ListRelays"></a>

Lists all the existing relay resources.

## Request Syntax
<a name="API_ListRelays_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## Request Parameters
<a name="API_ListRelays_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListRelays_RequestSyntax) **   <a name="sesmailmanager-ListRelays-request-NextToken"></a>
If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PageSize](#API_ListRelays_RequestSyntax) **   <a name="sesmailmanager-ListRelays-request-PageSize"></a>
The number of relays to be returned in one request.
Type: Integer
Required: No

## Response Syntax
<a name="API_ListRelays_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Relays": [
      {
         "LastModifiedTimestamp": number,
         "RelayId": "string",
         "RelayName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRelays_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRelays_ResponseSyntax) **   <a name="sesmailmanager-ListRelays-response-NextToken"></a>
If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Relays](#API_ListRelays_ResponseSyntax) **   <a name="sesmailmanager-ListRelays-response-Relays"></a>
The list of returned relays.
Type: Array of [Relay](API_Relay.md) objects

## Errors
<a name="API_ListRelays_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_ListRelays_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/ListRelays)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ListRelays)
