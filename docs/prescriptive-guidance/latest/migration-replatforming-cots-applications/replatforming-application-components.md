---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/replatforming-application-components.html
---

# Replatforming application components running on unsupported OSs
<a name="replatforming-application-components"></a>

The replatforming approach for application components that run on unsupported OSs is different for each application component. The following table summarizes the replatforming options available for application components that reached EOS.

|
|
| Application component | Solution for COTS applications | Solution for in-house applications |
| --- |--- |--- |
| **Application server** | Upgrade to the version recommended by the application's vendor. | Identify the most recent application server version. Build and validate it in a development environment before you upgrade. |
| **OS** | Upgrade to the version recommended by the application's vendor. | Identify the most recent OS version. Build and validate it in a development environment before you upgrade. |
| **Runtime libraries** | Upgrade to the version recommended by the application's vendor. | Upgrade and validate against the latest version. |
| **Other application components** | Request new application binaries from the application's vendor. | Build with the most recent OS, runtime, and application server versions. |

The following sections provide more information about replatforming approaches for your application components.

## Replacing unsupported OSs or application servers
<a name="replace-unsupported-oss"></a>

If you replace unsupported application servers (for example, Apache Tomcat 6.0, Apache 2.2, or IIS 7.x), your new application server versions might require an underlying OS upgrade. Most unsupported OSs are Red Hat Enterprise Linux (RHEL) versions 5 and 6, CentOS versions 5 and 6, or Windows 2008 R2. You should deploy the following steps for applications running those OSs:

1. Launch an EC2 instance with the required OS version.

1. Install the required application server version.

1. There are two separate approaches for in-house and COTS applications:
   + **In-house applications** – Redeploy the application to the EC2 instance.
   + **COTS applications – **Contact the application's vendor and request application binaries that are certified for the required OS or application server versions.**                                **

## Upgrading the OS for COTS applications
<a name="upgrading-os-cots-applications"></a>

Most COTS application vendors support Windows 2016 or RHEL 7. If your legacy COTS application doesn't support Windows 2016, we recommend an in-place upgrade from Windows 2008 R2 to Windows 2012 R2 by using the [in-place upgrade option provided by Microsoft](https://docs.microsoft.com/en-us/windows-server/upgrade/upgrade-2008r2-to-2012r2). You can also use [AWS Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to automatically upgrade Windows Server running on EC2 instances. We recommend that you contact the application's vendor and ask them to certify their software for the latest OS version.

## Upgrading the OS for in-house applications
<a name="upgrading-os-inhouse-applications"></a>

We recommend that you compile and rebuild your in-house application's software by using the most recent OS and software runtime versions (for example, Java, C\+\+, .NET, or Python). You can then clone the existing application environment, manually deploy and validate the functionality, and update your build environment to the most recent OS, runtime software components, and libraries before upgrading to your production environment.

## Replatforming application libraries and dependent software
<a name="replatforming-application-librairies"></a>

The approach for replatforming application libraries and dependent software is similar to the approach for OSs but you only upgrade the libraries. You then test the application's functionality and replicate the required libraries in your pre-production and production servers. Typically, the COTS application's vendor handles the required updates for application components through their ongoing software releases.
