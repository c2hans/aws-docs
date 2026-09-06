---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/creating-a-permissions-boundary.html
---

# Creating a permissions boundary
<a name="creating-a-permissions-boundary"></a>

After you deploy the permission sets, you establish a permissions boundary. This *permissions boundary* is a mechanism to delegate IAM access to only users who are developing, testing, launching, and managing your cloud infrastructure. Those users can perform only the actions that are permitted by the policy and the permissions boundary.

You can define the permissions boundary in an AWS CloudFormation template and then use CloudFormation StackSets to deploy the template into multiple accounts. This helps you establish and maintain standardized policies across your organization with a single operation. For more information and instructions, see [Working with AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) (CloudFormation documentation).

The following CloudFormation template provisions an IAM role and creates an IAM policy that acts as a permission boundary. Using a stack set, you can deploy this template to all of the member accounts in your organization.

```
CloudFormationRole:
  Type: "AWS::IAM::Role"
  Properties:
    AssumeRolePolicyDocument:
      Version: "2012-10-17"
      Statement:
        Effect: Allow
        Principal:
          Service: !Sub "cloudformation.${AWS::URLSuffix}"
        Action: "sts:AssumeRole"
        Condition:
          StringEquals:
            "aws:SourceAccount": !Ref "AWS::AccountId"
    Description: !Sub "DO NOT DELETE - Used by CloudFormation. Created by CloudFormation ${AWS::StackId}"
    ManagedPolicyArns:
      - !Sub "arn:${AWS::Partition}:iam::aws:policy/AdministratorAccess"
    PermissionsBoundary: !Ref DeveloperBoundary
    RoleName: CloudFormationRole

DeveloperBoundary:
  Type: "AWS::IAM::ManagedPolicy"
  Properties:
    Description: Permission boundary for developers
    ManagedPolicyName: PermissionsBoundary
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Sid: AllowModifyIamRolesWithBoundary
          Effect: Allow
          Action:
            - "iam:AttachRolePolicy"
            - "iam:CreateRole"
            - "iam:DeleteRolePolicy"
            - "iam:DetachRolePolicy"
            - "iam:PutRolePermissionsBoundary"
            - "iam:PutRolePolicy"
          Resource: !Sub "arn:${AWS::Partition}:iam::${AWS::AccountId}:role/app/*"
          Condition:
            ArnEquals:
              "iam:PermissionsBoundary": !Sub "arn:${AWS::Partition}:iam::${AWS::AccountId}:policy/PermissionsBoundary"
        - Sid: AllowModifyIamRoles
          Effect: Allow
          Action:
            - "iam:DeleteRole"
            - "iam:TagRole"
            - "iam:UntagRole"
            - "iam:UpdateAssumeRolePolicy"
            - "iam:UpdateRole"
            - "iam:UpdateRoleDescription"
          Resource: !Sub "arn:${AWS::Partition}:iam::${AWS::AccountId}:role/app/*"
        - Sid: OverlyPermissiveAllowedServices
          Effect: Allow
          Action:
            - "lambda:*"
            - "apigateway:*"
            - "events:*"
            - "s3:*"
            - "logs:*"
          Resource: "*"
```

The **CloudFormationRole** role, **PermissionsBoundary** policy, and the **DeveloperAccess** permission set work together to grant the following permissions:
+ Users have read-only access to most AWS services, through the **ReadOnlyAccess** AWS managed policy.
+ Users have access to open support cases, through the **AWSSupportAccess** AWS managed policy.
+ Users have read-only access to the AWS Billing console dashboard, through the **AWSBillingReadOnlyAccess** AWS managed policy.
+ Users are able to provision products from AWS Service Catalog, through the **AWSServiceCatalogEndUserFullAccess** AWS managed policy.
+ Users are able to validate and estimate the cost of any CloudFormation template, through the inline policy.
+ By using the **CloudFormationRole** IAM role, users are able to create, update, or delete any CloudFormation stack that starts with **app/**.
+ Users are able to use CloudFormation to create, update, or delete IAM roles that start with **app/**. The **PermissionsBoundary** IAM policy prevents users from escalating their privileges.
+ Users can provision AWS Lambda, Amazon EventBridge, Amazon CloudWatch, Amazon Simple Storage Service (Amazon S3), and Amazon API Gateway resources only by using CloudFormation.

The following image shows how an authorized user, such as a developer, can create a new IAM role in a member account by using the permissions sets, IAM roles, and permissions boundaries described in this guide:

1. The user authenticates in IAM Identity Center and assumes the **DeveloperAccess** IAM role.

1. The user initiates the `cloudformation:CreateStack` action and assumes the **CloudFormationRole** IAM role.

1. The user initiates the `iam:CreateRole` action and uses CloudFormation to create a new IAM role.

1. The **PermissionsBoundary** IAM policy is applied to the new IAM role.

![User creating an IAM role that is subject to the permissions boundary in the member account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/images/guide-img/b35f7443-fbaf-4ce8-bb48-32b6441d573f/images/76bc8b9a-7847-465b-92f4-9427011a76fb.png)

The **CloudFormationRole** role has the [AdministratorAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) managed policy attached, but due to the **PermissionsBoundary** IAM policy, the **CloudFormationRole** role's effective permissions become equal to the **PermissionsBoundary** policy. The **PermissionsBoundary** policy references itself when allowing the `iam:CreateRole` action, which ensures that roles can be created only if the permissions boundary is applied.
