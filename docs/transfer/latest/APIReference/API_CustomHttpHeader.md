---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_CustomHttpHeader.html
---

# CustomHttpHeader
<a name="API_CustomHttpHeader"></a>

Represents a custom HTTP header that can be included in AS2 messages. Each header consists of a key-value pair.

## Contents
<a name="API_CustomHttpHeader_Contents"></a>

 ** Key **   <a name="TransferFamily-Type-CustomHttpHeader-Key"></a>
The name of the custom HTTP header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** Value **   <a name="TransferFamily-Type-CustomHttpHeader-Value"></a>
The value of the custom HTTP header.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 +\-./:=@_]*`
Required: No

## See Also
<a name="API_CustomHttpHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/CustomHttpHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/CustomHttpHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/CustomHttpHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
