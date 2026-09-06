---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfFindingIdentifier.html
---

# OcsfFindingIdentifier
<a name="API_OcsfFindingIdentifier"></a>

Provides a standard to identify security findings using OCSF.

## Contents
<a name="API_OcsfFindingIdentifier_Contents"></a>

 ** CloudAccountUid **   <a name="securityhub-Type-OcsfFindingIdentifier-CloudAccountUid"></a>
Finding cloud.account.uid, which is a unique identifier in the AWS account..
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** FindingInfoUid **   <a name="securityhub-Type-OcsfFindingIdentifier-FindingInfoUid"></a>
Finding finding\_info.uid, which is a unique identifier for the finding from the finding provider.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** MetadataProductUid **   <a name="securityhub-Type-OcsfFindingIdentifier-MetadataProductUid"></a>
Finding metadata.product.uid, which is a unique identifier for the product.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_OcsfFindingIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/OcsfFindingIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/OcsfFindingIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/OcsfFindingIdentifier)
