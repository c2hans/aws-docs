---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-host-config-cinema4d.html
---

# Install Cinema 4D with Red Giant on Deadline Cloud Windows workers
<a name="examples-host-config-cinema4d"></a>

The [cinema4d\_redgiant](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant) host configuration script installs Cinema 4D with Red Giant plugins on Windows GPU service-managed fleet workers. The script fetches the installers from Amazon S3 and runs each one in silent mode on each worker launch.

**Important**
This script adds about 5-10 minutes to worker launch time, depending on instance size. Plan accordingly for fleet scaling and job scheduling.

To use this script, you need:
+ A Maxon account to download the Red Giant and Maxon App installers.
+ The Microsoft Edge WebView2 Runtime installer (required by the Maxon App installation).
+ An Amazon S3 bucket where you upload the installers, and IAM permissions for the fleet to read them.
+ A Windows GPU service-managed fleet with the latest GPU driver.
+ Red Giant licenses, available on SMF and CMF through a license endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
