---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositoriesItem.html
---

# ListSourceRepositoriesItem
<a name="API_ListSourceRepositoriesItem"></a>

Information about a source repository returned in a list of source repositories.

## Contents
<a name="API_ListSourceRepositoriesItem_Contents"></a>

 ** createdTime **   <a name="codecatalyst-Type-ListSourceRepositoriesItem-createdTime"></a>
The time the source repository was created, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

 ** id **   <a name="codecatalyst-Type-ListSourceRepositoriesItem-id"></a>
The system-generated unique ID of the source repository.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** lastUpdatedTime **   <a name="codecatalyst-Type-ListSourceRepositoriesItem-lastUpdatedTime"></a>
The time the source repository was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

 ** name **   <a name="codecatalyst-Type-ListSourceRepositoriesItem-name"></a>
The name of the source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** description **   <a name="codecatalyst-Type-ListSourceRepositoriesItem-description"></a>
The description of the repository, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ListSourceRepositoriesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListSourceRepositoriesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListSourceRepositoriesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListSourceRepositoriesItem)
