---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/map-application-attributes.html
---

# Map application attributes
<a name="map-application-attributes"></a>

In this step, you map application attributes to the user attribute in IAM Identity Center, using the email address for authentication.

1. From the list of applications, choose the SAML application you set up in the previous step.

1. Under **Actions**, choose **Edit attribute mappings**.

1. For the *Subject* **User attribute in the application** row, fill in the two corresponding fields:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/map-application-attributes.html)

1. Choose **Save Changes**.

**Note**
If you have configured IAM Identity Center to use an external identity provider, you need to ensure that the attribute mappings from external identity provider to IAM Identity Center are configured correctly. For more information refer to [Configuring an external identity provider](configuring-external-idp.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
