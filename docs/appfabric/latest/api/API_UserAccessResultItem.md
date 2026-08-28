---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_UserAccessResultItem.html
---

# UserAccessResultItem
<a name="API_UserAccessResultItem"></a>

Contains information about a user's access to an application.

## Contents
<a name="API_UserAccessResultItem_Contents"></a>

 ** app **   <a name="appfabric-Type-UserAccessResultItem-app"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** email **   <a name="appfabric-Type-UserAccessResultItem-email"></a>
The email address of the target user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 320.
Pattern: `[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*`
Required: No

 ** resultStatus **   <a name="appfabric-Type-UserAccessResultItem-resultStatus"></a>
The status of the user access result item.
The following states are possible:
+  `IN_PROGRESS`: The user access task is in progress.
+  `COMPLETED`: The user access task completed successfully.
+  `FAILED`: The user access task failed.
+  `EXPIRED`: The user access task expired.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED | EXPIRED`
Required: No

 ** taskError **   <a name="appfabric-Type-UserAccessResultItem-taskError"></a>
Contains information about an error returned from a user access task.
Type: [TaskError](API_TaskError.md) object
Required: No

 ** taskId **   <a name="appfabric-Type-UserAccessResultItem-taskId"></a>
The unique ID of the task.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** tenantDisplayName **   <a name="appfabric-Type-UserAccessResultItem-tenantDisplayName"></a>
The display name of the tenant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** tenantId **   <a name="appfabric-Type-UserAccessResultItem-tenantId"></a>
The ID of the application tenant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** userFirstName **   <a name="appfabric-Type-UserAccessResultItem-userFirstName"></a>
The first name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** userFullName **   <a name="appfabric-Type-UserAccessResultItem-userFullName"></a>
The full name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** userId **   <a name="appfabric-Type-UserAccessResultItem-userId"></a>
The unique ID of user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** userLastName **   <a name="appfabric-Type-UserAccessResultItem-userLastName"></a>
The last name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** userStatus **   <a name="appfabric-Type-UserAccessResultItem-userStatus"></a>
The status of the user returned by the application.
Type: String
Required: No

## See Also
<a name="API_UserAccessResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/UserAccessResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/UserAccessResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/UserAccessResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
