---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_IndexPolicy.html
---

# IndexPolicy
<a name="API_IndexPolicy"></a>

This structure contains information about one field index policy in this account.

## Contents
<a name="API_IndexPolicy_Contents"></a>

 ** lastUpdateTime **   <a name="CWL-Type-IndexPolicy-lastUpdateTime"></a>
The date and time that this index policy was most recently updated.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupIdentifier **   <a name="CWL-Type-IndexPolicy-logGroupIdentifier"></a>
The ARN of the log group that this index policy applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** policyDocument **   <a name="CWL-Type-IndexPolicy-policyDocument"></a>
The policy document for this index policy, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** policyName **   <a name="CWL-Type-IndexPolicy-policyName"></a>
The name of this policy. Responses about log group-level field index policies don't have this field, because those policies don't have names.
Type: String
Required: No

 ** source **   <a name="CWL-Type-IndexPolicy-source"></a>
This field indicates whether this is an account-level index policy or an index policy that applies only to a single log group.
Type: String
Valid Values: `ACCOUNT | LOG_GROUP`
Required: No

## See Also
<a name="API_IndexPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/IndexPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/IndexPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/IndexPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
