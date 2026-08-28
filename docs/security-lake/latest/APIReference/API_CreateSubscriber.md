---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriber.html
---

# CreateSubscriber
<a name="API_CreateSubscriber"></a>

Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current AWS Region.

## Request Syntax
<a name="API_CreateSubscriber_RequestSyntax"></a>

```
POST /v1/subscribers HTTP/1.1
Content-type: application/json

{
   "accessTypes": [ "{{string}}" ],
   "sources": [
      { ... }
   ],
   "subscriberDescription": "{{string}}",
   "subscriberIdentity": {
      "externalId": "{{string}}",
      "principal": "{{string}}"
   },
   "subscriberName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateSubscriber_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSubscriber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessTypes](#API_CreateSubscriber_RequestSyntax) **   <a name="securitylake-CreateSubscriber-request-accessTypes"></a>
The Amazon S3 or AWS Lake Formation access type.
Type: Array of strings
Valid Values: `LAKEFORMATION | S3`
Required: No

 ** [sources](#API_CreateSubscriber_RequestSyntax) **   <a name="securitylake-CreateSubscriber-request-sources"></a>
The supported AWS services from which logs and events are collected. Security Lake supports log and event collection for natively supported AWS services.
Type: Array of [LogSourceResource](API_LogSourceResource.md) objects
Required: Yes

 ** [subscriberDescription](#API_CreateSubscriber_RequestSyntax) **   <a name="securitylake-CreateSubscriber-request-subscriberDescription"></a>
The description for your subscriber account in Security Lake.
Type: String
Pattern: `[\\\w\s\-_:/,.@=+]*`
Required: No

 ** [subscriberIdentity](#API_CreateSubscriber_RequestSyntax) **   <a name="securitylake-CreateSubscriber-request-subscriberIdentity"></a>
The AWS identity used to access your data.
Type: [AwsIdentity](API_AwsIdentity.md) object
Required: Yes

 ** [subscriberName](#API_CreateSubscriber_RequestSyntax) **   <a name="securitylake-CreateSubscriber-request-subscriberName"></a>
The name of your Security Lake subscriber account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** [tags](#API_CreateSubscriber_RequestSyntax) **   <a name="securitylake-CreateSubscriber-request-tags"></a>
An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateSubscriber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "subscriber": {
      "accessTypes": [ "string" ],
      "createdAt": "string",
      "resourceShareArn": "string",
      "resourceShareName": "string",
      "roleArn": "string",
      "s3BucketArn": "string",
      "sources": [
         { ... }
      ],
      "subscriberArn": "string",
      "subscriberDescription": "string",
      "subscriberEndpoint": "string",
      "subscriberId": "string",
      "subscriberIdentity": {
         "externalId": "string",
         "principal": "string"
      },
      "subscriberName": "string",
      "subscriberStatus": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateSubscriber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subscriber](#API_CreateSubscriber_ResponseSyntax) **   <a name="securitylake-CreateSubscriber-response-subscriber"></a>
Retrieve information about the subscriber created using the `CreateSubscriber` API.
Type: [SubscriberResource](API_SubscriberResource.md) object

## Errors
<a name="API_CreateSubscriber_Errors"></a>

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
<a name="API_CreateSubscriber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/CreateSubscriber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CreateSubscriber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
