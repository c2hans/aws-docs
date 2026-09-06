---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeregisterTargets.html
---

# DeregisterTargets
<a name="API_DeregisterTargets"></a>

Deregisters the specified targets from the specified target group.

## Request Syntax
<a name="API_DeregisterTargets_RequestSyntax"></a>

```
POST /targetgroups/{{targetGroupIdentifier}}/deregistertargets HTTP/1.1
Content-type: application/json

{
   "targets": [
      {
         "id": "{{string}}",
         "port": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_DeregisterTargets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [targetGroupIdentifier](#API_DeregisterTargets_RequestSyntax) **   <a name="vpclattice-DeregisterTargets-request-uri-targetGroupIdentifier"></a>
The ID or ARN of the target group.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_DeregisterTargets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targets](#API_DeregisterTargets_RequestSyntax) **   <a name="vpclattice-DeregisterTargets-request-targets"></a>
The targets to deregister.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_DeregisterTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "successful": [
      {
         "id": "string",
         "port": number
      }
   ],
   "unsuccessful": [
      {
         "failureCode": "string",
         "failureMessage": "string",
         "id": "string",
         "port": number
      }
   ]
}
```

## Response Elements
<a name="API_DeregisterTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [successful](#API_DeregisterTargets_ResponseSyntax) **   <a name="vpclattice-DeregisterTargets-response-successful"></a>
The targets that were successfully deregistered.
Type: Array of [Target](API_Target.md) objects

 ** [unsuccessful](#API_DeregisterTargets_ResponseSyntax) **   <a name="vpclattice-DeregisterTargets-response-unsuccessful"></a>
The targets that the operation couldn't deregister.
Type: Array of [TargetFailure](API_TargetFailure.md) objects

## Errors
<a name="API_DeregisterTargets_Errors"></a>

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
<a name="API_DeregisterTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/DeregisterTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DeregisterTargets)
