---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkPathComponent.html
---

# NetworkPathComponent
<a name="API_NetworkPathComponent"></a>

Information about a network path component.

## Contents
<a name="API_NetworkPathComponent_Contents"></a>

 ** ComponentId **   <a name="securityhub-Type-NetworkPathComponent-ComponentId"></a>
The identifier of a component in the network path.
Length Constraints: Minimum of 1. Maximum of 32.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ComponentType **   <a name="securityhub-Type-NetworkPathComponent-ComponentType"></a>
The type of component.
Length Constraints: Minimum of 1. Maximum of 32.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Egress **   <a name="securityhub-Type-NetworkPathComponent-Egress"></a>
Information about the component that comes after the current component in the network path.
Type: [NetworkHeader](API_NetworkHeader.md) object
Required: No

 ** Ingress **   <a name="securityhub-Type-NetworkPathComponent-Ingress"></a>
Information about the component that comes before the current node in the network path.
Type: [NetworkHeader](API_NetworkHeader.md) object
Required: No

## See Also
<a name="API_NetworkPathComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkPathComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkPathComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkPathComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
