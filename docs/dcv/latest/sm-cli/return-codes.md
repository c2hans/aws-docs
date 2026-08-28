---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/return-codes.html
---

# Using return codes
<a name="return-codes"></a>

A return code is usually, but not always, a hidden code sent after running a Amazon DCV Session Manager CLI command describing its status.

To view these return codes, you can use the `echo` command. This displays the code sent from the last Session Manager CLI command. YOu can use these codes to determine if a command was successful or not and why a command may have an error.

In addition to the return codes, you can view more details about a failure by running your commands with `--debug`. This produces a detailed report of the steps the Session Manager CLI uses to process the command and the result of each step.

To determine the return code of a DCV SM CLI command, run one of the following commands immediately after running the CLI command.
+ Linux and macOS

  ```
  $  echo $?
  0
  ```
+ Windows PowerShell

  ```
  $  echo $lastexitcode
  0
  ```
+ Windows command prompt

  ```
  $  echo %errorlevel%
  0
  ```

The following return codes appear at the end of execution of a CLI command:
+ `0` The command was successful. There were no errors thrown by either the CLI or by the service that the request was made to.
+ `1` The configuration file parsed to the CLI was not found or might be corrupt.
+ `2` The command entered on the command line failed to be parsed. Parsing failures can be caused by, but are not limited to, missing any required subcommands or arguments or using any unknown commands or arguments. Note that this return code meaning is applicable to all CLI commands.
+ `130` The process received a SIGINT (Ctrl-C).
+ `252` Command syntax was invalid, an unknown parameter was provided, or a parameter value was incorrect and prevented the command from running.
+ `253` The system environment or configuration was invalid. While the command provided may be syntactically valid, missing configuration or credentials prevented the command from running.
+ `254` The command was successfully parsed and a request was made to the specified service but the service returned an error. This will generally indicate incorrect API usage or other service specific issues.
+ `255` General catch-all error. The command may have parsed correctly but an unspecified runtime error occurred when running the command. Because this is a general error code, an error may change from 255 to a more specific return code. A return code of 255 shouldn't be relied on to determine a specific error case.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
