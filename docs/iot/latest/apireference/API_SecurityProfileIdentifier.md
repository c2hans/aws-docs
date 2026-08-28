---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SecurityProfileIdentifier.html
---

# SecurityProfileIdentifier
<a name="API_SecurityProfileIdentifier"></a>

Identifying information for a Device Defender security profile.

## Contents
<a name="API_SecurityProfileIdentifier_Contents"></a>

 ** arn **   <a name="iot-Type-SecurityProfileIdentifier-arn"></a>
The ARN of the security profile.
Type: String
Required: Yes

 ** name **   <a name="iot-Type-SecurityProfileIdentifier-name"></a>
The name you've given to the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## See Also
<a name="API_SecurityProfileIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SecurityProfileIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SecurityProfileIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SecurityProfileIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
