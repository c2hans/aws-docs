---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetBulkPublishDetails.html
---

# GetBulkPublishDetails
<a name="API_GetBulkPublishDetails"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Get the status of the last BulkPublish operation for an identity pool.

This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

## Request Syntax
<a name="API_GetBulkPublishDetails_RequestSyntax"></a>

```
POST /identitypools/{{IdentityPoolId}}/getBulkPublishDetails HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBulkPublishDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentityPoolId](#API_GetBulkPublishDetails_RequestSyntax) **   <a name="Cognito-GetBulkPublishDetails-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_GetBulkPublishDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBulkPublishDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BulkPublishCompleteTime": number,
   "BulkPublishStartTime": number,
   "BulkPublishStatus": "string",
   "FailureMessage": "string",
   "IdentityPoolId": "string"
}
```

## Response Elements
<a name="API_GetBulkPublishDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BulkPublishCompleteTime](#API_GetBulkPublishDetails_ResponseSyntax) **   <a name="Cognito-GetBulkPublishDetails-response-BulkPublishCompleteTime"></a>
If BulkPublishStatus is SUCCEEDED, the time the last bulk publish operation completed.
Type: Timestamp

 ** [BulkPublishStartTime](#API_GetBulkPublishDetails_ResponseSyntax) **   <a name="Cognito-GetBulkPublishDetails-response-BulkPublishStartTime"></a>
The date/time at which the last bulk publish was initiated.
Type: Timestamp

 ** [BulkPublishStatus](#API_GetBulkPublishDetails_ResponseSyntax) **   <a name="Cognito-GetBulkPublishDetails-response-BulkPublishStatus"></a>
Status of the last bulk publish operation, valid values are:
+ NOT\_STARTED - No bulk publish has been requested for this identity pool
+ IN\_PROGRESS - Data is being published to the configured stream
+ SUCCEEDED - All data for the identity pool has been published to the configured stream
+ FAILED - Some portion of the data has failed to publish, check FailureMessage for the cause.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | FAILED | SUCCEEDED`

 ** [FailureMessage](#API_GetBulkPublishDetails_ResponseSyntax) **   <a name="Cognito-GetBulkPublishDetails-response-FailureMessage"></a>
If BulkPublishStatus is FAILED this field will contain the error message that caused the bulk publish to fail.
Type: String

 ** [IdentityPoolId](#API_GetBulkPublishDetails_ResponseSyntax) **   <a name="Cognito-GetBulkPublishDetails-response-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`

## Errors
<a name="API_GetBulkPublishDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
Indicates an internal service error.
 ** message **
Message returned by InternalErrorException.
HTTP Status Code: 500

 ** InvalidParameterException **
Thrown when a request parameter does not comply with the associated constraints.
 ** message **
Message returned by InvalidParameterException.
HTTP Status Code: 400

 ** NotAuthorizedException **
Thrown when a user is not authorized to access the requested resource.
 ** message **
The message returned by a NotAuthorizedException.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Thrown if the resource doesn't exist.
 ** message **
Message returned by a ResourceNotFoundException.
HTTP Status Code: 404

## See Also
<a name="API_GetBulkPublishDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/GetBulkPublishDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/GetBulkPublishDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
