---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddonInstance.html
---

# CreateAddonInstance
<a name="API_CreateAddonInstance"></a>

Creates an Add On instance for the subscription indicated in the request. The resulting Amazon Resource Name (ARN) can be used in a conditional statement for a rule set or traffic policy.

## Request Syntax
<a name="API_CreateAddonInstance_RequestSyntax"></a>

```
{
   "AddonSubscriptionId": "{{string}}",
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
<a name="API_CreateAddonInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddonSubscriptionId](#API_CreateAddonInstance_RequestSyntax) **   <a name="sesmailmanager-CreateAddonInstance-request-AddonSubscriptionId"></a>
The unique ID of a previously created subscription that an Add On instance is created for. You can only have one instance per subscription.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `as-[a-zA-Z0-9]{1,64}`
Required: Yes

 ** [ClientToken](#API_CreateAddonInstance_RequestSyntax) **   <a name="sesmailmanager-CreateAddonInstance-request-ClientToken"></a>
A unique token that Amazon SES uses to recognize subsequent retries of the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Tags](#API_CreateAddonInstance_RequestSyntax) **   <a name="sesmailmanager-CreateAddonInstance-request-Tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateAddonInstance_ResponseSyntax"></a>

```
{
   "AddonInstanceId": "string"
}
```

## Response Elements
<a name="API_CreateAddonInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddonInstanceId](#API_CreateAddonInstance_ResponseSyntax) **   <a name="sesmailmanager-CreateAddonInstance-response-AddonInstanceId"></a>
The unique ID of the Add On instance created by this API.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `ai-[a-zA-Z0-9]{1,64}`

## Errors
<a name="API_CreateAddonInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateAddonInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateAddonInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateAddonInstance)
