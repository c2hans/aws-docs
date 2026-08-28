---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ResourceDescription.html
---

# ResourceDescription
<a name="API_ResourceDescription"></a>

Represents information about a provisioned resource.

## Contents
<a name="API_ResourceDescription_Contents"></a>

 ** Identifier **   <a name="ccapi-Type-ResourceDescription-Identifier"></a>
The primary identifier for the resource.
For more information, see [Identifying resources](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html) in the * AWS Cloud Control API User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** Properties **   <a name="ccapi-Type-ResourceDescription-Properties"></a>
A list of the resource properties and their current values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ResourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/ResourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/ResourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/ResourceDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
