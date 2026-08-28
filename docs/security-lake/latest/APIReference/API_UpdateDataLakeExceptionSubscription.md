---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLakeExceptionSubscription.html
---

# UpdateDataLakeExceptionSubscription
<a name="API_UpdateDataLakeExceptionSubscription"></a>

Updates the specified notification subscription in Amazon Security Lake for the organization you specify.

## Request Syntax
<a name="API_UpdateDataLakeExceptionSubscription_RequestSyntax"></a>

```
PUT /v1/datalake/exceptions/subscription HTTP/1.1
Content-type: application/json

{
   "exceptionTimeToLive": {{number}},
   "notificationEndpoint": "{{string}}",
   "subscriptionProtocol": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataLakeExceptionSubscription_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateDataLakeExceptionSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [exceptionTimeToLive](#API_UpdateDataLakeExceptionSubscription_RequestSyntax) **   <a name="securitylake-UpdateDataLakeExceptionSubscription-request-exceptionTimeToLive"></a>
The time-to-live (TTL) for the exception message to remain. It is the duration of time until which the exception message remains.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** [notificationEndpoint](#API_UpdateDataLakeExceptionSubscription_RequestSyntax) **   <a name="securitylake-UpdateDataLakeExceptionSubscription-request-notificationEndpoint"></a>
The account that is subscribed to receive exception notifications.
Type: String
Pattern: `[\\\w\-_:/.@=+]*`
Required: Yes

 ** [subscriptionProtocol](#API_UpdateDataLakeExceptionSubscription_RequestSyntax) **   <a name="securitylake-UpdateDataLakeExceptionSubscription-request-subscriptionProtocol"></a>
The subscription protocol to which exception messages are posted.
Type: String
Pattern: `[a-z\-]*`
Required: Yes

## Response Syntax
<a name="API_UpdateDataLakeExceptionSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateDataLakeExceptionSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDataLakeExceptionSubscription_Errors"></a>

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
<a name="API_UpdateDataLakeExceptionSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/UpdateDataLakeExceptionSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
