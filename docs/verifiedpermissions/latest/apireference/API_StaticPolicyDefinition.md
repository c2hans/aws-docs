---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_StaticPolicyDefinition.html
---

# StaticPolicyDefinition
<a name="API_StaticPolicyDefinition"></a>

Contains information about a static policy.

This data type is used as a field that is part of the [PolicyDefinitionDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinitionDetail.html) type.

## Contents
<a name="API_StaticPolicyDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** statement **   <a name="verifiedpermissions-Type-StaticPolicyDefinition-statement"></a>
The policy content of the static policy, written in the Cedar policy language.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** description **   <a name="verifiedpermissions-Type-StaticPolicyDefinition-description"></a>
The description of the static policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Required: No

## See Also
<a name="API_StaticPolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/StaticPolicyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/StaticPolicyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/StaticPolicyDefinition)
