---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/troubleshooting-logs.html
---

# Using the Log Files
<a name="troubleshooting-logs"></a>

Use the Amazon DCV client log files to identify and troubleshoot problems with your Amazon DCV client. Logs are enabled by default on Windows (since 2024.0), Linux and macOS clients. When using older Windows clients a log file must be provided (see [Enabling debug in log files](#debugging-log-files)).
+ Windows client

  ```
  %localappdata%\Amazon\DCV\logs\client.log
  ```
+ Linux or macOS client

  ```
  ~/.local/share/NICE/dcvviewer/log/viewer.log
  ```

## Enabling debug in log files
<a name="debugging-log-files"></a>

In order to troubleshoot issues, the Amazon DCV debug logs must be explicitly enabled.

**For Windows clients**

1. Navigate to the folder where the `dcvviewer.exe` file is located. By default, this is `C:\Program Files (x86)\NICE\DCV\Client\bin\`.

1. Do one of the following:
   + Open a command prompt and enter the following:

     ```
     dcvviewer --log-level debug --log-file-name C:/ProgramData/client.log
     ```
   + Add the following configuration to the connection file and double click on it to connect:

     ```
     [debug]
     logfilename=C:/ProgramData/client.log
     loglevel=debug
     ```

**Note**
To enable logging on Windows without changing the default log level, set the value to `info` instead of `debug`. Logs are stored in the specified local file on your machine.

**For macOS clients**

1. Open a terminal.

1. Navigate to the folder where the `dcvviewer` file is located. Usually it is located here: `/Applications/DCV\ Viewer.app/Contents/MacOS/dcvviewer`.

1. Enter the following to launch the Amazon DCV client:

   ```
   dcvviewer --log-level debug
   ```

When the client launches, the log files appear in the terminal.

**For Linux clients**

1. Open a terminal.

1. Enter the following to launch the Amazon DCV client:

   ```
   dcvviewer --log-level debug
   ```

When the client launches, the log files appear in the terminal.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
