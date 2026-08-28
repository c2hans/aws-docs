---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NodeOutputPort.html
---

# NodeOutputPort
<a name="API_NodeOutputPort"></a>

A node output port.

## Contents
<a name="API_NodeOutputPort_Contents"></a>

 ** Description **   <a name="panorama-Type-NodeOutputPort-Description"></a>
The output port's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** Name **   <a name="panorama-Type-NodeOutputPort-Name"></a>
The output port's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9\_]+`
Required: No

 ** Type **   <a name="panorama-Type-NodeOutputPort-Type"></a>
The output port's type.
Type: String
Valid Values: `BOOLEAN | STRING | INT32 | FLOAT32 | MEDIA`
Required: No

## See Also
<a name="API_NodeOutputPort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NodeOutputPort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NodeOutputPort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NodeOutputPort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
