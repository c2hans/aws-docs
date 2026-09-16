---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateResiliencyPolicy.html
---

# CreateResiliencyPolicy
<a name="API_CreateResiliencyPolicy"></a>

Creates a resiliency policy for an application.

**Note**
 AWS Resilience Hub allows you to provide a value of zero for `rtoInSecs` and `rpoInSecs` of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for `rtoInSecs` and `rpoInSecs`, the estimated workload RTO and estimated workload RPO result will be near zero and the **Compliance status** for your application will be set to **Policy breached**.

## Request Syntax
<a name="API_CreateResiliencyPolicy_RequestSyntax"></a>

```
POST /create-resiliency-policy HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dataLocationConstraint": "{{string}}",
   "policy": {
      "{{string}}" : {
         "rpoInSecs": {{number}},
         "rtoInSecs": {{number}}
      }
   },
   "policyDescription": "{{string}}",
   "policyName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "tier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateResiliencyPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResiliencyPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-clientToken"></a>
Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [dataLocationConstraint](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-dataLocationConstraint"></a>
Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
Type: String
Valid Values: `AnyLocation | SameContinent | SameCountry`
Required: No

 ** [policy](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-policy"></a>
The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.
Type: String to [FailurePolicy](API_FailurePolicy.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: Yes

 ** [policyDescription](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-policyDescription"></a>
Description of the resiliency policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [policyName](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-policyName"></a>
Name of the resiliency policy.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [tags](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** [tier](#API_CreateResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-request-tier"></a>
The tier for this resiliency policy, ranging from the highest severity (`MissionCritical`) to lowest (`NonCritical`).
Type: String
Valid Values: `MissionCritical | Critical | Important | CoreServices | NonCritical | NotApplicable`
Required: Yes

## Response Syntax
<a name="API_CreateResiliencyPolicy_ResponseSyntax"></a>

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
<a name="API_CreateResiliencyPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_CreateResiliencyPolicy_ResponseSyntax) **   <a name="resiliencehub-CreateResiliencyPolicy-response-policy"></a>
The type of resiliency policy that was created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.
Type: [ResiliencyPolicy](API_ResiliencyPolicy.md) object

## Errors
<a name="API_CreateResiliencyPolicy_Errors"></a>

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

 ** ServiceQuotaExceededException **
This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreateResiliencyPolicy_Examples"></a>

### Sample ResilienceHub ResiliencyPolicy
<a name="API_CreateResiliencyPolicy_Example_1"></a>

This example illustrates one usage of CreateResiliencyPolicy.

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ResiliencyPolicyCFNCanaryStack:
    Type: AWS::ResilienceHub::ResiliencyPolicy
    Properties:
      PolicyName: "ResiliencyPolicyCFNCanaryExample"
      PolicyDescription: 'ResilienceHub TestResiliencyPolicy for CFN'
      Tier: 'MissionCritical'
      Tags:
        TagKey: ""
      Policy:
        Software:
          RtoInSecs: 10
          RpoInSecs: 10
        Hardware:
          RtoInSecs: 10
          RpoInSecs: 10
        AZ:
          RtoInSecs: 10
          RpoInSecs: 10
        Region:
          RtoInSecs: 10
          RpoInSecs: 10
```

## See Also
<a name="API_CreateResiliencyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/CreateResiliencyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/CreateResiliencyPolicy)
