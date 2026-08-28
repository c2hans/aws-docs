---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrio/build.html
---

This guide provides documentation for Wickr IO Integrations. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Build
<a name="build"></a>

Custom integrations in Wickr IO must be made available to the Wickr IO Docker container as a tarball named `software.tar.gz`. You can build that tarball from your source directory:

```
tar czf software.tar.gz —exclude=software.tar.gz .
```

Here's an example of what the output to this command will look like:

```
tar czf software.tar.gz —exclude=software.tar.gz .

tar: .: file changed as we read it
```

After you run this command, you will have the `software.tar.gz` file containing your source code and dependencies for your bot. Upload it to the server where you want to deploy your bot integration to continue on with the next deployment step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
