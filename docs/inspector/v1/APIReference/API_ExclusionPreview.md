---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_ExclusionPreview.html
---

# ExclusionPreview
<a name="API_ExclusionPreview"></a>

Contains information about what is excluded from an assessment run given the current state of the assessment template.

## Contents
<a name="API_ExclusionPreview_Contents"></a>

 ** description **   <a name="Inspector-Type-ExclusionPreview-description"></a>
The description of the exclusion preview.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: Yes

 ** recommendation **   <a name="Inspector-Type-ExclusionPreview-recommendation"></a>
The recommendation for the exclusion preview.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: Yes

 ** scopes **   <a name="Inspector-Type-ExclusionPreview-scopes"></a>
The AWS resources for which the exclusion preview pertains.
Type: Array of [Scope](API_Scope.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** title **   <a name="Inspector-Type-ExclusionPreview-title"></a>
The name of the exclusion preview.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: Yes

 ** attributes **   <a name="Inspector-Type-ExclusionPreview-attributes"></a>
The system-defined attributes for the exclusion preview.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_ExclusionPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/ExclusionPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ExclusionPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/ExclusionPreview)
