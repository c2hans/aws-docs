---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetListingDetails.html
---

# AssetListingDetails
<a name="API_AssetListingDetails"></a>

The details of an asset published in an Amazon DataZone catalog.

## Contents
<a name="API_AssetListingDetails_Contents"></a>

 ** listingId **   <a name="datazone-Type-AssetListingDetails-listingId"></a>
The identifier of an asset published in an Amazon DataZone catalog.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** listingStatus **   <a name="datazone-Type-AssetListingDetails-listingStatus"></a>
The status of an asset published in an Amazon DataZone catalog.
Type: String
Valid Values: `CREATING | ACTIVE | INACTIVE`
Required: Yes

## See Also
<a name="API_AssetListingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetListingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetListingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetListingDetails)
