---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AccountPolicy.html
---

# AccountPolicy
<a name="API_AccountPolicy"></a>

A structure that contains information about one CloudWatch Logs account policy.

## Contents
<a name="API_AccountPolicy_Contents"></a>

 ** accountId **   <a name="CWL-Type-AccountPolicy-accountId"></a>
The AWS account ID that the policy applies to.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** lastUpdatedTime **   <a name="CWL-Type-AccountPolicy-lastUpdatedTime"></a>
The date and time that this policy was most recently updated.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** policyDocument **   <a name="CWL-Type-AccountPolicy-policyDocument"></a>
The policy document for this account policy.
The JSON specified in `policyDocument` can be up to 30,720 characters.
Type: String
Required: No

 ** policyName **   <a name="CWL-Type-AccountPolicy-policyName"></a>
The name of the account policy.
Type: String
Required: No

 ** policyType **   <a name="CWL-Type-AccountPolicy-policyType"></a>
The type of policy for this account policy.
Type: String
Valid Values: `DATA_PROTECTION_POLICY | SUBSCRIPTION_FILTER_POLICY | FIELD_INDEX_POLICY | TRANSFORMER_POLICY | METRIC_EXTRACTION_POLICY`
Required: No

 ** scope **   <a name="CWL-Type-AccountPolicy-scope"></a>
The scope of the account policy.
Type: String
Valid Values: `ALL`
Required: No

 ** selectionCriteria **   <a name="CWL-Type-AccountPolicy-selectionCriteria"></a>
The log group selection criteria that is used for this policy.
Type: String
Required: No

## See Also
<a name="API_AccountPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/AccountPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/AccountPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/AccountPolicy)
