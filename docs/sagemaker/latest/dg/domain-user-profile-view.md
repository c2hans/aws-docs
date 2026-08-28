---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-view.html
---

# View user profiles in a domain
<a name="domain-user-profile-view"></a>

 The following section describes how to view a list of user profiles in a domain from the SageMaker AI console or the AWS CLI.

## View user profiles from the console
<a name="domain-user-profile-view-console"></a>

 Complete the following procedure to view a list of user profiles in the domain from the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**.

1. From the list of domains, select the domain that you want to view a list of user profiles for.

1. On the **domain details** page, choose the **User profiles** tab.

## View user profiles from the AWS CLI
<a name="domain-user-profile-view-cli"></a>

To view the user profiles in a domain from the AWS CLI, run the following command from the terminal of your local machine.

```
aws sagemaker list-user-profiles \
--region {{region}} \
--domain-id {{domain-id}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
