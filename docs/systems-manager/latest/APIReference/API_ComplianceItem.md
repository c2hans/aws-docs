---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ComplianceItem.html
---

# ComplianceItem
<a name="API_ComplianceItem"></a>

Information about the compliance as defined by the resource type. For example, for a patch resource type, `Items` includes information about the PatchSeverity, Classification, and so on.

## Contents
<a name="API_ComplianceItem_Contents"></a>

 ** ComplianceType **   <a name="systemsmanager-Type-ComplianceItem-ComplianceType"></a>
The compliance type. For example, Association (for a State Manager association), Patch, or Custom:`string` are all valid compliance types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([A-Za-z0-9_\-]\w+|Custom:[a-zA-Z0-9_\-]\w+)$`
Required: No

 ** Details **   <a name="systemsmanager-Type-ComplianceItem-Details"></a>
A "Key": "Value" tag combination for the compliance item.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** ExecutionSummary **   <a name="systemsmanager-Type-ComplianceItem-ExecutionSummary"></a>
A summary for the compliance item. The summary includes an execution ID, the execution type (for example, command), and the execution time.
For State Manager associations, the `ExecutionTime` value represents when the compliance status was captured and aggregated by the Systems Manager service, not necessarily when the underlying association was executed on the managed node. State Manager updates compliance status for all associations on an instance whenever any association executes, which means multiple associations may show the same execution time even if they were executed at different times.
Type: [ComplianceExecutionSummary](API_ComplianceExecutionSummary.md) object
Required: No

 ** Id **   <a name="systemsmanager-Type-ComplianceItem-Id"></a>
An ID for the compliance item. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article; for example: KB4010320.
Type: String
Required: No

 ** ResourceId **   <a name="systemsmanager-Type-ComplianceItem-ResourceId"></a>
An ID for the resource. For a managed node, this is the node ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-ComplianceItem-ResourceType"></a>
The type of resource. `ManagedInstance` is currently the only supported resource type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Severity **   <a name="systemsmanager-Type-ComplianceItem-Severity"></a>
The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** Status **   <a name="systemsmanager-Type-ComplianceItem-Status"></a>
The status of the compliance item. An item is either COMPLIANT, NON\_COMPLIANT, or an empty string (for Windows patches that aren't applicable).
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: No

 ** Title **   <a name="systemsmanager-Type-ComplianceItem-Title"></a>
A title for the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.
Type: String
Length Constraints: Maximum length of 500.
Required: No

## See Also
<a name="API_ComplianceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ComplianceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ComplianceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ComplianceItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
