---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IdNamespaceAssociationInputReferenceConfig.html
---

# IdNamespaceAssociationInputReferenceConfig
<a name="API_IdNamespaceAssociationInputReferenceConfig"></a>

Provides the information for the ID namespace association input reference configuration.

## Contents
<a name="API_IdNamespaceAssociationInputReferenceConfig_Contents"></a>

 ** inputReferenceArn **   <a name="API-Type-IdNamespaceAssociationInputReferenceConfig-inputReferenceArn"></a>
The Amazon Resource Name (ARN) of the AWS Entity Resolution resource that is being associated to the collaboration. Valid resource ARNs are from the ID namespaces that you own.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:entityresolution:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:idnamespace/[\d\w-]+`
Required: Yes

 ** manageResourcePolicies **   <a name="API-Type-IdNamespaceAssociationInputReferenceConfig-manageResourcePolicies"></a>
When `TRUE`, AWS Clean Rooms manages permissions for the ID namespace association resource.
When `FALSE`, the resource owner manages permissions for the ID namespace association resource.
Type: Boolean
Required: Yes

## See Also
<a name="API_IdNamespaceAssociationInputReferenceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IdNamespaceAssociationInputReferenceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IdNamespaceAssociationInputReferenceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IdNamespaceAssociationInputReferenceConfig)
