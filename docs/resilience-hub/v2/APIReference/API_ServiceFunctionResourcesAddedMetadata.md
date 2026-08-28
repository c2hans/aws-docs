---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceFunctionResourcesAddedMetadata.html
---

# ServiceFunctionResourcesAddedMetadata
<a name="API_ServiceFunctionResourcesAddedMetadata"></a>

Metadata for a service function resources added event.

## Contents
<a name="API_ServiceFunctionResourcesAddedMetadata_Contents"></a>

 ** resourcesAdded **   <a name="ngresiliencehub-Type-ServiceFunctionResourcesAddedMetadata-resourcesAdded"></a>
The list of resource ARNs that were added.
Type: Array of strings
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** serviceFunctionId **   <a name="ngresiliencehub-Type-ServiceFunctionResourcesAddedMetadata-serviceFunctionId"></a>
The identifier of the service function.
Type: String
Required: No

 ** serviceFunctionName **   <a name="ngresiliencehub-Type-ServiceFunctionResourcesAddedMetadata-serviceFunctionName"></a>
The name of the service function.
Type: String
Required: No

## See Also
<a name="API_ServiceFunctionResourcesAddedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceFunctionResourcesAddedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceFunctionResourcesAddedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceFunctionResourcesAddedMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
