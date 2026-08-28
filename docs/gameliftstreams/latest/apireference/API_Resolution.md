---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_Resolution.html
---

# Resolution
<a name="API_Resolution"></a>

Contains the width and height dimensions, in pixels, that define the resolution of the stream session's virtual monitor. The total number of pixels (width × height) must not exceed 2,073,600 (equivalent to 1920 × 1080).

## Contents
<a name="API_Resolution_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Height **   <a name="gameliftstreams-Type-Resolution-Height"></a>
The height of the stream session's virtual monitor, in pixels. The value must be an even number.
Type: Integer
Valid Range: Minimum value of 320. Maximum value of 4096.
Required: Yes

 ** Width **   <a name="gameliftstreams-Type-Resolution-Width"></a>
The width of the stream session's virtual monitor, in pixels. The value must be an even number.
Type: Integer
Valid Range: Minimum value of 320. Maximum value of 4096.
Required: Yes

## See Also
<a name="API_Resolution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/Resolution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/Resolution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/Resolution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
