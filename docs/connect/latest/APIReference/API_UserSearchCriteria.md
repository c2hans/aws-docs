---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserSearchCriteria.html
---

# UserSearchCriteria
<a name="API_UserSearchCriteria"></a>

The search criteria to be used to return users.

**Note**
The `name` and `description` fields support "contains" queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.

## Contents
<a name="API_UserSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-UserSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: Array of [UserSearchCriteria](#API_UserSearchCriteria) objects
Required: No

 ** HierarchyGroupCondition **   <a name="connect-Type-UserSearchCriteria-HierarchyGroupCondition"></a>
A leaf node condition which can be used to specify a hierarchy group condition.
Type: [HierarchyGroupCondition](API_HierarchyGroupCondition.md) object
Required: No

 ** ListCondition **   <a name="connect-Type-UserSearchCriteria-ListCondition"></a>
A leaf node condition which can be used to specify a List condition to search users with attributes included in Lists like Proficiencies.
Type: [ListCondition](API_ListCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-UserSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [UserSearchCriteria](#API_UserSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-UserSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
The currently supported values for `FieldName` are `Username`, `FirstName`, `LastName`, `RoutingProfileId`, `SecurityProfileId`, `resourceId`.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_UserSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserSearchCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
