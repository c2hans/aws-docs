---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ImageLocation.html
---

# ImageLocation
<a name="API_ImageLocation"></a>

Contains an image that is uploaded to AWS IoT SiteWise and available at a URL.

## Contents
<a name="API_ImageLocation_Contents"></a>

 ** id **   <a name="iotsitewise-Type-ImageLocation-id"></a>
The ID of the image.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** url **   <a name="iotsitewise-Type-ImageLocation-url"></a>
The URL where the image is available. The URL is valid for 15 minutes so that you can view and download the image
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(http|https)\://\S+`
Required: Yes

## See Also
<a name="API_ImageLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ImageLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ImageLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ImageLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
