---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/delete-environment-profile.html
---

# Delete an environment profile
<a name="delete-environment-profile"></a>

In Amazon DataZone, an environment proﬁle is a template that you can use to create environments. The purpose of an environment profile is to simplify environment creation by embedding placement information such as AWS account and region within the profiles. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md). To delete environment profiles in an Amazon DataZone domain, you must belong to an Amazon DataZone project.

**Note**
When you delete an environment profile, you can't create any more environments using this profile.

**To delete an environment profile**

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with the AWS account where the domain was created, then choose **Open data portal**.

1. Within the data portal, choose **Browse projects** and select the project in which you want to delete the environment profile.

1. Navigate to the **Environments** tab within the project, then choose **Environment profiles**, and then choose the environment profile that you want to delete.

1. Select the environment profile you want to delete, then choose **Actions**, **Delete** and confirm deletion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
