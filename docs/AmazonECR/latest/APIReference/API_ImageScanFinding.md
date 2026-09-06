---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanFinding.html
---

# ImageScanFinding
<a name="API_ImageScanFinding"></a>

Contains information about an image scan finding.

## Contents
<a name="API_ImageScanFinding_Contents"></a>

 ** attributes **   <a name="ECR-Type-ImageScanFinding-attributes"></a>
A collection of attributes of the host from which the finding is generated.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** description **   <a name="ECR-Type-ImageScanFinding-description"></a>
The description of the finding.
Type: String
Required: No

 ** name **   <a name="ECR-Type-ImageScanFinding-name"></a>
The name associated with the finding, usually a CVE number.
Type: String
Required: No

 ** severity **   <a name="ECR-Type-ImageScanFinding-severity"></a>
The finding severity.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL | UNDEFINED`
Required: No

 ** uri **   <a name="ECR-Type-ImageScanFinding-uri"></a>
A link containing additional details about the security vulnerability.
Type: String
Required: No

## See Also
<a name="API_ImageScanFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageScanFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageScanFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageScanFinding)
