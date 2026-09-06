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
