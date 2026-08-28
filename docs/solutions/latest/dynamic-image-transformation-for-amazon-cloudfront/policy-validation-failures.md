---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/policy-validation-failures.html
---

# Policy validation failures
<a name="policy-validation-failures"></a>

 **Symptoms:** - 400 Bad Request errors when creating policies - Policy creation fails in Admin UI - "Invalid policy JSON" error messages

 **Solutions:**

 **Check JSON syntax:**
+ Validate JSON structure using online JSON validators
+ Ensure all required fields are present
+ Verify transformation parameter types match schema requirements

 **Review transformation limits:** - Policy size limit: 400KB - Ensure transformation values are within valid ranges

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
