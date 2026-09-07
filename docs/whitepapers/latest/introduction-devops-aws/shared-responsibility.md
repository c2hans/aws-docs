---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/shared-responsibility.html
---

# AWS Shared Responsibility Model
<a name="shared-responsibility"></a>

Security is a shared responsibility between AWS and the customer. The different parts of the Shared Responsibility Model are:
+ **AWS responsibility “Security of the Cloud”** - AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.
+ **Customer responsibility “Security in the Cloud”** – Customer responsibility is determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities.

This shared model can help relieve the customer’s operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. This is critical in the cases where customer want to understand the security of their build environments.

![A diagram depicting the AWS Shared Responsibility Model.](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/images/figure-3.png)

For DevOps, assign permissions based on the [least-privilege permissions](https://aws.amazon.com/blogs/security/how-to-define-least-privileged-permissions-for-actions-called-by-aws-services/) model. This model states that “a user (or service)**should have the exact access rights necessary to complete their role's responsibilities—no more, no less. ”.

Permissions are maintained in IAM. You can use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
