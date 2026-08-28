---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-conda-autodock-vina.html
---

# Build an AutoDock Vina conda package for Deadline Cloud
<a name="examples-conda-autodock-vina"></a>

The [autodock-vina-1.2.5](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/autodock-vina-1.2.5) rattler-build recipe packages [AutoDock Vina](https://github.com/ccsb-scripps/AutoDock-Vina), an open-source molecular docking program that predicts how small molecules (drug candidates) bind to a protein target. The package downloads the pre-built Linux x86\_64 binary from the GitHub release and installs it as the `vina` command.

Submit the build from the `conda_recipes` directory:

```
./submit-package-job autodock-vina-1.2.5
```

For a job bundle that uses this package to run parallel virtual screening campaigns, see [Run virtual screening with AutoDock Vina on Deadline Cloud](examples-jb-virtual-screening.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
