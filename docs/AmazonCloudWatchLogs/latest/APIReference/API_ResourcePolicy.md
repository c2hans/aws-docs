---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ResourcePolicy.html
---

# ResourcePolicy
<a name="API_ResourcePolicy"></a>

A policy enabling one or more entities to put logs to a log group in this account.

## Contents
<a name="API_ResourcePolicy_Contents"></a>

 ** lastUpdatedTime **   <a name="CWL-Type-ResourcePolicy-lastUpdatedTime"></a>
Timestamp showing when this policy was last updated, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** policyDocument **   <a name="CWL-Type-ResourcePolicy-policyDocument"></a>
The details of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** policyName **   <a name="CWL-Type-ResourcePolicy-policyName"></a>
The name of the resource policy.
Type: String
Required: No

 ** policyScope **   <a name="CWL-Type-ResourcePolicy-policyScope"></a>
Specifies scope of the resource policy. Valid values are ACCOUNT or RESOURCE.
Type: String
Valid Values: `ACCOUNT | RESOURCE`
Required: No

 ** resourceArn **   <a name="CWL-Type-ResourcePolicy-resourceArn"></a>
The ARN of the CloudWatch Logs resource to which the resource policy is attached. Only populated for resource-scoped policies.
Type: String
Required: No

 ** revisionId **   <a name="CWL-Type-ResourcePolicy-revisionId"></a>
The revision ID of the resource policy. Only populated for resource-scoped policies.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ResourcePolicy)
