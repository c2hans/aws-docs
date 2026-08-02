---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/migration-at-a-glance.html
---

# Migrating a full configuration
<a name="migration-at-a-glance"></a>

In this approach, you take a configuration from an existing system and migrate it to a new system. This process will copy an existing configuration, IP addresses, certificates, keys, pass phrases, and sign-in credentials.

The primary reason for migrating an entire configuration is for a like-for-like system replacement, such as a hardware upgrade or an RMA. Typically, these concepts do not apply to the AWS Cloud.

You can use UCS or SCF files to migrate a full configuration, and the following tables provide an overview of the advantages and disadvantages of using them.

## Use a UCS or qkview file
<a name="use-a-ucs-or-qkview-file.52a1adc9-5d07-570d-b7ae-58a56272da93"></a>

|
|
| Advantages | Disadvantages |
| --- |--- |
| All files are moved as a single archive. | The primary use case for using a UCS file would be to replace a failed device. The archive contains device-specific information that might make the F5 BIG-IP workload unreachable. |
| Local user accounts are preserved. If they are integrated with your active directory, then the configuration is preserved. | If you have configured a directory integration, you might have access issues. If you do not have access to the user passwords, you might also have access issues. |
| All virtual server configurations are preserved. | You might have to edit the IP addresses of the device, virtual servers, and pool members. |
| The file structure is preserved. | You must know which files to edit. |
| This process is more complex than an SCF or object-by-object move. |
| Increased error risk, including a redeployment or potential for the configuration to fail to load. |
| Designed for entire system replacement workflows. |

## Use an SCF file
<a name="use-an-scf-file.47a57a29-f473-51ba-aab5-d86e87c9c80f"></a>

|
|
| Advantages | Disadvantages |
| --- |--- |
| Creates a text file of the configuration. | Edits will be required because there will be device-specific properties in the file that can impact access if the file is simply loaded. |
| Easily editable in any Unix or Linux text editor. | You must understand the configuration and file structure to make the edits. |
| The configuration file has the correct order of load operations. | You must know which parts of the file to remove to prevent one from overwriting device-specific configurations. |
| You can easily find objects that are to be migrated. |
