---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/quick-suite-users.html
---

# Creating local users in Quick
<a name="quick-suite-users"></a>

![Architecture diagram of user access through a locally configured Quick Suite user.](https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/images/guide-img/ec03a023-a3ad-4a10-93bb-22dcf4ea49a5/images/396ab044-41c5-4689-b645-3cb60a1421f3.png)

The following are the characteristics of this architecture and access approach:
+ This user has access to Amazon Quick only and cannot access other services and resources in your AWS account.
+ The user's password is managed locally in Quick.
+ You provision access by inviting the user through their email address.
+ The user must log in directly through the [Quick console](https://aws.amazon.com/).

## Considerations and use cases
<a name="qu-considerations"></a>

This is the most direct way to provision access to Quick because it creates a local user record inside the Quick user store and doesn't have any external dependencies. This user record exists only in Quick and has a password that is also managed in Quick.

This type of approach is also probably the most flexible because the only prerequisite is having an email address for the user. You don't have to create and manage users in another service or directory, and it can be a quick way to provision access for third-party vendors or partners who need to access your Quick dashboards. This access approach is best suited for users who require access to Quick only and don't require access to other services and resources in the AWS account.

Because these are local users in Quick, IT operations teams need to establish dedicated processes for managing access requests, provisioning access, and periodically reviewing and auditing access. For example, they cannot use existing access review processes for corporate identities because the user record is independent of other identity management systems.

## Prerequisites
<a name="qu-prereqs"></a>
+ Administrative permissions in Quick or permissions to create Quick users (see [IAM identity-based policies for Amazon Quick: creating users](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-policy-examples.html#security_iam_id-based-policy-examples-create-users))
+ Email address for the user

## Configuring access for a Quick local user
<a name="qu-configuration"></a>

For instructions on how to configure a local user, see [Inviting users to access Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/managing-user-access-qs-iam.html#inviting-users). Note the following when configuring this type of user access:
+ Although you can define any username and email address, we recommend that you use values that are consistent with your organization's employee directory. This improves accountability and consistency.
+ For **IAM user**, choose **No**.
+ The user has seven days to accept the invitation. If they don't accept within this time period, you can resend the invitation email.
+ When the user accepts the invitation, they are prompted to set and confirm their password.
