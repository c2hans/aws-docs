---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html
---

# Stopping the Amazon DCV Server
<a name="manage-stop"></a>

You can stop the Amazon DCV server at any time. Stopping the server terminates all active Amazon DCV sessions. You can't start new sessions until after the server is restarted.

------
#### [ Windows Amazon DCV server ]

Manually stop the Amazon DCV server using the Services snap-in for the Microsoft Management Console.

**To stop the Amazon DCV server on Windows**

1. Open the Services snap-in for the Microsoft Management Console.

1. In the right pane, open **DCV Server**.

1. Choose **Stop**.

**Note**
If the server is already stopped, the **Stop** button is disabled.

Disable automatic startup using the Services snap-in for the Microsoft Management Console.

**To prevent the Amazon DCV server from starting automatically on Windows**

1. Open the Services snap-in for the Microsoft Management Console.

1. In the right pane, open **DCV Server**.

1. For **Startup service**, choose **Manual**.

------
#### [ Linux Amazon DCV server ]

Stop the Amazon DCV server using the command line.

**To stop the Amazon DCV server on Linux**
Use the following command:

```
$ sudo systemctl stop dcvserver
```

Disable automatic Amazon DCV server startup using the command line.

**To prevent the Amazon DCV server from starting automatically on Linux**
Use the following command:

```
$ sudo systemctl disable dcvserver
```

------
#### [ macOS Amazon DCV server ]

Stop the Amazon DCV server using the command line.

**To stop the Amazon DCV server on macOS**
Use the following command:

```
$ sudo launchctl stop com.amazon.dcv.server.dcvserver
```

Disable automatic Amazon DCV server startup using the command line.

**To prevent the Amazon DCV server from starting automatically on macOS**
Use the following command:

```
$ sudo launchctl disable system/com.amazon.dcv.server.dcvserver
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
