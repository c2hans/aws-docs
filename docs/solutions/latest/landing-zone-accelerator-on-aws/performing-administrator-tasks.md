---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/performing-administrator-tasks.html
---

# Performing administrator tasks
<a name="performing-administrator-tasks"></a>

This solution allows you to automate operational tasks associated with managing a multi-account environment. This section includes common instructions and examples for managing your organizational units, accounts, core networking, and security guardrails.

**Note**
The following samples aren’t an exhaustive list of what you can define in the solution configuration files. For a full configuration reference, refer to the [Services, Features, and Configuration References section](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/user-guide/config/) of the solution’s [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/).

## Adding an Organizational Unit (OU)
<a name="adding-an-organizational-unit-ou"></a>

The Landing Zone Accelerator supports the registration of AWS Organizations organizational units with the AWS Control Tower using AWS Control Tower Baseline API.

To add news OUs, complete the following steps to add the OU to the solution configuration:

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Select the **organization-config.yaml** file.

1. Choose **Edit**.

1. In the `organizationalUnits` configuration block, append additional itemized OU name(s) and path(s). For example, to add `Testing` and `Production` OUs, your configuration would look like the following sample:

   ```
   enable: true
   organizationalUnits:
     - name: Security
     - name: Infrastructure
     - name: Testing
     - name: Production
   serviceControlPolicies: []
   ```

**Note**
Landing Zone Accelerator on AWS uses the AWS Organizations API to create your Ous, and AWS Control Tower Baseline API to register your Ous with the AWS Control Tower.

## Adding a new account
<a name="adding-a-new-account"></a>

To add an account using this solution, update the `accounts-config.yaml` file with new account definitions. Account names and emails for each account must be unique. You can add new accounts to the solution configuration using the following steps.

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Select the **accounts-config.yaml** file.

1. Choose **Edit**.

1. In the `workloadAccounts` configuration block, append additional account definition(s). For example, to add `SharedServices` and `Network` accounts to the `Infrastructure` OU and the `Testing-Workload` account to the `Testing` OU, your configuration would look like the following sample:

   ```
   workloadAccounts:
     - name: SharedServices
       description: The SharedServices account
       email: <shared-services>@example.com  <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Infrastructure
     - name: Network
       description: The Network account
       email: <network>@example.com  <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Infrastructure
     - name: Testing-Workload
       description: The Workload account
       email: <workload>@example.com  <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Testing
   ```
**Note**
 **Note:** For account creation steps specific to the AWS GovCloud (US) Regions, refer to [Deploy to AWS GovCloud (US) Regions](united-states-us-federal-and-department-of-defense-dod.md).

## Adding an existing account
<a name="adding-an-existing-account"></a>

