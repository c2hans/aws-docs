---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/compute-node-initialization-locale-v3.html
---

# Seeing `cannot change locale (en_US.utf-8) because it has an invalid name` in `slurm_resume.log`
<a name="compute-node-initialization-locale-v3"></a>

This can occur if you have an unsuccessful `yum` installation process that left the locale settings in an inconsistent state. For example, this can be caused when a user terminates the install process.

**To verify the cause, take the following actions:**
+ Run `su - pcluster-admin`.

  The shell shows an error, such as, `cannot change locale...no such file or directory`.
+ Run `localedef --list`.

  Returns an empty list or doesn't contain the default locale.
+ Check the last `yum` command with `yum history` and `yum history info #ID`. Does the last ID have `Return-Code: Success`?

  If the last ID doesn't have `Return-Code: Success`, the post-install scripts might not have run successfully.

To fix the issue, try rebuilding the locale with `yum reinstall glibc-all-langpacks`. After the rebuild, `su - pcluster-admin` doesn't show an error or warning if the issue is fixed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
