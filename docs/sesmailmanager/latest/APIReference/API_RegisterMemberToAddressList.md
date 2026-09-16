---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RegisterMemberToAddressList.html
---

# RegisterMemberToAddressList
<a name="API_RegisterMemberToAddressList"></a>

Adds a member to an address list.

## Request Syntax
<a name="API_RegisterMemberToAddressList_RequestSyntax"></a>

```
{
   "Address": "{{string}}",
   "AddressListId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterMemberToAddressList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Address](#API_RegisterMemberToAddressList_RequestSyntax) **   <a name="sesmailmanager-RegisterMemberToAddressList-request-Address"></a>
The address to be added to the address list.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 320.
Required: Yes

 ** [AddressListId](#API_RegisterMemberToAddressList_RequestSyntax) **   <a name="sesmailmanager-RegisterMemberToAddressList-request-AddressListId"></a>
The unique identifier of the address list where the address should be added.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Elements
<a name="API_RegisterMemberToAddressList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterMemberToAddressList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
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
<a name="API_RegisterMemberToAddressList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/RegisterMemberToAddressList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RegisterMemberToAddressList)
