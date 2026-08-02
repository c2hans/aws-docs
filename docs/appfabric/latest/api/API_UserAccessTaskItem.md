---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_UserAccessTaskItem.html
---

# UserAccessTaskItem
<a name="API_UserAccessTaskItem"></a>

Contains information about a user access task.

## Contents
<a name="API_UserAccessTaskItem_Contents"></a>

 ** app **   <a name="appfabric-Type-UserAccessTaskItem-app"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** tenantId **   <a name="appfabric-Type-UserAccessTaskItem-tenantId"></a>
The ID of the application tenant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** error **   <a name="appfabric-Type-UserAccessTaskItem-error"></a>
Error from the task, if any.
Type: [TaskError](API_TaskError.md) object
Required: No

 ** taskId **   <a name="appfabric-Type-UserAccessTaskItem-taskId"></a>
The unique ID of the task.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_UserAccessTaskItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/UserAccessTaskItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/UserAccessTaskItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/UserAccessTaskItem)
