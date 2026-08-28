---
source_url: https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-codecatalyst-actions.html
---

# Using CodeCatalyst actions with Amazon Inspector
<a name="cicd-inspector-codecatalyst-actions"></a>

 You can use Amazon Inspector with [Amazon CodeCatalyst](https://codecatalyst.aws/explore) to add Amazon Inspector vulnerability scans to your CodeCatalyst workflows. This leverages the [Amazon Inspector SBOM Generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html) and [Amazon Inspector Scan API](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Operations_Inspector_Scan.html) to produce detailed reports at the end of your build, so you can investigate and remediate risk before deployment. Amazon Inspector vulnerability scans can be configured to pass or fail workflows based on the number and severity of vulnerabilities detected. For information about how to integrate Amazon Inspector Scan into your CI/CD pipeline, see [Integrating Amazon Inspector scans into your CI/CD pipeline](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html). For a list of operating systems and programming languages that Amazon Inspector supports, see [Supported operating systems and programming languages](https://docs.aws.amazon.com/inspector/latest/user/supported.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
