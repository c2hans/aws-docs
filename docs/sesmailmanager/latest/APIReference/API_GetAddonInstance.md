---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddonInstance.html
---

# GetAddonInstance
<a name="API_GetAddonInstance"></a>

Gets detailed information about an Add On instance.

## Request Syntax
<a name="API_GetAddonInstance_RequestSyntax"></a>

```
{
   "AddonInstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAddonInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddonInstanceId](#API_GetAddonInstance_RequestSyntax) **   <a name="sesmailmanager-GetAddonInstance-request-AddonInstanceId"></a>
The Add On instance ID to retrieve information for.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `ai-[a-zA-Z0-9]{1,64}`
Required: Yes

## Response Syntax
<a name="API_GetAddonInstance_ResponseSyntax"></a>

```
{
   "AddonInstanceArn": "string",
   "AddonName": "string",
   "AddonSubscriptionId": "string",
   "CreatedTimestamp": number
}
```

## Response Elements
<a name="API_GetAddonInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddonInstanceArn](#API_GetAddonInstance_ResponseSyntax) **   <a name="sesmailmanager-GetAddonInstance-response-AddonInstanceArn"></a>
The Amazon Resource Name (ARN) of the Add On instance.
Type: String

 ** [AddonName](#API_GetAddonInstance_ResponseSyntax) **   <a name="sesmailmanager-GetAddonInstance-response-AddonName"></a>
The name of the Add On provider associated to the subscription of the instance.
Type: String

 ** [AddonSubscriptionId](#API_GetAddonInstance_ResponseSyntax) **   <a name="sesmailmanager-GetAddonInstance-response-AddonSubscriptionId"></a>
The subscription ID associated to the instance.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `as-[a-zA-Z0-9]{1,64}`

 ** [CreatedTimestamp](#API_GetAddonInstance_ResponseSyntax) **   <a name="sesmailmanager-GetAddonInstance-response-CreatedTimestamp"></a>
The timestamp of when the Add On instance was created.
Type: Timestamp

## Errors
<a name="API_GetAddonInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetAddonInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetAddonInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetAddonInstance)
