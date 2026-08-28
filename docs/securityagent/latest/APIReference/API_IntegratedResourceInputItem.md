---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegratedResourceInputItem.html
---

# IntegratedResourceInputItem
<a name="API_IntegratedResourceInputItem"></a>

Represents an input item for updating integrated resources, including the resource and its capabilities.

## Contents
<a name="API_IntegratedResourceInputItem_Contents"></a>

 ** resource **   <a name="securityagent-Type-IntegratedResourceInputItem-resource"></a>
The integrated resource to update.
Type: [IntegratedResource](API_IntegratedResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** capabilities **   <a name="securityagent-Type-IntegratedResourceInputItem-capabilities"></a>
The capabilities to enable for the integrated resource.
Type: [ProviderResourceCapabilities](API_ProviderResourceCapabilities.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_IntegratedResourceInputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegratedResourceInputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegratedResourceInputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegratedResourceInputItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
