---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Creates or updates a resource policy allowing other AWS services to put log events to this account, such as Amazon Route 53. This API has the following restrictions:
+  **Supported actions** - Policy only supports `logs:PutLogEvents` and `logs:CreateLogStream ` actions
+  **Supported principals** - Policy only applies when operations are invoked by AWS service principals (not IAM users, roles, or cross-account principals
+  **Policy limits** - An account can have a maximum of 10 policies without resourceARN and one per LogGroup resourceARN

**Important**
Resource policies with actions invoked by non-AWS service principals (such as IAM users, roles, or other AWS accounts) will not be enforced. For access control involving these principals, use the IAM policies.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
{
   "expectedRevisionId": "{{string}}",
   "policyDocument": "{{string}}",
   "policyName": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [expectedRevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="CWL-PutResourcePolicy-request-expectedRevisionId"></a>
The expected revision ID of the resource policy. Required when `resourceArn` is provided to prevent concurrent modifications. Use `null` when creating a resource policy for the first time.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [policyDocument](#API_PutResourcePolicy_RequestSyntax) **   <a name="CWL-PutResourcePolicy-request-policyDocument"></a>
Details of the new policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. This parameter is required.
The following example creates a resource policy enabling the Route 53 service to put DNS query logs in to the specified log group. Replace `"logArn"` with the ARN of your CloudWatch Logs resource, such as a log group or log stream.
CloudWatch Logs also supports [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) condition context keys.
In the example resource policy, you would replace the value of `SourceArn` with the resource making the call from Route 53 to CloudWatch Logs. You would also replace the value of `SourceAccount` with the AWS account ID making that call.

 `{ "Version": "2012-10-17", "Statement": [ { "Sid": "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service": [ "route53.amazonaws.com" ] }, "Action": "logs:PutLogEvents", "Resource": "logArn", "Condition": { "ArnLike": { "aws:SourceArn": "myRoute53ResourceArn" }, "StringEquals": { "aws:SourceAccount": "myAwsAccountId" } } } ] }`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [policyName](#API_PutResourcePolicy_RequestSyntax) **   <a name="CWL-PutResourcePolicy-request-policyName"></a>
Name of the new policy. This parameter is required.
Type: String
Required: No

 ** [resourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="CWL-PutResourcePolicy-request-resourceArn"></a>
The ARN of the CloudWatch Logs resource to which the resource policy needs to be added or attached. Currently only supports LogGroup ARN.
Type: String
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
{
   "resourcePolicy": {
      "lastUpdatedTime": number,
      "policyDocument": "string",
      "policyName": "string",
      "policyScope": "string",
      "resourceArn": "string",
      "revisionId": "string"
   },
   "revisionId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourcePolicy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="CWL-PutResourcePolicy-response-resourcePolicy"></a>
The new policy.
Type: [ResourcePolicy](API_ResourcePolicy.md) object

 ** [revisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="CWL-PutResourcePolicy-response-revisionId"></a>
The revision ID of the created or updated resource policy. Only returned for resource-scoped policies.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutResourcePolicy)
