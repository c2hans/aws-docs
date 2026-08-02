---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyDefinition.html
---

# UpdatePolicyDefinition
<a name="API_UpdatePolicyDefinition"></a>

Contains information about updates to be applied to a policy.

This data type is used as a request parameter in the [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html) operation.

## Contents
<a name="API_UpdatePolicyDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** static **   <a name="verifiedpermissions-Type-UpdatePolicyDefinition-static"></a>
Contains details about the updates to be applied to a static policy.
Type: [UpdateStaticPolicyDefinition](API_UpdateStaticPolicyDefinition.md) object
Required: No

## See Also
<a name="API_UpdatePolicyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdatePolicyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdatePolicyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdatePolicyDefinition)
