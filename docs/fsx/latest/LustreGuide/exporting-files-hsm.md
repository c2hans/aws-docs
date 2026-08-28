---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/exporting-files-hsm.html
---

# Exporting files using HSM commands
<a name="exporting-files-hsm"></a>

**Note**
To export changes in your FSx for Lustre file system's data and metadata to a durable data repository on Amazon S3, use the automatic export feature described in [Automatically export updates to your S3 bucket](autoexport-data-repo-dra.md). You can also use export data repository tasks, described in [Using data repository tasks to export changes](export-data-repo-task-dra.md).

To export an individual file to your data repository and verify that the file has successfully been exported to your data repository, you can run the commands shown following. A return value of `states: (0x00000009) exists archived` indicates that the file has successfully been exported.

```
sudo lfs hsm_archive {{path/to/export/file}}
sudo lfs hsm_state {{path/to/export/file}}
```

**Note**
You must run the HSM commands (such as `hsm_archive`) as the root user or using `sudo`.

To export your entire file system or an entire directory in your file system, run the following commands. If you export multiple files simultaneously, Amazon FSx for Lustre exports your files to your Amazon S3 data repository in parallel.

```
nohup find {{local/directory}} -type f -print0 | xargs -0 -n 1 sudo lfs hsm_archive &
```

To determine whether the export has completed, run the following command.

```
find {{path/to/export/file}} -type f -print0 | xargs -0 -n 1 -P 8 sudo lfs hsm_state | awk '!/\<archived\>/ || /\<dirty\>/' | wc -l
```

If the command returns with zero files remaining, the export is complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
