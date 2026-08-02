---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetResourcePolicy.html
---

# GetResourcePolicy
<a name="API_GetResourcePolicy"></a>

Retrieves information about the specified resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.

## Request Syntax
<a name="API_GetResourcePolicy_RequestSyntax"></a>

```
GET /resourcepolicy/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_GetResourcePolicy_RequestSyntax) **   <a name="vpclattice-GetResourcePolicy-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the service network or service.
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc)|(resourceconfiguration/rcfg))-[0-9a-z]{17}`
Required: Yes

## Request Body
<a name="API_GetResourcePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string"
}
```

## Response Elements
<a name="API_GetResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_GetResourcePolicy_ResponseSyntax) **   <a name="vpclattice-GetResourcePolicy-response-policy"></a>
An IAM policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `.*\S.*`

## Errors
<a name="API_GetResourcePolicy_Errors"></a>

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
<a name="API_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetResourcePolicy)
