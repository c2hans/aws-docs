---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-coderepository.html
---

# CodeRepository object in ASFF
<a name="asff-resourcedetails-coderepository"></a>

The `CodeRepository` object provides information about an external code repository that you connected to AWS resources and configured Amazon Inspector to scan for vulnerabilities.

The following example shows the AWS Security Finding Format (ASFF) syntax for the `CodeRepository` object. To view descriptions of `CodeRepository` attributes, see [CodeRepositoryDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CodeRepositoryDetails.html) in the *AWS Security Hub API Reference*. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

**Example**

```
"CodeRepository": {
    "ProviderType": "GITLAB_SELF_MANAGED",
    "ProjectName": "projectName",
    "CodeSecurityIntegrationArn": "arn:aws:inspector2:us-east-1:123456789012:codesecurity-integration/00000000-0000-0000-0000-000000000000"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
