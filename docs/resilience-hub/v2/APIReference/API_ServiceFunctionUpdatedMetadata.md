---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceFunctionUpdatedMetadata.html
---

# ServiceFunctionUpdatedMetadata
<a name="API_ServiceFunctionUpdatedMetadata"></a>

Metadata for a service function updated event.

## Contents
<a name="API_ServiceFunctionUpdatedMetadata_Contents"></a>

 ** resourcesAdded **   <a name="ngresiliencehub-Type-ServiceFunctionUpdatedMetadata-resourcesAdded"></a>
The list of resource ARNs that were added.
Type: Array of strings
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** resourcesRemoved **   <a name="ngresiliencehub-Type-ServiceFunctionUpdatedMetadata-resourcesRemoved"></a>
The list of resource ARNs that were removed.
Type: Array of strings
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** serviceFunctionId **   <a name="ngresiliencehub-Type-ServiceFunctionUpdatedMetadata-serviceFunctionId"></a>
The identifier of the service function.
Type: String
Required: No

 ** serviceFunctionName **   <a name="ngresiliencehub-Type-ServiceFunctionUpdatedMetadata-serviceFunctionName"></a>
The name of the service function.
Type: String
Required: No

## See Also
<a name="API_ServiceFunctionUpdatedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceFunctionUpdatedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceFunctionUpdatedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceFunctionUpdatedMetadata)
