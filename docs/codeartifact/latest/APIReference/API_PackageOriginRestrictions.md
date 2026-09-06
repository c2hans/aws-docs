---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html
---

# PackageOriginRestrictions
<a name="API_PackageOriginRestrictions"></a>

Details about the origin restrictions set on the package. The package origin restrictions determine how new versions of a package can be added to a specific repository.

## Contents
<a name="API_PackageOriginRestrictions_Contents"></a>

 ** publish **   <a name="codeartifact-Type-PackageOriginRestrictions-publish"></a>
The package origin configuration that determines if new versions of the package can be published directly to the repository.
Type: String
Valid Values: `ALLOW | BLOCK`
Required: Yes

 ** upstream **   <a name="codeartifact-Type-PackageOriginRestrictions-upstream"></a>
The package origin configuration that determines if new versions of the package can be added to the repository from an external connection or upstream source.
Type: String
Valid Values: `ALLOW | BLOCK`
Required: Yes

## See Also
<a name="API_PackageOriginRestrictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageOriginRestrictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageOriginRestrictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageOriginRestrictions)
