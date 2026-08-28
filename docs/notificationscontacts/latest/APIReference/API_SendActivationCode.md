---
source_url: https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_SendActivationCode.html
---

# SendActivationCode
<a name="API_SendActivationCode"></a>

Sends an activation email to the email address associated with the specified email contact.

**Note**
It might take a few minutes for the activation email to arrive. If it doesn't arrive, check in your spam folder or try sending another activation email.

## Request Syntax
<a name="API_SendActivationCode_RequestSyntax"></a>

```
POST /2022-10-31/emailcontacts/{{arn}}/activate/send HTTP/1.1
```

## URI Request Parameters
<a name="API_SendActivationCode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_SendActivationCode_RequestSyntax) **   <a name="notificationscontacts-SendActivationCode-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Pattern: `arn:[a-z-]{3,10}:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_SendActivationCode_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_SendActivationCode_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendActivationCode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendActivationCode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID that prompted the conflict error.
 ** resourceType **
The resource type that prompted the conflict error.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Your request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_SendActivationCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notificationscontacts-2018-05-10/SendActivationCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notificationscontacts-2018-05-10/SendActivationCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications Contacts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notificationscontacts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
