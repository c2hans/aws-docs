---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateAccessLogSubscription.html
---

# CreateAccessLogSubscription
<a name="API_CreateAccessLogSubscription"></a>

Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see [Access logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_CreateAccessLogSubscription_RequestSyntax"></a>

```
POST /accesslogsubscriptions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "destinationArn": "{{string}}",
   "resourceIdentifier": "{{string}}",
   "serviceNetworkLogType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAccessLogSubscription_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccessLogSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [destinationArn](#API_CreateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-request-destinationArn"></a>
The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

 ** [resourceIdentifier](#API_CreateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-request-resourceIdentifier"></a>
The ID or ARN of the service network or service.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 200.
Pattern: `((((sn)|(svc)|(rcfg))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(resourceconfiguration/rcfg)|(service/svc))-[0-9a-z]{17}))`
Required: Yes

 ** [serviceNetworkLogType](#API_CreateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-request-serviceNetworkLogType"></a>
The type of log that monitors your Amazon VPC Lattice service networks.
Type: String
Valid Values: `SERVICE | RESOURCE`
Required: No

 ** [tags](#API_CreateAccessLogSubscription_RequestSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-request-tags"></a>
The tags for the access log subscription.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAccessLogSubscription_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "destinationArn": "string",
   "id": "string",
   "resourceArn": "string",
   "resourceId": "string",
   "serviceNetworkLogType": "string"
}
```

## Response Elements
<a name="API_CreateAccessLogSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-response-arn"></a>
The Amazon Resource Name (ARN) of the access log subscription.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}`

 ** [destinationArn](#API_CreateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-response-destinationArn"></a>
The Amazon Resource Name (ARN) of the log destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`

 ** [id](#API_CreateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-response-id"></a>
The ID of the access log subscription.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `als-[0-9a-z]{17}`

 ** [resourceArn](#API_CreateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the service network or service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc)|(resourceconfiguration/rcfg))-[0-9a-z]{17}`

 ** [resourceId](#API_CreateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-response-resourceId"></a>
The ID of the service network or service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 50.
Pattern: `((sn)|(svc))-[0-9a-z]{17}`

 ** [serviceNetworkLogType](#API_CreateAccessLogSubscription_ResponseSyntax) **   <a name="vpclattice-CreateAccessLogSubscription-response-serviceNetworkLogType"></a>
The type of log that monitors your Amazon VPC Lattice service networks.
Type: String
Valid Values: `SERVICE | RESOURCE`

## Errors
<a name="API_CreateAccessLogSubscription_Errors"></a>

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
<a name="API_CreateAccessLogSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateAccessLogSubscription)
