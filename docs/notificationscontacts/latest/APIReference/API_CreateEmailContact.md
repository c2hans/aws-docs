---
source_url: https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_CreateEmailContact.html
---

# CreateEmailContact
<a name="API_CreateEmailContact"></a>

Creates an email contact for the provided email address.

## Request Syntax
<a name="API_CreateEmailContact_RequestSyntax"></a>

```
POST /2022-09-19/emailcontacts HTTP/1.1
Content-type: application/json

{
   "emailAddress": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEmailContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEmailContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [emailAddress](#API_CreateEmailContact_RequestSyntax) **   <a name="notificationscontacts-CreateEmailContact-request-emailAddress"></a>
The email address this email contact points to. The activation email and any subscribed emails are sent here.
This email address can't receive emails until it's activated.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 254.
Pattern: `(.+)@(.+)`
Required: Yes

 ** [name](#API_CreateEmailContact_RequestSyntax) **   <a name="notificationscontacts-CreateEmailContact-request-name"></a>
The name of the email contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[\w-.~]+.*`
Required: Yes

 ** [tags](#API_CreateEmailContact_RequestSyntax) **   <a name="notificationscontacts-CreateEmailContact-request-tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateEmailContact_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_CreateEmailContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateEmailContact_ResponseSyntax) **   <a name="notificationscontacts-CreateEmailContact-response-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}`

## Errors
<a name="API_CreateEmailContact_Errors"></a>

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

 ** ServiceQuotaExceededException **
 Request would cause a service quota to be exceeded.
 ** quotaCode **
The code for the service quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** resourceId **
The ID of the resource that exceeds the service quota.
 ** resourceType **
The type of the resource that exceeds the service quota.
 ** serviceCode **
The code for the service quota exceeded in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 402

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
<a name="API_CreateEmailContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notificationscontacts-2018-05-10/CreateEmailContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notificationscontacts-2018-05-10/CreateEmailContact)
