---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetAccountPreferences.html
---

# GetAccountPreferences
<a name="API_GetAccountPreferences"></a>

Returns Amazon Q Developer account preferences.

## Request Syntax
<a name="API_GetAccountPreferences_RequestSyntax"></a>

```
POST /get-account-preferences HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountPreferences_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountPreferences": {
      "TrainingDataCollectionEnabled": boolean,
      "UserAuthorizationRequired": boolean
   }
}
```

## Response Elements
<a name="API_GetAccountPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountPreferences](#API_GetAccountPreferences_ResponseSyntax) **   <a name="qdevinchatapps-GetAccountPreferences-response-AccountPreferences"></a>
The preferences related to Amazon Q Developer usage in the calling AWS account.
Type: [AccountPreferences](API_AccountPreferences.md) object

## Errors
<a name="API_GetAccountPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GetAccountPreferencesException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

## See Also
<a name="API_GetAccountPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/GetAccountPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/GetAccountPreferences)
