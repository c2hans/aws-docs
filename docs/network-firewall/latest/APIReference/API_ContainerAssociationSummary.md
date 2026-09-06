---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContainerAssociationSummary.html
---

# ContainerAssociationSummary
<a name="API_ContainerAssociationSummary"></a>

The metadata for a container association returned by `ListContainerAssociations`. Contains the ARN and name that you use to identify the container association in other operations.

## Contents
<a name="API_ContainerAssociationSummary_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-ContainerAssociationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** Name **   <a name="networkfirewall-Type-ContainerAssociationSummary-Name"></a>
The descriptive name of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## See Also
<a name="API_ContainerAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContainerAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContainerAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContainerAssociationSummary)
