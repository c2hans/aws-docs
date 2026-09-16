---
source_url: https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_GetEmailContact.html
---

# GetEmailContact
<a name="API_GetEmailContact"></a>

Returns an email contact.

## Request Syntax
<a name="API_GetEmailContact_RequestSyntax"></a>

```
GET /emailcontacts/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEmailContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetEmailContact_RequestSyntax) **   <a name="notificationscontacts-GetEmailContact-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the email contact to get.
Pattern: `arn:[a-z-]{3,10}:notifications-contacts::[0-9]{12}:emailcontact/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_GetEmailContact_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEmailContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "emailContact": {
      "address": "string",
      "arn": "string",
      "creationTime": "string",
      "name": "string",
      "status": "string",
      "updateTime": "string"
   }
}
```

## Response Elements
<a name="API_GetEmailContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [emailContact](#API_GetEmailContact_ResponseSyntax) **   <a name="notificationscontacts-GetEmailContact-response-emailContact"></a>
The email contact for the provided email address.
Type: [EmailContact](API_EmailContact.md) object

## Errors
<a name="API_GetEmailContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetEmailContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notificationscontacts-2018-05-10/GetEmailContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notificationscontacts-2018-05-10/GetEmailContact)
