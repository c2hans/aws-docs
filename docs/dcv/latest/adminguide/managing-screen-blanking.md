---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/managing-screen-blanking.html
---

# Managing screen blanking on Linux
<a name="managing-screen-blanking"></a>

For Console sessions on a Linux server, DCV blanks the local screen by default when at least one remote user is connected to the server, and restores the output (also locking the screen) upon disconnection of the last remote user.

This prevents user in the physical proximity of a server to see the screen and interact with the remote session using the input devices connected to the host. This may be undesirable for privacy reasons or local laws compliance when remotely working on console sessions. Local input is prevented by disabling the physically connected devices such as the keyboard and the mouse. Input devices are disabled as soon as they are plugged in or when found to be enabled. Analogously, input devices are enabled back when no remote user is connected, thus permitting local log in and interaction.

**Disabling screen blanking and input blocking**
Screen blanking can be disabled using the following procedure:

1. Navigate to `/etc/dcv/` and open the `dcv.conf` file with your preferred text editor.

1. Locate the `disable-local-console parameter` in the `[display/linux]` section. To permit locally connected displays to stay active and show the ongoing remote session, and permit interaction through locally connected devices set `disable-local-console=false`. The default value is `true` (i.e.: screen blanking and input blocking active). If there's no `disable-local-console` parameter in the `[display/linux]` section, add it manually using the following format:

   ```
    [display/linux]
    disable-local-console=false|true
   ```

1. Save and close the file.

1. [Stop](manage-stop.md) and [restart](manage-start.md) the Amazon DCV server.

**Preventing selected input devices from being disabled**
Specific devices can be set to remain enabled.

 Input devices whose name starts with `DCV ` (please pay attention to the space after the name) will never be disabled irrespective of the value of the `display-local-console` setting. To rename input devices, refer to this guide: [Enable Stylus](enable-stylus.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
