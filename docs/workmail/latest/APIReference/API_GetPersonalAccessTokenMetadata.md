---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetPersonalAccessTokenMetadata.html
---

# GetPersonalAccessTokenMetadata
<a name="API_GetPersonalAccessTokenMetadata"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Requests details of a specific Personal Access Token within the WorkMail organization.

## Request Syntax
<a name="API_GetPersonalAccessTokenMetadata_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}",
   "PersonalAccessTokenId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPersonalAccessTokenMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_GetPersonalAccessTokenMetadata_RequestSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-request-OrganizationId"></a>
 The Organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [PersonalAccessTokenId](#API_GetPersonalAccessTokenMetadata_RequestSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-request-PersonalAccessTokenId"></a>
 The Personal Access Token ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_GetPersonalAccessTokenMetadata_ResponseSyntax"></a>

```
{
   "DateCreated": number,
   "DateLastUsed": number,
   "ExpiresTime": number,
   "Name": "string",
   "PersonalAccessTokenId": "string",
   "Scopes": [ "string" ],
   "UserId": "string"
}
```

## Response Elements
<a name="API_GetPersonalAccessTokenMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DateCreated](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-DateCreated"></a>
 The date when the Personal Access Token ID was created.
Type: Timestamp

 ** [DateLastUsed](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-DateLastUsed"></a>
 The date when the Personal Access Token ID was last used.
Type: Timestamp

 ** [ExpiresTime](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-ExpiresTime"></a>
 The time when the Personal Access Token ID will expire.
Type: Timestamp

 ** [Name](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-Name"></a>
 The Personal Access Token name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`

 ** [PersonalAccessTokenId](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-PersonalAccessTokenId"></a>
 The Personal Access Token ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [Scopes](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-Scopes"></a>
 Lists all the Personal Access Token permissions for a mailbox.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`

 ** [UserId](#API_GetPersonalAccessTokenMetadata_ResponseSyntax) **   <a name="workmail-GetPersonalAccessTokenMetadata-response-UserId"></a>
 The WorkMail User ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.

## Errors
<a name="API_GetPersonalAccessTokenMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** ResourceNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_GetPersonalAccessTokenMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetPersonalAccessTokenMetadata)
