---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteTargetGroup.html
---

# DeleteTargetGroup
<a name="API_DeleteTargetGroup"></a>

Deletes a target group. You can't delete a target group if it is used in a listener rule or if the target group creation is in progress.

## Request Syntax
<a name="API_DeleteTargetGroup_RequestSyntax"></a>

```
DELETE /targetgroups/{{targetGroupIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTargetGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [targetGroupIdentifier](#API_DeleteTargetGroup_RequestSyntax) **   <a name="vpclattice-DeleteTargetGroup-request-uri-targetGroupIdentifier"></a>
The ID or ARN of the target group.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_DeleteTargetGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTargetGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteTargetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteTargetGroup_ResponseSyntax) **   <a name="vpclattice-DeleteTargetGroup-response-arn"></a>
The Amazon Resource Name (ARN) of the target group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}`

 ** [id](#API_DeleteTargetGroup_ResponseSyntax) **   <a name="vpclattice-DeleteTargetGroup-response-id"></a>
The ID of the target group.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `tg-[0-9a-z]{17}`

 ** [status](#API_DeleteTargetGroup_ResponseSyntax) **   <a name="vpclattice-DeleteTargetGroup-response-status"></a>
The status. You can retry the operation if the status is `DELETE_FAILED`. However, if you retry it while the status is `DELETE_IN_PROGRESS`, the status doesn't change.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_DeleteTargetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DeleteTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/DeleteTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DeleteTargetGroup)
