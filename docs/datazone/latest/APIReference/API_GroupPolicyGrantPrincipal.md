---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GroupPolicyGrantPrincipal.html
---

# GroupPolicyGrantPrincipal
<a name="API_GroupPolicyGrantPrincipal"></a>

The group principal to whom the policy is granted.

## Contents
<a name="API_GroupPolicyGrantPrincipal_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** groupIdentifier **   <a name="datazone-Type-GroupPolicyGrantPrincipal-groupIdentifier"></a>
The ID Of the group of the group principal.
Type: String
Pattern: `.*(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+).*`
Required: No

## See Also
<a name="API_GroupPolicyGrantPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GroupPolicyGrantPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GroupPolicyGrantPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GroupPolicyGrantPrincipal)
