---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_FleetAttributeCapability.html
---

# FleetAttributeCapability
<a name="API_FleetAttributeCapability"></a>

Defines the fleet's capability name, minimum, and maximum.

## Contents
<a name="API_FleetAttributeCapability_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-FleetAttributeCapability-name"></a>
The name of the fleet attribute capability for the worker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([a-zA-Z][a-zA-Z0-9]{0,63}:)?attr(\.[a-zA-Z][a-zA-Z0-9]{0,63})+`
Required: Yes

 ** values **   <a name="deadlinecloud-Type-FleetAttributeCapability-values"></a>
The number of fleet attribute capabilities.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z_]([a-zA-Z0-9_\-]{0,99})`
Required: Yes

## See Also
<a name="API_FleetAttributeCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetAttributeCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetAttributeCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetAttributeCapability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
