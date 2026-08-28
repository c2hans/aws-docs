---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AcceptAccountLinkInvitation.html
---

# AcceptAccountLinkInvitation
<a name="API_AcceptAccountLinkInvitation"></a>

Accepts the account link invitation.

**Important**
There's currently no unlinking capability after you accept the account linking invitation.

## Request Syntax
<a name="API_AcceptAccountLinkInvitation_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "LinkId": "{{string}}"
}
```

## Request Parameters
<a name="API_AcceptAccountLinkInvitation_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_AcceptAccountLinkInvitation_RequestSyntax) **   <a name="WorkSpaces-AcceptAccountLinkInvitation-request-ClientToken"></a>
A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.
Type: String
Pattern: `^.{1,64}$`
Required: No

 ** [LinkId](#API_AcceptAccountLinkInvitation_RequestSyntax) **   <a name="WorkSpaces-AcceptAccountLinkInvitation-request-LinkId"></a>
The identifier of the account link.
Type: String
Pattern: `^link-.{8,24}$`
Required: Yes

## Response Syntax
<a name="API_AcceptAccountLinkInvitation_ResponseSyntax"></a>

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
<a name="API_AcceptAccountLinkInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountLink](#API_AcceptAccountLinkInvitation_ResponseSyntax) **   <a name="WorkSpaces-AcceptAccountLinkInvitation-response-AccountLink"></a>
Information about the account link.
Type: [AccountLink](API_AccountLink.md) object

## Errors
<a name="API_AcceptAccountLinkInvitation_Errors"></a>

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

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
You either haven't provided a `TargetAccountId` or are using the same value for `TargetAccountId` and `SourceAccountId`.
HTTP Status Code: 400

## See Also
<a name="API_AcceptAccountLinkInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/AcceptAccountLinkInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AcceptAccountLinkInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
