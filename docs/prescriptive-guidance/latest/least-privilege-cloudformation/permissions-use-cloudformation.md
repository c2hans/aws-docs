---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/permissions-use-cloudformation.html
---

# Configuring least-privilege permissions to use CloudFormation
<a name="permissions-use-cloudformation"></a>

This chapter reviews the options for configuring permissions to access and use the AWS CloudFormation service.

When a user or a service provisions AWS resources through CloudFormation, the first step is to make a call to the CloudFormation service through an AWS Identity and Access Management (IAM) principal. This IAM principal must have permissions to create  the CloudFormation stacks. Next, the IAM principal uses one of the following approaches to provision resources through CloudFormation:
+ If the IAM principal doesn't pass the stack operations to a CloudFormation [service role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html), CloudFormation uses the credentials of the IAM principal to perform the stack operations. This is the default. Therefore, in addition to permissions to perform the CloudFormation stack operations, the IAM principal also needs permissions to provision the resources defined in the CloudFormation templates they'll be using. For example, if the IAM principal doesn't have permissions to create Amazon Elastic Compute Cloud (Amazon EC2) instances, then they can't create a CloudFormation stack that would provision an Amazon EC2 instance.
+ If the IAM principal passes the stack operations to a CloudFormation service role, then CloudFormation uses the service role to perform the stack operations and provision the resources in the CloudFormation template. This CloudFormation service role should be defined with permissions to provision the AWS services on behalf of the IAM principal. This approach avoids giving direct permissions to the IAM principal to provision the AWS resources defined in the CloudFormation templates. The IAM principal needs CloudFormation stack creation permissions, and CloudFormation uses the service role's policy to make calls instead of the IAM principal's policy.

By using the service role approach and the principle of least privilege, you can standardize resource provisioning in your AWS environment and require that users provision resources as IaC through CloudFormation. Because the policies attached to IAM principals don't contain permissions to provision AWS resources directly, users must use CloudFormation to provision them.

This chapter reviews the following mechanisms for configuring and managing access to the CloudFormation service and to CloudFormation stacks:
+ [Identity-based policies for CloudFormation](identity-based-policies-for-cloudformation.md) – Use this type of policy to configure which IAM principals can access CloudFormation and which actions they can perform in CloudFormation.
+ [Service roles for CloudFormation](service-roles-for-cloudformation.md) – Create a service role that allows CloudFormation to create, update, or delete stack resources on behalf of the IAM principal who deploys the stack. The service role is created in IAM and can be associated with one or more stacks.
+ [CloudFormation stack policies](cloudformation-stack-policies.md) – Use this type of policy to determine when a stack can be updated. This type of policy can help prevent stack resources from being unintentionally updated or deleted. Stack policies are created and associated to stacks in CloudFormation.
