---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_VmEntitlement.html
---

# VmEntitlement
<a name="API_VmEntitlement"></a>

An object that represents a Windows Server License entitlement for a virtual machine in an Amazon EVS environment.

## Contents
<a name="API_VmEntitlement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** connectorId **   <a name="evs-Type-VmEntitlement-connectorId"></a>
The unique ID of the connector associated with the entitlement.
Type: String
Pattern: `(cnctr-[a-zA-Z0-9]{10})`
Required: No

 ** environmentId **   <a name="evs-Type-VmEntitlement-environmentId"></a>
The unique ID of the environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: No

 ** errorDetail **   <a name="evs-Type-VmEntitlement-errorDetail"></a>
The error details associated with the entitlement, if applicable.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** lastSyncedAt **   <a name="evs-Type-VmEntitlement-lastSyncedAt"></a>
The date and time that the entitlement was last synced.
Type: Timestamp
Required: No

 ** startedAt **   <a name="evs-Type-VmEntitlement-startedAt"></a>
The date and time that the entitlement started.
Type: Timestamp
Required: No

 ** status **   <a name="evs-Type-VmEntitlement-status"></a>
The status of the entitlement.
Type: String
Valid Values: `CREATING | CREATED | DELETED | AT_RISK | ENTITLEMENT_REMOVED | CREATE_FAILED`
Required: No

 ** stoppedAt **   <a name="evs-Type-VmEntitlement-stoppedAt"></a>
The date and time that the entitlement stopped.
Type: Timestamp
Required: No

 ** type **   <a name="evs-Type-VmEntitlement-type"></a>
The type of entitlement.
Type: String
Valid Values: `WINDOWS_SERVER`
Required: No

 ** vmId **   <a name="evs-Type-VmEntitlement-vmId"></a>
The unique ID of the virtual machine.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `vm-[0-9]+`
Required: No

 ** vmName **   <a name="evs-Type-VmEntitlement-vmName"></a>
The name of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_VmEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/VmEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/VmEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/VmEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
