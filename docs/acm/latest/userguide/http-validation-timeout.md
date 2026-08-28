---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/http-validation-timeout.html
---

# Validation timeout
<a name="http-validation-timeout"></a>

HTTP validation may time out if the content isn't available within the expected time frame. To troubleshoot validation issues, follow these steps.

**To troubleshoot validation timeout**

1. Do one of the following to check which domains are pending validation:

   1. Open the ACM console and view the certificate details page. Look for domains marked as **Pending validation**.

   1. Call the `DescribeCertificate` API operation to view the validation status of each domain.

1. For each pending domain, verify that the validation content is accessible from the internet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
