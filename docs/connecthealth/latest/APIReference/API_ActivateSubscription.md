---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ActivateSubscription.html
---

# ActivateSubscription
<a name="API_ActivateSubscription"></a>

Activates a Subscription to enable billing for a user.

## Request Syntax
<a name="API_ActivateSubscription_RequestSyntax"></a>

```
POST /domains/{{domainId}}/subscriptions/{{subscriptionId}}/activate HTTP/1.1
```

## URI Request Parameters
<a name="API_ActivateSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_ActivateSubscription_RequestSyntax) **   <a name="connecthealth-ActivateSubscription-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** [subscriptionId](#API_ActivateSubscription_RequestSyntax) **   <a name="connecthealth-ActivateSubscription-request-uri-subscriptionId"></a>
The unique identifier of the Subscription.
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`
Required: Yes

## Request Body
<a name="API_ActivateSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ActivateSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "subscription": {
      "activatedAt": number,
      "arn": "string",
      "createdAt": number,
      "deactivatedAt": number,
      "domainId": "string",
      "lastUpdatedAt": number,
      "status": "string",
      "subscriptionId": "string"
   }
}
```

## Response Elements
<a name="API_ActivateSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subscription](#API_ActivateSubscription_ResponseSyntax) **   <a name="connecthealth-ActivateSubscription-response-subscription"></a>

Type: [SubscriptionDescription](API_SubscriptionDescription.md) object

## Errors
<a name="API_ActivateSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_ActivateSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/ActivateSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/ActivateSubscription)
