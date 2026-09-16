---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateTargetGroup.html
---

# UpdateTargetGroup
<a name="API_UpdateTargetGroup"></a>

Updates the specified target group.

## Request Syntax
<a name="API_UpdateTargetGroup_RequestSyntax"></a>

```
PATCH /targetgroups/{{targetGroupIdentifier}} HTTP/1.1
Content-type: application/json

{
   "healthCheck": {
      "enabled": {{boolean}},
      "healthCheckIntervalSeconds": {{number}},
      "healthCheckTimeoutSeconds": {{number}},
      "healthyThresholdCount": {{number}},
      "matcher": { ... },
      "path": "{{string}}",
      "port": {{number}},
      "protocol": "{{string}}",
      "protocolVersion": "{{string}}",
      "unhealthyThresholdCount": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateTargetGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [targetGroupIdentifier](#API_UpdateTargetGroup_RequestSyntax) **   <a name="vpclattice-UpdateTargetGroup-request-uri-targetGroupIdentifier"></a>
The ID or ARN of the target group.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_UpdateTargetGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [healthCheck](#API_UpdateTargetGroup_RequestSyntax) **   <a name="vpclattice-UpdateTargetGroup-request-healthCheck"></a>
The health check configuration.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateTargetGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "config": {
      "healthCheck": {
         "enabled": boolean,
         "healthCheckIntervalSeconds": number,
         "healthCheckTimeoutSeconds": number,
         "healthyThresholdCount": number,
         "matcher": { ... },
         "path": "string",
         "port": number,
         "protocol": "string",
         "protocolVersion": "string",
         "unhealthyThresholdCount": number
      },
      "ipAddressType": "string",
      "lambdaEventStructureVersion": "string",
      "port": number,
      "protocol": "string",
      "protocolVersion": "string",
      "vpcIdentifier": "string"
   },
   "id": "string",
   "name": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_UpdateTargetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateTargetGroup_ResponseSyntax) **   <a name="vpclattice-UpdateTargetGroup-response-arn"></a>
The Amazon Resource Name (ARN) of the target group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}`

 ** [config](#API_UpdateTargetGroup_ResponseSyntax) **   <a name="vpclattice-UpdateTargetGroup-response-config"></a>
The target group configuration.
Type: [TargetGroupConfig](API_TargetGroupConfig.md) object

 ** [id](#API_UpdateTargetGroup_ResponseSyntax) **   <a name="vpclattice-UpdateTargetGroup-response-id"></a>
The ID of the target group.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `tg-[0-9a-z]{17}`

 ** [name](#API_UpdateTargetGroup_ResponseSyntax) **   <a name="vpclattice-UpdateTargetGroup-response-name"></a>
The name of the target group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?!tg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_UpdateTargetGroup_ResponseSyntax) **   <a name="vpclattice-UpdateTargetGroup-response-status"></a>
The status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

 ** [type](#API_UpdateTargetGroup_ResponseSyntax) **   <a name="vpclattice-UpdateTargetGroup-response-type"></a>
The target group type.
Type: String
Valid Values: `IP | LAMBDA | INSTANCE | ALB`

## Errors
<a name="API_UpdateTargetGroup_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
 ** serviceCode **
The service code.
HTTP Status Code: 402

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
<a name="API_UpdateTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/UpdateTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/UpdateTargetGroup)
