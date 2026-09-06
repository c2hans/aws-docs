---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListPersonalAccessTokens.html
---

# ListPersonalAccessTokens
<a name="API_ListPersonalAccessTokens"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Returns a summary of your Personal Access Tokens.

## Request Syntax
<a name="API_ListPersonalAccessTokens_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPersonalAccessTokens_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPersonalAccessTokens_RequestSyntax) **   <a name="workmail-ListPersonalAccessTokens-request-MaxResults"></a>
 The maximum amount of items that should be returned in a response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPersonalAccessTokens_RequestSyntax) **   <a name="workmail-ListPersonalAccessTokens-request-NextToken"></a>
 The token from the previous response to query the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`
Required: No

 ** [OrganizationId](#API_ListPersonalAccessTokens_RequestSyntax) **   <a name="workmail-ListPersonalAccessTokens-request-OrganizationId"></a>
 The Organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserId](#API_ListPersonalAccessTokens_RequestSyntax) **   <a name="workmail-ListPersonalAccessTokens-request-UserId"></a>
 The WorkMail User ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: No

## Response Syntax
<a name="API_ListPersonalAccessTokens_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PersonalAccessTokenSummaries": [
      {
         "DateCreated": number,
         "DateLastUsed": number,
         "ExpiresTime": number,
         "Name": "string",
         "PersonalAccessTokenId": "string",
         "Scopes": [ "string" ],
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPersonalAccessTokens_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPersonalAccessTokens_ResponseSyntax) **   <a name="workmail-ListPersonalAccessTokens-response-NextToken"></a>
 The token from the previous response to query the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`

 ** [PersonalAccessTokenSummaries](#API_ListPersonalAccessTokens_ResponseSyntax) **   <a name="workmail-ListPersonalAccessTokens-response-PersonalAccessTokenSummaries"></a>
 Lists all the personal tokens in an organization or user, if user ID is provided.
Type: Array of [PersonalAccessTokenSummary](API_PersonalAccessTokenSummary.md) objects

## Errors
<a name="API_ListPersonalAccessTokens_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** EntityStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You are performing an operation on a user, group, or resource that isn't in the expected state, such as trying to delete an active user.
HTTP Status Code: 400

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

## See Also
<a name="API_ListPersonalAccessTokens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/ListPersonalAccessTokens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListPersonalAccessTokens)
