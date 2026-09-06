---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/al2027-libreoffice.html
---

# Tutorial: Install LibreOffice on AL2027
<a name="al2027-libreoffice"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

LibreOffice is a free, open-source office productivity suite that includes applications for word processing, spreadsheets, presentations, diagrams, databases, and formula editing. You can install LibreOffice on Amazon Linux 2027 (AL2027) instances to provide users with a full-featured desktop office suite.

This tutorial takes approximately 15–20 minutes to complete.

**Note**
Completing this tutorial requires a running Amazon EC2 instance, which might result in charges to your AWS account for the instance, Amazon Elastic Block Store (Amazon EBS) storage, and associated resources. For pricing details, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/). To avoid ongoing charges, stop or terminate the instance when you are finished.

**Topics**
+ [Prerequisites](#al2027-libreoffice-prerequisites)
+ [Step 1: Determine your system architecture](#al2027-libreoffice-architecture)
+ [Step 2: Download the LibreOffice RPM package](#al2027-libreoffice-download)
+ [Step 3: Extract the archive](#al2027-libreoffice-extract)
+ [Step 4: Install the RPM packages](#al2027-libreoffice-install)
+ [Step 5: Verify the installation](#al2027-libreoffice-verify)
+ [Launching LibreOffice](#al2027-libreoffice-launching)
+ [Clean up](#al2027-libreoffice-cleanup)
+ [Troubleshooting](#al2027-libreoffice-troubleshooting)

## Prerequisites
<a name="al2027-libreoffice-prerequisites"></a>
+ An Amazon EC2 instance running AL2027 with a graphical desktop environment configured and accessible through a remote desktop protocol (for example, Amazon DCV). For more information, see the following:
  + [Tutorial: Install the GNOME desktop environment](installing-gnome.md)
  + [Setting up the Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up.html)
+ `sudo` or root access on the instance.
+ At least 1.5 GB of free disk space for the installation.
+ An active internet connection to download the LibreOffice package, or the package pre-downloaded and transferred to the instance.

## Step 1: Determine your system architecture
<a name="al2027-libreoffice-architecture"></a>

Run the following command to identify your processor architecture. This determines which RPM package to download.

```
uname -m
```

The output is one of the following:

| Output | Architecture | RPM package type |
| --- | --- | --- |
| `x86_64` | 64-bit Intel/AMD | `Linux_x86-64_rpm` |
| `aarch64` | 64-bit ARM (Graviton) | `Linux_aarch64_rpm` |

## Step 2: Download the LibreOffice RPM package
<a name="al2027-libreoffice-download"></a>

**To download the LibreOffice RPM package**

1. Open the [LibreOffice download page](https://www.libreoffice.org/download/download-libreoffice/).

1. Select **Linux (64-bit) (rpm)** as the operating system.

1. Choose the version appropriate for your architecture (x86\_64 or aarch64).

1. Download the `.tar.gz` archive to your instance. You can use `wget` or `curl` to download directly from the terminal.

   ```
   cd ~/Downloads
   curl -OL {{TAR_DOWNLOAD_URL}}
   ```

## Step 3: Extract the archive
<a name="al2027-libreoffice-extract"></a>

Navigate to the directory where you downloaded the archive and extract it.

```
cd ~/Downloads
tar -xf LibreOffice_{{VERSION}}_Linux_{{ARCHITECTURE}}_rpm.tar.gz
```

This creates a directory with a name similar to `LibreOffice_{{VERSION}}_Linux_{{ARCHITECTURE}}_rpm/`.

## Step 4: Install the RPM packages
<a name="al2027-libreoffice-install"></a>

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
<a name="al2027-libreoffice-verify"></a>

Confirm that LibreOffice was installed successfully by checking the version.

```
libreoffice --version
```

Expected output:

```
LibreOffice {{VERSION}} ...
```

## Launching LibreOffice
<a name="al2027-libreoffice-launching"></a>

**From the terminal**
Run the following command:

```
libreoffice
```

If the `libreoffice` command is not available, the binary may be versioned. You can launch it using the versioned name instead:

```
libreoffice{{MAJOR_VERSION}}
```

For example, `libreoffice26.8`.

To launch a specific application directly:

```
libreoffice --writer    # Word processor
libreoffice --calc      # Spreadsheet
libreoffice --impress   # Presentations
libreoffice --draw      # Diagrams
libreoffice --base      # Database
libreoffice --math      # Formula editor
```

**From the graphical desktop**
After installation, LibreOffice applications appear in the desktop applications menu. Open the applications menu, search for "LibreOffice", and select the desired application.

## Clean up
<a name="al2027-libreoffice-cleanup"></a>

To avoid incurring charges, uninstall LibreOffice by running the following command, or terminate the Amazon EC2 instance if it was created only for this tutorial.

```
sudo dnf remove libreoffice*
```

## Troubleshooting
<a name="al2027-libreoffice-troubleshooting"></a>

The following section can help you troubleshoot common issues when installing or running LibreOffice on AL2027.

### Java Runtime Environment warning
<a name="al2027-libreoffice-ts-java"></a>

Some LibreOffice features (such as Base and certain extensions) require a Java Runtime Environment (JRE). If you see a warning about missing Java, install it:

```
sudo dnf install -y java-25-amazon-corretto-headless
```

Then, in LibreOffice, go to **Tools** > **Options** > **LibreOffice** > **Advanced** and verify that the JRE is detected.

### LibreOffice command not found
<a name="al2027-libreoffice-ts-notfound"></a>

If the `libreoffice` command is not found after installation, the binary may be versioned. Try running:

```
libreoffice{{MAJOR_VERSION}}
```

For example, `libreoffice26.8`. You can also locate the binary:

```
find /opt -name "soffice" 2>/dev/null
```

### Additional resources
<a name="al2027-libreoffice-ts-resources"></a>

If you encounter other issues, refer to the official LibreOffice installation documentation for Linux:
+ [LibreOffice Linux Installation Guide](https://wiki.documentfoundation.org/Documentation/Install/Linux)
+ [LibreOffice Download Page](https://www.libreoffice.org/download/download-libreoffice/)

For more information on AL2027 graphical desktop, refer to our guides:
+ [AL2027 graphical desktop](graphical-desktop.md)
