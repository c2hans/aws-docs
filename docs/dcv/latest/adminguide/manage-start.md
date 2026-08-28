---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html
---

# Starting the Amazon DCV Server
<a name="manage-start"></a>

The Amazon DCV server must be running to host sessions.

By default, the Amazon DCV server starts whenever the server that it's hosted on starts up. If you chose to disable automatic startup when you installed the Amazon DCV server, you must start the server manually or set up automatic startup again. To do either option, follow one of these procedures.

------
#### [ Windows Amazon DCV server ]

Manually start the Amazon DCV server using the Services snap-in for the Microsoft Management Console.

**To start the Amazon DCV server on Windows**

1. Open the Services snap-in for the Microsoft Management Console.

1. In the right pane, open **DCV Server**.

1. Choose **Start**.

**Note**
If the server is already up and running, the **Start** button is disabled.

Configure automatic startup using the Services snap-in for the Microsoft Management Console.

**To configure the Amazon DCV server to start automatically on Windows**

1. Open the Services snap-in for the Microsoft Management Console.

1. In the right pane, open **DCV Server**.

1. For **Startup service**, choose **Automatic**.

------
#### [ Linux Amazon DCV server ]

Manually start the Amazon DCV server using the command line.

**To start the Amazon DCV server on Linux**
Use the following commands:
+ RHEL, CentOS, SUSE Linux Enterprise 12, and Ubuntu 18.x

  ```
  $ sudo systemctl start dcvserver
  ```

Configure the Amazon DCV server to start automatically using the command line.

**To configure the Amazon DCV server to start automatically on Linux**
Use the following commands:
+ RHEL, CentOS, SUSE Linux Enterprise 12, and Ubuntu 18.x

  ```
  $ sudo systemctl enable dcvserver
  ```

------
#### [ macOS Amazon DCV server ]

Manually start the Amazon DCV server using the command line.

**To start the Amazon DCV server on macOS**
Use the following commands:
+

  ```
  $ sudo launchctl start com.amazon.dcv.server.dcvserver
  ```

Configure the Amazon DCV server to start automatically using the command line.

**To configure the Amazon DCV server to start automatically on macOS**
Use the following commands:
+

  ```
  $ sudo launchctl enable system/com.amazon.dcv.server.dcvserver
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
