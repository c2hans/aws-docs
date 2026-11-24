---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/simplified-tip-enabling.html
---

# Enable the simplified experience

As of November 23, 2026, you can turn on the simplified experience for trusted identity propagation from the IAM Identity Center console. Your instance stays in the legacy experience until you turn it on.

## Turn on the simplified experience
<a name="simplified-tip-how-to-enable"></a>

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. In the navigation pane, choose **Settings**. On the **Identity source** tab, scroll to the **Simplified trusted identity propagation** section.

1. Choose **Enable**.

1. In the **Enable Simplified trusted identity propagation?** dialog box, review the note that the signed-in user's username will be added to the `subject` field of the `onBehalfOf` element in AWS CloudTrail. Then choose **Enable**.

1. Confirm that the section now shows **Status: Enabled** and **Propagated subject: Username**.

The setting is visible to administrators of the IAM Identity Center instance (management account). The setting applies to your entire IAM Identity Center instance; you cannot turn on the simplified experience for individual services separately.

We recommend that you enable the simplified experience on a non-production instance first. If you manage a large or shared instance, coordinate across teams before you turn it on in production. This is especially important for any team that might have configured OAuth scopes on applications. After you turn it on, the simplified experience no longer enforces OAuth scopes for SigV4 requests. An IAM role can then reach any resource that its own policies allow. To keep access limited as intended, move each restriction from the application onto the policy of the IAM role used with that application. For sample policies, see [Move authorized target scope restrictions to IAM policies](simplified-tip-prerequisites.md#simplified-tip-prereq-authorized-targets).

**Note**
AWS services that support the legacy experience of trusted identity propagation but haven't yet adopted the simplified experience also stop checking OAuth scopes. They keep their other configuration requirements, including per-service application registration and user and group assignments, until they adopt the simplified experience.

## Switching between the legacy experience and the simplified experience
<a name="simplified-tip-switching"></a>

You can switch between the legacy experience and the simplified experience using the same setting. You can use this to validate that your IAM policies and service native controls are sufficient. You can also test identity propagation across all three access paths: web applications, IAM roles created from permission sets, and IAM roles assigned with IAM account access manager. Make sure that your workflows operate as expected.

## Returning to the legacy experience
<a name="simplified-tip-returning-to-legacy"></a>

You can switch back by choosing **Return to legacy mode** in the same settings section. The simpler setup and the username identifier changes in CloudTrail no longer apply. In the legacy experience, IAM roles used for trusted identity propagation again require the `sts:SetContext` permission in their trust policies.

**Important**
Before you switch back, remove or relax any policy that requires the IAM Identity Center context keys, such as a deny unless `aws:OriginIdentity/Subject` matches. In the legacy experience, sessions no longer carry those keys, so those policies would deny every request.
Also add the `sts:SetContext` permission to the trust policy of any IAM role used for trusted identity propagation that you created or updated without it while the simplified experience was on.

When you return to the legacy experience:
+ **The change affects new sign-in sessions only.** Sessions vended while the simplified experience was enabled, and existing user sign-ins that are already using the simplified experience, continue to use it until they end. Legacy behavior applies only to fresh sign-in sessions created after you switch back.
+ Those new sessions enforce OAuth scopes again.
+ IAM Identity Center keeps the application registrations, user and group assignments, and OAuth scopes that you configured before you turned on the simplified experience. They apply again when you switch back.
+ You lose access to capabilities available only through the simplified experience (identity propagation for IAM roles created from permission sets, and newer service features that only support the simplified experience) until you turn it on again.

For the AWS managed applications that support the legacy experience of trusted identity propagation, see the trusted identity propagation column in [AWS managed applications that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md).

## Trusted identity propagation with an IAM identity provider
<a name="tip-iam-federation"></a>

If you use trusted identity propagation with an IAM SAML or OIDC identity provider, and you connected an IAM Identity Center instance for group-based access, users don't have IAM Identity Center credentials by default, so they can't sign in to the AWS access portal. Users continue to sign in through your IAM identity provider. For more information, see [Configure group-based access for TIP](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_tip_federation_configure_group_access.html) in the *IAM User Guide*.

When you're ready, you can enable user sign-in through IAM Identity Center. Users, groups, and their identifiers in the connected Identity Store stay the same, so access that you granted to them continues to work. For more information, see [Manage your identity source](manage-your-identity-source.md).

**Important**
Some actions in IAM Identity Center let users sign in to the AWS access portal with an IAM Identity Center credential. If you want your users to sign in only through your IAM identity provider, make sure that this access is intended before you do any of the following:
Add a user in the IAM Identity Center console. The console sets up an IAM Identity Center password for the user whether you choose to send the user an email with password setup instructions or to generate a one-time password that you share with the user. See [Add users to your Identity Center directory](addusers.md).
Reset a user's password. See [Reset the IAM Identity Center user password for an end user](reset-password-for-user.md).
Configure standard authentication and turn on **Send email OTP** for users without a password. All users in the directory can then sign in with an IAM Identity Center credential. See [Email one-time password to users created with API or CLI](userswithoutpwd.md).
The IAM Identity Center console shows a warning before you complete these actions. The same operations performed through the API don't show a warning.
