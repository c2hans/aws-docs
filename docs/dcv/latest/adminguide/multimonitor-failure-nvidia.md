---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/multimonitor-failure-nvidia.html
---

# Multimonitor/full screen failure with NVIDIA GPUs on Windows
<a name="multimonitor-failure-nvidia"></a>

DCV full screen/multimonitor feature may fail in cases where a Windows server host has an NVIDIA GPU. When this happens, the display will refuse to enter full screen mode or the server will fail to configure a display layout with multiple remote monitors.

The cause for this issue is a failure on the integration with the NVIDIA driver.

It can be identified by looking at the `C:\ProgramData\NICE\dcv\log\` on the server host, it will report the error:

`WARN display - Cannot change display layout`

This will display multiple times (20 - 30) before displaying:

`EDID not set on output x gpu x after attempt x INFO DLMNVAPI:display - Unable to set EDID on output x, gpu x: NVAPI_ERROR (-1)`

When the issue is reproduced, the host is unhealthy: the server will not be able to consistently configure a multimonitor layout, and there is no working way to fix the issue persistently (only few temporary mitigations).

The trigger of the issue is a server OS reboot performed while multimonitor is in use, i.e. when virtual monitors are present on the server host when the host is shut down. So to avoid the issue, it is required to remove all monitors on the server side before shutting down the server. The following command (executed with admin rights) can be used to ensure this:

```
C:\Program Files\NICE\DCV\Server\bin\dcvnvedid.exe --remove
```

Possible mitigation is to reinstall or update the Nvidia driver and reboot the host.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
