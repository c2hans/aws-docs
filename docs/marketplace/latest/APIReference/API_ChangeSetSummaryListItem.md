---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ChangeSetSummaryListItem.html
---

# ChangeSetSummaryListItem
<a name="API_ChangeSetSummaryListItem"></a>

A summary of a change set returned in a list of change sets when the `ListChangeSets` action is called.

## Contents
<a name="API_ChangeSetSummaryListItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChangeSetArn **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-ChangeSetArn"></a>
The ARN associated with the unique identifier for the change set referenced in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`
Required: No

 ** ChangeSetId **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-ChangeSetId"></a>
The unique identifier for a change set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

 ** ChangeSetName **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-ChangeSetName"></a>
The non-unique name for the change set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w\s+=.:@-]+$`
Required: No

 ** EndTime **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-EndTime"></a>
The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was finished.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** EntityIdList **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-EntityIdList"></a>
This object is a list of entity IDs (string) that are a part of a change set. The entity ID list is a maximum of 20 entities. It must contain at least one entity.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: No

 ** FailureCode **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-FailureCode"></a>
Returned if the change set is in `FAILED` status. Can be either `CLIENT_ERROR`, which means that there are issues with the request (see the `ErrorDetailList` of `DescribeChangeSet`), or `SERVER_FAULT`, which means that there is a problem in the system, and you should retry your request.
Type: String
Valid Values: `CLIENT_ERROR | SERVER_FAULT`
Required: No

 ** StartTime **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-StartTime"></a>
The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was started.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** Status **   <a name="AWSMarketplaceService-Type-ChangeSetSummaryListItem-Status"></a>
The current status of the change set.
Type: String
Valid Values: `PREPARING | APPLYING | SUCCEEDED | CANCELLED | FAILED`
Required: No

## See Also
<a name="API_ChangeSetSummaryListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ChangeSetSummaryListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ChangeSetSummaryListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ChangeSetSummaryListItem)
