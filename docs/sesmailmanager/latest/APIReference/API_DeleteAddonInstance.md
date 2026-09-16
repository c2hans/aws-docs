---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteAddonInstance.html
---

# DeleteAddonInstance
<a name="API_DeleteAddonInstance"></a>

Deletes an Add On instance.

## Request Syntax
<a name="API_DeleteAddonInstance_RequestSyntax"></a>

```
{
   "AddonInstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAddonInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddonInstanceId](#API_DeleteAddonInstance_RequestSyntax) **   <a name="sesmailmanager-DeleteAddonInstance-request-AddonInstanceId"></a>
The Add On instance ID to delete.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `ai-[a-zA-Z0-9]{1,64}`
Required: Yes

## Response Elements
<a name="API_DeleteAddonInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAddonInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAddonInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/DeleteAddonInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/DeleteAddonInstance)
