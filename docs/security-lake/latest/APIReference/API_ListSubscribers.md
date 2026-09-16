---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListSubscribers.html
---

# ListSubscribers
<a name="API_ListSubscribers"></a>

Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or AWS account.

## Request Syntax
<a name="API_ListSubscribers_RequestSyntax"></a>

```
GET /v1/subscribers?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSubscribers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSubscribers_RequestSyntax) **   <a name="securitylake-ListSubscribers-request-uri-maxResults"></a>
The maximum number of accounts for which the configuration is displayed.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSubscribers_RequestSyntax) **   <a name="securitylake-ListSubscribers-request-uri-nextToken"></a>
If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_ListSubscribers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSubscribers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "subscribers": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListSubscribers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSubscribers_ResponseSyntax) **   <a name="securitylake-ListSubscribers-response-nextToken"></a>
If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [subscribers](#API_ListSubscribers_ResponseSyntax) **   <a name="securitylake-ListSubscribers-response-subscribers"></a>
The subscribers available for the specified Security Lake account ID.
Type: Array of [SubscriberResource](API_SubscriberResource.md) objects

## Errors
<a name="API_ListSubscribers_Errors"></a>

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
<a name="API_ListSubscribers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/ListSubscribers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/ListSubscribers)
