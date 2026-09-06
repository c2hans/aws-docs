---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/security_iam_troubleshoot.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Troubleshooting identity and access issues for AWS IoT Greengrass
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS IoT Greengrass and IAM.

**Topics**
+ [I'm not authorized to perform an action in AWS IoT Greengrass](#security_iam_troubleshoot-no-permissions)
+ [Error: Greengrass is not authorized to assume the Service Role associated with this account, or the error: Failed: TES service role is not associated with this account.](#troubleshoot-assume-service-role)
+ [Error: Permission denied when attempting to use role arn:aws:iam::<account-id>:role/<role-name> to access s3 url https://<region>-greengrass-updates.s3.<region>.amazonaws.com/core/<architecture>/greengrass-core-<distribution-version>.tar.gz.](#troubleshoot-ota-region-access)
+ [Device shadow does not sync with the cloud.](#troubleshoot-shadow-sync)
+ [I'm not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)
+ [I'm an administrator and want to allow others to access AWS IoT Greengrass](#security_iam_troubleshoot-admin-delegate)
+ [I want to allow people outside of my AWS account to access my AWS IoT Greengrass resources](#security_iam_troubleshoot-cross-account-access)

For general troubleshooting help, see [Troubleshooting AWS IoT Greengrass](gg-troubleshooting.md).

## I'm not authorized to perform an action in AWS IoT Greengrass
<a name="security_iam_troubleshoot-no-permissions"></a>

If you receive an error that states you're not authorized to perform an action, you must contact your administrator for assistance. Your administrator is the person who provided you with your user name and password.

The following example error occurs when the `mateojackson` IAM user tries to view details about a core definition version, but does not have `greengrass:GetCoreDefinitionVersion` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: greengrass:GetCoreDefinitionVersion on resource: resource: arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/78cd17f3-bc68-ee18-47bd-5bda5EXAMPLE/versions/368e9ffa-4939-6c75-859c-0bd4cEXAMPLE
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/cores/78cd17f3-bc68-ee18-47bd-5bda5EXAMPLE/versions/368e9ffa-4939-6c75-859c-0bd4cEXAMPLE` resource using the `greengrass:GetCoreDefinitionVersion` action.

## Error: Greengrass is not authorized to assume the Service Role associated with this account, or the error: Failed: TES service role is not associated with this account.
<a name="troubleshoot-assume-service-role"></a>

**Solution:** You might see this error when the deployment fails. Check that a Greengrass service role is associated with your AWS account in the current AWS Region. For more information, see [Managing the Greengrass service role (CLI)](service-role.md#manage-service-role-cli) or [Managing the Greengrass service role (console)](service-role.md#manage-service-role-console).

## Error: Permission denied when attempting to use role arn:aws:iam::<account-id>:role/<role-name> to access s3 url https://<region>-greengrass-updates.s3.<region>.amazonaws.com/core/<architecture>/greengrass-core-<distribution-version>.tar.gz.
<a name="troubleshoot-ota-region-access"></a>

**Solution:** You might see this error when an over-the-air (OTA) update fails. In the signer role policy, add the target AWS Region as a `Resource`. This signer role is used to presign the S3 URL for the AWS IoT Greengrass software update. For more information, see [S3 URL signer role](core-ota-update.md#s3-url-signer-role).

## Device shadow does not sync with the cloud.
<a name="troubleshoot-shadow-sync"></a>

**Solution:** Make sure that AWS IoT Greengrass has permissions for `iot:UpdateThingShadow` and `iot:GetThingShadow` actions in the [Greengrass service role](service-role.md). If the service role uses the `AWSGreengrassResourceAccessRolePolicy` managed policy, these permissions are included by default.

See [Troubleshooting shadow synchronization timeout issues](gg-troubleshooting.md#troubleshooting-shadow-sync).

The following are general IAM issues that you might encounter when working with AWS IoT Greengrass.

## I'm not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to AWS IoT Greengrass.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in AWS IoT Greengrass. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I'm an administrator and want to allow others to access AWS IoT Greengrass
<a name="security_iam_troubleshoot-admin-delegate"></a>

To allow others to access AWS IoT Greengrass, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in the *AWS IAM Identity Center User Guide*.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach a policy to the entity that grants them the correct permissions in AWS IoT Greengrass. After the permissions are granted, provide the credentials to the user or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions, see [IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) and [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

## I want to allow people outside of my AWS account to access my AWS IoT Greengrass resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create an IAM role that users in other accounts or people outside of your organization can use to access your AWS resources. You can specify the who is trusted to assume the role. For more information, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) and [Providing access to Amazon Web Services accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.

AWS IoT Greengrass doesn't support cross-account access based on resource-based policies or access control lists (ACLs).
