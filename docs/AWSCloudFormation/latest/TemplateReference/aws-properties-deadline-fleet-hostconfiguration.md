---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-hostconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet HostConfiguration
<a name="aws-properties-deadline-fleet-hostconfiguration"></a>

Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.

To remove a script from a fleet, use the [UpdateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFleet.html) operation with the `hostConfiguration``scriptBody` parameter set to an empty string ("").

## Syntax
<a name="aws-properties-deadline-fleet-hostconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-hostconfiguration-syntax.json"></a>

```
{
  "[ScriptBody](#cfn-deadline-fleet-hostconfiguration-scriptbody)" : {{String}},
  "[ScriptTimeoutSeconds](#cfn-deadline-fleet-hostconfiguration-scripttimeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-hostconfiguration-syntax.yaml"></a>

```
  [ScriptBody](#cfn-deadline-fleet-hostconfiguration-scriptbody): {{String}}
  [ScriptTimeoutSeconds](#cfn-deadline-fleet-hostconfiguration-scripttimeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-hostconfiguration-properties"></a>

`ScriptBody`  <a name="cfn-deadline-fleet-hostconfiguration-scriptbody"></a>
The text of the script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet. The script runs after a worker enters the `STARTING` state and before the worker processes tasks.
For more information about using the script, see [Run scripts as an administrator to configure workers](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-admin.html) in the *Deadline Cloud Developer Guide*.
The script runs as an administrative user (`sudo root` on Linux, as an Administrator on Windows).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScriptTimeoutSeconds`  <a name="cfn-deadline-fleet-hostconfiguration-scripttimeoutseconds"></a>
The maximum time that the host configuration can run. If the timeout expires, the worker enters the `NOT RESPONDING` state and shuts down. You are charged for the time that the worker is running the host configuration script.
You should configure your fleet for a maximum of one worker while testing your host configuration script to avoid starting additional workers.
The default is 300 seconds (5 minutes).
*Required*: No
*Type*: Integer
*Minimum*: `300`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
