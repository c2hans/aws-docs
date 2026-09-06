---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_KeyRange.html
---

# KeyRange
<a name="API_KeyRange"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Contains a key range. For export jobs, a `S3Resource` object can have an optional `KeyRange` value. The length of the range is defined at job creation, and has either an inclusive `BeginMarker`, an inclusive `EndMarker`, or both. Ranges are UTF-8 binary sorted.

## Contents
<a name="API_KeyRange_Contents"></a>

 ** BeginMarker **   <a name="Snowball-Type-KeyRange-BeginMarker"></a>
The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** EndMarker **   <a name="Snowball-Type-KeyRange-EndMarker"></a>
The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_KeyRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/KeyRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/KeyRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/KeyRange)