If your existing account has already been registered with AWS Organizations and AWS Control Tower, you can follow the steps listed in [Adding a new account](#adding-a-new-account) to add the account to the solution configuration.

If the account has not yet been invited to your organization, follow the steps in [Inviting an account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.

For AWS Control Tower-based installations, refer to [Prerequisites for enrollment](https://docs.aws.amazon.com/controltower/latest/userguide/enrollment-prerequisites.html) in the *AWS Control Tower User Guide\*0\** The Landing Zone Accelerator on AWS solution can enroll the account in AWS Control Tower for you after you have completed these prerequisites.

## Moving an account between OUs
<a name="moving-an-account-between-ous"></a>

If you need to move one of your accounts between OUs, complete the following steps.

**Important**
If the solution previously deployed resources to this account, identify resources in your configuration files that use the ` [deploymentTargets](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.DeploymentTargets.html) ` property. You can use this property to deploy resources to all accounts contained within an OU. The solution might add or remove resources from the account depending on the targeted OU(s) in this configuration property. For example, if you target only the **Testing** OU and move the account to the **Workloads** OU, the solution removes resources using that target from the account during the next Core pipeline run.

### For AWS Organizations-only deployments
<a name="for-aws-organizations-only-deployments"></a>

For versions 1.3.0 and later of the solution, follow the [Update procedure](#update-procedure) to update the `accounts-config.yaml` file with the new `organizationalUnit` property value. When you release the pipeline, the solution will move the account to the specified OU.

For versions prior to 1.3.0, first move the account from the AWS Organizations console. See [Moving accounts to an OU](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html#move_account_to_ou) in the *AWS Organizations User Guide* for additional details. Then follow the [Update procedure](#update-procedure) instructions.

### For AWS Control Tower deployments
<a name="for-aws-control-tower-deployments"></a>

**Note**
There might be implications of moving an Account Factory account prior to completing the following procedure. See [Update and move accounts](https://docs.aws.amazon.com/controltower/latest/userguide/updating-account-factory-accounts.html) in the *AWS Control Tower User Guide* for more information.
This section is intended for accounts actively managed by [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html). If moving an unmanaged or suspended account, refer to [Moving accounts to an OU](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html#move_account_to_ou) in the *AWS Organizations User Guide*.

1. Sign in to the [AWS Control Tower console](https://us-east-1.console.aws.amazon.com/controltower/home/dashboard) from your management account.

1. From the navigation menu, select **Organization**.

1. Select **\\\+** to expand the OU your account currently belongs to. Choose the account you want to move.

1. Select **Actions**, then select **Update**.

1. From the **Account detail** page, in **Organizational unit**, select the OU.

1. Choose **Update account**.

1. A confirmation box displays. Confirm the details, then select **Update account**.

   It takes approximately 5-10 minutes to process this update.

1. Proceed with the [Update procedure](#update-procedure).

### Update procedure
<a name="update-procedure"></a>

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Select the **accounts-config.yaml** file.

1. Choose **Edit**.

1. In the `workloadAccounts` configuration block, change the `organizationalUnit` property to the name of the new OU. In this example, we have replaced the previous OU value of **Testing** with a new value of **Workloads**:

   ```
   workloadAccounts:
     - name: Testing-Workload
       description: The Workload account
       email: <workload>@example.com  <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Workloads
   ```

## Ignoring an account from resource provisioning
<a name="ignoring-an-account-from-resource-provisioning"></a>

As of v1.3.0 of the solution, you can designate an ignored OU in the `organization-config.yaml` file. If you would like the solution to ignore an account so that no resources are deployed to it, perform the following steps.

1.  [Create](#adding-an-organizational-unit-ou) or identify an existing OU that you’d like to use to contain ignored accounts. For this example, our OU is named `Suspended`.

1.  [Move your account(s)](#moving-an-account-between-ous) that you’d like to ignore to this OU. Do this manually and not using the solution so that resources are not provisioned in the account. **Do not** follow the additional steps to update the `accounts-config.yaml` file or release changes to the Core pipeline if following the steps from the previous section.

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Select the **organization-config.yaml** file.

1. Choose **Edit**.

1. In the `organizationalUnits` configuration block, append or edit the OU you’ve selected with the `ignore: true` flag:

   ```
   organizationalUnits:
     - name: Security
     - name: Infrastructure
     - name: Testing
     - name: Production
     - name: Suspended
       ignore: true
   ```

1. Commit these changes, and then select the `accounts-config.yaml` file.

1. Choose **Edit**.

1. Comment out or remove the configuration(s) for the account(s) that you would like to be ignored. In this example, we are commenting out our **Testing-Workload** account with hash (\#) marks so that it is no longer processed by the solution engine:

   ```
   workloadAccounts:
     # - name: Testing-Workload
     #   description: The Workload account
     #   email: <workload>@example.com  <----- UPDATE EMAIL ADDRESS
     #   organizationalUnit: Workloads
   ```

1. Commit these changes. It is now safe to make additional configuration changes and release the Core pipeline without provisioning resources to the ignored account(s).
**Note**
Landing Zone Accelerator on AWS will not deploy any AWS CloudFormation stacks into ignored OU accounts, but AWS Organizations features could result in stacks being deployed within accounts in the ignored OUs.

When you use AWS Security Services, such as Macie, Security Hub, and GuardDuty with an AWS Organizations organization, security services are managed for every account in your organization. The solution configures auto-enable for new accounts, therefore when new accounts are added to your AWS Organizations, security services are automatically enabled.

## Closing an account
<a name="closing-an-account"></a>

To close an account that is managed by the solution, use one of the following procedures based off of your deployment type:

For Control Tower deployments, use the following procedure:

1.  [Unmanage](https://docs.aws.amazon.com/controltower/latest/userguide/unmanage-account.html) the account.

1. Once the account is unmanaged, move it under an [ignored OU](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/performing-administrator-tasks.html#ignoring-an-account-from-resource-provisioning).

1. Release changes to run the pipeline.

1. Once pipeline run is successful, [close the account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html).

For AWS Organizations deployments, use the following procedure:

1. Move the account under an [ignored OU](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/performing-administrator-tasks.html#ignoring-an-account-from-resource-provisioning).

1. Release changes to run the pipeline.

1. Once pipeline run is successful, [close the account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html).

For all deployments, follow the steps in [Ignoring an account from resource provisioning](#ignoring-an-account-from-resource-provisioning).

## Adding a Service Control Policy (SCP)
<a name="adding-a-service-control-policy-scp"></a>

We recommend creating a new directory in your **aws-accelerator-config** repository to store SCPs. Follow these steps to add a custom SCP to your multi-account environment.

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Choose **Create file**.

1. Copy and paste the following policy into the blank box:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "NoInternet",
         "Effect": "Deny",
         "Action": [
           "ec2:CreateInternetGateway",
           "ec2:CreateEgressOnlyInternetGateway"
         ],
         "Resource": "*",
         "Condition": {
           "ArnNotLike": {
             "aws:PrincipalARN": [
               "arn:${PARTITION}:iam::*:role/${ACCELERATOR_PREFIX}-*",
               "arn:${PARTITION}:iam::*:role/AWSControlTowerExecution",
               "arn:${PARTITION}:iam::*:role/cdk-accel-*"
             ]
           }
         }
       }
     ]
   }
   ```

1. For **File name**, save the file as `service-control-policies/block-internet.json`.

1. Enter the **Author name** and **Email address**.

1. Choose **Commit changes**.

1. Select the **organization-config.yaml** file.

1. Choose **Edit**.

1. In the `serviceControlPolicies` configuration block, append the SCP definition. For example, to add the `block-internet` SCP to the `Testing` OU, your configuration would look like the following sample:

   ```
   serviceControlPolicies:
     - name: BlockInternetAccess
       description: >
         Blocks creating Internet gateways
       policy: service-control-policies/block-internet.json
       type: customerManaged
       deploymentTargets:
         organizationalUnits:
           - Testing
   ```

## Adding an AWS Config rule
<a name="adding-an-aws-config-rule"></a>

You can add managed and custom AWS Config rules to account(s) and OU(s) within your organization. Use the following steps to add a rule to your solution configuration:

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Open the **security-config.yaml** file.

1. Add the following lines to the **awsConfig** configuration block of the **security-config.yaml** file. This example adds the managed rule [IAM\_USER\_GROUP\_MEMBERSHIP\_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-group-membership-check.html) to all accounts managed by the solution:

   ```
   awsConfig:
     enableConfigurationRecorder: true
     enableDeliveryChannel: true
     ruleSets:
       - deploymentTargets:
           organizationalUnits:
             - Root
         rules:
           - name: accelerator-iam-user-group-membership-check
             complianceResourceTypes:
               - AWS::IAM::User
             identifier: IAM_USER_GROUP_MEMBERSHIP_CHECK
   ```

## Central Security Services
<a name="central-security-services"></a>

This solution supports the concept of [delegated administration](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html) for security services such as AWS Security Hub, Amazon GuardDuty, Amazon Macie, Amazon Detective, and AWS Audit Manager. The solution simplifies configuring your delegated administrator account and sets up organization member accounts to forward their findings to a central location. Use the following steps to activate central security services in the solution configuration.

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Open the **security-config.yaml** file.

1. Add the following lines to the `centralSecurityServices` configuration block. This example turns on all supported central security services (except Amazon Detective):
**Important**
Amazon Detective isn’t activated in our configuration sample due to a prerequisite that Amazon GuardDuty is activated for 48 hours before activating Amazon Detective. Refer to [Amazon Detective prerequisites and recommendations](https://docs.aws.amazon.com/detective/latest/adminguide/detective-prerequisites.html) in the *Amazon Detective User Guide* for additional information.
**Note**
When activating Audit Manager, the service creates an Amazon S3 bucket in your organization’s Audit account specifically for Audit Manager reports. This is created for scenarios where third-party auditors require access to reports. This is a deviation from other central security services, which send logs to the central logging bucket in your organization’s Log Archive account.

   ```
   centralSecurityServices:
     delegatedAdminAccount: Audit
     ebsDefaultVolumeEncryption:
       enable: true
       excludeRegions: []
     s3PublicAccessBlock:
       enable: true
       excludeAccounts: []
     macie:
       enable: true
       excludeRegions: []
       policyFindingsPublishingFrequency: FIFTEEN_MINUTES
       publishSensitiveDataFindings: true
     guardduty:
       enable: true
       excludeRegions: []
       s3Protection:
         enable: true
         excludeRegions: []
       exportConfiguration:
         enable: true
         destinationType: S3
         exportFrequency: FIFTEEN_MINUTES
     auditManager:
       enable: true
       excludeRegions: []
       defaultReportsConfiguration:
         enable: true
         destinationType: S3
     detective:
       enable: false
       excludeRegions: []
     securityHub:
       enable: true
       regionAggregation: true
       excludeRegions: []
       standards:
         - name: AWS Foundational Security Best Practices v1.0.0
           enable: true
           controlsToDisable:[]
         - name: PCI DSS v3.2.1
           enable: true
           controlsToDisable: []
         - name: CIS AWS Foundations Benchmark v1.2.0
           enable: true
           controlsToDisable:[]
   ```

## Adding an AWS Transit Gateway
<a name="adding-an-aws-transit-gateway"></a>

Use the following steps to deploy a Transit Gateway to your multi-account environment.

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Open the **network-config.yaml** file.

1. Add the following lines to the `transitGateways` configuration block. This example adds a Transit Gateway with an AWS Resource Access Manager (AWS RAM) share for the entire organization to the Network account in the US East (N. Virginia) Region:

   ```
   transitGateways:
     - name: Network-Main
       account: Network
       region: us-east-1
       shareTargets:
         organizationalUnits:
           - Root
       asn: 65521
       dnsSupport: enable
       vpnEcmpSupport: enable
       defaultRouteTableAssociation: disable
       defaultRouteTablePropagation: disable
       autoAcceptSharingAttachments: enable
       routeTables:
         - name: Network-Main-Core
           routes: []
         - name: Network-Main-Segregated
           routes: []
         - name: Network-Main-Shared
           routes: []
         - name: Network-Main-Standalone
           routes: []
   ```

## Adding an Amazon VPC
<a name="adding-an-amazon-vpc"></a>

Use the following steps to deploy a VPC to your multi-account environment:

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Open the **network-config.yaml** file.

1. Add the following lines to the `vpcs` configuration block. This example adds a VPC with routes for the Transit Gateway created in [Adding an AWS Transit Gateway](#adding-an-aws-transit-gateway).

   ```
   vpcs:
     - name: Network-Example
       account: Network
       region: us-east-1
       cidrs:
         - 10.1.0.0/22
       internetGateway: false
       enableDnsHostnames: true
       enableDnsSupport: true
       instanceTenancy: default
       routeTables:
         - name: Network-Endpoints-Tgw-A
           routes: []
         - name: Network-Endpoints-Tgw-B
           routes: []
         - name: Network-Endpoints-A
           routes:
             - name: TgwRoute
               destination: 0.0.0.0/0
               type: transitGateway
               target: Network-Main
         - name: Network-Endpoints-B
           routes:
             - name: TgwRoute
               destination: 0.0.0.0/0
               type: transitGateway
               target: Network-Main
       subnets:
         - name: Network-Endpoints-A
           availabilityZone: a
           routeTable: Network-Endpoints-A
           ipv4CidrBlock: 10.1.0.0/24
         - name: Network-Endpoints-B
           availabilityZone: b
           routeTable: Network-Endpoints-B
           ipv4CidrBlock: 10.1.1.0/24
         - name: Network-EndpointsTgwAttach-A
           availabilityZone: a
           routeTable: Network-Endpoints-Tgw-A
           ipv4CidrBlock: 10.1.3.208/28
         - name: Network-EndpointsTgwAttach-B
           availabilityZone: b
           routeTable: Network-Endpoints-Tgw-B
           ipv4CidrBlock: 10.1.3.224/28
       transitGatewayAttachments:
         - name: Network-Endpoints
           transitGateway:
             name: Network-Main
             account: Network
           routeTableAssociations:
             - Network-Main-Shared
           routeTablePropagations:
             - Network-Main-Core
             - Network-Main-Shared
             - Network-Main-Segregated
           subnets:
             - Network-EndpointsTgwAttach-A
             - Network-EndpointsTgwAttach-B
   ```

**Important**
Landing Zone Accelerator on AWS does not support creation of users and groups in Identity Center. Users and groups are required to be created in Identity Center before the solution can use those principals for permission set assignments.

## Adding an IAM Identity Center permission set
<a name="adding-an-iam-identity-center-permission-set"></a>

Use the following steps to deploy an IAM Identity Center permission set to your multi-account environment:

1. Sign in to the [AWS CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).

1. Select the **aws-accelerator-config** repository.

1. Open the **iam-config.yaml** file.

1. Add the `identityCenter` configuration block. This example creates two predefined permission sets that use a single AWS managed policy and modifies the session duration.

   ```
   identityCenter:
     name: identityCenter
     identityCenterPermissionSets:
       - name: PowerAccessUser
         policies:
           awsManaged:
             - arn:aws:iam::aws:policy/PowerUserAccess
           customerManaged: []
         sessionDuration: 60
       - name: ViewOnlyAccess
         policies:
           awsManaged:
             - arn:aws:iam::aws:policy/job-function/ViewOnlyAccess
           customerManaged: []
         sessionDuration: 60
   ```

**Important**
Landing Zone Accelerator on AWS does not support creation of users and groups in Identity Center. Users and groups are required to be created in Identity Center before the solution can use those principals for permission set assignments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
