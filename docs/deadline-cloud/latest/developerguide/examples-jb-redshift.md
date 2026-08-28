---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-redshift.html
---

# Render Redshift scenes on Deadline Cloud
<a name="examples-jb-redshift"></a>

The [redshift-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/redshift-2025) job bundle renders Redshift scenes using the standalone `redshiftCmdLine.exe` renderer that ships with Cinema 4D 2025. The bundle is designed for Windows systems. Cinema 4D is used because it is available in the `deadline-cloud` conda channel and includes the Redshift CLI renderer.

The bundle installs Cinema 4D 2025 through the `cinema4d=2025` conda package, configures Windows host requirements, and uses `redshiftCmdLine.exe` directly for rendering. The executable is located at `%CONDA_PREFIX%\cinema4d\RedshiftData\bin\redshiftCmdLine.exe`, which resolves automatically when the Cinema 4D conda package is installed.

To run this bundle, you need:
+ A Windows operating system
+ A Redshift compatible GPU
+ The `cinema4d=2025` conda package
+ A valid Redshift scene file (`.rs`)

You can create a `.rs` file in Cinema 4D with Redshift materials and lighting, then export the scene as a Redshift scene file.

Submit the bundle:

```
deadline bundle gui-submit redshift-2025
```

A Deadline Cloud Windows GPU service-managed fleet works with no further configuration. Make sure that the queue has access to the `cinema4d=2025` conda package and Redshift licensing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
