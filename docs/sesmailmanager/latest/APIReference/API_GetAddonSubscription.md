---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddonSubscription.html
---

# GetAddonSubscription
<a name="API_GetAddonSubscription"></a>

Gets detailed information about an Add On subscription.

## Request Syntax
<a name="API_GetAddonSubscription_RequestSyntax"></a>

```
{
   "AddonSubscriptionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAddonSubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddonSubscriptionId](#API_GetAddonSubscription_RequestSyntax) **   <a name="sesmailmanager-GetAddonSubscription-request-AddonSubscriptionId"></a>
The Add On subscription ID to retrieve information for.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `as-[a-zA-Z0-9]{1,64}`
Required: Yes

## Response Syntax
<a name="API_GetAddonSubscription_ResponseSyntax"></a>

```
{
   "AddonName": "string",
   "AddonSubscriptionArn": "string",
   "CreatedTimestamp": number
}
```

## Response Elements
<a name="API_GetAddonSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddonName](#API_GetAddonSubscription_ResponseSyntax) **   <a name="sesmailmanager-GetAddonSubscription-response-AddonName"></a>
The name of the Add On for the subscription.
Type: String

 ** [AddonSubscriptionArn](#API_GetAddonSubscription_ResponseSyntax) **   <a name="sesmailmanager-GetAddonSubscription-response-AddonSubscriptionArn"></a>
Amazon Resource Name (ARN) for the subscription.
Type: String

 ** [CreatedTimestamp](#API_GetAddonSubscription_ResponseSyntax) **   <a name="sesmailmanager-GetAddonSubscription-response-CreatedTimestamp"></a>
The timestamp of when the Add On subscription was created.
Type: Timestamp

## Errors
<a name="API_GetAddonSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetAddonSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetAddonSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetAddonSubscription)
