---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/service-roles-for-cloudformation.html
---

# Service roles for CloudFormation
<a name="service-roles-for-cloudformation"></a>

A *service role* is an AWS Identity and Access Management (IAM) role that allows AWS CloudFormation to create, update, or delete stack resources. If you do not provide a service role, CloudFormation uses the credentials of the IAM principal to perform the stack operations. If you create a service role for CloudFormation and specify the service role during stack creation, then CloudFormation uses the credentials of the service role to perform the operations, instead of the credentials of the IAM principal.

When using a service role, the identity-based policy attached to the IAM principal doesn't require permissions to provision all of the AWS resources defined in the CloudFormation template. If you are not ready to provision AWS resources for critical business operations through a development pipeline (an AWS recommended best practice), using a service role can add an extra layer of protection for resource management in AWS. The benefits of this approach are:
+ The IAM principals in your organization follow a least-privilege model that prevents them from manually creating or changing AWS resources in your environment.
+ To create, update, or delete AWS resources, IAM principals must use CloudFormation. This standardizes resource provisioning through infrastructure as code.

For example, to create a stack that contains an Amazon Elastic Compute Cloud (Amazon EC2) instance, the IAM principal would need to have permissions to create EC2 instances through their identity-based policy. Instead, CloudFormation can assume a service role that has permissions to create EC2 instances on the principal's behalf. With this approach, the IAM principal can create the stack, and you don't need to give the IAM principal overly broad permissions for a service that they shouldn't have regular access to.

To use a service role to create CloudFormation stacks, IAM principals must have permissions to pass the service role to CloudFormation, and the trust policy of the service role must allow CloudFormation to assume the role.

**This section contains the following topics:**
+ [Implementing least privilege for CloudFormation service roles](#least-privilege-service-roles)
+ [Configuring service roles](#configuring-service-roles)
+ [Granting an IAM principal permissions to use a CloudFormation service role](#permissions-use-cloudformation-service-role)
+ [Configuring a trust policy for the CloudFormation service role](#trust-policy-cloudformation-service-role)
+ [Associating a service role with a stack](#associate-service-role-to-stack)

## Implementing least privilege for CloudFormation service roles
<a name="least-privilege-service-roles"></a>

In a service role, you define a permissions policy that explicitly specifies which actions the service can perform. These might not be the same actions that an IAM principal can perform. We recommend that you work backward from your CloudFormation templates to create a service role that adheres to the principle of least privilege.

Properly scoping the identity-based policy of an IAM principal to pass only specific service roles and scoping a service role's trust policy to allow only specific principals to assume the role helps prevent possible privilege escalation through service roles.

## Configuring service roles
<a name="configuring-service-roles"></a>

|
|
| Note: Service roles are configured in IAM. To create a service role, you must have permissions to do so. An IAM principal with permissions to create a role and attach any policy can escalate their own permissions. AWS recommends creating one service role for each AWS service for each use case. After you create CloudFormation service roles for your use cases, you can allow users to pass only the approved service role to CloudFormation. For sample identity-based policies that allow users to create service roles, see [Service role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#id_roles_create_service-permissions) in the IAM documentation. |
| --- |

For instructions about how to create service roles, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). Specify CloudFormation (`cloudformation.amazonaws.com`) as the service that can assume the role. This prevents an IAM principal from assuming the role themselves or passing it to other services. When you configure a service role, the `Effect`, `Action`, and `Resource` elements are required. You can optionally define a `Condition` element too.

For more information about these elements, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html). For a complete list of actions, resources, and condition keys, see [Actions, resources, and condition keys for Identity And Access Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagement.html).

## Granting an IAM principal permissions to use a CloudFormation service role
<a name="permissions-use-cloudformation-service-role"></a>

To provision resources through CloudFormation by using the CloudFormation service role, the IAM principal must have permissions to pass the service role. You can limit the IAM principal's permissions to pass only certain roles by specifying the ARN of the role in the principal's permissions. For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the IAM documentation.

The following IAM identity-based policy statement allows the principal to pass roles, including service roles, that are in the `cfnroles` path. The principal cannot pass roles that are in a different path.

```
{
"Sid": "AllowPassingAppRoles",
"Effect": "Allow",
"Action": "iam:PassRole",
"Resource":"arn:aws:iam::<account ID>:role/cfnroles/*"
}
```

Another approach for limiting principals to certain roles is to use a prefix for CloudFormation service role names. The following policy statement allows IAM principals to pass only roles  that have a `CFN-` prefix.

```
{
"Sid": "AllowPassingAppRoles",
"Effect": "Allow",
"Action": "iam:PassRole",
"Resource":"arn:aws:iam::<account ID>:role/CFN-*"
}
```

In addition to the previous policy statements, you can use the `cloudformation:RoleARN` condition key to provide further fine-grained controls in the identity-based policy, for least privilege access. The following policy statement allows the IAM principal to create, update, and delete stacks only if they pass a specific CloudFormation service role. As a variation, you can define the ARNs of more than one CloudFormation service role in the condition key.

```
{
"Sid": "RestrictCloudFormationAccess",
"Effect": "Allow",
"Action": [
            "cloudformation:CreateStack",
            "cloudformation:DeleteStack",
            "cloudformation:UpdateStack"
      ],
"Resource":"arn:aws:iam::<account ID>:role/CFN-*",
"Condition": {
        "StringEquals": {
          "cloudformation:RoleArn" : [<ARN of the specific CloudFormation service role>]
        }
      }

}
```

Additionally you can also use the `cloudformation:RoleARN` condition key to restrict an IAM principal from passing a highly privileged CloudFormation service role for stack operations. The only change required is in the conditional operator, from `StringEquals` to `StringNotEquals`.

```
{
"Sid": "RestrictCloudFormationAccess",
"Effect": "Allow",
"Action": [
            "cloudformation:CreateStack",
            "cloudformation:DeleteStack",
            "cloudformation:UpdateStack"
      ],
"Resource":"arn:aws:iam::<account ID>:role/CFN-*",
"Condition": {
        "StringNotEquals": {
          "cloudformation:RoleArn" : [<ARN of a privilege CloudFormation service role>]
        }
      }

}
```

## Configuring a trust policy for the CloudFormation service role
<a name="trust-policy-cloudformation-service-role"></a>

A role *trust policy* is a required resource-based policy that is attached to an IAM role. A trust policy defines which IAM principals can assume the role. In a trust policy, you can specify users, roles, accounts, or services as principals. To prevent IAM principals from passing service roles for CloudFormation to other services, you can specify CloudFormation as the principal in role's trust policy.

The following trust policy allows only the CloudFormation service to assume the service role.

```
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Principal": {"Service": "cloudformation.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }
}
```

## Associating a service role with a stack
<a name="associate-service-role-to-stack"></a>

After a service role is created, you can associate it with a stack when you create the stack. For more information, see *Permissions* in [Setting AWS CloudFormation stack options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.html). Before you specify a service role, make sure that IAM principals have permissions to pass it. For more information, see [Granting an IAM principal permissions to use a CloudFormation service role](#permissions-use-cloudformation-service-role).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
