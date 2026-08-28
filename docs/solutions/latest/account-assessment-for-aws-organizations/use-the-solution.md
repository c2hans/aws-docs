---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/use-the-solution.html
---

# Use the solution
<a name="use-the-solution"></a>

**Note**
Dependencies outside the scope of this solution can impact the account migration between AWS Organizations (for example, [quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html), resources shared by [AWS RAM](https://aws.amazon.com/ram/), and service-managed CloudFormation [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)).

## Login page
<a name="login-page"></a>

At the email address you provided for the `Provide Web UI Login User Email` input when you [launched the Hub stack](step-1-launch-the-hub-stack.md), you will receive an email with the subject **WebUI Credentials - Account Assessment for AWS Organizations** that contains the following:
+ Your temporary login credentials
+ The URL for the web UI

You may alternatively retrieve the web UI URL from the CloudFormation template outputs under `"WebUserInterfaceURL"`. To add or manage additional users, use the Cognito Service user interface in the AWS Console.

## Welcome page
<a name="welcome-page"></a>

This page displays after you log in. If applicable, it shows your previous scan job status and assessment type for that job.

![Screenshot of welcome page](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/welcome_page.png)

## Findings
<a name="findings"></a>

The left pane lists three types of assessments.

1. Resource-Based Polices (Deprecated, read-only page since v1.1.0)

1. Delegated Admin Accounts

1. Trusted Access

Begin an assessment by selecting **Start Scan or download the table content as .csv file by selecting Download Results**.

**Note**
You can run one active scan per assessment type at a time.

![Screenshot of Resource-Based Polices page](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/delegated_admins.png)

![Screenshot of Delegated Admin Accounts page](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/trusted_access.png)

### Policy Explorer
<a name="policy-explorer"></a>

Beginning with Account Assessment v1.1.0, the Policy Explorer allows you to conduct nuanced searches for policies in your AWS Organization.

**Note**
Policy Explorer runs a nightly scan for policies across your AWS Organization and stores a string representation of each policy in DynamoDB. Search results you see on the Policy Explorer page are not real-time, but based on the last successful scan. Consult the JobHistory page to find out when the last successful scan was conducted.

![Screenshot of Policy Explorer page](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/policy_explorer.png)

You can search for policies
+ By type (Identity Based Policies, Resource Based Policies, Service Control Policies)
+ By region. Use `GLOBAL` for region-independent policies
+ By principal
+ By action
+ By resource
+ By condition
+ By effect (Allow, Deny or Both)

The matching strategy is `string contains`, e.g. a search input like `us-` will match policies in all us regions. The search criteria is applied server-side. If your search is too broad, and the amount of result data exceeds what the frontend can handle, you will see a message asking you to narrow down the search with additional criteria.

Use the `View Policies` button to see the full string representation of any policy.

![Screenshot of Policy Explorer page](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/view_policies.png)

#### Dependencies on your AWS Organization
<a name="dependencies-on-your-aws-organization"></a>

A main use case of the "Resource-based Policy Scan" in Account Assessment prior to v1.1.0 was to find policies that contain a condition with the Organization ID, hinting at a policy that may break when the account is moved to a different AWS Organization.

This use case is now covered by PolicyExplorer. To search for Policies that contain your Organizational ID in the condition, press the button `Add OrgId` which will prepopulate the `Condition` search input field with your Org ID. Leave all other fields blank.

![Screenshot of Policy Explorer page](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/org_dependencies.png)

### Job History
<a name="job-history"></a>

The Job History page helps you review the previous scans and their status. The solution provides four status possibilities:
+  **ACTIVE** – Scan is currently running
+  **SUCCEEDED** – Scan completed successfully
+  **SUCCEEDED\_WITH\_FAILED\_TASKS** – Scan completed, but some tasks have errors
+  **FAILED** – Scan failed

Select the **Job ID** to view specific findings per job.

![Screenshot of job history](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/job_history.png)

When you select the **Job ID**, the Job Details page displays the findings and any failed tasks during your selected job. You can use this information to help you identify the resource and errors. If the error states that a certain account/region/service/resource could not be scanned, that means that there may be possible findings which the solution was not able to assess. Use your judgement to decide how to proceed.

The AccessDenied error often hints at the fact that the SpokeRole of the Account Assessment solution was not installed in the respective account, so the solution has no permission to access the account in question for a scan.

![Example job details for SUCCEEDED_WITH_FAILED_TASKS](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/failed_tasks.png)

## Next steps
<a name="next-steps"></a>

We designed this solution to help you determine specific AWS Organizations dependencies in your underlying resource-based policies. It does not check the validity or correctness of these policies. There are myriad ways in which you can use this data, not limited to common use cases such as consolidating multiple AWS Organizations, preparing for a security audit, or changing your AWS Organization’s management account.

### Account migration
<a name="account-migration"></a>

One of the common use cases for this solution is to help you plan for migrating your AWS Organizations accounts, such as with a company merger or acquisition. Migrating your accounts requires careful consideration. Specifically, we recommend:
+ Verifying that your policies work as intended before making changes.
+ Using IAM Access Analyzer to verify that your policies achieve your desired permissions.
+ Reviewing and updating the `Condition` policy element to meet your security requirements. Do not delete the `Condition` without reviewing the underlying impact.
+ Reviewing other dependencies outside the scope of this solution that can impact the account migration between AWS Organizations.

We recommend that you engage with AWS Solutions Architects, Technical Account Managers, and AWS Professional Services to review your AWS Organizations-based dependencies identified by the solution before initiating account migration. Additional resources include the following:
+  [How do I move accounts between organizations in AWS Organizations?](https://aws.amazon.com/premiumsupport/knowledge-center/organizations-move-accounts/) – This blog post identifies some of the account, reporting, billing, and other considerations you will need to take when migrating accounts.
+  [Migrating accounts between AWS Organizations with consolidated billing to all features](https://aws.amazon.com/blogs/mt/migrating-accounts-between-aws-organizations-with-consolidated-billing-to-all-features/) – This blog post provides further insights into consolidated billing and account migration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
