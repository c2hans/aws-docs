---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-host-config-page-file.html
---

# Configure the Windows page file on Deadline Cloud workers
<a name="examples-host-config-page-file"></a>

The [worker\_configuration/windows/configure\_page\_file.ps1](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/worker_configuration/windows/configure_page_file.ps1) script configures the Windows page file size and placement on Deadline Cloud workers. It prefers local NVMe instance storage when available for the best performance.

The page file sizing logic works as follows:
+ For NVMe drives, the script uses the smaller of 2× RAM or 75% of NVMe space by default.
+ If NVMe isn't available, the script uses the largest non-boot drive with 2× RAM.
+ If no non-boot drives are available, the script falls back to the boot drive (C:).

The script automatically detects EC2 NVMe instance storage, disables automatic page file management, formats the drive and assigns a drive letter if needed, then reboots the worker to apply changes. A marker file at `C:\deadline-pagefile-configured` prevents reconfiguration on subsequent worker starts. Adjust the `$RAM_MULTIPLIER`, `$NVME_SPACE_PERCENTAGE`, and `$MIN_DISK_SIZE_GB` variables at the top of the script to match your workload.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
