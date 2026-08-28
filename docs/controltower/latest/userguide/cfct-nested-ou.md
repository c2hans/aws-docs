---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/cfct-nested-ou.html
---

# Nested OU
<a name="cfct-nested-ou"></a>

CfCT supports listing one or more nested OUs under the `organizational_units` keyword in manifest V2 version (2021-03-15).

A complete path (excluding Root) for the nested OU is required, using a colon as the separator between OUs. For deployment method `scp` or `rcp`, AWS Control Tower deploys the SCPs or RCPs to the last OU in the nested OU path. For deployment method `stack_set`, AWS Control Tower deploys the stack sets to all the accounts under the last OU in the nested OU path.

For example, consider the path `OUName1:OUName2:OUName3`. The last OU in the path is `OUName3`. CfCT deploys the SCPs or RCPs to `OUName3` and stack sets to all of the accounts directly under `OUName3`, only.

```
---
region: {{your-home-region}}
version: 2021-03-15

resources:

  …truncated…

    deployment_targets:
      organizational_units:
        - OuName1:OUName2:OUName3
```

**Note**
The nested OU feature is supported only in the V2 version of the manifest file (2021-03-15).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
