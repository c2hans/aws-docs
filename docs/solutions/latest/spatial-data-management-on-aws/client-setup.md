---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/client-setup.html
---

# Client setup
<a name="client-setup"></a>

This section describes how to set up and configure the client applications for accessing Spatial Data Management on AWS:
+  **Web portal** – Browser-based interface for resource management, asset creation and modification, and file upload and download. Convenient for one-off tasks. Uploads are limited to 5,000 files per asset, 50 GB total size, 20 GB per file, and 3 simultaneous operations.
+  **Command-Line Interface (CLI) and Python SDK** – Python package that provides both a CLI tool and a programmatic SDK for automation, scripting, and file operations.
+  **Desktop application** – Native application for Windows, macOS, and Linux with graphical interface for file upload and download. Recommended for routine or large-scale data operations.

## Prerequisites
<a name="client-setup-prerequisites"></a>

Before setting up any client application, ensure you have:
+ The Spatial Data Management on AWS solution deployed in an AWS account
  + Your IT Administrator may have already deployed this for you
+ User credentials for authentication:
  + Amazon Cognito username and password from your registration email or IT Administrator, or
  + Single Sign-On credentials if SSO is configured
+ Network access to your deployment
  + Contact your IT Administrator if you need custom domain access or VPN connection

## Web portal setup
<a name="web-portal-setup"></a>

The web portal requires no installation and can be accessed directly through a web browser.

### Access the web portal
<a name="access-web-portal"></a>

1. Obtain the portal URL from your IT Administrator or the person who deployed the solution.

1. Open the URL in a supported web browser (Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari).

1. Sign in with your Amazon Cognito credentials provided by your IT Administrator.

 **If you do not have the portal URL:**

You can retrieve it from the AWS CloudFormation console:

1. Sign in to the AWS Management Console and open the CloudFormation console

1. Locate the main stack for your Spatial Data Management deployment

1. In the **Resources** tab, find the nested stack with a logical ID starting with `PortalStack`

1. Choose the nested stack link

1. In the **Outputs** tab, copy the value for `PortalCloudFrontDistributionUrl`

Alternatively, if you have AWS CLI access:

```
# Replace <stack-name> with your CloudFormation stack name
aws cloudformation describe-stacks --stack-name $(aws cloudformation list-stack-resources --stack-name <stack-name> --query 'StackResourceSummaries[?starts_with(LogicalResourceId, `PortalStackNested`)].PhysicalResourceId' --output text) --query 'Stacks[0].Outputs[?OutputKey==`PortalCloudFrontDistributionUrl`].OutputValue' --output text
```

## Desktop application setup
<a name="desktop-client-setup"></a>

The desktop application provides a graphical interface for managing spatial data with enhanced performance for large file operations. The desktop application is a standalone installer and does not require the CLI to be installed.

### Download desktop application
<a name="download-desktop-application"></a>

Download the appropriate installer for your platform.
+  **Windows:**
  +  [SpatialDataPortal\_0.2.4\_x64-setup.exe](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/windows_v2/SpatialDataPortal_0.2.4_x64-setup.exe)
+  **macOS:**
  +  **Intel:** [Spatial Data Portal 0.2.4 x64.dmg](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/macos_v2/Spatial+Data+Portal+0.2.4+x64.dmg) – For Intel-based Macs
  +  **Apple Silicon (M1/M2/M3):** [Spatial Data Portal 0.2.4 aarch64.dmg](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/macos_v2/Spatial+Data+Portal+0.2.4+aarch64.dmg) – Optimized for Apple Silicon
+  **Linux:**
  +  **AppImage (Universal):** [spatial-data-portal\_0.2.4\_amd64.AppImage](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/ubuntu_v2/spatial-data-portal_0.2.4_amd64.AppImage) – No installation required, runs on any Linux distribution
  +  **DEB Package:** [spatial-data-portal\_0.2.4\_amd64.deb](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/ubuntu_v2/spatial-data-portal_0.2.4_amd64.deb) – For Ubuntu, Debian, and derivatives
  +  **RPM Package:** [spatial-data-portal-0.2.4-1.x86\_64.rpm](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/ubuntu_v2/spatial-data-portal-0.2.4-1.x86_64.rpm) – For Red Hat, Fedora, SUSE, and derivatives

