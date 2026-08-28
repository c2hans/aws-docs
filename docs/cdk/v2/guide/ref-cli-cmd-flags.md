---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-flags.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk flags`
<a name="ref-cli-cmd-flags"></a>

View and modify your feature flag configurations for the CDK CLI.

Feature flags control the behavior of the CDK CLI and you can use them to enable or disable specific features. Use the `cdk flags` command to view your current feature flag configurations and modify them as needed.

**Warning**
The `cdk flags` command is in development for the AWS CDK. The current features of this command are considered production-ready and safe to use. However, the scope of this command and its features are subject to change. Therefore, you must opt in by providing the `unstable=flags` option to use this command.

## Usage
<a name="ref-cli-cmd-flags-usage"></a>

```
$ cdk flags <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-flags-args"></a><a name="ref-cli-cmd-flags-args-flagname"></a>

 **FLAGNAME**
The name of the specific feature flag that you want to view or modify.
 *Type*: String
 *Required*: No

## Options
<a name="ref-cli-cmd-flags-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-flags-options-set"></a>

 `--set <BOOLEAN>`
Modify a feature flag configuration.<a name="ref-cli-cmd-flags-options-all"></a>

 `--all <BOOLEAN>`
Modify or view all feature flags.<a name="ref-cli-cmd-flags-options-recommended"></a>

 `--recommended <BOOLEAN>`
Change flags to recommended states.<a name="ref-cli-cmd-flags-options-default"></a>

 `--default <BOOLEAN>`
Change flags to default states.<a name="ref-cli-cmd-flags-options-unconfigured"></a>

 `--unconfigured <BOOLEAN>`
Modify unconfigured feature flags.<a name="ref-cli-cmd-flags-options-value"></a>

 `--value <STRING>`
The value to set the feature flag configuration to.
 *requiresArg*: true<a name="ref-cli-cmd-flags-options-safe"></a>

 `--safe <BOOLEAN>`
Enable all feature flags that do not impact your application.<a name="ref-cli-cmd-flags-options-interactive"></a>

 `--interactive, -i <BOOLEAN>`
Interactive option for the flags command.

## Examples
<a name="ref-cli-cmd-flags-examples"></a>

### View feature flag configurations
<a name="ref-cli-cmd-flags-examples-1"></a>

Run `cdk flags` to view a report of your feature flag configurations that differ from our recommended states. Unconfigured flags are labeled with `<unset>` to indicate that the flag currently has no value. The flags are displayed in the following order:
+ Flags set to a value that doesn’t match our recommended value
+ Flags that you haven’t configured

```
$ cdk flags --unstable=flags
Feature Flag                           Recommended                       User
* @aws-cdk/...                              true                         false
* @aws-cdk/...                              true                         false
* @aws-cdk/...                              true                         <unset>
```

You can also run `cdk flags --all` to see a report of all feature flags in the following order:
+ Flags set to a value that matches our recommended value
+ Flags set to a value that doesn’t match our recommended value
+ Flags that you haven’t configured

```
$ cdk flags --unstable=flags --all
Feature Flag                              Recommended                     User
@aws-cdk/...                                true                         true
* @aws-cdk/...                              true                         false
* @aws-cdk/...                              true                         false
* @aws-cdk/...                              true                         <unset>
```

### Modify feature flag values
<a name="ref-cli-cmd-flags-examples-2"></a>

To modify your feature flags interactively, run `cdk flags --interactive` (or `cdk flags -i`) to view a list of menu options.

To change every feature flag to our recommended value, run `cdk flags --set --recommended --all`. This command keeps your feature flag configuration up-to-date with the latest CDK feature flag configurations. Be aware that running this command can potentially overwrite existing configured values.

