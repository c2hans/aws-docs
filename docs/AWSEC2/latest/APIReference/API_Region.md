---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Region.html
---

# Region
<a name="API_Region"></a>

Describes a Region.

## Contents
<a name="API_Region_Contents"></a>

 ** GeographySet.N **
The geography information for the Region. The geography is returned as a list.
Type: Array of [RegionGeography](API_RegionGeography.md) objects
Required: No

 ** optInStatus **
The Region opt-in status. The possible values are `opt-in-not-required`, `opted-in`, and `not-opted-in`.
Type: String
Required: No

 ** regionEndpoint **
The Region service endpoint.
Type: String
Required: No

 ** regionName **
The name of the Region.
Type: String
Required: No

## See Also
<a name="API_Region_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Region)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Region)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Region)
