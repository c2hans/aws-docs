---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_VulnerablePackage.html
---

# VulnerablePackage
<a name="API_VulnerablePackage"></a>

Information on the vulnerable package identified by a finding.

## Contents
<a name="API_VulnerablePackage_Contents"></a>

 ** arch **   <a name="ECR-Type-VulnerablePackage-arch"></a>
The architecture of the vulnerable package.
Type: String
Required: No

 ** epoch **   <a name="ECR-Type-VulnerablePackage-epoch"></a>
The epoch of the vulnerable package.
Type: Integer
Required: No

 ** filePath **   <a name="ECR-Type-VulnerablePackage-filePath"></a>
The file path of the vulnerable package.
Type: String
Required: No

 ** fixedInVersion **   <a name="ECR-Type-VulnerablePackage-fixedInVersion"></a>
The version of the package that contains the vulnerability fix.
Type: String
Required: No

 ** name **   <a name="ECR-Type-VulnerablePackage-name"></a>
The name of the vulnerable package.
Type: String
Required: No

 ** packageManager **   <a name="ECR-Type-VulnerablePackage-packageManager"></a>
The package manager of the vulnerable package.
Type: String
Required: No

 ** release **   <a name="ECR-Type-VulnerablePackage-release"></a>
The release of the vulnerable package.
Type: String
Required: No

 ** sourceLayerHash **   <a name="ECR-Type-VulnerablePackage-sourceLayerHash"></a>
The source layer hash of the vulnerable package.
Type: String
Required: No

 ** version **   <a name="ECR-Type-VulnerablePackage-version"></a>
The version of the vulnerable package.
Type: String
Required: No

## See Also
<a name="API_VulnerablePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/VulnerablePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/VulnerablePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/VulnerablePackage)
