---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceSet.html
---

# ResourceSet
<a name="API_ResourceSet"></a>

A set of resources to include in a policy.

## Contents
<a name="API_ResourceSet_Contents"></a>

 ** Name **   <a name="fms-Type-ResourceSet-Name"></a>
The descriptive name of the resource set. You can't change the name of a resource set after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** ResourceTypeList **   <a name="fms-Type-ResourceSet-ResourceTypeList"></a>
Determines the resources that can be associated to the resource set. Depending on your setting for max results and the number of resource sets, a single call might not return the full list.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Description **   <a name="fms-Type-ResourceSet-Description"></a>
A description of the resource set.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Id **   <a name="fms-Type-ResourceSet-Id"></a>
A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^[a-z0-9A-Z]{22}$`
Required: No

 ** LastUpdateTime **   <a name="fms-Type-ResourceSet-LastUpdateTime"></a>
The last time that the resource set was changed.
Type: Timestamp
Required: No

 ** ResourceSetStatus **   <a name="fms-Type-ResourceSet-ResourceSetStatus"></a>
Indicates whether the resource set is in or out of an admin's Region scope.
+  `ACTIVE` - The administrator can manage and delete the resource set.
+  `OUT_OF_ADMIN_SCOPE` - The administrator can view the resource set, but they can't edit or delete the resource set. Existing protections stay in place. Any new resource that come into scope of the resource set won't be protected.
Type: String
Valid Values: `ACTIVE | OUT_OF_ADMIN_SCOPE`
Required: No

 ** UpdateToken **   <a name="fms-Type-ResourceSet-UpdateToken"></a>
An optional token that you can use for optimistic locking. Firewall Manager returns a token to your requests that access the resource set. The token marks the state of the resource set resource at the time of the request. Update tokens are not allowed when creating a resource set. After creation, each subsequent update call to the resource set requires the update token.
To make an unconditional change to the resource set, omit the token in your update request. Without the token, Firewall Manager performs your updates regardless of whether the resource set has changed since you last retrieved it.
To make a conditional change to the resource set, provide the token in your update request. Firewall Manager uses the token to ensure that the resource set hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the resource set again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ResourceSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ResourceSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ResourceSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ResourceSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
