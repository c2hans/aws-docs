---
source_url: https://docs.aws.amazon.com/cdk/v1/guide/featureflags.html
---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches. New features will be developed for CDK v2 exclusively. Support for CDK v1 will end entirely on June 1, 2023. [Migrate to CDK v2](work-with-cdk-v2.md) to have access to the latest features and fixes.

# Feature flags
<a name="featureflags"></a>

The AWS CDK uses *feature flags* to enable potentially breaking behaviors in a release. Flags are stored as [Runtime context](context.md) values in `cdk.json` (or `~/.cdk.json`) as shown here.

```
{
  "app": "npx ts-node bin/tscdk.ts",
  "context": {
    "@aws-cdk/core:enableStackNameDuplicates": true
  }
}
```

The names of all feature flags begin with the NPM name of the package affected by the particular flag. In the example above, this is `@aws-cdk/core`, the AWS CDK framework itself, since the flag affects stack naming rules, a core AWS CDK function. AWS Construct Library modules can also use feature flags.

Feature flags are disabled by default, so existing projects that do not specify the flag will continue to work as expected with later AWS CDK releases. New projects created using **cdk init** include flags enabling all features available in the release that created the project. Edit `cdk.json` to disable any flags for which you prefer the old behavior, or to add flags to enable new behaviors after upgrading the AWS CDK.

See the `CHANGELOG` in a given release for a description of any new feature flags added in that release. A list of all current feature flags can be found on the AWS CDK GitHub repository in [`FEATURE_FLAGS.md`](https://github.com/aws/aws-cdk/blob/main/packages/%40aws-cdk/cx-api/FEATURE_FLAGS.md).

As feature flags are stored in `cdk.json`, they are not removed by the **cdk context --reset** or **cdk context --clear** commands.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
