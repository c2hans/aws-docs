---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/create-session-scripts.html
---

# Creating Session Scripts
<a name="create-session-scripts"></a>

WorkSpaces Applications provides on-instance session scripts on both Windows- and Linux-based streaming instances. For more information about session scripts, see [Use Session Scripts to Manage Your Amazon WorkSpaces Applications Users' Streaming Experience](use-session-scripts.md).

Session scripts are specified within an WorkSpaces Applications image. To locate the session scripts configuration file on a Linux instance, navigate to `/opt/appstream/SessionScripts/config.json`. The following code is a sample `config.json` file that specifies a session start script named “`test-session-start`” and a session end script named “`test-session-stop`” together with their runtime parameters. Make sure that the scripts referenced in `config.json` have run permissions and a command interpreter is defined (for example, \#\!/bin/bash).

```
{
     "SessionStart": {
          "Executables": [
               {
                    "Context": "system",
                    "Filename": "/opt/appstream/SessionScripts/test-session-start",
                    "Arguments": "arg1",
                    "S3LogEnabled": true
               }
          ],
          "WaitingTime": 30
     },
     "SessionTermination": {
          "Executables": [
               {
                    "Context": "system",
                    "Filename": "/opt/appstream/SessionScripts/test-session-stop",
                    "Arguments": "arg2",
                    "S3LogEnabled": true
               }
          ],
          "WaitingTime": 30
     }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
