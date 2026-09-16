---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetAuthPolicy.html
---

# GetAuthPolicy
<a name="API_GetAuthPolicy"></a>

Retrieves information about the auth policy for the specified service or service network.

## Request Syntax
<a name="API_GetAuthPolicy_RequestSyntax"></a>

```
GET /authpolicy/{{resourceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAuthPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceIdentifier](#API_GetAuthPolicy_RequestSyntax) **   <a name="vpclattice-GetAuthPolicy-request-uri-resourceIdentifier"></a>
The ID or ARN of the service network or service.
Length Constraints: Minimum length of 17. Maximum length of 200.
Pattern: `((((sn)|(svc)|(rcfg))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(resourceconfiguration/rcfg)|(service/svc))-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetAuthPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAuthPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "lastUpdatedAt": "string",
   "policy": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_GetAuthPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetAuthPolicy_ResponseSyntax) **   <a name="vpclattice-GetAuthPolicy-response-createdAt"></a>
The date and time that the auth policy was created, in ISO-8601 format.
Type: Timestamp

 ** [lastUpdatedAt](#API_GetAuthPolicy_ResponseSyntax) **   <a name="vpclattice-GetAuthPolicy-response-lastUpdatedAt"></a>
The date and time that the auth policy was last updated, in ISO-8601 format.
Type: Timestamp

 ** [policy](#API_GetAuthPolicy_ResponseSyntax) **   <a name="vpclattice-GetAuthPolicy-response-policy"></a>
The auth policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36864.

 ** [state](#API_GetAuthPolicy_ResponseSyntax) **   <a name="vpclattice-GetAuthPolicy-response-state"></a>
The state of the auth policy. The auth policy is only active when the auth type is set to `AWS_IAM`. If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the auth type is `NONE`, then any auth policy that you provide remains inactive. For more information, see [Create a service network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#create-service-network) in the *Amazon VPC Lattice User Guide*.
Type: String
Valid Values: `Active | Inactive`

## Errors
<a name="API_GetAuthPolicy_Errors"></a>

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
<a name="API_GetAuthPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetAuthPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetAuthPolicy)
