---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_PackageFilter.html
---

# PackageFilter
<a name="API_PackageFilter"></a>

Contains information on the details of a package filter.

## Contents
<a name="API_PackageFilter_Contents"></a>

 ** architecture **   <a name="inspector2-Type-PackageFilter-architecture"></a>
An object that contains details on the package architecture type to filter on.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** epoch **   <a name="inspector2-Type-PackageFilter-epoch"></a>
An object that contains details on the package epoch to filter on.
Type: [NumberFilter](API_NumberFilter.md) object
Required: No

 ** filePath **   <a name="inspector2-Type-PackageFilter-filePath"></a>
An object that contains details on the package file path to filter on.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** name **   <a name="inspector2-Type-PackageFilter-name"></a>
An object that contains details on the name of the package to filter on.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** release **   <a name="inspector2-Type-PackageFilter-release"></a>
An object that contains details on the package release to filter on.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** sourceLambdaLayerArn **   <a name="inspector2-Type-PackageFilter-sourceLambdaLayerArn"></a>
An object that describes the details of a string filter.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** sourceLayerHash **   <a name="inspector2-Type-PackageFilter-sourceLayerHash"></a>
An object that contains details on the source layer hash to filter on.
Type: [StringFilter](API_StringFilter.md) object
Required: No

 ** version **   <a name="inspector2-Type-PackageFilter-version"></a>
The package version to filter on.
Type: [StringFilter](API_StringFilter.md) object
Required: No

## See Also
<a name="API_PackageFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/PackageFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/PackageFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/PackageFilter)
