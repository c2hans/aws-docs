---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ParameterInlinePolicy.html
---

# ParameterInlinePolicy
<a name="API_ParameterInlinePolicy"></a>

One or more policies assigned to a parameter.

## Contents
<a name="API_ParameterInlinePolicy_Contents"></a>

 ** PolicyStatus **   <a name="systemsmanager-Type-ParameterInlinePolicy-PolicyStatus"></a>
The status of the policy. Policies report the following statuses: Pending (the policy hasn't been enforced or applied yet), Finished (the policy was applied), Failed (the policy wasn't applied), or InProgress (the policy is being applied now).
Type: String
Required: No

 ** PolicyText **   <a name="systemsmanager-Type-ParameterInlinePolicy-PolicyText"></a>
The JSON text of the policy.
Type: String
Required: No

 ** PolicyType **   <a name="systemsmanager-Type-ParameterInlinePolicy-PolicyType"></a>
The type of policy. Parameter Store, a tool in AWS Systems Manager, supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification.
Type: String
Required: No

## See Also
<a name="API_ParameterInlinePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ParameterInlinePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ParameterInlinePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ParameterInlinePolicy)
