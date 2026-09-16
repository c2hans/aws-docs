---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_ListRegisteredSubscriptionProviders.html
---

# ListRegisteredSubscriptionProviders
<a name="API_ListRegisteredSubscriptionProviders"></a>

List Bring Your Own License (BYOL) subscription registration resources for your account.

## Request Syntax
<a name="API_ListRegisteredSubscriptionProviders_RequestSyntax"></a>

```
POST /subscription/ListRegisteredSubscriptionProviders HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubscriptionProviderSources": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListRegisteredSubscriptionProviders_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRegisteredSubscriptionProviders_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRegisteredSubscriptionProviders_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListRegisteredSubscriptionProviders-request-MaxResults"></a>
The maximum items to return in a request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListRegisteredSubscriptionProviders_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListRegisteredSubscriptionProviders-request-NextToken"></a>
A token to specify where to start paginating. This is the nextToken from a previously truncated response.
Type: String
Required: No

 ** [SubscriptionProviderSources](#API_ListRegisteredSubscriptionProviders_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListRegisteredSubscriptionProviders-request-SubscriptionProviderSources"></a>
To filter your results, specify which subscription providers to return in the list.
Type: Array of strings
Valid Values: `RedHat`
Required: No

## Response Syntax
<a name="API_ListRegisteredSubscriptionProviders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RegisteredSubscriptionProviders": [
      {
         "LastSuccessfulDataRetrievalTime": "string",
         "SecretArn": "string",
         "SubscriptionProviderArn": "string",
         "SubscriptionProviderSource": "string",
         "SubscriptionProviderStatus": "string",
         "SubscriptionProviderStatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRegisteredSubscriptionProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRegisteredSubscriptionProviders_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListRegisteredSubscriptionProviders-response-NextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String

 ** [RegisteredSubscriptionProviders](#API_ListRegisteredSubscriptionProviders_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-ListRegisteredSubscriptionProviders-response-RegisteredSubscriptionProviders"></a>
The list of BYOL registration resources that fit the criteria you specified in the request.
Type: Array of [RegisteredSubscriptionProvider](API_RegisteredSubscriptionProvider.md) objects

## Errors
<a name="API_ListRegisteredSubscriptionProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListRegisteredSubscriptionProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/ListRegisteredSubscriptionProviders)
