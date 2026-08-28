---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-platform-shrinkwrap.html
---

# Locking dependencies with npm shrinkwrap on Elastic Beanstalk
<a name="nodejs-platform-shrinkwrap"></a>

The Node.js platform runs `npm install` as the *webapp* user each time you deploy. When new versions of your dependencies are available, they're installed when you deploy your application, potentially causing the deployment to take a long time.

You can avoid upgrading dependencies by creating an `npm-shrinkwrap.json` file that locks down your application's dependencies to the current version.

```
$ npm install
$ npm shrinkwrap
wrote npm-shrinkwrap.json
```

Include this file in your source bundle to ensure that dependencies are only installed once.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
