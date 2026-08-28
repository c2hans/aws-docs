---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_ExpireSession.html
---

# ExpireSession
<a name="API_ExpireSession"></a>

Expires an active secure browser session.

## Request Syntax
<a name="API_ExpireSession_RequestSyntax"></a>

```
DELETE /portals/{{portalId}}/sessions/{{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ExpireSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [portalId](#API_ExpireSession_RequestSyntax) **   <a name="workspacesweb-ExpireSession-request-uri-portalId"></a>
The ID of the web portal for the session.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

 ** [sessionId](#API_ExpireSession_RequestSyntax) **   <a name="workspacesweb-ExpireSession-request-uri-sessionId"></a>
The ID of the session to expire.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

## Request Body
<a name="API_ExpireSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ExpireSession_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ExpireSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ExpireSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
There is an internal server error.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource cannot be found.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
There is a throttling error.
 ** quotaCode **
The originating quota.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
 ** serviceCode **
The originating service.
HTTP Status Code: 429

 ** ValidationException **
There is a validation error.
 ** fieldList **
The field that caused the error.
 ** reason **
Reason the request failed validation
HTTP Status Code: 400

## See Also
<a name="API_ExpireSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/ExpireSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/ExpireSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
