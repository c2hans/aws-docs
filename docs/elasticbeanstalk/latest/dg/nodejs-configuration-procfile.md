---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-configuration-procfile.html
---

# Configuring custom start commands with a Procfileon Elastic Beanstalk
<a name="nodejs-configuration-procfile"></a>

You can include a file that's called `Procfile` at the root of your source bundle to specify the command that starts your application.

**Example Procfile**

```
web: node index.js
```

For information about `Procfile` usage see [Buildfile and Procfile](platforms-linux-extend.build-proc.md).

**Note**
This feature replaces the legacy `NodeCommand` option in the `aws:elasticbeanstalk:container:nodejs` namespace.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
