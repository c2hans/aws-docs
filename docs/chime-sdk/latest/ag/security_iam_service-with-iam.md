---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_service-with-iam.html
---

# How the Amazon Chime SDK works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to the Amazon Chime SDK, learn the IAM features available for use with the Amazon Chime SDK. To get a high-level view of how the Amazon Chime SDK and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Amazon Chime SDK identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Resources](#security_iam_service-with-iam-id-based-policies-resources)
+ [Examples](#security_iam_service-with-iam-id-based-policies-examples)

## Amazon Chime SDK identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. The Amazon Chime SDK supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

For more information about actions, see [Actions, resources, and condition keys for Amazon Chime](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html) in the *Service Authorization Reference*.

### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

The Amazon Chime SDK provides a set of service-specific condition keys. For more information, see [Condition keys for Amazon Chime](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html#amazonchime-policy-keys) in the *Service Authorization Reference*.

## Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

The Amazon Chime SDK supports specifying resource ARNs in a policy. For more information, see [Resource types defined by Amazon Chime](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html#amazonchime-resources-for-iam-policies)

## Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Amazon Chime SDK identity-based policies, see [Amazon Chime SDK identity-based policy examples](security_iam_id-based-policy-examples.md).
