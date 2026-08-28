---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageScanFindingsFilter.html
---

# ImageScanFindingsFilter
<a name="API_ImageScanFindingsFilter"></a>

A name value pair that Image Builder applies to streamline results from the vulnerability scan findings list action.

## Contents
<a name="API_ImageScanFindingsFilter_Contents"></a>

 ** name **   <a name="imagebuilder-Type-ImageScanFindingsFilter-name"></a>
The name of the image scan finding filter. Filter names are case-sensitive.
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