### Installation instructions
<a name="installation-instructions"></a>

#### Windows installation
<a name="windows-installation"></a>

1. Double-click the downloaded `.exe` file.

1. Follow the installation wizard:
   + Accept the license agreement
   + Choose installation location (default: `C:\Program Files\SpatialDataManagement`)
   + Choose whether to create desktop shortcut
   + Choose **Install**

1. Launch the application from Start Menu or desktop shortcut.

 **Security note:** The application is digitally signed. If Windows SmartScreen shows a warning about an unrecognized app, do not proceed with the installation. Contact your IT Administrator to verify you have the official signed application.

#### macOS installation
<a name="macos-installation"></a>

 **Choose the correct version for your Mac:**
+  **Apple Silicon Macs** (M1, M2, M3): Download the `aarch64.dmg` version for best performance
+  **Intel Macs**: Download the `x64.dmg` version
+  **Not sure?** Go to Apple Menu, choose About This Mac, and check the "Chip" field

  1. Double-click the downloaded `.dmg` file.

  1. Drag the Spatial Data Management icon to the Applications folder.

  1. Open Applications folder and double-click Spatial Data Management.

  1. The application launches.

 **Security note:** The application is digitally signed. If macOS shows a security warning about an unidentified developer, do not proceed with the installation. Contact your IT Administrator to verify you have the official signed application.

#### Linux installation
<a name="linux-installation"></a>

 **Option 1: AppImage (Recommended for most users)**

1. Make executable and run:

   ```
   chmod +x spatial-data-portal_0.2.4_amd64.AppImage
   ./spatial-data-portal_0.2.4_amd64.AppImage
   ```

1. (Optional) Integrate with system:

   ```
   # Move to applications directory
   sudo mkdir -p /opt/spatial-data-management
   sudo mv spatial-data-portal_0.2.4_amd64.AppImage /opt/spatial-data-management/

   # Create desktop entry
   cat > ~/.local/share/applications/spatial-data-management.desktop <<EOF
   [Desktop Entry]
   Name=Spatial Data Management
   Exec=/opt/spatial-data-management/spatial-data-portal_0.2.4_amd64.AppImage
   Icon=spatial-data-management
   Type=Application
   Categories=Utility;
   EOF
   ```

 **Option 2: DEB Package (Ubuntu/Debian)**

```
sudo dpkg -i spatial-data-portal_0.2.4_amd64.deb
sudo apt-get install -f  # Fix any dependency issues if needed
```

 **Option 3: RPM Package (Red Hat/Fedora/SUSE)**

```
# Red Hat/CentOS
sudo rpm -i spatial-data-portal-0.2.4-1.x86_64.rpm

# Fedora (preferred method)
sudo dnf install spatial-data-portal-0.2.4-1.x86_64.rpm

# SUSE
sudo zypper install spatial-data-portal-0.2.4-1.x86_64.rpm
```

### Configure desktop application
<a name="configure-desktop-application"></a>

1. Launch the application.

1. Sign in with your Amazon Cognito credentials provided by your IT Administrator.

## CLI and Python SDK setup
<a name="cli-setup"></a>

The CLI and Python SDK are distributed as a single Python package that provides both a command-line tool and a programmatic SDK for full access to Spatial Data Management features, including file upload and download capabilities.

**Important**
The CLI/SDK can be installed independently for automation and scripting workflows.

### Prerequisites
<a name="cli-prerequisites"></a>
+ Python 3.8 or later
+ pip (Python package installer)

### Verify Python installation
<a name="verify-python-installation"></a>

```
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version
# or
pip3 --version
```

