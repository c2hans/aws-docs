---
source_url: https://docs.aws.amazon.com/elemental-live/latest/installguide/install-lv-ig-install-ks.html
---

# Step B: Install (kickstart) the operating system software
<a name="install-lv-ig-install-ks"></a>

Install the operating system on the node. This action is known as *kickstarting* the system.

**To kickstart the system**

1. Insert the USB thumb drive into the hardware unit.

1. Restart the system using the following command.

   ```
   [elemental@hostname ~]$ sudo reboot
   ```

1. Use the arrow keys to select each option and complete the field, using the instructions in the following table as a guide.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/installguide/install-lv-ig-install-ks.html)

   The operating system is installed.

1. At the `Press return to quit` prompt, press **Enter** to reboot the system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
