---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html
---

# How Application Auto Scaling works with IAM
<a name="security_iam_service-with-iam"></a>

**Note**
In December 2017, there was an update for Application Auto Scaling, enabling several service-linked roles for Application Auto Scaling integrated services. Specific IAM permissions *and* an Application Auto Scaling service-linked role (or a service role for Amazon EMR auto scaling) are required so that users can configure scaling.

Before you use IAM to manage access to Application Auto Scaling, learn what IAM features are available to use with Application Auto Scaling.

**IAM features you can use with Application Auto Scaling**

| IAM feature | Application Auto Scaling support |
| --- | --- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes |
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  |
| [ACLs](#security_iam_service-with-iam-acls) |  No  |
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Partial |
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes |
| [Service roles](#security_iam_service-with-iam-roles-service) |  Yes |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes |

To get a high-level view of how Application Auto Scaling and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Application Auto Scaling identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Identity-based policy examples for Application Auto Scaling
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Application Auto Scaling identity-based policies, see [Application Auto Scaling identity-based policy examples](security_iam_id-based-policy-examples.md).

### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

In an IAM policy statement, you can specify any API action from any service that supports IAM. For Application Auto Scaling, use the following prefix with the name of the API action: `application-autoscaling:`. For example: `application-autoscaling:RegisterScalableTarget`, `application-autoscaling:PutScalingPolicy`, and `application-autoscaling:DeregisterScalableTarget`.

To specify multiple actions in a single statement, separate them with commas as shown in the following example.

```
"Action": [
      "application-autoscaling:DescribeScalingPolicies",
      "application-autoscaling:DescribeScalingActivities"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action.

```
"Action": "application-autoscaling:Describe*"
```

For a list of Application Auto Scaling actions, see [Actions defined by AWS Application Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationautoscaling.html#awsapplicationautoscaling-actions-as-permissions) in the *Service Authorization Reference*.

### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

In an IAM policy statement, the `Resource` element specifies the object or objects that the statement covers. For Application Auto Scaling, each IAM policy statement applies to the scalable targets that you specify using their Amazon Resource Names (ARNs).

The ARN resource format for scalable targets:

```
arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/{{unique-identifier}}
```

For example, you can indicate a specific scalable target in your statement using its ARN as follows. The unique ID (1234abcd56ab78cd901ef1234567890ab123) is a value assigned by Application Auto Scaling to the scalable target.

```
"Resource": "arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
```

You can specify all instances that belong to a specific account by replacing the unique identifier with a wildcard (\*) as follows.

```
"Resource": "arn:aws:application-autoscaling:us-east-1:123456789012:scalable-target/*"
```

To specify all resources, or if a specific API action does not support ARNs, use a wildcard (\*) as the `Resource` element as follows.

```
"Resource": "*"
```

For more information, see [Resource types defined by AWS Application Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationautoscaling.html#awsapplicationautoscaling-policy-keys) in the *Service Authorization Reference*.

### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

You can specify conditions in the IAM policies that control access to Application Auto Scaling resources. The policy statement is effective only when the conditions are true.

Application Auto Scaling supports the following service-defined condition keys that you can use in identity-based policies to determine who can perform Application Auto Scaling API actions.
+ `application-autoscaling:scalable-dimension`
+ `application-autoscaling:service-namespace`

To learn which Application Auto Scaling API actions you can use a condition key with, see [Actions defined by AWS Application Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationautoscaling.html#awsapplicationautoscaling-actions-as-permissions) in the *Service Authorization Reference*. For more information about using Application Auto Scaling condition keys, see [Condition keys for AWS Application Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationautoscaling.html#awsapplicationautoscaling-policy-keys).

To view the global condition keys that are available to all services, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## Resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No

Other AWS services, such as Amazon Simple Storage Service, support resource-based permissions policies. For example, you can attach a permissions policy to an S3 bucket to manage access permissions to that bucket.

Application Auto Scaling does not support resource-based policies.

## Access Control Lists (ACLs)
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No

Application Auto Scaling does not support Access Control Lists (ACLs).

## ABAC with Application Auto Scaling
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes. In AWS, these attributes are called *tags*. You can attach tags to IAM entities (users or roles) and to many AWS resources. Tagging entities and resources is the first step of ABAC. Then you design ABAC policies to allow operations when the principal's tag matches the tag on the resource that they are trying to access.

ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

ABAC is possible for resources that support tags, but not everything supports tags. Scheduled actions and scaling policies don't support tags, but scalable targets support tags. For more information, see [Tagging support for Application Auto Scaling](resource-tagging-support.md).

For more information about ABAC, see [What is ABAC?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with Application Auto Scaling
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Service roles
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

If your Amazon EMR cluster uses automatic scaling, this feature allows Application Auto Scaling to assume a service role on your behalf. Similar to a service-linked role, a service role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator can change the permissions for this role. However, doing so might break the functionality of the service.

Application Auto Scaling supports service roles only for Amazon EMR. For documentation for the EMR service role, see [Using automatic scaling with a custom policy for instance groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html) in the *Amazon EMR Management Guide*.

**Note**
With the introduction of service-linked roles, several legacy service roles are no longer required, for example, for Amazon ECS and Spot Fleet.

## Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles.

For information about Application Auto Scaling service-linked roles, see [Service-linked roles for Application Auto Scaling](application-auto-scaling-service-linked-roles.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
