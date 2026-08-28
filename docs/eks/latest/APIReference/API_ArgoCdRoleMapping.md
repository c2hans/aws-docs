---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_ArgoCdRoleMapping.html
---

# ArgoCdRoleMapping
<a name="API_ArgoCdRoleMapping"></a>

A mapping between an Argo CD role and IAM Identity CenterIAM; Identity Center identities. This defines which users or groups have specific permissions in Argo CD.

## Contents
<a name="API_ArgoCdRoleMapping_Contents"></a>

 ** identities **   <a name="AmazonEKS-Type-ArgoCdRoleMapping-identities"></a>
A list of IAM Identity CenterIAM; Identity Center identities (users or groups) that should be assigned this Argo CD role.
Type: Array of [SsoIdentity](API_SsoIdentity.md) objects
Required: Yes

 ** role **   <a name="AmazonEKS-Type-ArgoCdRoleMapping-role"></a>
The Argo CD role to assign. Valid values are:
+  `ADMIN` – Full administrative access to Argo CD.
+  `EDITOR` – Edit access to Argo CD resources.
+  `VIEWER` – Read-only access to Argo CD resources.
Type: String
Valid Values: `ADMIN | EDITOR | VIEWER`
Required: Yes

## See Also
<a name="API_ArgoCdRoleMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ArgoCdRoleMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ArgoCdRoleMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ArgoCdRoleMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
