---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-iamenduser.html
---

# Grant permissions to AWS Service Catalog end users
<a name="getstarted-iamenduser"></a>

Before the end user can use AWS Service Catalog, you must grant access to the AWS Service Catalog end user console view. To grant access, you attach policies to the IAM user, group, or role that is used by the end user. In the following procedure, we attach the ****`AWSServiceCatalogEndUserFullAccess`**** policy to an IAM group.

**To grant permissions to an end user group**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **User groups**.

1. Choose **Create group** and do the following:

   1. For **User group name**, type **Endusers**.

   1. In the search field, type **AWSServiceCatalog** to filter the policy list.

   1. Select the checkbox for the ****`AWSServiceCatalogEndUserFullAccess`**** policy. You also have the option to choose ****`AWSServiceCatalogEndUserReadOnlyAccess`**** instead.

   1. Choose **Create Group**.

1. In the navigation pane, choose **Users**.

1. Choose **Add users** and do the following:

   1. For **User name**, type a name for the user.

   1. Select **Password - AWS Management Console access**.

   1. Choose **Next: Permissions**.

   1. Choose **Add user to group**.

   1. Select the checkbox for the **Endusers** group and choose **Next: Tags** and then **Next: Review**.

   1. On the **Review** page, choose **Create user**. Download or copy the credentials and then choose **Close**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
