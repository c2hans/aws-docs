---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceSystemDisassociatedMetadata.html
---

# ServiceSystemDisassociatedMetadata
<a name="API_ServiceSystemDisassociatedMetadata"></a>

Metadata for a service system disassociated event.

## Contents
<a name="API_ServiceSystemDisassociatedMetadata_Contents"></a>

 ** systemArn **   <a name="ngresiliencehub-Type-ServiceSystemDisassociatedMetadata-systemArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** systemId **   <a name="ngresiliencehub-Type-ServiceSystemDisassociatedMetadata-systemId"></a>
The identifier of the disassociated system.
Type: String
Required: No

 ** systemName **   <a name="ngresiliencehub-Type-ServiceSystemDisassociatedMetadata-systemName"></a>
The name of the disassociated system.
Type: String
Required: No

## See Also
<a name="API_ServiceSystemDisassociatedMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceSystemDisassociatedMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceSystemDisassociatedMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceSystemDisassociatedMetadata)
