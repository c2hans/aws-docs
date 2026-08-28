---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-background-tasks.html
---

# Background tasks in build environments
<a name="build-env-ref-background-tasks"></a>

You can run background tasks in build environments. To do this, in your buildspec, use the `nohup` command to run a command as a task in the background, even if the build process exits the shell. Use the **disown** command to forcibly stop a running background task.

**Examples:**
+ Start a background process and wait for it to complete later:

  ```
  |
  nohup sleep 30 & echo $! > pidfile
  …
  wait $(cat pidfile)
  ```
+  Start a background process and do not wait for it to ever complete:

  ```
  |
  nohup sleep 30 & disown $!
  ```
+  Start a background process and kill it later:

  ```
  |
  nohup sleep 30 & echo $! > pidfile
  …
  kill $(cat pidfile)
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
