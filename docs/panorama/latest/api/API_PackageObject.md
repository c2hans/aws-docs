---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_PackageObject.html
---

# PackageObject
<a name="API_PackageObject"></a>

A package object.

## Contents
<a name="API_PackageObject_Contents"></a>

 ** Name **   <a name="panorama-Type-PackageObject-Name"></a>
The object's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** PackageVersion **   <a name="panorama-Type-PackageObject-PackageVersion"></a>
The object's package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: Yes

 ** PatchVersion **   <a name="panorama-Type-PackageObject-PatchVersion"></a>
The object's patch version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`
Required: Yes

## See Also
<a name="API_PackageObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/PackageObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/PackageObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/PackageObject)
