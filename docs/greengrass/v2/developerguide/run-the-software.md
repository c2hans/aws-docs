---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/run-the-software.html
---

# (Optional) Run the Greengrass software (Linux)
<a name="run-the-software"></a>

**Note**
These steps do not apply to nucleus lite.

If you installed the software as a system service, the installer runs the software for you. Otherwise, you must run the software. To see if the installer set up the software as a system service, look for the following line in the installer output.

```
Successfully set up Nucleus as a system service
```

If you don't see this message, do the following to run the software:

1. Run the following command to run the software.

   ```
   sudo {{/greengrass/v2}}/alts/current/distro/bin/loader
   ```

   The software prints the following message if it launches successfully.

   ```
   Launched Nucleus successfully.
   ```

1. You must leave the current command shell open to keep the AWS IoT Greengrass Core software running. If you use SSH to connect to the core device, run the following command on your development computer to open a second SSH session that you can use to run additional commands on the core device. Replace {{username}} with the name of the user to sign in, and replace {{pi-ip-address}} with the IP address of the device.

   ```
   ssh {{username}}@{{pi-ip-address}}
   ```

For more information about how to interact with the Greengrass system service, see [Configure the Greengrass nucleus as a system service](configure-greengrass-core-v2.md#configure-system-service).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
