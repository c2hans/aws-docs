---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetAccessLogSubscription.html
---

# GetAccessLogSubscription
<a name="API_GetAccessLogSubscription"></a>

Retrieves information about the specified access log subscription.

## Request Syntax
<a name="API_GetAccessLogSubscription_RequestSyntax"></a>

```
GET /accesslogsubscriptions/{{accessLogSubscriptionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccessLogSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessLogSubscriptionIdentifier](#API_GetAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-GetAccessLogSubscription-request-uri-accessLogSubscriptionIdentifier"></a>
The ID or ARN of the access log subscription.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((als-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetAccessLogSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccessLogSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "destinationArn": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "resourceArn": "string",
   "resourceId": "string",
   "serviceNetworkLogType": "string"
}
```

## Response Elements
<a name="API_GetAccessLogSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-arn"></a>
The Amazon Resource Name (ARN) of the access log subscription.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}`

 ** [createdAt](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-createdAt"></a>
The date and time that the access log subscription was created, in ISO-8601 format.
Type: Timestamp

 ** [destinationArn](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-destinationArn"></a>
The Amazon Resource Name (ARN) of the access log destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [id](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-id"></a>
The ID of the access log subscription.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `als-[0-9a-z]{17}`

 ** [lastUpdatedAt](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-lastUpdatedAt"></a>
The date and time that the access log subscription was last updated, in ISO-8601 format.
Type: Timestamp

 ** [resourceArn](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the service network or service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc)|(resourceconfiguration/rcfg))-[0-9a-z]{17}`

 ** [resourceId](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-resourceId"></a>
The ID of the service network or service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 50.
Pattern: `((sn)|(svc))-[0-9a-z]{17}`

 ** [serviceNetworkLogType](#API_GetAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-GetAccessLogSubscription-response-serviceNetworkLogType"></a>
The log type for the service network.
Type: String
Valid Values: `SERVICE | RESOURCE`

## Errors
<a name="API_GetAccessLogSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetAccessLogSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetAccessLogSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetAccessLogSubscription)
