---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateAccountPreferences.html
---

# UpdateAccountPreferences
<a name="API_UpdateAccountPreferences"></a>

Updates Amazon Q Developer account preferences.

## Request Syntax
<a name="API_UpdateAccountPreferences_RequestSyntax"></a>

```
POST /update-account-preferences HTTP/1.1
Content-type: application/json

{
   "TrainingDataCollectionEnabled": {{boolean}},
   "UserAuthorizationRequired": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateAccountPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAccountPreferences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TrainingDataCollectionEnabled](#API_UpdateAccountPreferences_RequestSyntax) **   <a name="qdevinchatapps-UpdateAccountPreferences-request-TrainingDataCollectionEnabled"></a>
 This paramater is *deprecated*. For more information about Amazon Q Developer service improvements, see [Amazon Q Developer service improvement](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/service-improvement.html) in the *Amazon Q Developer User Guide*.
Turns on training data collection.
This helps improve the Amazon Q Developer experience by allowing Amazon Q Developer to store and use your customer information, such as Amazon Q Developer configurations, notifications, user inputs, Amazon Q Developer generated responses, and interaction data. This data helps us to continuously improve and develop Artificial Intelligence (AI) technologies. Your data is not shared with any third parties and is protected using sophisticated controls to prevent unauthorized access and misuse. Amazon Q Developer does not store or use interactions in chat channels with Amazon Q for training AI technologies for Amazon Q Developer.
Type: Boolean
Required: No

 ** [UserAuthorizationRequired](#API_UpdateAccountPreferences_RequestSyntax) **   <a name="qdevinchatapps-UpdateAccountPreferences-request-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateAccountPreferences_ResponseSyntax"></a>

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
<a name="API_UpdateAccountPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountPreferences](#API_UpdateAccountPreferences_ResponseSyntax) **   <a name="qdevinchatapps-UpdateAccountPreferences-response-AccountPreferences"></a>
Preferences related to Amazon Q Developer usage in the calling AWS account.
Type: [AccountPreferences](API_AccountPreferences.md) object

## Errors
<a name="API_UpdateAccountPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** UpdateAccountPreferencesException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_UpdateAccountPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/UpdateAccountPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/UpdateAccountPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
