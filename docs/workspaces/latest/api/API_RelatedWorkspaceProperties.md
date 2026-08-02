---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_RelatedWorkspaceProperties.html
---

# RelatedWorkspaceProperties
<a name="API_RelatedWorkspaceProperties"></a>

Describes the related WorkSpace. The related WorkSpace could be a standby WorkSpace or primary WorkSpace related to the specified WorkSpace.

## Contents
<a name="API_RelatedWorkspaceProperties_Contents"></a>

 ** Region **   <a name="WorkSpaces-Type-RelatedWorkspaceProperties-Region"></a>
The Region of the related WorkSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 31.
Pattern: `^[-0-9a-z]{1,31}$`
Required: No

 ** State **   <a name="WorkSpaces-Type-RelatedWorkspaceProperties-State"></a>
Indicates the state of the WorkSpace.
Type: String
Valid Values: `PENDING | AVAILABLE | IMPAIRED | UNHEALTHY | REBOOTING | STARTING | REBUILDING | RESTORING | MAINTENANCE | ADMIN_MAINTENANCE | TERMINATING | TERMINATED | SUSPENDED | UPDATING | STOPPING | STOPPED | ERROR`
Required: No

 ** Type **   <a name="WorkSpaces-Type-RelatedWorkspaceProperties-Type"></a>
Indicates the type of WorkSpace.
Type: String
Valid Values: `PRIMARY | STANDBY`
Required: No

 ** WorkspaceId **   <a name="WorkSpaces-Type-RelatedWorkspaceProperties-WorkspaceId"></a>
The identifier of the related WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

## See Also
<a name="API_RelatedWorkspaceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/RelatedWorkspaceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/RelatedWorkspaceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/RelatedWorkspaceProperties)
