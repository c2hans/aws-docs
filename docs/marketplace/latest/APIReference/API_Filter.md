---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter object, used to optionally filter results from calls to the `ListEntities` and `ListChangeSets` actions.

## Contents
<a name="API_Filter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="AWSMarketplaceService-Type-Filter-Name"></a>
For `ListEntities`, the supported value for this is an `EntityId`.
For `ListChangeSets`, the supported values are as follows:
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** ValueList **   <a name="AWSMarketplaceService-Type-Filter-ValueList"></a>
 `ListEntities` - This is a list of unique `EntityId`s.
 `ListChangeSets` - The supported filter names and associated `ValueList`s is as follows:
+  `ChangeSetName` - The supported `ValueList` is a list of non-unique `ChangeSetName`s. These are defined when you call the `StartChangeSet` action.
+  `Status` - The supported `ValueList` is a list of statuses for all change set requests.
+  `EntityId` - The supported `ValueList` is a list of unique `EntityId`s.
+  `BeforeStartTime` - The supported `ValueList` is a list of all change sets that started before the filter value.
+  `AfterStartTime` - The supported `ValueList` is a list of all change sets that started after the filter value.
+  `BeforeEndTime` - The supported `ValueList` is a list of all change sets that ended before the filter value.
+  `AfterEndTime` - The supported `ValueList` is a list of all change sets that ended after the filter value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/Filter)
