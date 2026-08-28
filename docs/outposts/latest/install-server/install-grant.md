---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/install-grant.html
---

# Step 1: Grant permissions to install the Outposts server
<a name="install-grant"></a>

To verify the identity of the new device, you must have IAM credentials in the AWS account that contains the Outpost. The [AWS OutpostsAuthorizeServerPolicy](https://docs.aws.amazon.com/outposts/latest/server-userguide/security-iam-awsmanpol.html#AWSOutpostsAuthorizeServerPolicy) policy grants the permissions required to install an Outposts server. For more information, see [Identity and access management (IAM) for AWS Outposts](https://docs.aws.amazon.com/outposts/latest/server-userguide/identity-access-management.html) in the *AWS Outposts user guide for servers*.

**Considerations**
+ If you are using a third party that does not have access to your AWS account, you must provide temporary access.
+ AWS Outposts supports using temporary credentials. You can configure temporary credentials that last up to 36 hours. Ensure that you give the installer enough time to perform all the steps for server installation. For more information, see [Using temporary credentials with AWS Outposts](https://docs.aws.amazon.com/outposts/latest/server-userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-roles-tempcreds) in the *AWS Outposts User Guide for Outposts servers*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
