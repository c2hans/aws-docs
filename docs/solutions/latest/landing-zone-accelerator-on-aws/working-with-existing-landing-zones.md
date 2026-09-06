---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/working-with-existing-landing-zones.html
---

# Working with existing landing zones
<a name="working-with-existing-landing-zones"></a>

This solution can integrate with and manage your accounts and OUs in existing landing zone environments. Remember the following when deploying the solution to an existing environment.

## Existing accounts and OUs
<a name="existing-accounts-and-ous"></a>

Landing Zone Accelerator on AWS requires that all accounts in the organization are defined in the `accounts-config.yaml` file unless they are contained in an [ignored OU](performing-administrator-tasks.md#ignoring-an-account-from-resource-provisioning). Additionally, it requires that all OUs in the organization are defined in the `organization-config.yaml` file.

**Note**
If you’re using the solution-provisioned configuration repository, your existing environment might not match the base configuration applied to the configuration files when the solution is initially deployed. This will cause your Core pipeline to fail environment validation during the **Prepare** stage until the configuration files are updated with these details.

As of version 1.3.1 of this solution, you can provide your own configuration repository during installation of the solution to overcome this initial pipeline failure. If you pre-load the repository with your landing zone’s account and OU configuration, the solution will use it on the initial Core pipeline run. For more information, refer to the [installer stack parameters](option-2-deploy-on-new-aws-govcloud-us-accounts.md#step-1.-launch-the-stack-1.title).

For more information on adding an existing account to the solution, see [Adding an existing account](performing-administrator-tasks.md#adding-an-existing-account).

For more information on adding OUs to the solution configuration, see [Adding an organizational unit (OU)](performing-administrator-tasks.md#adding-an-organizational-unit-ou).

For information on troubleshooting environment validation errors, see [Problem: Account enrollment and environment validation failures](problem-account-enrollment-and-environment-validation-failures.md).

## Existing resources
<a name="existing-resources"></a>

Most configurable services and features in this solution don’t currently support the import and management of your existing resources in the Core pipeline. Therefore, most resources defined in the solution configuration files will deploy new resources to your environment.

**Note**
In some instances, deploying these new resources can cause conflicts with resource quotas or existing configurations in your environment. Consider this when deploying organization-wide configurations using the solution, such as centralized security services and organizational policies.

If you want to migrate from your existing resources to resources managed by the solution, do the following:

1. Identify a change window where it is acceptable for the resource(s) to be unavailable.

1. Deactivate the existing service(s) and resource(s).

1. Refer to the [Services, Features, and Configuration References section](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/user-guide/config/) of the solution’s [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/) to configure the service in the solution configuration files.

1. Release a change to the Core pipeline.

If you encounter errors related to existing resource conflicts during your solution deployment, refer to [Troubleshooting](troubleshooting.md).

## Existing service control policies (SCPs)
<a name="existing-service-control-policies-scps"></a>

Existing SCPs in your environment can cause deployment of accelerator resources to fail. If the solution encounters an explicit deny from an SCP, ensure that the [conditions block](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-condition) of your statements (if applicable) are updated to allow actions from the solution [administrative role](administrative-role.md) and roles using the **Accelerator Resource name prefix** parameter.

Alternatively, you can migrate the management of your SCPs to the solution. This provides you the added benefit of using our [policy replacement variables](working-with-solution-specific-variables.md#policy-replacement-variables) in your policy documents to reference the aforementioned role names. For more information, see [Adding a service control policy (SCP)](performing-administrator-tasks.md#adding-a-service-control-policy-scp).
