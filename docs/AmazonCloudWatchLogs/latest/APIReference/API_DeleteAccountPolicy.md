---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteAccountPolicy.html
---

# DeleteAccountPolicy
<a name="API_DeleteAccountPolicy"></a>

Deletes a CloudWatch Logs account policy. This stops the account-wide policy from applying to log groups or data sources in the account. If you delete a data protection policy or subscription filter policy, any log-group level policies of those types remain in effect. If you delete a retention policy, the log groups that it applied to use their own retention setting, unless another retention policy applies to them. Deleting a retention policy does not restore log events that CloudWatch Logs has already deleted. This operation supports deletion of data source-based field index policies, including facet configurations, in addition to log group-based policies.

To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are deleting.
+ To delete a data protection policy, you must have the `logs:DeleteDataProtectionPolicy` and `logs:DeleteAccountPolicy` permissions.
+ To delete a subscription filter policy, you must have the `logs:DeleteSubscriptionFilter` and `logs:DeleteAccountPolicy` permissions.
+ To delete a transformer policy, you must have the `logs:DeleteTransformer` and `logs:DeleteAccountPolicy` permissions.
+ To delete a field index policy, you must have the `logs:DeleteIndexPolicy` and `logs:DeleteAccountPolicy` permissions.

  If you delete a field index policy that included facet configurations, those facets will no longer be available for interactive exploration in the CloudWatch Logs Insights console. However, facet data is retained for up to 30 days.
+ To delete a retention policy, you must have the `logs:DeleteRetentionPolicy` and `logs:DeleteAccountPolicy` permissions. To preview the impact of deleting a retention policy, specify `true` for `dryRun`. A dry run requires the same permissions as the operation that it previews, and no additional permissions.

If you delete a field index policy, the indexing of the log events that happened before you deleted the policy will still be used for up to 30 days to improve CloudWatch Logs Insights queries.

## Request Syntax
<a name="API_DeleteAccountPolicy_RequestSyntax"></a>

```
{
   "dryRun": {{boolean}},
   "policyName": "{{string}}",
   "policyType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAccountPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dryRun](#API_DeleteAccountPolicy_RequestSyntax) **   <a name="CWL-DeleteAccountPolicy-request-dryRun"></a>
Specifies whether to preview the impact of deleting the policy without deleting it. If you specify `true`, CloudWatch Logs does not delete the policy and returns the estimated impact in `dryRunResult`. The default is `false`.
Specifying `dryRun` is valid only when you specify `RETENTION_POLICY` for `policyType`. Only one dry run can be in progress for an account at a time.
Type: Boolean
Required: No

 ** [policyName](#API_DeleteAccountPolicy_RequestSyntax) **   <a name="CWL-DeleteAccountPolicy-request-policyName"></a>
The name of the policy to delete.
Type: String
Required: Yes

 ** [policyType](#API_DeleteAccountPolicy_RequestSyntax) **   <a name="CWL-DeleteAccountPolicy-request-policyType"></a>
The type of policy to delete.
Type: String
Valid Values: `DATA_PROTECTION_POLICY | SUBSCRIPTION_FILTER_POLICY | FIELD_INDEX_POLICY | TRANSFORMER_POLICY | METRIC_EXTRACTION_POLICY | RETENTION_POLICY`
Required: Yes

## Response Syntax
<a name="API_DeleteAccountPolicy_ResponseSyntax"></a>

```
{
   "dryRunResult": {
      "decreasedRetentionLogGroupCount": number,
      "failedAnalysisCount": number,
      "increasedRetentionLogGroupCount": number,
      "topLogGroupsImpacted": [
         {
            "currentRetention": "string",
            "logGroupName": "string",
            "proposedRetention": "string",
            "storedBytes": number
         }
      ],
      "totalMatchedLogGroups": number,
      "unchangedRetentionLogGroupCount": number
   }
}
```

## Response Elements
<a name="API_DeleteAccountPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dryRunResult](#API_DeleteAccountPolicy_ResponseSyntax) **   <a name="CWL-DeleteAccountPolicy-response-dryRunResult"></a>
The estimated impact of deleting the policy. This field is returned only when the request specifies `dryRun` as `true`.
Type: [DryRunResult](API_DryRunResult.md) object

## Errors
<a name="API_DeleteAccountPolicy_Errors"></a>

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
<a name="API_DeleteAccountPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DeleteAccountPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DeleteAccountPolicy)
