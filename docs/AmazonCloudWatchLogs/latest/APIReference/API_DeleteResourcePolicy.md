---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes a resource policy from this account. This revokes the access of the identities in that policy to put log events to this account.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
{
   "expectedRevisionId": "{{string}}",
   "policyName": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [expectedRevisionId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="CWL-DeleteResourcePolicy-request-expectedRevisionId"></a>
The expected revision ID of the resource policy. Required when deleting a resource-scoped policy to prevent concurrent modifications.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [policyName](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="CWL-DeleteResourcePolicy-request-policyName"></a>
The name of the policy to be revoked. This parameter is required.
Type: String
Required: No

 ** [resourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="CWL-DeleteResourcePolicy-request-resourceArn"></a>
The ARN of the CloudWatch Logs resource for which the resource policy needs to be deleted
Type: String
Required: No

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
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
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DeleteResourcePolicy)
