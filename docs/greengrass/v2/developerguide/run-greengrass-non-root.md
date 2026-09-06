---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/run-greengrass-non-root.html
---

# Run AWS IoT Greengrass V2 as a non-root user
<a name="run-greengrass-non-root"></a>

Typically, the root user installs and runs the AWS IoT Greengrass Core software on Linux devices. To increase device security, you can set up a non-root user to run the AWS IoT Greengrass Core software instead. This section provides guidance on setting up non-root configurations.

Choose from the following topics based on your needs:
+ **Set up AWS IoT Greengrass V2 core devices as non-root**

  If you are setting up new AWS IoT Greengrass V2 core devices and want to run them as a non-root user from the start, see [Set up AWS IoT Greengrass V2 core devices as non-root](setup-greengrass-non-root.md). This guide covers multiple solutions based on your device constraints and security requirements.
+ **Migrate AWS IoT Greengrass V2 core devices to non-root**

  If you have existing AWS IoT Greengrass core devices running as root and want to migrate them to a non-root configuration, see [Migrate AWS IoT Greengrass V2 core devices to non-root](migrate-to-nonroot.md).

**Note**
The non-root configurations in this section apply to Linux devices only. On Windows, AWS IoT Greengrass must run as a system service.

**Topics**
+ [Set up AWS IoT Greengrass V2 core devices as non-root](setup-greengrass-non-root.md)
+ [Migrate AWS IoT Greengrass V2 core devices to non-root](migrate-to-nonroot.md)
