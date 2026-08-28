---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserDataFilters.html
---

# UserDataFilters
<a name="API_UserDataFilters"></a>

A filter for the user data.

## Contents
<a name="API_UserDataFilters_Contents"></a>

 ** Agents **   <a name="connect-Type-UserDataFilters-Agents"></a>
A list of up to 100 agent IDs or ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** ContactFilter **   <a name="connect-Type-UserDataFilters-ContactFilter"></a>
A filter for the user data based on the contact information that is associated to the user. It contains a list of contact states.
Type: [ContactFilter](API_ContactFilter.md) object
Required: No

 ** Queues **   <a name="connect-Type-UserDataFilters-Queues"></a>
A list of up to 100 queues or ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** RoutingProfiles **   <a name="connect-Type-UserDataFilters-RoutingProfiles"></a>
A list of up to 100 routing profile IDs or ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** UserHierarchyGroups **   <a name="connect-Type-UserDataFilters-UserHierarchyGroups"></a>
A UserHierarchyGroup ID or ARN.
Type: Array of strings
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_UserDataFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserDataFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserDataFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserDataFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
