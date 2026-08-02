---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_RelatedItemTypeFilter.html
---

# RelatedItemTypeFilter
<a name="API_connect-cases_RelatedItemTypeFilter"></a>

The list of types of related items and their parameters to use for filtering.

## Contents
<a name="API_connect-cases_RelatedItemTypeFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** comment **   <a name="connect-Type-connect-cases_RelatedItemTypeFilter-comment"></a>
A filter for related items of type `Comment`.
Type: [CommentFilter](API_connect-cases_CommentFilter.md) object
Required: No

 ** connectCase **   <a name="connect-Type-connect-cases_RelatedItemTypeFilter-connectCase"></a>
Represents the Connect Customer case to be created as a related item.
Type: [ConnectCaseFilter](API_connect-cases_ConnectCaseFilter.md) object
Required: No

 ** contact **   <a name="connect-Type-connect-cases_RelatedItemTypeFilter-contact"></a>
A filter for related items of type `Contact`.
Type: [ContactFilter](API_connect-cases_ContactFilter.md) object
Required: No

 ** custom **   <a name="connect-Type-connect-cases_RelatedItemTypeFilter-custom"></a>
Represents the content of a `Custom` type related item.
Type: [CustomFilter](API_connect-cases_CustomFilter.md) object
Required: No

 ** file **   <a name="connect-Type-connect-cases_RelatedItemTypeFilter-file"></a>
A filter for related items of this type of `File`.
Type: [FileFilter](API_connect-cases_FileFilter.md) object
Required: No

 ** sla **   <a name="connect-Type-connect-cases_RelatedItemTypeFilter-sla"></a>
 Filter for related items of type `SLA`.
Type: [SlaFilter](API_connect-cases_SlaFilter.md) object
Required: No

## See Also
<a name="API_connect-cases_RelatedItemTypeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/RelatedItemTypeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/RelatedItemTypeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/RelatedItemTypeFilter)
