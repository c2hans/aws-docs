---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateAccessLogSubscription.html
---

# UpdateAccessLogSubscription
<a name="API_UpdateAccessLogSubscription"></a>

Updates the specified access log subscription.

## Request Syntax
<a name="API_UpdateAccessLogSubscription_RequestSyntax"></a>

```
PATCH /accesslogsubscriptions/{{accessLogSubscriptionIdentifier}} HTTP/1.1
Content-type: application/json

{
   "destinationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAccessLogSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessLogSubscriptionIdentifier](#API_UpdateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-request-uri-accessLogSubscriptionIdentifier"></a>
The ID or ARN of the access log subscription.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((als-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_UpdateAccessLogSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationArn](#API_UpdateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-request-destinationArn"></a>
The Amazon Resource Name (ARN) of the access log destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

## Response Syntax
<a name="API_UpdateAccessLogSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "destinationArn": "string",
   "id": "string",
   "resourceArn": "string",
   "resourceId": "string"
}
```

## Response Elements
<a name="API_UpdateAccessLogSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-response-arn"></a>
The Amazon Resource Name (ARN) of the access log subscription.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}`

 ** [destinationArn](#API_UpdateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-response-destinationArn"></a>
The Amazon Resource Name (ARN) of the access log destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [id](#API_UpdateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-response-id"></a>
The ID of the access log subscription.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `als-[0-9a-z]{17}`

 ** [resourceArn](#API_UpdateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the access log subscription.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc)|(resourceconfiguration/rcfg))-[0-9a-z]{17}`

 ** [resourceId](#API_UpdateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-UpdateAccessLogSubscription-response-resourceId"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 50.
Pattern: `((sn)|(svc))-[0-9a-z]{17}`

## Errors
<a name="API_UpdateAccessLogSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAccessLogSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/UpdateAccessLogSubscription)
