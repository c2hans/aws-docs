---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_SearchRelatedItemsResponseItem.html
---

# SearchRelatedItemsResponseItem
<a name="API_connect-cases_SearchRelatedItemsResponseItem"></a>

A list of items that represent RelatedItems.

## Contents
<a name="API_connect-cases_SearchRelatedItemsResponseItem_Contents"></a>

 ** associationTime **   <a name="connect-Type-connect-cases_SearchRelatedItemsResponseItem-associationTime"></a>
Time at which a related item was associated with a case.
Type: Timestamp
Required: Yes

 ** content **   <a name="connect-Type-connect-cases_SearchRelatedItemsResponseItem-content"></a>
Represents the content of a particular type of related item.
Type: [RelatedItemContent](API_connect-cases_RelatedItemContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** relatedItemId **   <a name="connect-Type-connect-cases_SearchRelatedItemsResponseItem-relatedItemId"></a>
Unique identifier of a related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** type **   <a name="connect-Type-connect-cases_SearchRelatedItemsResponseItem-type"></a>
Type of a related item.
Type: String
Valid Values: `Contact | Comment | File | Sla | ConnectCase | Custom`
Required: Yes

 ** performedBy **   <a name="connect-Type-connect-cases_SearchRelatedItemsResponseItem-performedBy"></a>
Represents the creator of the related item.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-connect-cases_SearchRelatedItemsResponseItem-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map
Required: No

## See Also
<a name="API_connect-cases_SearchRelatedItemsResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SearchRelatedItemsResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SearchRelatedItemsResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SearchRelatedItemsResponseItem)
