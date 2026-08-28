---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceBundle.html
---

# WorkspaceBundle
<a name="API_WorkspaceBundle"></a>

Describes a WorkSpace bundle.

## Contents
<a name="API_WorkspaceBundle_Contents"></a>

 ** BundleId **   <a name="WorkSpaces-Type-WorkspaceBundle-BundleId"></a>
The identifier of the bundle.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** BundleType **   <a name="WorkSpaces-Type-WorkspaceBundle-BundleType"></a>
The type of WorkSpace bundle.
Type: String
Valid Values: `REGULAR | STANDBY`
Required: No

 ** ComputeType **   <a name="WorkSpaces-Type-WorkspaceBundle-ComputeType"></a>
The compute type of the bundle. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).
Type: [ComputeType](API_ComputeType.md) object
Required: No

 ** CreationTime **   <a name="WorkSpaces-Type-WorkspaceBundle-CreationTime"></a>
The time when the bundle was created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpaces-Type-WorkspaceBundle-Description"></a>
The description of the bundle.
Type: String
Required: No

 ** ImageId **   <a name="WorkSpaces-Type-WorkspaceBundle-ImageId"></a>
The identifier of the image that was used to create the bundle.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: No

 ** LastUpdatedTime **   <a name="WorkSpaces-Type-WorkspaceBundle-LastUpdatedTime"></a>
The last time that the bundle was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="WorkSpaces-Type-WorkspaceBundle-Name"></a>
The name of the bundle.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Owner **   <a name="WorkSpaces-Type-WorkspaceBundle-Owner"></a>
The owner of the bundle. This is the account identifier of the owner, or `AMAZON` if the bundle is provided by AWS.
Type: String
Required: No

 ** RootStorage **   <a name="WorkSpaces-Type-WorkspaceBundle-RootStorage"></a>
The size of the root volume.
Type: [RootStorage](API_RootStorage.md) object
Required: No

 ** State **   <a name="WorkSpaces-Type-WorkspaceBundle-State"></a>
The state of the WorkSpace bundle.
Type: String
Valid Values: `AVAILABLE | PENDING | ERROR`
Required: No

 ** UserStorage **   <a name="WorkSpaces-Type-WorkspaceBundle-UserStorage"></a>
The size of the user volume.
Type: [UserStorage](API_UserStorage.md) object
Required: No

## See Also
<a name="API_WorkspaceBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceBundle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
