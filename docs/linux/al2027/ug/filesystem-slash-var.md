---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-var.html
---

# `/var` (persistent variable system data)
<a name="filesystem-slash-var"></a>

The `/var` directory stores persistent variable system data.

## `/var/cache` (cache)
<a name="filesystem-slash-var-cache"></a>

Applications must be able to rebuild their `/var/cache` data from other sources, so erasing data here does not cause data loss. For example, DNF keeps its repository metadata cache under `/var/cache/libdnf5` and rebuilds it on the next metadata refresh.

## `/var/lib` (persistent system data)
<a name="filesystem-slash-var-lib"></a>

System components store persistent, private data under `/var/lib`. In contrast to [`/var/cache`](#filesystem-slash-var-cache), erasing data here causes data loss. For example, the RPM database lives in `/var/lib/rpm`, and the PostgreSQL database server stores database data in `/var/lib/pgsql`.

## `/var/log` (persistent logs)
<a name="filesystem-slash-var-log"></a>

The `/var/log` directory holds persistent logs. Software should prefer the `syslog(3)` or `sd_journal_print(3)` API calls over writing log files directly. Read the `systemd` journal with `journalctl`; for more information, see the `journalctl(1)` man page. Applications that write their own log files under `/var/log` document their own rotation configuration.

## `/var/spool` (queued data)
<a name="filesystem-slash-var-spool"></a>

Persistent queued data, such as mail or printer queues.

## `/var/tmp` (larger temporary files)
<a name="filesystem-slash-var-tmp"></a>

Although [`/tmp`](filesystem-slash-tmp.md) is a `tmpfs` file system, `/var/tmp` is a path on the root file system, and is the place for larger and longer-lived temporary files. A cleanup job removes files not recently accessed; to configure it, see the `tmpfiles.d(5)` and `systemd-tmpfiles(8)` man pages.

As with `/tmp`, prefer the `$TMPDIR` environment variable over the hardcoded path, use safe temporary file creation (see [Using `/tmp` and `/var/tmp` safely](https://systemd.io/TEMPORARY_DIRECTORIES/) on the systemd.io website), and set `PrivateTmp=` for `systemd` services.
