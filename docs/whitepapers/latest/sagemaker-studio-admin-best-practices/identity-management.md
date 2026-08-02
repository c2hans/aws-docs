---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/identity-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Identity management
<a name="identity-management"></a>

 This section discusses how workforce users in a corporate directory federate into AWS accounts and access SageMaker AI Studio. First, we will briefly describe how users, groups, and roles are mapped, and how user federation works.

## Users, groups, and role
<a name="users-groups-and-role"></a>

 In AWS, resource permissions are managed using users, groups, and roles. Customers can manage their users and groups either through IAM, or in a corporate directory such as Active Directory (AD), enabled through an external IdP such as Okta, that allows them to authenticate the users to various applications running in the cloud and on-premises.

 As discussed in the AWS Security Pillar [Identity Management section](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-management.html), it is a best practice to manage your user identities in a central IdP, because this helps to easily integrate with your back-end HR processes, and helps to manage access to your workforce users.

 IdPs such as Okta allow end users to authenticate to one or more AWS accounts and gain access to specific roles using SSO with security assertation markup language (SAML). IdP admins have the ability to download roles from AWS accounts into IdP, and assign those to users. When logging in to AWS, end users are presented with an AWS screen that displays a list AWS roles assigned to them in one or more AWS accounts. They can select the role to assume for login, which defines their permissions for the duration of that authenticated session.

 A group must exist in IdP for each specific account and role combination that you want to provide access to. You can think of these groups as *AWS role-specific groups*. Any user who is a member of these role specific groups is granted a single entitlement: access to one specific role in one specific AWS account. However, this single entitlement process does not scale to manage user access by assigning each user to specific AWS role groups. To simplify administration, we recommend you also create a number of groups for all of the distinct user-sets in your organization that require different sets of AWS entitlements.

 To illustrate the central IdP setup, consider an enterprise with AD setup, where users and groups are synchronized to the IdP directory. In AWS, these AD groups are mapped to IAM roles. The major steps of the workflow follow:

![A diagram that depicts a workflow for onboarding AD users, AD groups and IAM roles.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/onboarding-workflow.png)

1.  In AWS, Setup SAML integration for each of your AWS accounts with your IdP.

1.  In AWS, set up roles in each AWS account and sync to IdP.

1.  In the corporate AD system:

   1.  Create an AD Group for each account role and sync to IdP (for example, `Account1-Platform-Admin-Group` (aka AWS Role Group)).

   1.  Create a management group at each persona level (for example, `Platform-Mgmt-Group`) and assign AWS role groups as members.

   1.  Assign users to that management group to allow access to AWS account roles.

1.  In IdP, map AWS role groups (such as `Account1-Platform-Admin-Group`) to AWS account roles (such as Platform Admin in Account1).

1.  When Data Scientist Alice logs in to Idp, they are presented with an AWS Federation App UI with two options to choose from: ‘Account 1 Data Scientist’ and ‘Account 2 Data Scientist’.

1.  Alice chooses the ‘Account 1 Data Scientist’ option, and they are connected to their authorized application in AWS Account 1 (SageMaker AI Console).

 For detailed instructions on setting up SAML account federation refer Okta’s [How to Configure SAML 2.0 for AWS Account Federation](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Amazon-Web-Service).

## User federation
<a name="user-federation"></a>

Authentication for SageMaker AI Studio can either be done using IAM or IAM IdC. If the users are managed through IAM, they can choose the IAM mode. If the enterprise uses an external IdP, they can either federate through IAM or IAM IdC. Note that the authentication mode cannot be updated for an existing SageMaker AI Studio domain, so it is critical to make the decision before creating a production SageMaker AI Studio domain.

If SageMaker AI Studio is set up in IAM mode, SageMaker AI Studio users access the app through a pre-signed URL that automatically signs a user in to the SageMaker AI Studio app when accessed through a browser.

