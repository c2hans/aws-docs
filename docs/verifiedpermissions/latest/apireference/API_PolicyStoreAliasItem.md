---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyStoreAliasItem.html
---

# PolicyStoreAliasItem
<a name="API_PolicyStoreAliasItem"></a>

Contains information about a policy store alias.

This data type is used as a response parameter for the [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html) operation.

## Contents
<a name="API_PolicyStoreAliasItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** aliasArn **   <a name="verifiedpermissions-Type-PolicyStoreAliasItem-aliasArn"></a>
The Amazon Resource Name (ARN) of the policy store alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: Yes

 ** aliasName **   <a name="verifiedpermissions-Type-PolicyStoreAliasItem-aliasName"></a>
The name of the policy store alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** createdAt **   <a name="verifiedpermissions-Type-PolicyStoreAliasItem-createdAt"></a>
The date and time the policy store alias was created.
Type: Timestamp
Required: Yes

 ** policyStoreId **   <a name="verifiedpermissions-Type-PolicyStoreAliasItem-policyStoreId"></a>
The ID of the policy store associated with the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** state **   <a name="verifiedpermissions-Type-PolicyStoreAliasItem-state"></a>
The state of the policy store alias. Policy Store Aliases in the Active state can be used normally. When a policy store alias is deleted, it enters the PendingDeletion state. Policy Store Aliases in the PendingDeletion state cannot be used, and creating a policy store alias with the same alias name will fail.
Type: String
Valid Values: `Active | PendingDeletion`
Required: Yes

## See Also
<a name="API_PolicyStoreAliasItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyStoreAliasItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyStoreAliasItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyStoreAliasItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
