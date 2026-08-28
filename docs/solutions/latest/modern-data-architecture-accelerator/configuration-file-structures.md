---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/configuration-file-structures.html
---

# Configuration File Structures
<a name="configuration-file-structures"></a>

You can organize your configurations in several ways.

## Single Domain, Shared CDK Apps Configs Across Envs
<a name="single-domain-shared-cdk-apps-configs-across-envs"></a>

```
root_folder
│    mdaa.yaml
│    tags.yaml
│
└───  domain1
     roles.yaml
     datalake.yaml
```

## Single Domain, Separate CDK Apps Configs Across Envs
<a name="single-domain-separate-cdk-apps-configs-across-envs"></a>

```
root_folder
│    mdaa.yaml
│    tags.yaml
│
└───  domain1
    └───  dev
    │    │  dev_roles.yaml
    │    │  dev_datalake.yaml
    │
    └───  test
    │    │  test_roles.yaml
    │    │  test_datalake.yaml
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
