---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SubdomainAttachableResource.html
---

# SubdomainAttachableResource
<a name="API_SubdomainAttachableResource"></a>

Describes a Lightsail resource that a subdomain is associated with, or is being associated with.

## Contents
<a name="API_SubdomainAttachableResource_Contents"></a>

 ** arn **   <a name="Lightsail-Type-SubdomainAttachableResource-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** attachedAt **   <a name="Lightsail-Type-SubdomainAttachableResource-attachedAt"></a>
The timestamp when the subdomain was associated with the resource.
Type: Timestamp
Required: No

 ** name **   <a name="Lightsail-Type-SubdomainAttachableResource-name"></a>
The name of the resource.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## See Also
<a name="API_SubdomainAttachableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SubdomainAttachableResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SubdomainAttachableResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SubdomainAttachableResource)
