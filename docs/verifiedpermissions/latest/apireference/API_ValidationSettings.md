---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ValidationSettings.html
---

# ValidationSettings
<a name="API_ValidationSettings"></a>

A structure that contains Cedar policy validation settings for the policy store. The validation mode determines which validation failures that Cedar considers serious enough to block acceptance of a new or edited static policy or policy template.

This data type is used as a request parameter in the [CreatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html) and [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html) operations.

## Contents
<a name="API_ValidationSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** mode **   <a name="verifiedpermissions-Type-ValidationSettings-mode"></a>
The validation mode currently configured for this policy store. The valid values are:
+  **OFF** – Neither Verified Permissions nor Cedar perform any validation on policies. No validation errors are reported by either service.
+  **STRICT** – Requires a schema to be present in the policy store. Cedar performs validation on all submitted new or updated static policies and policy templates. Any that fail validation are rejected and Cedar doesn't store them in the policy store.
If `Mode=STRICT` and the policy store doesn't contain a schema, Verified Permissions rejects all static policies and policy templates because there is no schema to validate against.
To submit a static policy or policy template without a schema, you must turn off validation.
Type: String
Valid Values: `OFF | STRICT`
Required: Yes

## See Also
<a name="API_ValidationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ValidationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ValidationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ValidationSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
