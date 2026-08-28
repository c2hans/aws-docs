---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectionTypeVariant.html
---

# ConnectionTypeVariant
<a name="API_ConnectionTypeVariant"></a>

Represents a variant of a connection type in AWS Glue. Connection type variants provide specific configurations and behaviors for different implementations of the same general connection type.

## Contents
<a name="API_ConnectionTypeVariant_Contents"></a>

 ** ConnectionTypeVariantName **   <a name="Glue-Type-ConnectionTypeVariant-ConnectionTypeVariantName"></a>
The unique identifier for the connection type variant. This name is used internally to identify the specific variant of a connection type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Description **   <a name="Glue-Type-ConnectionTypeVariant-Description"></a>
A detailed description of the connection type variant, including its purpose, use cases, and any specific configuration requirements.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** DisplayName **   <a name="Glue-Type-ConnectionTypeVariant-DisplayName"></a>
The human-readable name for the connection type variant that is displayed in the AWS Glue console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LogoUrl **   <a name="Glue-Type-ConnectionTypeVariant-LogoUrl"></a>
The URL of the logo associated with a connection type variant.
Type: String
Required: No

## See Also
<a name="API_ConnectionTypeVariant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectionTypeVariant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectionTypeVariant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectionTypeVariant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
