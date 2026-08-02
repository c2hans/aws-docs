---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Windows.html
---

# Windows operating systems supported by Elastic Disaster Recovery
<a name="Supported-Operating-Systems-Windows"></a>

AWS Elastic Disaster Recovery allows replication of physical, virtual or cloud-based source servers to the AWS Cloud for several versions of Windows.

## General Notes
<a name="General-Notes"></a>

**Important**
**Windows 2003** is no longer supported.

[Review the AWS Replication Agent installation requirements.](installation-requirements.md)

**These Windows operating systems are supported:**

| Operating system | Supported versions | Prerequisites and Limitations |
| --- | --- | --- |
| Microsoft Windows Server 2025 64-bit |  | Requires .NET Framework version 4.5 or above.  |
| Microsoft Windows Server 2022 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows Server 2019 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows Server 2016 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows 10 64-bit |   | Ensure that the [auto sleep function in Windows 10](https://answers.microsoft.com/en-us/windows/forum/all/turn-off-auto-sleep-in-windows-10/79f2d86c-3378-495f-8da2-4d78021876d4) is disabled. Data replication may be interrupted if the feature is activated. |
| Microsoft Windows Server 2012 <br />**This version has reached end of life. We recommend that you update to a more recent version.** | 64-bit and R2 64-bit |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Windows.html)  |
| Microsoft Windows Server 2008 <br />**This version has reached end of life. We recommend that you update to a more recent version.** | 64-bit and R2 64-bit | [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Windows.html)  |
| Microsoft Windows 7 64-bit<br />**This version has reached end of life. We recommend that you update to a more recent version.** |  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Windows.html)  |
