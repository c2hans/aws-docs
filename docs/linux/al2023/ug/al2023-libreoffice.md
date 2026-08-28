---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/al2023-libreoffice.html
---

# Tutorial: Install LibreOffice on AL2023
<a name="al2023-libreoffice"></a>

LibreOffice is a free, open-source office productivity suite that includes applications for word processing, spreadsheets, presentations, diagrams, databases, and formula editing. You can install LibreOffice on Amazon Linux 2023 (AL2023) instances to provide users with a full-featured desktop office suite.

LibreOffice is officially tested and supported on AL2023 by The Document Foundation. For more information, see [LibreOffice 64-bit progress, and support for Amazon Linux 2023](https://blog.documentfoundation.org/blog/2025/10/09/libreoffice-64-bit-progress-and-support-for-amazon-linux-2023/).

**Topics**
+ [Prerequisites](#al2023-libreoffice-prerequisites)
+ [Step 1: Determine your system architecture](#al2023-libreoffice-architecture)
+ [Step 2: Download the LibreOffice RPM package](#al2023-libreoffice-download)
+ [Step 3: Extract the archive](#al2023-libreoffice-extract)
+ [Step 4: Install the RPM packages](#al2023-libreoffice-install)
+ [Step 5: Verify the installation](#al2023-libreoffice-verify)
+ [Launching LibreOffice](#al2023-libreoffice-launching)
+ [Troubleshooting](#al2023-libreoffice-troubleshooting)

## Prerequisites
<a name="al2023-libreoffice-prerequisites"></a>
+ An Amazon EC2 instance running AL2023 with GNOME graphical desktop environment configured and accessible through a remote desktop protocol (for example, Amazon DCV). For more information, see the following:
  + [Tutorial: Install the GNOME desktop environment on AL2023](installing-gnome-al2023.md)
  + [Setting up the Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up.html)
+ `sudo` or root access on the instance.
+ At least 1.5 GB of free disk space for the installation.
+ An active internet connection to download the LibreOffice package, or the package pre-downloaded and transferred to the instance.

## Step 1: Determine your system architecture
<a name="al2023-libreoffice-architecture"></a>

Run the following command to identify your processor architecture. This determines which RPM package to download.

```
uname -p
```

The output is one of the following:

| Output | Architecture | RPM package type |
| --- | --- | --- |
| `x86_64` | 64-bit Intel/AMD | `Linux_x86-64_rpm` |
| `aarch64` | 64-bit ARM (Graviton) | `Linux_aarch64_rpm` |

## Step 2: Download the LibreOffice RPM package
<a name="al2023-libreoffice-download"></a>

**To download the LibreOffice RPM package**

1. Open the [LibreOffice download page](https://www.libreoffice.org/download/download-libreoffice/).

1. Select **Linux (64-bit) (rpm)** as the operating system.

1. Choose the version appropriate for your architecture (x86\_64 or aarch64).

1. Download the `.tar.gz` archive to your instance. You can use `wget` or `curl` to download directly from the terminal.

   ```
   cd ~/Downloads
   wget https://download.documentfoundation.org/libreoffice/stable/{{VERSION}}/rpm/{{ARCHITECTURE}}/LibreOffice_{{VERSION}}_Linux_{{ARCHITECTURE}}_rpm.tar.gz
   ```

   Replace {{VERSION}} and {{ARCHITECTURE}} with the version number and architecture you want to install (for example, 25.2.5 and x86\_64).
**Note**
To find the latest stable version number, visit the [LibreOffice download page](https://www.libreoffice.org/download/download-libreoffice/).

## Step 3: Extract the archive
<a name="al2023-libreoffice-extract"></a>

Navigate to the directory where you downloaded the archive and extract it.

```
cd ~/Downloads
tar zxvf LibreOffice_{{VERSION}}_Linux_{{ARCHITECTURE}}_rpm.tar.gz
```

This creates a directory with a name similar to `LibreOffice_{{VERSION}}_Linux_{{ARCHITECTURE}}_rpm/`.

## Step 4: Install the RPM packages
<a name="al2023-libreoffice-install"></a>

**To install the RPM packages**

1. Change to the `RPMS/` subdirectory inside the extracted folder.

   ```
   cd LibreOffice_{{VERSION}}_Linux_{{ARCHITECTURE}}_rpm/RPMS/
   ```

1. Install all RPM packages using `sudo rpm`.

   ```
   sudo rpm -i *.rpm
   ```

   Alternatively, you can use `dnf` for dependency resolution:

   ```
   sudo dnf install -y *.rpm
   ```

## Step 5: Verify the installation
<a name="al2023-libreoffice-verify"></a>

Confirm that LibreOffice was installed successfully by checking the version.

```
libreoffice --version
```

Expected output:

```
LibreOffice {{VERSION}} ...
```

## Launching LibreOffice
<a name="al2023-libreoffice-launching"></a>

**From the terminal**
Run the following command:

```
libreoffice
```

If the `libreoffice` command is not available, the binary may be versioned. You can launch it using the versioned name instead:

```
libreoffice{{MAJOR_VERSION}}
```

For example, `libreoffice25.2`.

To launch a specific application directly:

```
libreoffice --writer    # Word processor
libreoffice --calc      # Spreadsheet
libreoffice --impress   # Presentations
libreoffice --draw      # Diagrams
libreoffice --base      # Database
libreoffice --math      # Formula editor
```

**From the GNOME desktop**
After installation, LibreOffice applications appear in the GNOME Activities menu. Choose **Activities** in the top-left corner, search for "LibreOffice", and select the desired application.

## Troubleshooting
<a name="al2023-libreoffice-troubleshooting"></a>

The following section can help you troubleshoot common issues when installing or running LibreOffice on AL2023.

### Java Runtime Environment warning
<a name="al2023-libreoffice-ts-java"></a>

Some LibreOffice features (such as Base and certain extensions) require a Java Runtime Environment (JRE). If you see a warning about missing Java, install it:

```
sudo dnf install -y java-17-amazon-corretto-headless
```

Then, in LibreOffice, go to **Tools** > **Options** > **LibreOffice** > **Advanced** and verify that the JRE is detected.

### LibreOffice command not found
<a name="al2023-libreoffice-ts-notfound"></a>

If the `libreoffice` command is not found after installation, the binary may be versioned. Try running:

```
libreoffice{{MAJOR_VERSION}}
```

For example, `libreoffice25.2`. You can also locate the binary:

```
find /opt -name "soffice" 2>/dev/null
```

### Additional resources
<a name="al2023-libreoffice-ts-resources"></a>

If you encounter other issues, refer to the official LibreOffice installation documentation for Linux:
+ [LibreOffice Linux Installation Guide](https://wiki.documentfoundation.org/Documentation/Install/Linux)
+ [LibreOffice Download Page](https://www.libreoffice.org/download/download-libreoffice/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
