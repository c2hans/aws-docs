---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddressList.html
---

# GetAddressList
<a name="API_GetAddressList"></a>

Fetch attributes of an address list.

## Request Syntax
<a name="API_GetAddressList_RequestSyntax"></a>

```
{
   "AddressListId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAddressList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressListId](#API_GetAddressList_RequestSyntax) **   <a name="sesmailmanager-GetAddressList-request-AddressListId"></a>
The identifier of an existing address list resource to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetAddressList_ResponseSyntax"></a>

```
{
   "AddressListArn": "string",
   "AddressListId": "string",
   "AddressListName": "string",
   "CreatedTimestamp": number,
   "LastUpdatedTimestamp": number
}
```

## Response Elements
<a name="API_GetAddressList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddressListArn](#API_GetAddressList_ResponseSyntax) **   <a name="sesmailmanager-GetAddressList-response-AddressListArn"></a>
The Amazon Resource Name (ARN) of the address list resource.
Type: String

 ** [AddressListId](#API_GetAddressList_ResponseSyntax) **   <a name="sesmailmanager-GetAddressList-response-AddressListId"></a>
The identifier of the address list resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`

 ** [AddressListName](#API_GetAddressList_ResponseSyntax) **   <a name="sesmailmanager-GetAddressList-response-AddressListName"></a>
A user-friendly name for the address list resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [CreatedTimestamp](#API_GetAddressList_ResponseSyntax) **   <a name="sesmailmanager-GetAddressList-response-CreatedTimestamp"></a>
The date of when then address list was created.
Type: Timestamp

 ** [LastUpdatedTimestamp](#API_GetAddressList_ResponseSyntax) **   <a name="sesmailmanager-GetAddressList-response-LastUpdatedTimestamp"></a>
The date of when the address list was last updated.
Type: Timestamp

## Errors
<a name="API_GetAddressList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetAddressList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetAddressList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetAddressList)
