---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-var.html
---

# `/var` (Persistent Variable System Data)
<a name="filesystem-slash-var"></a>

## `/var/cache` (Cache)
<a name="filesystem-slash-var-cache"></a>

 In contrast to [`/var/lib`](#filesystem-slash-var-lib), erasing data in `/var/cache` will not result in data loss, as applications are required to be able to rebuild their `/var/cache` data from other sources.

## `/var/lib` (Persistent system data)
<a name="filesystem-slash-var-lib"></a>

 The `/var/lib` directory is used for persistent system data. Various system components will place data here which is private to that component. In contrast to [`/var/cache`](#filesystem-slash-var-cache), erasing data in `/var/lib` will result in data loss.

 For example, the PostgreSQL database server will by default store database data in `/var/lib/pgsql`. The layout and file formats of this data is private to PostgreSQL, and it is persistent data as if erased, the user experiences data loss.

## `/var/log` (Persistent logs)
<a name="filesystem-slash-var-log"></a>

 This directory is used for storing persistent logs. It is recommended that software use the `syslog(3)` or `sd_journal_print(3)` API calls rather than directly storing log files under `/var/log`.

**Note**
 In AL2023 the [`systemd` journal replaces `rsyslog`](journald.md), which is a notable difference from the default Amazon Linux 2 configuration.

 For more information on reading logs using `journalctl`, see the [https://www.freedesktop.org/software/systemd/man/journalctl.html](https://www.freedesktop.org/software/systemd/man/journalctl.html) manual page.

 Many applications use their own mechanisms for writing, and sometimes rotating, log files found in `/var/log`. See the documentation for these applications on how to configure their log files.

## `/var/spool` (Mail and Printer queues)
<a name="filesystem-slash-var-spool"></a>

 This directory is used for persistent data such as mail or printer queues.

## `/var/tmp` (larger temporary files)
<a name="filesystem-slash-var-tmp"></a>

 For small, size-bound temporary files, [`/tmp`](filesystem-slash-tmp.md) should possibly be used instead.

 While [`/tmp`](filesystem-slash-tmp.md) is by default configured to be a `tmpfs` volume, `/var/tmp` is by default configured to be a path on the root file system, and is thus the place for larger and more persistent temporary files. By default, there is a cleanup job run on a regular schedule which removes files not recently accessed.

 For information on how to configure the clean-up of temporary files, see the `tmpfiles.d(5)` and `systemd-tmpfiles(8)` man man pages.

 As with [`/tmp`](filesystem-slash-tmp.md), applications should prefer the path specified in the `$TMPDIR` environment variable over `/var/tmp`. Users can then set the `$TMPDIR` environment variable to override the path an application should use for `/var/tmp`.

**Warning**
 Since `/var/tmp` is shared (as is [`/tmp`](filesystem-slash-tmp.md), it is important to use safe methods of creating temporary files. For details, see the upstream `systemd` documentation on [Using `/tmp` and `/var/tmp` Safely](https://systemd.io/TEMPORARY_DIRECTORIES/).

**Note**
 It is best practice for `systemd` services to be configured with the `PrivateTmp=` directive set to `yes` or `disconnected` which runs the service in a sandbox where [`/tmp`](filesystem-slash-tmp.md) and [`/var/tmp`](#filesystem-slash-var-tmp) are not shared with the host or other services.
 For more information, including how to configure two services to share the same private temporary directories, see the `systemd.exec(5)` man page.

 The [`/tmp`](filesystem-slash-tmp.md) and [`/var/tmp`](#filesystem-slash-var-tmp) paths are closely related and exist for different purposes.
