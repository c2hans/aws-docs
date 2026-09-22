---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageScanFindingsFilter.html
---

# ImageScanFindingsFilter
<a name="API_ImageScanFindingsFilter"></a>

A name value pair that Image Builder applies to streamline results from the vulnerability scan findings list action.

## Contents
<a name="API_ImageScanFindingsFilter_Contents"></a>

 ** name **   <a name="imagebuilder-Type-ImageScanFindingsFilter-name"></a>
The name of the image scan finding filter. Filter names are case-sensitive. Valid filter names are:
+  `imageBuildVersionArn` – Filters findings by the image build version that was scanned.
+  `imagePipelineArn` – Filters findings by the pipeline that created the scanned image.
+  `vulnerabilityId` – Filters findings by vulnerability ID, for example a CVE ID.
+  `severity` – Filters findings by severity level.
Type: String
Pattern: `^[a-zA-Z]{1,1024}$`
Required: No

 ** values **   <a name="imagebuilder-Type-ImageScanFindingsFilter-values"></a>
The filter values. Filter values are case-sensitive.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `^[0-9a-zA-Z./_ :,{}"-]{1,1024}$`
Required: No

## See Also
<a name="API_ImageScanFindingsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageScanFindingsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageScanFindingsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageScanFindingsFilter)
