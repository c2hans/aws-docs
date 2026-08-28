---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkHeader.html
---

# NetworkHeader
<a name="API_NetworkHeader"></a>

Details about a network path component that occurs before or after the current component.

## Contents
<a name="API_NetworkHeader_Contents"></a>

 ** Destination **   <a name="securityhub-Type-NetworkHeader-Destination"></a>
Information about the destination of the component.
Type: [NetworkPathComponentDetails](API_NetworkPathComponentDetails.md) object
Required: No

 ** Protocol **   <a name="securityhub-Type-NetworkHeader-Protocol"></a>
The protocol used for the component.
Length Constraints: Minimum of 1. Maximum of 16.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Source **   <a name="securityhub-Type-NetworkHeader-Source"></a>
Information about the origin of the component.
Type: [NetworkPathComponentDetails](API_NetworkPathComponentDetails.md) object
Required: No

## See Also
<a name="API_NetworkHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
