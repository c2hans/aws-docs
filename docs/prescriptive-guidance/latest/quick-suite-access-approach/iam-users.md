---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/iam-users.html
---

# Granting Quick access to IAM users
<a name="iam-users"></a>

**Note**
An *IAM user* is an entity that you create in AWS Identity and Access Management (IAM). This type of entity accesses your AWS account by using long-term credentials. As a best practice, AWS recommends that you grant access through temporary credentials by using identity federation and IAM roles. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

![Architecture diagram of an IAM user accessing Quick Suite.](http://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/images/guide-img/ec03a023-a3ad-4a10-93bb-22dcf4ea49a5/images/01bb1fdf-7a7f-42fb-a01a-90fc27c3f67e.png)

The following are the characteristics of this architecture and access approach:
+ The Amazon Quick user record is linked to the user in IAM.
+ User passwords are managed in IAM.
+ You can invite IAM users directly or create an IAM identity-based policy that permits users to self-provision access.
+ This type of user can log in through the Quick console or through the AWS Management Console.

## Considerations and use cases
<a name="iam-considerations"></a>

Although AWS generally doesn't recommend configuring access through IAM users, other access approaches, such as federation, might not be currently available in your organization. Many organizations that are just starting their cloud journey have not yet established IAM roles and are working in a single-account architecture. If your organization uses IAM users to access your AWS environment, then reapplying that approach to Quick might be the most straightforward and sensible approach until your organization supports other approaches.

## Prerequisites
<a name="iam-prereqs"></a>
+ For the direct invitation approach, you need:
  + Administrative permissions in Quick (see IAM identity-based policies for the [Standard](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-policy-examples.html#security_iam_id-based-policy-examples-all-access-standard-edition) or [Enterprise](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-policy-examples.html#security_iam_id-based-policy-examples-all-access-enterprise-edition) editions)
  + The email address of the IAM user
+ For the self-provisioned access approach, the user needs permissions to create Amazon Quick (see [IAM identity-based policies for Amazon Quick: creating users](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-policy-examples.html#security_iam_id-based-policy-examples-create-users))
+ The IAM user must have a password associated with their IAM credentials

## Configuring access for an IAM user
<a name="iam-configuration"></a>

You can grant access to Quick for IAM users by using either of the following options:
+ **Direct invitation** – You invite the IAM user to access Quick, and the user can accept the invitation through their email.
+ **Self-provisioned access** – You create an IAM policy that permits users to provision their own access. When a user accesses Quick for the first time, they are granted access and define the email address that will be associated with their Quick user record.

The result of both options is the same: the IAM user can access Quick. However, there are advantages and disadvantages to each, as shown in the following table. For example, the direct invitation might be preferable for organizations that want to enforce use of approved corporate email addresses.

|
|
| Approach | Advantages | Disadvantages |
| --- |--- |--- |
| Direct invitation | + Administrators can control which email address is associated with the user record in Quick<br />+ No IAM policy management tasks | + More manual |
| Self-provisioned access | + Can be integrated into existing IT operations processes for provisioning access through IAM policies, where the self-provisioning capability is already part of existing IAM policies | + Administrators can't control which email address the user provides to Quick |

### Direct invitation
<a name="direct-invitation.d62dfb5a-f4f4-5308-bb54-b513dba4f2b6"></a>

For instructions on how to configure access for an IAM user, see [Inviting users to access Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/managing-user-access-qs-iam.html#inviting-users). Note the following when configuring this type of user access:
+ For the Quick username, enter the username of the IAM user. Allowed characters are letters, numbers, and the following characters: . \_ - (hyphen).
+ For **IAM user**, choose **Yes**.
+ The user has seven days to accept the invitation. If they don't accept within this time period, you can resend the invitation email.
+ When the user accepts the invitation, they must enter the password that is associated with their IAM credentials.

### Self-provisioned access
<a name="self-provisioned-access.4a8b9002-354a-5344-821b-0b7c09af5a61"></a>

When IAM users can self-provision access, they don't need to be invited to the Quick account. The first time they try to access the Quick console, they must enter an email address. When the user chooses **Continue**, Quick creates a user record for that IAM user.

To grant permission to provision their own access, you create an identity-based policy and apply that policy to the IAM users or IAM user group. For more information, see [Configuring IAM policies](configuring-iam-policies.md) in this guide.
