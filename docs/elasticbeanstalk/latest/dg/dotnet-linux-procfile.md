---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-procfile.html
---

# Using a Procfile to configure your .NET Core on Linux Elastic Beanstalk environment
<a name="dotnet-linux-procfile"></a>

To run multiple applications on the same web server, you must include a `Procfile` in your source bundle that tells Elastic Beanstalk which applications to run.

We recommend that you always provide a `Procfile` in the source bundle with your application. This way you precisely control which processes Elastic Beanstalk runs for your application and which arguments these processes receive.

The following example uses a `Procfile` to specify two applications for Elastic Beanstalk to run on the same web server.

**Example Procfile**

```
web: dotnet ./dotnet-core-app1/dotnetcoreapp1.dll
web2: dotnet ./dotnet-core-app2/dotnetcoreapp2.dll
```

For details about writing and using a `Procfile`, see [Buildfile and Procfile](platforms-linux-extend.build-proc.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
