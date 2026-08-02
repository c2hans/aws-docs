---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/managing-permissions-for-individuals.html
---

# Managing permissions for individuals
<a name="managing-permissions-for-individuals"></a>

By using permissions sets, the permissions boundary, and the **CloudFormationRole** IAM role, you can limit the amount of permissions that you need to assign directly to individual principals. This helps you manage access as your company grows and helps you apply the security best practice of granting least privilege.

You can also use *service-linked roles*, which grant permissions to an AWS service to provision resources on your behalf. Instead of granting permissions to the IAM principal (user, user group, or role), you can grant the permissions to the service. For example, the service-linked role for [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) allows you to provision your own templates, resources, and environments, without assigning permissions to the IAM principal. For more information, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (IAM documentation).

Another best practice is to limit the amount of access individuals have to the AWS Management Console. By limiting access to the console, you can require individuals to provision resources by using infrastructure as code (IaC) technologies, such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [HashiCorp Terraform](https://www.terraform.io/), or [Pulumi](https://www.pulumi.com/). Managing infrastructure through IaC you to track changes to resources over time and introduce mechanisms for approving changes, such as GitHub pull requests.
