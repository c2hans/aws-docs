---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

From version v1.1.0 on, we improved the generation of the Cognito UserPool name and the AppRegistry application name to make it less likely that your deployment fails due to a name conflict. As these changes are not backwards compatible, it is not possible to update the v1.0.x Hub stack to v1.1.x in place.

If you have v1.0.x installed in your account, and you want to start using v1.1.x, take the following steps:
+ Undeploy the CloudFormation stacks of your v1.0.x installation
+ Before deleting the UserPool, check if there are any users (except from the default user created at deployment time) that you need to re-create in the new UserPool. Note their email addresses if needed.
+ Delete the UserPool, S3 buckets and DynamoDB tables of your v1.0.x installation. As your scan data are stale, you do not need to migrate any data to the new solution version. You will be able to run a fresh scan after installing the new solution version. See [uninstall instructions](uninstall-the-solution.md) for details.
+ Choose a new "namespace" and install v1.1.x freshly in your accounts, following the [deployment instructions](deploy-the-solution.md#deployment-process-overview) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
