---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_JobResourceTags.html
---

# JobResourceTags
<a name="API_JobResourceTags"></a>

Tags for a job.

## Contents
<a name="API_JobResourceTags_Contents"></a>

 ** ResourceType **   <a name="panorama-Type-JobResourceTags-ResourceType"></a>
The job's type.
Type: String
Valid Values: `PACKAGE`
Required: Yes

 ** Tags **   <a name="panorama-Type-JobResourceTags-Tags"></a>
The job's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: Yes

## See Also
<a name="API_JobResourceTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/JobResourceTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/JobResourceTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/JobResourceTags)
