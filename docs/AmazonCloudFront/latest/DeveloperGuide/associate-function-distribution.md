---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/associate-function-distribution.html
---

# Step 4: Associate the function to your distribution
<a name="associate-function-distribution"></a>

Once you publish your Connection Function, associate it with your mTLS-enabled distribution to activate certificate revocation checking.

You can associate the function from the distribution settings page or from the Connection Function's associated distributions table. Navigate to your distribution settings, scroll to the **Viewer mutual authentication (mTLS)** section, select your Connection Function, and save the changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