```
$ cdk flags --unstable=flags --set --recommended --all
Feature Flag                              Recommended Value            User Value
* @aws-cdk/...                              true                         false
* @aws-cdk/...                              true                         false
* @aws-cdk/...                              true                         <unset>
  Synthesizing...
    Resources
    [~] AWS::S3::Bucket MyBucket
    └─ [~] Properties
        └─ [~] Encryption
                ...
    Number of stacks with differences: 2
  Do you want to accept these changes? (y/n) y
  Resynthesizing...
```

If you want to preserve the state of your existing configured flags, run `cdk flags --set --recommended --unconfigured`. This option changes only the unconfigured feature flags to our recommended values.

```
$ cdk flags --unstable=flags --set --recommended --unconfigured
Feature Flag                              Recommended Value            User Value
* @aws-cdk/...                              true                         <unset>
* @aws-cdk/...                              true                         <unset>
  Synthesizing...
    Resources
    [~] AWS::S3::Bucket MyBucket
    └─ [~] Properties
        └─ [~] Encryption
            ├─ [-] None
            └─ [+] ServerSideEncryptionConfiguration:
                    - ...
            ...
    Number of stacks with differences: 2
  Do you want to accept these changes? (y/n) y
  Resynthesizing...
```

If you want to ensure that any unconfigured feature flags don’t interfere with your application, run the `cdk flags --set --default --unconfigured` command to change the unconfigured flags to their default values. For example, if `@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021` is unconfigured, a notification displays after running `cdk synth`. However, if you set the flag to its default state (false), it will be configured, turned off, and not impact your application.

```
$ cdk flags --unstable=flags --set --default --unconfigured
Feature Flag                              Recommended Value            User Value
* @aws-cdk/...                              true                         <unset>
* @aws-cdk/...                              true                         <unset>
  Synthesizing...

  Do you want to accept these changes? (y/n) y
  Resynthesizing...
```

### Inspect specific feature flags
<a name="ref-cli-cmd-flags-examples-3"></a>

#### View more information about a flag
<a name="_view_more_information_about_a_flag"></a>

In addition to running `cdk flags` and `cdk flags --all` to view your feature flag configuration, you can also utilize `cdk flags "FLAGNAME"` to inspect a specific feature flag and find out what the flag does. This can be helpful in cases where you want to understand a particular flag and its impact on your application.

```
$ cdk flags --unstable=flags "@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021"
    Description: Enable this feature flag to have cloudfront distributions use the security policy TLSv1.2_2021 by default.
    Recommended Value: true
    User Value: true
```

#### Filter flags by substring
<a name="_filter_flags_by_substring"></a>

You can also run `cdk flags substring` to view all matching feature flags. If there is only one feature flag that matches that substring, specific details are displayed.

```
$ cdk flags --unstable=flags ebs
@aws-cdk/aws-ec2:ebsDefaultGp3Volume
    Description: When enabled, the default volume type of the EBS volume will be GP3
    Recommended Value: true
    User Value: true
```

If multiple flags match the substring, all matching flags are displayed in a table. If you enter multiple substrings, all matching flags that contain any of the substrings are returned.

```
$ cdk flags --unstable=flags s3 lambda
Feature Flag                              Recommended                     User
* @aws-cdk/s3...                            true                         false
* @aws-cdk/lambda...                        true                         false
* @aws-cdk/lambda...                        true                         <unset>
```

#### Modify a specific flag
<a name="_modify_a_specific_flag"></a>

If you need to modify the value of a flag and want to make sure you’re setting it to a correct and supported state, run `cdk flags --set "FLAGNAME" --value="state"`.

```
$ cdk flags --unstable=flags --set "@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021" --value="true"
  Synthesizing...
    Resources
    [~] AWS::CloudFront::Distribution MyDistribution
    └─ [~] Properties
        └─ [~] DefaultSecurityPolicy
            ├─ [-] TLSv1.0
            └─ [+] TLSv1.2_2021
                    - ...
    Number of stacks with differences: 2
  Do you want to accept these changes? (y/n) y
  Resynthesizing...
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
