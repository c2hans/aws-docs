---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QuickResponseSearchResultData.html
---

# QuickResponseSearchResultData
<a name="API_amazon-q-connect_QuickResponseSearchResultData"></a>

The result of quick response search.

## Contents
<a name="API_amazon-q-connect_QuickResponseSearchResultData_Contents"></a>

 ** contents **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-contents"></a>
The contents of the quick response.
Type: [QuickResponseContents](API_amazon-q-connect_QuickResponseContents.md) object
Required: Yes

 ** contentType **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-contentType"></a>
The media type of the quick response content.
+ Use `application/x.quickresponse;format=plain` for quick response written in plain text.
+ Use `application/x.quickresponse;format=markdown` for quick response written in richtext.
Type: String
Pattern: `(application/x\.quickresponse;format=(plain|markdown))`
Required: Yes

 ** createdTime **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-createdTime"></a>
The timestamp when the quick response was created.
Type: Timestamp
Required: Yes

 ** isActive **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-isActive"></a>
Whether the quick response is active.
Type: Boolean
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-lastModifiedTime"></a>
The timestamp when the quick response search result data was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-name"></a>
The name of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** quickResponseArn **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-quickResponseArn"></a>
The Amazon Resource Name (ARN) of the quick response.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** quickResponseId **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-quickResponseId"></a>
The identifier of the quick response.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-status"></a>
The resource status of the quick response.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** attributesInterpolated **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-attributesInterpolated"></a>
The user defined contact attributes that are resolved when the search result is returned.
Type: Array of strings
Required: No

 ** attributesNotInterpolated **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-attributesNotInterpolated"></a>
The user defined contact attributes that are not resolved when the search result is returned.
Type: Array of strings
Required: No

 ** channels **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-channels"></a>
The Connect Customer contact channels this quick response applies to. The supported contact channel types include `Chat`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-description"></a>
The description of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** groupingConfiguration **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-groupingConfiguration"></a>
The configuration information of the user groups that the quick response is accessible to.
Type: [GroupingConfiguration](API_amazon-q-connect_GroupingConfiguration.md) object
Required: No

 ** language **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-language"></a>
The language code value for the language in which the quick response is written.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** lastModifiedBy **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-lastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the quick response search result data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: No

 ** shortcutKey **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-shortcutKey"></a>
The shortcut key of the quick response. The value should be unique across the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchResultData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_QuickResponseSearchResultData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QuickResponseSearchResultData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QuickResponseSearchResultData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QuickResponseSearchResultData)
