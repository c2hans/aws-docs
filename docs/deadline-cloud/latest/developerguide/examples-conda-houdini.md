---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-conda-houdini.html
---

# Build a SideFX Houdini conda package for Deadline Cloud
<a name="examples-conda-houdini"></a>

The samples repository on the GitHub website includes the following Houdini conda recipes:
+ [houdini-20.5](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-20.5)
+ [houdini-21.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-21.0)
+ [houdini-22.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-22.0): Houdini 22.0 builds are compiled with GCC 14.2, so download the `gcc14.2` source archive from SideFX rather than the archive that earlier versions use.
+ [houdini-redshift-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2025) and [houdini-redshift-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2026): Redshift renderer for Houdini.
+ [houdini-vray-7](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-vray-7): V-Ray 7 renderer for Houdini.

The [Render USD scenes with Houdini Husk on Deadline Cloud](examples-jb-houdini-husk-usd.md) job bundle uses these recipes to render USD scenes with Karma, V-Ray, and Redshift Hydra render delegates.

Submit the build:

```
./submit-package-job houdini-21.0
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
