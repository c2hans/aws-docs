---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-tmp.html
---

# `/tmp` (small temporary files)
<a name="filesystem-slash-tmp"></a>

**Note**
 Amazon Linux 2023 is different to Amazon Linux 2 as by default `/tmp` is now `tmpfs` rather than a path on the root file system.

**Note**
 When running in a container, it will typically be your container runtime configuration that dictates if `/tmp` is `tmpfs`, or a path on disk, and if there is a running clean-up process or not.

 The `/tmp` directory is for small, size-bounded temporary files. By default, AL2023 configures it to be a `tmpfs` file system with a size limit of 50% of RAM and a maximum of one million inodes.

 Applications should prefer the path in the `$TMPDIR` environment variable over `/tmp`. Users can then set the `$TMPDIR` environment variable to override the path an application should use for `/tmp`

 For larger temporary files, [`/var/tmp`](filesystem-slash-var.md#filesystem-slash-var-tmp) should be used instead.

**Warning**
 Since `/tmp` is shared, it is important to use safe methods of creating temporary files. For details, see the upstream `systemd` documentation on [Using `/tmp` and `/var/tmp` Safely](https://systemd.io/TEMPORARY_DIRECTORIES/).

**Note**
 It is best practice for `systemd` services to be configured with the `PrivateTmp=` directive set to `yes` or `disconnected` which runs the service in a sandbox where `/tmp` and [`/var/tmp`](filesystem-slash-var.md#filesystem-slash-var-tmp) are not shared with the host or other services.
 For more information, including how to configure two services to share the same private temporary directories, see the `systemd.exec(5)` man page.

 The content of `/tmp` is typically cleaned at boot time, and unused files are regularly cleaned up. By default, the cleanup process runs shortly after boot and then every day. For information on how to configure the clean-up of temporary files, see the `tmpfiles.d(5)` and `systemd-tmpfiles(8)` man man pages.

 The `/tmp` and [`/var/tmp`](filesystem-slash-var.md#filesystem-slash-var-tmp) paths are closely related and exist for different purposes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
