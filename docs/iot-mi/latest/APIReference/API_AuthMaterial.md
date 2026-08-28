---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_AuthMaterial.html
---

# AuthMaterial
<a name="API_AuthMaterial"></a>

The authorization material containing the Secrets Manager arn and version.

## Contents
<a name="API_AuthMaterial_Contents"></a>

 ** AuthMaterialName **   <a name="managedintegrations-Type-AuthMaterial-AuthMaterialName"></a>
The name of the authorization material.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9=_+/-]+`
Required: Yes

 ** SecretsManager **   <a name="managedintegrations-Type-AuthMaterial-SecretsManager"></a>
Configuration for AWS Secrets Manager, used to securely store and manage sensitive information for connector destinations.
Type: [SecretsManager](API_SecretsManager.md) object
Required: Yes

## See Also
<a name="API_AuthMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/AuthMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/AuthMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/AuthMaterial)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
