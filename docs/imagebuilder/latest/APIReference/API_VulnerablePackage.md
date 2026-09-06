---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_VulnerablePackage.html
---

# VulnerablePackage
<a name="API_VulnerablePackage"></a>

Information about a vulnerable package that Amazon Inspector identifies in a finding.

## Contents
<a name="API_VulnerablePackage_Contents"></a>

 ** arch **   <a name="imagebuilder-Type-VulnerablePackage-arch"></a>
The architecture of the vulnerable package.
Type: String
Required: No

 ** epoch **   <a name="imagebuilder-Type-VulnerablePackage-epoch"></a>
The epoch of the vulnerable package.
Type: Integer
Required: No

 ** filePath **   <a name="imagebuilder-Type-VulnerablePackage-filePath"></a>
The file path of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** fixedInVersion **   <a name="imagebuilder-Type-VulnerablePackage-fixedInVersion"></a>
The version of the package that contains the vulnerability fix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-VulnerablePackage-name"></a>
The name of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** packageManager **   <a name="imagebuilder-Type-VulnerablePackage-packageManager"></a>
The package manager of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** release **   <a name="imagebuilder-Type-VulnerablePackage-release"></a>
The release of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** remediation **   <a name="imagebuilder-Type-VulnerablePackage-remediation"></a>
The code to run in your environment to update packages with a fix available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** sourceLayerHash **   <a name="imagebuilder-Type-VulnerablePackage-sourceLayerHash"></a>
The source layer hash of the vulnerable package.
Type: String
Required: No

 ** version **   <a name="imagebuilder-Type-VulnerablePackage-version"></a>
The version of the vulnerable package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_VulnerablePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/VulnerablePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/VulnerablePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/VulnerablePackage)
