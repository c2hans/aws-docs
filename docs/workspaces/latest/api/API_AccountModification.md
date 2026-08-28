---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AccountModification.html
---

# AccountModification
<a name="API_AccountModification"></a>

Describes a modification to the configuration of Bring Your Own License (BYOL) for the specified account.

## Contents
<a name="API_AccountModification_Contents"></a>

 ** DedicatedTenancyManagementCidrRange **   <a name="WorkSpaces-Type-AccountModification-DedicatedTenancyManagementCidrRange"></a>
The IP address range, specified as an IPv4 CIDR block, for the management network interface used for the account.
Type: String
Pattern: `(^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.0\.0)(\/(16$))$`
Required: No

 ** DedicatedTenancySupport **   <a name="WorkSpaces-Type-AccountModification-DedicatedTenancySupport"></a>
The status of BYOL (whether BYOL is being enabled or disabled).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ErrorCode **   <a name="WorkSpaces-Type-AccountModification-ErrorCode"></a>
The error code that is returned if the configuration of BYOL cannot be modified.
Type: String
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-AccountModification-ErrorMessage"></a>
The text of the error message that is returned if the configuration of BYOL cannot be modified.
Type: String
Required: No

 ** ModificationState **   <a name="WorkSpaces-Type-AccountModification-ModificationState"></a>
The state of the modification to the configuration of BYOL.
Type: String
Valid Values: `PENDING | COMPLETED | FAILED`
Required: No

 ** StartTime **   <a name="WorkSpaces-Type-AccountModification-StartTime"></a>
The timestamp when the modification of the BYOL configuration was started.
Type: Timestamp
Required: No

## See Also
<a name="API_AccountModification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AccountModification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AccountModification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AccountModification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
