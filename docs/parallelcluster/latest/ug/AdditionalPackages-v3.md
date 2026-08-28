---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/AdditionalPackages-v3.html
---

# `AdditionalPackages` section
<a name="AdditionalPackages-v3"></a>

**(Optional)** Used to identify additional packages to install.

```
AdditionalPackages:
  IntelSoftware:
    IntelHpcPlatform: {{boolean}}
```

[Update policy: If this setting is changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3)

## `IntelSoftware`
<a name="AdditionalPackages-v3-IntelSoftware"></a>

**(Optional)** Defines the configuration for Intel select solutions.

```
IntelSoftware:
  IntelHpcPlatform: {{boolean}}
```

[Update policy: If this setting is changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3)

### `IntelSoftware` properties
<a name="AdditionalPackages-v3-IntelSoftware.properties"></a>

` IntelHpcPlatform` (**Optional**, `Boolean`)
If `true`, indicates that the [ End user license agreement](https://software.intel.com/en-us/articles/end-user-license-agreement) for Intel Parallel Studio is accepted. This causes Intel Parallel Studio to be installed on the head node and shared with the compute nodes. This adds several minutes to the time it takes the head node to bootstrap.
[Update policy: If this setting is changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3)
Starting with AWS ParallelCluster version 3.10.0 the `IntelHpcPlatform` parameter is no longer supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
