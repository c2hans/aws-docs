---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeResiliencyPolicy.html
---

# DescribeResiliencyPolicy
<a name="API_DescribeResiliencyPolicy"></a>

Describes a specified resiliency policy for an AWS Resilience Hub application. The returned policy object includes creation time, data location constraints, the Amazon Resource Name (ARN) for the policy, tags, tier, and more.

## Request Syntax
<a name="API_DescribeResiliencyPolicy_RequestSyntax"></a>

```
POST /describe-resiliency-policy HTTP/1.1
Content-type: application/json

{
   "policyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeResiliencyPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeResiliencyPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policyArn](#API_DescribeResiliencyPolicy_RequestSyntax) **   <a name="resiliencehub-DescribeResiliencyPolicy-request-policyArn"></a>
Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:resiliency-policy/`policy-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_DescribeResiliencyPolicy_ResponseSyntax"></a>

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
<a name="API_DescribeResiliencyPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_DescribeResiliencyPolicy_ResponseSyntax) **   <a name="resiliencehub-DescribeResiliencyPolicy-response-policy"></a>
Information about the specific resiliency policy, returned as an object. This object includes creation time, data location constraints, its name, description, tags, the recovery time objective (RTO) and recovery point objective (RPO) in seconds, and more.
Type: [ResiliencyPolicy](API_ResiliencyPolicy.md) object

## Errors
<a name="API_DescribeResiliencyPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

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
<a name="API_DescribeResiliencyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/DescribeResiliencyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/DescribeResiliencyPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
