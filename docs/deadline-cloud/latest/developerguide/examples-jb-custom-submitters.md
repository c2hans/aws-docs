---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-custom-submitters.html
---

# Build a custom submitter for Deadline Cloud
<a name="examples-jb-custom-submitters"></a>

The [custom\_submitters](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters) directory holds reference submitters that go beyond what bundle editing and the integrated submitters support. Use these as starting points when your team needs UI controls, custom handlers, or fleet attributes that the integrated submitter doesn't expose:
+ [fuzzypixel\_maya](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters/fuzzypixel_maya) — The Maya custom submitter the AWS FuzzyPixel team developed for production. The submitter consolidates render settings into a single tab, exposes a QTree widget for activating individual render layers and overriding their resolution and frame range, surfaces custom fleet attributes (for example, `spot` or `onDemand`) as user-selectable options, and runs custom handlers that update `template.yaml` after the user clicks Submit.

Custom submitters can co-exist with the integrated submitter, but they don't receive updates or patches that ship with the integrated submitter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
