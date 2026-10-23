---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_AffectedPackage.html
---

# AffectedPackage
<a name="API_AffectedPackage"></a>

A software package implicated by a finding.

## Contents
<a name="API_AffectedPackage_Contents"></a>

 ** name **   <a name="continuum-Type-AffectedPackage-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** fixedInVersion **   <a name="continuum-Type-AffectedPackage-fixedInVersion"></a>
The fixed In Version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** packageManager **   <a name="continuum-Type-AffectedPackage-packageManager"></a>
The package Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** version **   <a name="continuum-Type-AffectedPackage-version"></a>
The version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AffectedPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/AffectedPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/AffectedPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/AffectedPackage)
