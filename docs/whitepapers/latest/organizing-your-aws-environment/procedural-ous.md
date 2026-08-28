---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/procedural-ous.html
---

# Procedural OUs
<a name="procedural-ous"></a>

## Exceptions OU
<a name="exceptions-ou"></a>

 The Exceptions OU houses accounts that require an exception to the security policies that are applied to your Workloads OU. Normally, there should be a minimal number of accounts, if any, in this OU.

### Service control policies and scrutiny
<a name="service-control-policies-and-scrutiny"></a>

 Given the unique nature of the exceptions, SCPs are typically applied at the account level in this OU. Due to the customized security controls that apply to these accounts, owners of these accounts can expect to experience greater scrutiny from security monitoring systems.

### Consider Workloads OU as an alternative
<a name="consider-workloads-ou-as-an-alternative"></a>

 If you observe a pattern in which multiple accounts require the same set of exceptions, we recommend that you examine either your existing workloads policies or an extended form of the Workloads OU structure and house the accounts under the Workloads OU. You can introduce another level of OU under the Workloads OU to represent a common set of security policies and/or operational processes that can be applied to multiple workload environments. For more information, refer to [Organizing workload-oriented OUs](advanced-ous.md#organizing-workload-oriented-ous).

## Transitional OU
<a name="transitional-ou"></a>

 The Transitional OU is intended as a temporary holding area for existing accounts and workloads that you move to your organization before formally integrating them into the more standardized areas of your AWS environment structure.

### Common scenarios for moving accounts into your organization
<a name="common-scenarios-for-moving-accounts-into-your-organization"></a>

 Common scenarios for moving accounts into your organization include:
+  Acquisition of a company that is already using AWS and has a set of accounts
+  Existence of your own accounts that were created before you established your newer AWS environment structure
+  Movement of accounts that have previously been managed by a third party
+  Divestment of specific workload to be migrated out of your AWS Organization

### Considerations for moving accounts into your organization
<a name="considerations-for-moving-accounts-into-your-organization"></a>

 With direct account transfers, you can move an account from one organization to another. You do not need to remove it from its current organization or operate it as a standalone account first. The destination organization sends an invitation, and the migrating account accepts it using the same AWS Organizations console experience and APIs. You retain access to governance features and consolidated billing before and after the transfer. For more information, see [Migrate an account to another organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_account_migration.html).

 If you instead want an account to leave its organization and operate as a standalone account, that option is still available to you and requires the `organizations:LeaveOrganization` permission.

 Moving an account that does not have dependencies on other accounts is a straightforward process. In this case, there's generally no need to migrate or modify the existing workloads in the account to be moved. For more information, see [Inviting an account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html).

 If the standalone account to be moved has dependencies on other accounts, then you should evaluate those dependencies to determine if they should be addressed before moving the account.

 In your target organization, we recommend that you review SCPs in the organization's root to ensure that those SCPs won't adversely impact the accounts to be moved.

 If you're moving a set of related accounts to your organization, you can create a child OU under the Transitional OU for the related set of accounts.

### After moving accounts
<a name="after-moving-accounts"></a>

 Over time, as you better understand the direction for these accounts and the workloads contained in them, you can either move the accounts to your Workloads OU as is, invest in migrating the workloads to other accounts, or decommission either the workloads or accounts.

## Policy Staging OU
<a name="policy-staging-ou"></a>

 The Policy Staging OU is intended to help teams that manage overall policies for your AWS environment to safely test potentially broadly impacting policy changes before applying them to the intended OUs or accounts. For example, SCPs and tag policies should be tested prior to applying them to the intended OUs or accounts. Similarly, broadly applicable account baseline IAM roles and policies should also be tested using the Policy Staging OU.

### Workload-specific policies
<a name="workload-specific-policies"></a>

 Development and testing of workload-specific IAM roles and policies do not need to use the Policy Staging OU. Rather, workload owning teams typically develop and test these resources alongside other workload-specific resources in development and test accounts within your Security, Infrastructure, and Workloads OUs.

### Recommended testing and promotion workflow
<a name="recommended-testing-and-promotion-workflow"></a>

 Once you have tested changes in the Policy Staging OU, we recommend that you temporarily associate the policy changes to a single account in the intended OU. If the changes are ultimately targeting an OU, apply the changes to the intended OU and remove the changes from the account only after you have validated that the changes are working as intended.

 This approach enables you to validate the changes in production before more broadly applying them.

### Example structure
<a name="example-structure-3"></a>

 In this example, a set of child OUs mirrors an overall OU structure. At least one test account is included under each child OU.

 In support of testing SCPs and tag policies that are intended to be applied at the OU level, your teams should first apply them to one of the test child OUs. SCPs and tag policies that are applied to a specific account require creation of a test account under the appropriate test child OU.

![Diagram showing example structure of Policy Staging OU](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-policy-ou.png)

## Suspended OU
<a name="suspended-ou"></a>

 The Suspended OU is used as a temporary holding area for accounts that are required to have their use suspended.

 Moving an account to this OU does not automatically change the overall status of the account. For example, in cases where you intend to permanently stop using an account, you would follow the [Closing an account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/close-account.html) process to permanently close the account.

 Examples of using the Suspended OU include:
+  A person's sandbox account is no longer needed due to the departure of the person from the company.
+  A workload account is no longer needed due to the resources having been either retired or migrated to another account.

### Constraining activity in suspended accounts
<a name="constraining-activity-in-suspended-accounts"></a>

 You can use service control policies (SCPs) to inhibit users other than your security and cloud platform teams from using AWS APIs in each account. Additionally, you can remove application-level access so that users can no longer access and manage application resources for each suspended account.

 To reduce risk and potentially minimize costs, you can also stop any running resources and applications in each suspended account.

 Resources should not be deleted from a suspended account unless the account is intended to be closed.

### Tagging suspended accounts
<a name="tagging-suspended-accounts"></a>

 Because you might use the Suspended OU for a variety of use cases, we recommend that you apply tags to each account to record the reason for moving the account and the OU from where the account originated. Each process that you establish to support your suspension use cases can use the tag to automatically process the suspended accounts. This tag can also aid in your internal tracing and auditing of an account's lifecycle.

### Closing suspended accounts
<a name="closing-suspended-accounts"></a>

 If an account is moved to this OU prior to the start of the closure process, you can implement a policy and process to automatically start the account closing process a certain number of days after an account has been moved to this OU.

 Once the account closure process has been completed, the account is no longer visible in your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
