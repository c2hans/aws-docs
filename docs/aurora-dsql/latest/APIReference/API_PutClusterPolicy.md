---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_PutClusterPolicy.html
---

# PutClusterPolicy
<a name="API_PutClusterPolicy"></a>

Attaches a resource-based policy to a cluster. This policy defines access permissions and conditions for the cluster, allowing you to control which principals can perform actions on the cluster.

## Request Syntax
<a name="API_PutClusterPolicy_RequestSyntax"></a>

```
POST /cluster/{{identifier}}/policy HTTP/1.1
Content-type: application/json

{
   "bypassPolicyLockoutSafetyCheck": {{boolean}},
   "clientToken": "{{string}}",
   "expectedPolicyVersion": "{{string}}",
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutClusterPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_PutClusterPolicy_RequestSyntax) **   <a name="auroradsql-PutClusterPolicy-request-uri-identifier"></a>
The ID of the cluster.
Pattern: `[a-z0-9]{26}`
Required: Yes

## Request Body
<a name="API_PutClusterPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [bypassPolicyLockoutSafetyCheck](#API_PutClusterPolicy_RequestSyntax) **   <a name="auroradsql-PutClusterPolicy-request-bypassPolicyLockoutSafetyCheck"></a>
A flag that allows you to bypass the policy lockout safety check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.
Type: Boolean
Required: No

 ** [clientToken](#API_PutClusterPolicy_RequestSyntax) **   <a name="auroradsql-PutClusterPolicy-request-clientToken"></a>
Idempotency token so a request is only processed once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!-~]+`
Required: No

 ** [expectedPolicyVersion](#API_PutClusterPolicy_RequestSyntax) **   <a name="auroradsql-PutClusterPolicy-request-expectedPolicyVersion"></a>
The expected version of the current policy. This parameter ensures that you're updating the correct version of the policy and helps prevent concurrent modification conflicts.
Type: String
Required: No

 ** [policy](#API_PutClusterPolicy_RequestSyntax) **   <a name="auroradsql-PutClusterPolicy-request-policy"></a>
The resource-based policy document to attach to the cluster. This should be a valid JSON policy document that defines permissions and conditions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Required: Yes

## Response Syntax
<a name="API_PutClusterPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyVersion": "string"
}
```

## Response Elements
<a name="API_PutClusterPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyVersion](#API_PutClusterPolicy_ResponseSyntax) **   <a name="auroradsql-PutClusterPolicy-response-policyVersion"></a>
The version of the policy after it has been updated or created.
Type: String

## Errors
<a name="API_PutClusterPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The submitted action has conflicts.
 ** resourceId **
Resource Id
 ** resourceType **
Resource Type
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
Retry after seconds.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceId **
The resource ID could not be found.
 ** resourceType **
The resource type could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
The message that the request was denied due to request throttling.
 ** quotaCode **
The request exceeds a request rate quota.
 ** retryAfterSeconds **
The request exceeds a request rate quota. Retry after seconds.
 ** serviceCode **
The request exceeds a service quota.
HTTP Status Code: 429

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_PutClusterPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dsql-2018-05-10/PutClusterPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/PutClusterPolicy)
