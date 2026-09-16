---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_DeregisterSubscriptionProvider.html
---

# DeregisterSubscriptionProvider
<a name="API_DeregisterSubscriptionProvider"></a>

Remove a third-party subscription provider from the Bring Your Own License (BYOL) subscriptions registered to your account.

## Request Syntax
<a name="API_DeregisterSubscriptionProvider_RequestSyntax"></a>

```
POST /subscription/DeregisterSubscriptionProvider HTTP/1.1
Content-type: application/json

{
   "SubscriptionProviderArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeregisterSubscriptionProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeregisterSubscriptionProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SubscriptionProviderArn](#API_DeregisterSubscriptionProvider_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-DeregisterSubscriptionProvider-request-SubscriptionProviderArn"></a>
The Amazon Resource Name (ARN) of the subscription provider resource to deregister.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,510}/[a-z0-9-\.]{1,510}`
Required: Yes

## Response Syntax
<a name="API_DeregisterSubscriptionProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeregisterSubscriptionProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterSubscriptionProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Unable to find the requested AWS resource.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DeregisterSubscriptionProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/DeregisterSubscriptionProvider)
