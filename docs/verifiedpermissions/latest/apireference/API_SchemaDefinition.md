---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_SchemaDefinition.html
---

# SchemaDefinition
<a name="API_SchemaDefinition"></a>

Contains a list of principal types, resource types, and actions that can be specified in policies stored in the same policy store. If the validation mode for the policy store is set to `STRICT`, then policies that can't be validated by this schema are rejected by Verified Permissions and can't be stored in the policy store.

## Contents
<a name="API_SchemaDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cedarJson **   <a name="verifiedpermissions-Type-SchemaDefinition-cedarJson"></a>
A JSON string representation of the schema supported by applications that use this policy store. To delete the schema, run [PutSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PutSchema.html) with `{}` for this parameter. For more information, see [Policy store schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html) in the *Amazon Verified Permissions User Guide*.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_SchemaDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/SchemaDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/SchemaDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/SchemaDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
