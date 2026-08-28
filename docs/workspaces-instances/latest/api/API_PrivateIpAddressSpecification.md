---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_PrivateIpAddressSpecification.html
---

# PrivateIpAddressSpecification
<a name="API_PrivateIpAddressSpecification"></a>

Defines private IP address configuration for network interface.

## Contents
<a name="API_PrivateIpAddressSpecification_Contents"></a>

 ** Primary **   <a name="workspacesinstances-Type-PrivateIpAddressSpecification-Primary"></a>
Indicates if this is the primary private IP address.
Type: Boolean
Required: No

 ** PrivateIpAddress **   <a name="workspacesinstances-Type-PrivateIpAddressSpecification-PrivateIpAddress"></a>
Specific private IP address for the network interface.
Type: String
Pattern: `(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}`
Required: No

## See Also
<a name="API_PrivateIpAddressSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/PrivateIpAddressSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/PrivateIpAddressSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/PrivateIpAddressSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
