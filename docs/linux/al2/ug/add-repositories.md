---
source_url: https://docs.aws.amazon.com/linux/al2/ug/add-repositories.html
---

# Add repositories on an AL2 instance
<a name="add-repositories"></a>

This information applies to AL2. For information about AL2023, see [Deterministic upgrades through versioned repositories on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades.html) in the *Amazon Linux 2023 User Guide*.

By default, AL2 instances launch with the following repositories enabled:
+ `amzn2-core`
+ `amzn2extra-docker`

While there are many packages available in these repositories that are updated by Amazon Web Services, there might be a package that you want to install that is contained in another repository.

To install a package from a different repository with **yum**, you need to add the repository information to the `/etc/yum.conf` file or to its own `{{repository}}.repo` file in the `/etc/yum.repos.d` directory. You can do this manually, but most yum repositories provide their own `{{repository}}.repo` file at their repository URL.

**To determine what yum repositories are already installed**
List the installed yum repositories with the following command:

```
[ec2-user ~]$ yum repolist all
```

The resulting output lists the installed repositories and reports the status of each. Enabled repositories display the number of packages they contain.

**To add a yum repository to /etc/yum.repos.d**

1. Find the location of the `.repo` file. This will vary depending on the repository you are adding. In this example, the `.repo` file is at `https://www.{{example}}.com/{{repository}}.repo`.

1. Add the repository with the **yum-config-manager** command.

   ```
   [ec2-user ~]$ sudo yum-config-manager --add-repo https://www.{{example}}.com/{{repository}}.repo
   Loaded plugins: priorities, update-motd, upgrade-helper
   adding repo from: https://www.{{example}}.com/{{repository}}.repo
   grabbing file https://www.{{example}}.com/{{repository}}.repo to /etc/yum.repos.d/{{repository}}.repo
   {{repository}}.repo                                      | 4.0 kB     00:00
   repo saved to /etc/yum.repos.d/{{repository}}.repo
   ```

After you install a repository, you must enable it as described in the next procedure.

**To enable a yum repository in /etc/yum.repos.d**
Use the **yum-config-manager** command with the `--enable {{repository}}` flag. The following command enables the Extra Packages for Enterprise Linux (EPEL) repository from the Fedora project. By default, this repository is present in `/etc/yum.repos.d` on Amazon Linux AMI instances, but it is not enabled.

```
[ec2-user ~]$ sudo yum-config-manager --enable {{epel}}
```

For more information, and to download the latest version of this package, see [https://fedoraproject.org/wiki/EPEL](https://fedoraproject.org/wiki/EPEL).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
