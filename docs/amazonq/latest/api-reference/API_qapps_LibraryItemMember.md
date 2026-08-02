---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_LibraryItemMember.html
---

# LibraryItemMember
<a name="API_qapps_LibraryItemMember"></a>

A library item is a snapshot of an Amazon Q App that can be published so the users in their Amazon Q Apps library can discover it, clone it, and run it.

## Contents
<a name="API_qapps_LibraryItemMember_Contents"></a>

 ** appId **   <a name="qbusiness-Type-qapps_LibraryItemMember-appId"></a>
The unique identifier of the Q App associated with the library item.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** appVersion **   <a name="qbusiness-Type-qapps_LibraryItemMember-appVersion"></a>
The version of the Q App associated with the library item.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** categories **   <a name="qbusiness-Type-qapps_LibraryItemMember-categories"></a>
The categories associated with the library item.
Type: Array of [Category](API_qapps_Category.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: Yes

 ** createdAt **   <a name="qbusiness-Type-qapps_LibraryItemMember-createdAt"></a>
The date and time the library item was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="qbusiness-Type-qapps_LibraryItemMember-createdBy"></a>
The user who created the library item.
Type: String
Required: Yes

 ** libraryItemId **   <a name="qbusiness-Type-qapps_LibraryItemMember-libraryItemId"></a>
The unique identifier of the library item.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** ratingCount **   <a name="qbusiness-Type-qapps_LibraryItemMember-ratingCount"></a>
The number of ratings the library item has received.
Type: Integer
Required: Yes

 ** status **   <a name="qbusiness-Type-qapps_LibraryItemMember-status"></a>
The status of the library item.
Type: String
Required: Yes

 ** isRatedByUser **   <a name="qbusiness-Type-qapps_LibraryItemMember-isRatedByUser"></a>
Whether the current user has rated the library item.
Type: Boolean
Required: No

 ** isVerified **   <a name="qbusiness-Type-qapps_LibraryItemMember-isVerified"></a>
Indicates whether the library item has been verified.
Type: Boolean
Required: No

 ** updatedAt **   <a name="qbusiness-Type-qapps_LibraryItemMember-updatedAt"></a>
The date and time the library item was last updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="qbusiness-Type-qapps_LibraryItemMember-updatedBy"></a>
The user who last updated the library item.
Type: String
Required: No

 ** userCount **   <a name="qbusiness-Type-qapps_LibraryItemMember-userCount"></a>
The number of users who have the associated Q App.
Type: Integer
Required: No

## See Also
<a name="API_qapps_LibraryItemMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/LibraryItemMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/LibraryItemMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/LibraryItemMember)
