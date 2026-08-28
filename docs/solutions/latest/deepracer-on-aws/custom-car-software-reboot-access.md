---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-software-reboot-access.html
---

# Reboot and access the console
<a name="custom-car-software-reboot-access"></a>

1. Reboot the Raspberry Pi:

   ```
   sudo reboot
   ```

1. After the reboot, open `https://deepracer.local` in a browser, or navigate to the Raspberry Pi’s IP address. Accept the self-signed certificate warning.

1. Log in with the default password: `deepracer`.

**Change the default password**
Change the default `deepracer` password immediately after your first login.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
