---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ManagementPreference.html
---

# ManagementPreference
<a name="API_ManagementPreference"></a>

 Preferences for migrating an application to AWS.

## Contents
<a name="API_ManagementPreference_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsManagedResources **   <a name="migrationhubstrategy-Type-ManagementPreference-awsManagedResources"></a>
 Indicates interest in solutions that are managed by AWS.
Type: [AwsManagedResources](API_AwsManagedResources.md) object
Required: No

 ** noPreference **   <a name="migrationhubstrategy-Type-ManagementPreference-noPreference"></a>
 No specific preference.
Type: [NoManagementPreference](API_NoManagementPreference.md) object
Required: No

 ** selfManageResources **   <a name="migrationhubstrategy-Type-ManagementPreference-selfManageResources"></a>
 Indicates interest in managing your own resources on AWS.
Type: [SelfManageResources](API_SelfManageResources.md) object
Required: No

## See Also
<a name="API_ManagementPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ManagementPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ManagementPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ManagementPreference)
