---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualNodeRef.html
---

# VirtualNodeRef
<a name="API_VirtualNodeRef"></a>

An object that represents a virtual node returned by a list operation.

## Contents
<a name="API_VirtualNodeRef_Contents"></a>

 ** arn **   <a name="appmesh-Type-VirtualNodeRef-arn"></a>
The full Amazon Resource Name (ARN) for the virtual node.
Type: String
Required: Yes

 ** createdAt **   <a name="appmesh-Type-VirtualNodeRef-createdAt"></a>
The Unix epoch timestamp in seconds for when the resource was created.
Type: Timestamp
Required: Yes

 ** lastUpdatedAt **   <a name="appmesh-Type-VirtualNodeRef-lastUpdatedAt"></a>
The Unix epoch timestamp in seconds for when the resource was last updated.
Type: Timestamp
Required: Yes

 ** meshName **   <a name="appmesh-Type-VirtualNodeRef-meshName"></a>
The name of the service mesh that the virtual node resides in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** meshOwner **   <a name="appmesh-Type-VirtualNodeRef-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).
Type: String
Length Constraints: Fixed length of 12.
Required: Yes

 ** resourceOwner **   <a name="appmesh-Type-VirtualNodeRef-resourceOwner"></a>
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it's the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).
Type: String
Length Constraints: Fixed length of 12.
Required: Yes

 ** version **   <a name="appmesh-Type-VirtualNodeRef-version"></a>
The version of the resource. Resources are created at version 1, and this version is incremented each time that they're updated.
Type: Long
Required: Yes

 ** virtualNodeName **   <a name="appmesh-Type-VirtualNodeRef-virtualNodeName"></a>
The name of the virtual node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_VirtualNodeRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualNodeRef)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualNodeRef)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualNodeRef)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