### IAM users
<a name="iam-users"></a>

 For IAM users, the administrator creates SageMaker AI Studio user profiles for each user, and associates the user profile with an IAM role that allows the necessary actions that the user needs to perform from within Studio. To restrict an AWS user from accessing only their SageMaker AI Studio user profile, the administrator should tag the SageMaker AI Studio user profile and attach an IAM policy to the user that allows them to access only if the tag value is the same as the AWS user name. The policy statement looks like this:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AmazonSageMakerPresignedUrlPolicy",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePresignedDomainUrl"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sagemaker:ResourceTag/studiouserid": "${aws:username}"
                }
            }
        }
    ]
}
```

------

### AWS IAM or account federation
<a name="aws-iam-or-account-federation"></a>

 The AWS account federation method enables customers to federate into the SageMaker AI Console from their SAML IdP, such as Okta. To restrict users from accessing only their user profile, the administrator should tag the SageMaker AI Studio user profile, add `PrincipalTags` on the IdP, and set them as transitive tags. The following diagram depicts how the federated user (Data Scientist Alice) is authorized to access their own SageMaker AI Studio user profile.

![A diagram depicting AWS IAM account federation for accessing SageMaker AI Studio .](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/account-federation.png)

1.  The Alice SageMaker AI Studio user profile is tagged with their user ID, and associated to execution role.

1.  Alice authenticates to IdP (Okta).

1.  IdP authenticates Alice and posts a SAML assertion with the two roles (Data Scientist for accounts 1 and 2) Alice is member of. Alice selects the Data Scientist role for account 1.

1.  Alice is logged in to Account 1 SageMaker AI Console, with the assumed role of Data Scientist. Alice opens their Studio app instance from the list of studio app instances.

1.  The Alice principal tag in the assumed role session is validated against the selected SageMaker AI Studio app instance user profile tag. If the profile tag is valid, the SageMaker AI Studio app instance is launched, assuming the execution role.

 If you want to automate the creation of SageMaker AI Execution roles and policies as part of user onboarding, the following is one way to accomplish this:

1.  Set up an AD group such as `SageMaker AI-Account1-Group` at each account and Studio Domain level.

1.  Add SageMaker AI-Account1-Group to the user’s group membership when you need to onboard a user to SageMaker AI Studio.

Set up an automation process that listens to the `SageMaker AI-Account1-Group` membership event, and use AWS APIs to create the role, policies, tags, and SageMaker AI Studio user profile based on their AD group memberships. Attach the role to the user profile. For a sample policy, refer to [Prevent SageMaker AI Studio users from accessing other user profiles](permissions-management.md#prevent-sagemaker-studio-users-from-accessing-other-user-profiles).

### SAML authentication using AWS Lambda
<a name="saml-authentication-using-aws-lambda"></a>

 In IAM mode, users can also be authenticated into SageMaker AI Studio using SAML assertions. In this architecture, the customer has an existing IdP, where they can create a SAML application for the users to access Studio (instead of AWS Identity Federation application). The customer’s IdP is added to IAM. An AWS Lambda function helps validate the SAML assertion using IAM and STS, and then invokes an API gateway or a Lambda function directly, to create the pre-signed domain URL.

 The advantage of this solution is that the Lambda function can customize logic for access to SageMaker AI Studio. For example:
+  Automatically create a user profile if one does not exist.
+  Attach or remove roles or policy documents to the SageMaker AI Studio [execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) by parsing the SAML attributes.
+  Customize the user profile by adding Life Cycle Configuration (LCC) and adding tags.

 In summary, this solution will expose SageMaker AI Studio as a SAML2.0 application with custom logic for authentication and authorization. Refer the appendix section *[SageMaker Studio access using SAML assertion](appendix.md#sagemaker-studio-access-using-saml)* for implementation details.

![A diagram that depicts accessing SageMaker AI Studio using a custom SAML application.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/access-studio-using-saml.png)

## AWS IAM IdC federation
<a name="aws-iam-idc-federation"></a>

IdC federation method enables customers to federate directly into SageMaker AI Studio application from their SAML IdP (such as Okta). The following diagram depicts how the federated user is authorized to access their own SageMaker AI Studio instance.

![A diagram that depicts accessing SageMaker AI Studio in IAM IdC mode.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/access-studio-with-sso.png)

1. In the corporate AD, the user is a member of AD groups such as the Platform Admin group and the Data Scientist group.

1. The AD user and AD groups from Identity Provider (IdP) are synced to AWS IAM Identity Center and available as single sign-on users and groups for assignments respectively.

1. The IdP posts a SAML assertion to the AWS IdC SAML endpoint.

1. In the SageMaker AI Studio, the IdC user is assigned to the SageMaker Studio application. This assignment can be done using IdC Group and SageMaker AI Studio will apply at each IdC user level. When this assignment is created, SageMaker AI Studio creates IdC user profile and attaches the domain execution role.

1. The user accesses the SageMaker AI Studio Application using the secure presigned URL hosted as a cloud application from the IdC. SageMaker AI Studio assumes the execution role attached to their IdC user profile.

### Domain authentication guidance
<a name="domain-authentication-guidance"></a>

Here are a few considerations when choosing a domain's authentication mode:

1. If you want your users to not access the AWS Management Console and view the SageMaker AI Studio UI directly, use single sign-on mode with AWS IAM IdC.

1. If you want your users to not access the AWS Management Console and view the SageMaker AI Studio UI directly in IAM mode, you can do that by using a Lambda function in the backend to generate a presigned URL for the user profile and redirecting them to the SageMaker AI Studio UI.

1. In IdC mode, each user is mapped to a single user profile.

1. All user profiles are automatically assigned the default execution role in IdC mode. If you would like your users to be assigned different execution roles, you will need to update the user profiles using the [UpdateUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateUserProfile.html) API.

1. If you would like to restrict SageMaker AI Studio UI access in IAM mode (using the generated presigned URL) to a VPC endpoint, without traversing the internet, you can use a custom DNS resolver. Refer to the [Secure Amazon SageMaker AI Studio presigned URLs Part 1: Foundational infrastructure](https://aws.amazon.com/blogs/machine-learning/secure-amazon-sagemaker-studio-presigned-urls-part-1-foundational-infrastructure/) blog post.
