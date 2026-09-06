---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateAccountLinkInvitation.html
---

# CreateAccountLinkInvitation
<a name="API_CreateAccountLinkInvitation"></a>

Creates the account link invitation.

## Request Syntax
<a name="API_CreateAccountLinkInvitation_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "TargetAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateAccountLinkInvitation_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateAccountLinkInvitation_RequestSyntax) **   <a name="WorkSpaces-CreateAccountLinkInvitation-request-ClientToken"></a>
A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.
Type: String
Pattern: `^.{1,64}$`
Required: No

 ** [TargetAccountId](#API_CreateAccountLinkInvitation_RequestSyntax) **   <a name="WorkSpaces-CreateAccountLinkInvitation-request-TargetAccountId"></a>
The identifier of the target account.
Type: String
Pattern: `^\d{12}$`
Required: Yes

## Response Syntax
<a name="API_CreateAccountLinkInvitation_ResponseSyntax"></a>

```
{
   "AccountLink": {
      "AccountLinkId": "string",
      "AccountLinkStatus": "string",
      "SourceAccountId": "string",
      "TargetAccountId": "string"
   }
}
```

## Response Elements
<a name="API_CreateAccountLinkInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountLink](#API_CreateAccountLinkInvitation_ResponseSyntax) **   <a name="WorkSpaces-CreateAccountLinkInvitation-response-AccountLink"></a>
Information about the account link.
Type: [AccountLink](API_AccountLink.md) object

## Errors
<a name="API_CreateAccountLinkInvitation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** ConflictException **
The `TargetAccountId` is already linked or invited.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected server error occured.
HTTP Status Code: 400

 ** ValidationException **
You either haven't provided a `TargetAccountId` or are using the same value for `TargetAccountId` and `SourceAccountId`.
HTTP Status Code: 400

## See Also
<a name="API_CreateAccountLinkInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateAccountLinkInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateAccountLinkInvitation)
