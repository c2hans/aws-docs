---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetResourcePoliciesResponseEntry.html
---

# GetResourcePoliciesResponseEntry
<a name="API_GetResourcePoliciesResponseEntry"></a>

A resource policy helps you to define the IAM entity (for example, an AWS account) that can manage your Systems Manager resources. Currently, `OpsItemGroup` is the only resource that supports Systems Manager resource policies. The resource policy for `OpsItemGroup` enables AWS accounts to view and interact with OpsCenter operational work items (OpsItems).

## Contents
<a name="API_GetResourcePoliciesResponseEntry_Contents"></a>

 ** Policy **   <a name="systemsmanager-Type-GetResourcePoliciesResponseEntry-Policy"></a>
A resource policy helps you to define the IAM entity (for example, an AWS account) that can manage your Systems Manager resources. Currently, `OpsItemGroup` is the only resource that supports Systems Manager resource policies. The resource policy for `OpsItemGroup` enables AWS accounts to view and interact with OpsCenter operational work items (OpsItems).
Type: String
Pattern: `^(?!\s*$).+`
Required: No

 ** PolicyHash **   <a name="systemsmanager-Type-GetResourcePoliciesResponseEntry-PolicyHash"></a>
ID of the current policy version. The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash when updating or deleting a policy.
Type: String
Required: No

 ** PolicyId **   <a name="systemsmanager-Type-GetResourcePoliciesResponseEntry-PolicyId"></a>
A policy ID.
Type: String
Required: No

## See Also
<a name="API_GetResourcePoliciesResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetResourcePoliciesResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetResourcePoliciesResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetResourcePoliciesResponseEntry)
