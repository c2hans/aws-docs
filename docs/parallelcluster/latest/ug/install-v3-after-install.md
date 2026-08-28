---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-after-install.html
---

# Steps to take after installation
<a name="install-v3-after-install"></a>

This section assumes that you've installed AWS ParallelCluster. You will learn how to verify that AWS ParallelCluster installed correctly, how to update to the latest version of AWS ParallelCluster, and how to uninstall.

You can verify that AWS ParallelCluster was installed correctly by running [`pcluster version`](pcluster.version-v3.md).

```
$ pcluster version
{
"version": "3.15.1"
}
```

AWS ParallelCluster is updated regularly. To update to the latest version of AWS ParallelCluster, run the installation command again. For more information about the latest version of AWS ParallelCluster, see the [AWS ParallelCluster release notes](https://github.com/aws/aws-parallelcluster/blob/v3.1.1/CHANGELOG.md).

```
$ pip3 install aws-parallelcluster --upgrade --user
```

To uninstall AWS ParallelCluster, use `pip3 uninstall`.

```
$ pip3 uninstall aws-parallelcluster
```

If you don't have Python and `pip3`, use the procedure for your environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
