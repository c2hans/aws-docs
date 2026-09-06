---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnapshotAnonymousUser.html
---

# SnapshotAnonymousUser
<a name="API_SnapshotAnonymousUser"></a>

A structure that contains information on the anonymous user configuration.

## Contents
<a name="API_SnapshotAnonymousUser_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RowLevelPermissionTags **   <a name="QS-Type-SnapshotAnonymousUser-RowLevelPermissionTags"></a>
The tags to be used for row-level security (RLS). Make sure that the relevant datasets have RLS tags configured before you start a snapshot export job. You can configure the RLS tags of a dataset with a `DataSet$RowLevelPermissionTagConfiguration` API call.
These are not the tags that are used for AWS resource tagging. For more information on row level security in Amazon Quick Sight, see [Using Row-Level Security (RLS) with Tags](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html)in the *Amazon Quick User Guide*.
Type: Array of [SessionTag](API_SessionTag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_SnapshotAnonymousUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnapshotAnonymousUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnapshotAnonymousUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnapshotAnonymousUser)
