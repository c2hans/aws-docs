---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_FunctionResponse.html
---

# FunctionResponse
<a name="API_FunctionResponse"></a>

The function response.

## Contents
<a name="API_FunctionResponse_Contents"></a>

 ** implementedBy **   <a name="tm-Type-FunctionResponse-implementedBy"></a>
The data connector.
Type: [DataConnector](API_DataConnector.md) object
Required: No

 ** isInherited **   <a name="tm-Type-FunctionResponse-isInherited"></a>
Indicates whether this function is inherited.
Type: Boolean
Required: No

 ** requiredProperties **   <a name="tm-Type-FunctionResponse-requiredProperties"></a>
The required properties of the function.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** scope **   <a name="tm-Type-FunctionResponse-scope"></a>
The scope of the function.
Type: String
Valid Values: `ENTITY | WORKSPACE`
Required: No

## See Also
<a name="API_FunctionResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/FunctionResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/FunctionResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/FunctionResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
