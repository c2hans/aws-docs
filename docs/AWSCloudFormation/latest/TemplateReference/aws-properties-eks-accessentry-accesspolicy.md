---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-accessentry-accesspolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::AccessEntry AccessPolicy
<a name="aws-properties-eks-accessentry-accesspolicy"></a>

An access policy includes permissions that allow Amazon EKS to authorize an IAM principal to work with Kubernetes objects on your cluster. The policies are managed by Amazon EKS, but they're not IAM policies. You can't view the permissions in the policies using the API. The permissions for many of the policies are similar to the Kubernetes `cluster-admin`, `admin`, `edit`, and `view` cluster roles. For more information about these cluster roles, see [User-facing roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) in the Kubernetes documentation. To view the contents of the policies, see [Access policy permissions](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html#access-policy-permissions) in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-accessentry-accesspolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-accessentry-accesspolicy-syntax.json"></a>

```
{
  "[AccessScope](#cfn-eks-accessentry-accesspolicy-accessscope)" : {{AccessScope}},
  "[PolicyArn](#cfn-eks-accessentry-accesspolicy-policyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-accessentry-accesspolicy-syntax.yaml"></a>

```
  [AccessScope](#cfn-eks-accessentry-accesspolicy-accessscope): {{
    AccessScope}}
  [PolicyArn](#cfn-eks-accessentry-accesspolicy-policyarn): {{String}}
```

## Properties
<a name="aws-properties-eks-accessentry-accesspolicy-properties"></a>

`AccessScope`  <a name="cfn-eks-accessentry-accesspolicy-accessscope"></a>
The scope of an `AccessPolicy` that's associated to an `AccessEntry`.
*Required*: Yes
*Type*: [AccessScope](aws-properties-eks-accessentry-accessscope.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyArn`  <a name="cfn-eks-accessentry-accesspolicy-policyarn"></a>
The ARN of the access policy.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
