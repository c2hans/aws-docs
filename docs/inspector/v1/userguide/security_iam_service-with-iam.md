---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/security_iam_service-with-iam.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# How Amazon Inspector Classic works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon Inspector, learn what IAM features are available to use with Amazon Inspector.

**IAM features you can use with Amazon Inspector Classic**

| IAM feature | Amazon Inspector support |
| --- | --- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes |
| [Policy resources](security-iam.md#security_iam_service-with-iam-id-based-policies-resources) |  Yes |
| [Policy condition keys (service-specific)](security-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes |
| [ACLs](security-iam.md#security_iam_service-with-iam-acls) |  No  |
| [ABAC (tags in policies)](security-iam.md#security_iam_service-with-iam-tags) |  Partial |
| [Temporary credentials](security-iam.md#security_iam_service-with-iam-roles-tempcreds) |  Yes |
| [Principal permissions](security-iam.md#security_iam_service-with-iam-principal-permissions) |  Yes |
| [Service roles](security-iam.md#security_iam_service-with-iam-roles-service) |  No  |
| [Service-linked roles](security-iam.md#security_iam_service-with-iam-roles-service-linked) |  Yes |

To get a high-level view of how Amazon Inspector and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Amazon Inspector
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Amazon Inspector
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Amazon Inspector identity-based policies, see [Identity-based policy examples for Amazon Inspector Classic](security_iam_id-based-policy-examples.md).

## Resource-based policies within Amazon Inspector
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Amazon Inspector
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon Inspector actions, see [Actions defined by Amazon Inspector Classic](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspector.html#amazoninspector-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Amazon Inspector use the following prefix before the action:

```
inspector
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "inspector:{{action1}}",
      "inspector:{{action2}}"
         ]
```

The following permissions policy grants a user permission to run all the operations that begin with `Describe` and `List`. These operations show information about an Amazon Inspector resource, such as an assessment target or finding. The wildcard character (\*) in the `Resource` element indicates that the operations are allowed for all Amazon Inspector resources that are owned by the account:

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action": [
            "inspector:Describe*",
            "inspector:List*"
            ],
         "Resource":"*"
      }
   ]
}
```

------
