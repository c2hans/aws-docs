---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_WorkspaceInstance.html
---

# WorkspaceInstance
<a name="API_WorkspaceInstance"></a>

Represents a single WorkSpace Instance.

## Contents
<a name="API_WorkspaceInstance_Contents"></a>

 ** EC2ManagedInstance **   <a name="workspacesinstances-Type-WorkspaceInstance-EC2ManagedInstance"></a>
Details of the associated EC2 managed instance.
Type: [EC2ManagedInstance](API_EC2ManagedInstance.md) object
Required: No

 ** ProvisionState **   <a name="workspacesinstances-Type-WorkspaceInstance-ProvisionState"></a>
Current provisioning state of the WorkSpace Instance.
Type: String
Valid Values: `ALLOCATING | ALLOCATED | DEALLOCATING | DEALLOCATED | ERROR_ALLOCATING | ERROR_DEALLOCATING`
Required: No

 ** WorkspaceInstanceId **   <a name="workspacesinstances-Type-WorkspaceInstance-WorkspaceInstanceId"></a>
Unique identifier for the WorkSpace Instance.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 70.
Pattern: `wsinst-[0-9a-zA-Z]{8,63}`
Required: No

## See Also
<a name="API_WorkspaceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/WorkspaceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/WorkspaceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/WorkspaceInstance)
