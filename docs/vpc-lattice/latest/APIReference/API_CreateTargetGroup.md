---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateTargetGroup.html
---

# CreateTargetGroup
<a name="API_CreateTargetGroup"></a>

Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.

For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_CreateTargetGroup_RequestSyntax"></a>

```
POST /targetgroups HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "config": {
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
      },
      "ipAddressType": "{{string}}",
      "lambdaEventStructureVersion": "{{string}}",
      "port": {{number}},
      "protocol": "{{string}}",
      "protocolVersion": "{{string}}",
      "vpcIdentifier": "{{string}}"
   },
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTargetGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTargetGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateTargetGroup_RequestSyntax) **   <a name="vpclattice-CreateTargetGroup-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[!-~]+.*`
Required: No

 ** [config](#API_CreateTargetGroup_RequestSyntax) **   <a name="vpclattice-CreateTargetGroup-request-config"></a>
The target group configuration.
Type: [TargetGroupConfig](API_TargetGroupConfig.md) object
Required: No

 ** [name](#API_CreateTargetGroup_RequestSyntax) **   <a name="vpclattice-CreateTargetGroup-request-name"></a>
The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?!tg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: Yes

 ** [tags](#API_CreateTargetGroup_RequestSyntax) **   <a name="vpclattice-CreateTargetGroup-request-tags"></a>
The tags for the target group.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [type](#API_CreateTargetGroup_RequestSyntax) **   <a name="vpclattice-CreateTargetGroup-request-type"></a>
The type of target group.
Type: String
Valid Values: `IP | LAMBDA | INSTANCE | ALB`
Required: Yes

## Response Syntax
<a name="API_CreateTargetGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateTargetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateTargetGroup_ResponseSyntax) **   <a name="vpclattice-CreateTargetGroup-response-arn"></a>
The Amazon Resource Name (ARN) of the target group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}`

 ** [config](#API_CreateTargetGroup_ResponseSyntax) **   <a name="vpclattice-CreateTargetGroup-response-config"></a>
The target group configuration.
Type: [TargetGroupConfig](API_TargetGroupConfig.md) object

 ** [id](#API_CreateTargetGroup_ResponseSyntax) **   <a name="vpclattice-CreateTargetGroup-response-id"></a>
The ID of the target group.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `tg-[0-9a-z]{17}`

 ** [name](#API_CreateTargetGroup_ResponseSyntax) **   <a name="vpclattice-CreateTargetGroup-response-name"></a>
The name of the target group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `(?!tg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [status](#API_CreateTargetGroup_ResponseSyntax) **   <a name="vpclattice-CreateTargetGroup-response-status"></a>
The status. You can retry the operation if the status is `CREATE_FAILED`. However, if you retry it while the status is `CREATE_IN_PROGRESS`, there is no change in the status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

 ** [type](#API_CreateTargetGroup_ResponseSyntax) **   <a name="vpclattice-CreateTargetGroup-response-type"></a>
The type of target group.
Type: String
Valid Values: `IP | LAMBDA | INSTANCE | ALB`

## Errors
<a name="API_CreateTargetGroup_Errors"></a>

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
<a name="API_CreateTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/CreateTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/CreateTargetGroup)
