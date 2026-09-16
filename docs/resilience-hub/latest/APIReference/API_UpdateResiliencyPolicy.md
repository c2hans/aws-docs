---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateResiliencyPolicy.html
---

# UpdateResiliencyPolicy
<a name="API_UpdateResiliencyPolicy"></a>

Updates a resiliency policy.

**Note**
 AWS Resilience Hub allows you to provide a value of zero for `rtoInSecs` and `rpoInSecs` of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for `rtoInSecs` and `rpoInSecs`, the estimated workload RTO and estimated workload RPO result will be near zero and the **Compliance status** for your application will be set to **Policy breached**.

## Request Syntax
<a name="API_UpdateResiliencyPolicy_RequestSyntax"></a>

```
POST /update-resiliency-policy HTTP/1.1
Content-type: application/json

{
   "dataLocationConstraint": "{{string}}",
   "policy": {
      "{{string}}" : {
         "rpoInSecs": {{number}},
         "rtoInSecs": {{number}}
      }
   },
   "policyArn": "{{string}}",
   "policyDescription": "{{string}}",
   "policyName": "{{string}}",
   "tier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateResiliencyPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateResiliencyPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataLocationConstraint](#API_UpdateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-request-dataLocationConstraint"></a>
Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
Type: String
Valid Values: `AnyLocation | SameContinent | SameCountry`
Required: No

 ** [policy](#API_UpdateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-request-policy"></a>
Resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.
Type: String to [FailurePolicy](API_FailurePolicy.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** [policyArn](#API_UpdateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-request-policyArn"></a>
Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:resiliency-policy/`policy-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [policyDescription](#API_UpdateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-request-policyDescription"></a>
Description of the resiliency policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [policyName](#API_UpdateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-request-policyName"></a>
Name of the resiliency policy.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** [tier](#API_UpdateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-request-tier"></a>
The tier for this resiliency policy, ranging from the highest severity (`MissionCritical`) to lowest (`NonCritical`).
Type: String
Valid Values: `MissionCritical | Critical | Important | CoreServices | NonCritical | NotApplicable`
Required: No

## Response Syntax
<a name="API_UpdateResiliencyPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": {
      "creationTime": number,
      "dataLocationConstraint": "string",
      "estimatedCostTier": "string",
      "policy": {
         "string" : {
            "rpoInSecs": number,
            "rtoInSecs": number
         }
      },
      "policyArn": "string",
      "policyDescription": "string",
      "policyName": "string",
      "tags": {
         "string" : "string"
      },
      "tier": "string"
   }
}
```

## Response Elements
<a name="API_UpdateResiliencyPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_UpdateResiliencyPolicy_ResponseSyntax) **   <a name="resiliencehub-UpdateResiliencyPolicy-response-policy"></a>
The resiliency policy that was updated, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.
Type: [ResiliencyPolicy](API_ResiliencyPolicy.md) object

## Errors
<a name="API_UpdateResiliencyPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** ConflictException **
This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 409

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception occurs when the specified resource could not be found.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 404

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateResiliencyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/UpdateResiliencyPolicy)
