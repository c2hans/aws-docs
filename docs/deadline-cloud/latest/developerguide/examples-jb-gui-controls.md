---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-gui-controls.html
---

# Use every Open Job Description GUI control on Deadline Cloud
<a name="examples-jb-gui-controls"></a>

The [gui\_control\_showcase](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gui_control_showcase) job bundle shows every GUI control supported by user interface metadata on [Open Job Description job parameters](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#2-jobparameterdefinition). Use it as a reference when you add GUI controls to your own job templates.

Open the GUI submitter to see every control:

```
deadline bundle gui-submit job_bundles/gui_control_showcase
```

![The job-specific settings tab for the gui_control_showcase bundle, showing generated controls grouped by type.](http://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/gui-control-showcase.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
