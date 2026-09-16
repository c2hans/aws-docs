---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriberNotification.html
---

# CreateSubscriberNotification
<a name="API_CreateSubscriberNotification"></a>

Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.

## Request Syntax
<a name="API_CreateSubscriberNotification_RequestSyntax"></a>

```
POST /v1/subscribers/{{subscriberId}}/notification HTTP/1.1
Content-type: application/json

{
   "configuration": { ... }
}
```

## URI Request Parameters
<a name="API_CreateSubscriberNotification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [subscriberId](#API_CreateSubscriberNotification_RequestSyntax) **   <a name="securitylake-CreateSubscriberNotification-request-uri-subscriberId"></a>
The subscriber ID for the notification subscription.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_CreateSubscriberNotification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_CreateSubscriberNotification_RequestSyntax) **   <a name="securitylake-CreateSubscriberNotification-request-configuration"></a>
Specify the configuration using which you want to create the subscriber notification.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateSubscriberNotification_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "subscriberEndpoint": "string"
}
```

## Response Elements
<a name="API_CreateSubscriberNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subscriberEndpoint](#API_CreateSubscriberNotification_ResponseSyntax) **   <a name="securitylake-CreateSubscriberNotification-response-subscriberEndpoint"></a>
The subscriber endpoint to which exception messages are posted.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`

## Errors
<a name="API_CreateSubscriberNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific AWS action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.
 ** errorCode **
A coded string to provide more information about the access denied exception. You can use the error code to check the exception type.
HTTP Status Code: 403

 ** BadRequestException **
The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceName **
The resource name.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
That the rate of requests to Security Lake is exceeding the request quotas for your AWS account.
 ** retryAfterSeconds **
Retry the request after the specified time.
 ** serviceCode **
The code for the service in Service Quotas.
HTTP Status Code: 429

## See Also
<a name="API_CreateSubscriberNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/CreateSubscriberNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CreateSubscriberNotification)