If Python is not installed, download from [python.org](https://www.python.org/downloads/).

### Install from wheel file
<a name="install-cli-from-wheel"></a>

#### Step 1: Obtain the wheel file
<a name="obtain-cli-wheel"></a>

Download the wheel file (`.whl`) from your IT Administrator or from the Amazon S3 location:

**Note**
Always download the latest available version for the most recent features and bug fixes. For information about all releases, see the [Release notes](release-notes.html).
+ Download [CLI wheel 0.1.8](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/cli_v2/amzn_spatial_data_mgmt-0.1.8-py3-none-any.whl)
+ Download [Checksum 0.1.8](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/artifacts/cli_v2/amzn_spatial_data_mgmt-0.1.8-py3-none-any.whl.sha256)

#### Step 2: Verify file integrity (recommended)
<a name="verify-file-integrity"></a>

Verify the downloaded file using the SHA256 checksum:

 **Windows (PowerShell):**

```
# Calculate SHA256 hash (replace <filename> with your downloaded file)
$hash = Get-FileHash -Algorithm SHA256 <filename>.whl

# Compare with expected hash
$expectedHash = Get-Content <filename>.whl.sha256

if ($hash.Hash -eq $expectedHash.Split()[0]) {
    Write-Host "Checksum verified successfully" -ForegroundColor Green
} else {
    Write-Host "Checksum verification failed" -ForegroundColor Red
}
```

 **macOS and Linux:**

```
# Verify checksum (replace <filename> with your downloaded file)
sha256sum -c <filename>.whl.sha256

# Expected output: <filename>.whl: OK
```

 **Important:** Do not proceed with installation if the checksum verification fails. Contact your IT Administrator for a valid file.

#### Step 3: Install the wheel file
<a name="install-cli-wheel"></a>

 **Windows:**

```
# Install CLI (replace <filename> with your downloaded file)
pip install <filename>.whl

# Verify installation
spatial-data-mgmt -h
```

 **macOS and Linux:**

```
# Install CLI (replace <filename> with your downloaded file)
pip3 install <filename>.whl

# Or install for current user only (if you do not have admin rights)
pip3 install --user <filename>.whl

# Verify installation
spatial-data-mgmt -h
```

### Update CLI/SDK
<a name="update-cli"></a>

To update to a newer version:

```
# Uninstall current version
pip uninstall amzn-spatial-data-mgmt

# Install new version (replace <filename> with your downloaded file)
pip install <filename>.whl

# Verify new version
spatial-data-mgmt -h
```

### Uninstall CLI/SDK
<a name="uninstall-cli"></a>

```
# Uninstall CLI
pip uninstall amzn-spatial-data-mgmt

# Remove configuration (optional)
rm -rf ~/.spatial-data-mgmt
```

## System requirements and browser compatibility
<a name="system-requirements"></a>

### Web portal browser requirements
<a name="web-portal-browser-requirements"></a>

 **Supported browsers:**
+ Google Chrome 90 or later (recommended)
+ Mozilla Firefox 88 or later
+ Microsoft Edge 90 or later
+ Safari 14 or later

 **Browser settings:**
+ JavaScript must be enabled
+ Cookies must be enabled for authentication
+ Local storage required for session management

### Desktop application system requirements
<a name="desktop-system-requirements"></a>

 **Windows:**
+ Windows 10 or later (64-bit)
+ 4 GB RAM minimum (8 GB recommended)
+ 500 MB available disk space

 **macOS:**
+ macOS 11 (Big Sur) or later
+ Apple Silicon or Intel processor
+ 4 GB RAM minimum (8 GB recommended)
+ 500 MB available disk space

 **Linux:**
+ Ubuntu 20.04 LTS or later
+ Debian 11 or later
+ Fedora 35 or later
+ 4 GB RAM minimum (8 GB recommended)
+ 500 MB available disk space

### CLI/SDK system requirements
<a name="cli-system-requirements"></a>
+ Python 3.8 or later
+ pip (Python package installer)
+ 100 MB available disk space

## Troubleshooting
<a name="troubleshooting"></a>

This section provides solutions to common issues you might encounter when setting up or using the client applications.

### Web portal issues
<a name="web-portal-issues"></a>

 **Issue: Cannot access portal URL**
+ Verify the URL is correct from your IT Administrator
+ If you have AWS CLI access, retrieve the portal URL from AWS CloudFormation:

  ```
  aws cloudformation describe-stacks --stack-name $(aws cloudformation list-stack-resources --stack-name <YOUR STACK> --query 'StackResourceSummaries[?starts_with(LogicalResourceId, `PortalStackNested`)].PhysicalResourceId' --output text) --query 'Stacks[0].Outputs[?OutputKey==`PortalCloudFrontDistributionUrl`].OutputValue' --output text
  ```
+ Check network connectivity and VPN if required
+ Verify Amazon CloudFront distribution is deployed
+ Try accessing from a different browser

 **Issue: Login fails**
+ Verify Amazon Cognito credentials are correct
+ Check if user account is enabled in Amazon Cognito User Pool
+ Verify user is assigned to appropriate group
+ Clear browser cache and cookies
+ Try incognito/private browsing mode

 **Issue: Portal loads but features do not work**
+ Verify JavaScript is enabled in browser
+ Check browser console for errors
+ Ensure cookies and local storage are enabled
+ Update browser to latest version

### Desktop application issues
<a name="desktop-application-issues"></a>

 **Issue: Application will not start**
+ Verify system requirements are met
+ Check antivirus is not blocking the application
+ Review application logs in:
  + Windows: `%USERPROFILE%\.spatial-data-mgmt\logs`
  + macOS: `~/.spatial-data-mgmt/logs`
  + Linux: `~/.spatial-data-mgmt/logs`

 **Issue: Cannot connect to API**
+ Verify API endpoint URL is correct
+ Check network connectivity
+ Verify VPN connection if required
+ Check firewall settings

 **Issue: File uploads fail**
+ Check available disk space
+ Verify network stability
+ Check file permissions
+ Review upload logs for specific errors
+ Try smaller files first to isolate issue

 **Issue: File downloads fail**
+ Check available disk space in download location
+ Verify network stability
+ Check write permissions for download directory
+ Review download logs for specific errors

### CLI/SDK issues
<a name="cli-issues"></a>

 **Issue: Access denied when downloading CLI version 0.1.1**
+ Version 0.1.1 may not be available for your account or region
+ Use version 0.1.0 instead, which is fully supported
+ Download version 0.1.0 using the links provided in the installation section
+ Contact your IT Administrator if you require access to version 0.1.1

 **Issue: Command not found after installation**
+ Verify installation: `pip list | grep spatial`
+ Check PATH includes Python scripts directory
+ On macOS/Linux with `--user` install, add `~/.local/bin` to PATH
+ Reinstall CLI if necessary

 **Issue: Authentication fails**
+ Verify API endpoint URL is correct in config file
+ Check Amazon Cognito credentials
+ Verify network connectivity
+ Check if user account is enabled
+ Verify config file format is correct YAML

 **Issue: SSL certificate errors**
+ Update CA certificates: `pip install --upgrade certifi`
+ Verify system time is correct
+ Check corporate proxy settings
+ Verify API endpoint URL uses HTTPS

 **Issue: Slow upload/download performance**
+ Adjust chunk size in config file
+ Increase concurrent transfers (max\_concurrent\_transfers)
+ Check network bandwidth
+ Verify no VPN bottlenecks
+ Test network speed to AWS Region

 **Issue: Python version conflicts**
+ Verify Python 3.8 or later is installed
+ Check pip is using correct Python version: `pip --version`
+ Ensure you are using `pip3` on macOS/Linux if multiple Python versions exist

## Getting help
<a name="getting-help"></a>

### Web portal
<a name="web-portal-help"></a>
+ In-app help: Choose the **?** icon in top navigation
+ User guide: Available in portal under **Help**, and then choose **Documentation**

### Desktop application
<a name="desktop-application-help"></a>
+ In-app help: **Help** → **Documentation**
+ Logs location:
  + Windows: `%USERPROFILE%\.spatial-data-mgmt\logs`
  + macOS: `~/.spatial-data-mgmt/logs`
  + Linux: `~/.spatial-data-mgmt/logs`

### CLI/SDK
<a name="cli-help"></a>
+ Command help: `spatial-data-mgmt --help`
+ Subcommand help: `spatial-data-mgmt <command> --help`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
