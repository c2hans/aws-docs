---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_PutAuthPolicy.html
---

# PutAuthPolicy
<a name="API_PutAuthPolicy"></a>

Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.

For more information, see [Auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) in the *Amazon VPC Lattice User Guide*.

## Request Syntax
<a name="API_PutAuthPolicy_RequestSyntax"></a>

```
PUT /authpolicy/{{resourceIdentifier}} HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAuthPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceIdentifier](#API_PutAuthPolicy_RequestSyntax) **   <a name="vpclattice-PutAuthPolicy-request-uri-resourceIdentifier"></a>
The ID or ARN of the service network or service for which the policy is created.
Length Constraints: Minimum length of 17. Maximum length of 200.
Pattern: `((((sn)|(svc)|(rcfg))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(resourceconfiguration/rcfg)|(service/svc))-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_PutAuthPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_PutAuthPolicy_RequestSyntax) **   <a name="vpclattice-PutAuthPolicy-request-policy"></a>
The auth policy. The policy string in JSON must not contain newlines or blank lines.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36864.
Required: Yes

## Response Syntax
<a name="API_PutAuthPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_PutAuthPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_PutAuthPolicy_ResponseSyntax) **   <a name="vpclattice-PutAuthPolicy-response-policy"></a>
The auth policy. The policy string in JSON must not contain newlines or blank lines.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36864.

 ** [state](#API_PutAuthPolicy_ResponseSyntax) **   <a name="vpclattice-PutAuthPolicy-response-state"></a>
The state of the auth policy. The auth policy is only active when the auth type is set to `AWS_IAM`. If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the Auth type is `NONE`, then, any auth policy that you provide remains inactive. For more information, see [Create a service network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#create-service-network) in the *Amazon VPC Lattice User Guide*.
Type: String
Valid Values: `Active | Inactive`

## Errors
<a name="API_PutAuthPolicy_Errors"></a>

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
<a name="API_PutAuthPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/PutAuthPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/PutAuthPolicy)
