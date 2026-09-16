---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddonSubscription.html
---

# CreateAddonSubscription
<a name="API_CreateAddonSubscription"></a>

Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.

## Request Syntax
<a name="API_CreateAddonSubscription_RequestSyntax"></a>

```
{
   "AddonName": "{{string}}",
   "ClientToken": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAddonSubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddonName](#API_CreateAddonSubscription_RequestSyntax) **   <a name="sesmailmanager-CreateAddonSubscription-request-AddonName"></a>
The name of the Add On to subscribe to. You can only have one subscription for each Add On name.
Type: String
Required: Yes

 ** [ClientToken](#API_CreateAddonSubscription_RequestSyntax) **   <a name="sesmailmanager-CreateAddonSubscription-request-ClientToken"></a>
A unique token that Amazon SES uses to recognize subsequent retries of the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Tags](#API_CreateAddonSubscription_RequestSyntax) **   <a name="sesmailmanager-CreateAddonSubscription-request-Tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateAddonSubscription_ResponseSyntax"></a>

```
{
   "AddonSubscriptionId": "string"
}
```

## Response Elements
<a name="API_CreateAddonSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddonSubscriptionId](#API_CreateAddonSubscription_ResponseSyntax) **   <a name="sesmailmanager-CreateAddonSubscription-response-AddonSubscriptionId"></a>
The unique ID of the Add On subscription created by this API.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `as-[a-zA-Z0-9]{1,64}`

## Errors
<a name="API_CreateAddonSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateAddonSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateAddonSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateAddonSubscription)
