---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ImageFile.html
---

# ImageFile
<a name="API_ImageFile"></a>

Contains an image file.

## Contents
<a name="API_ImageFile_Contents"></a>

 ** data **   <a name="iotsitewise-Type-ImageFile-data"></a>
The image file contents, represented as a base64-encoded string. The file size must be less than 1 MB.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 1500000.
Required: Yes

 ** type **   <a name="iotsitewise-Type-ImageFile-type"></a>
The file type of the image.
Type: String
Valid Values: `PNG`
Required: Yes

## See Also
<a name="API_ImageFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ImageFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ImageFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ImageFile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
