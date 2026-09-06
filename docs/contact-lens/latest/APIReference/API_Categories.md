---
source_url: https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_Categories.html
---

# Categories
<a name="API_connect-contact-lens_Categories"></a>

Provides the category rules that are used to automatically categorize contacts based on uttered keywords and phrases.

## Contents
<a name="API_connect-contact-lens_Categories_Contents"></a>

 ** MatchedCategories **   <a name="connect-Type-connect-contact-lens_Categories-MatchedCategories"></a>
The category rules that have been matched in the analyzed segment.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** MatchedDetails **   <a name="connect-Type-connect-contact-lens_Categories-MatchedDetails"></a>
The category rule that was matched and when it occurred in the transcript.
Type: String to [CategoryDetails](API_connect-contact-lens_CategoryDetails.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 150 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_connect-contact-lens_Categories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/Categories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/Categories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/Categories)
