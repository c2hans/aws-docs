---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-serverprocess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet ServerProcess
<a name="aws-properties-gamelift-fleet-serverprocess"></a>

A set of instructions for launching server processes on each instance in a fleet. Server processes run either an executable in a custom game build or a Realtime Servers script.

## Syntax
<a name="aws-properties-gamelift-fleet-serverprocess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-serverprocess-syntax.json"></a>

```
{
  "[ConcurrentExecutions](#cfn-gamelift-fleet-serverprocess-concurrentexecutions)" : {{Integer}},
  "[LaunchPath](#cfn-gamelift-fleet-serverprocess-launchpath)" : {{String}},
  "[Parameters](#cfn-gamelift-fleet-serverprocess-parameters)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-serverprocess-syntax.yaml"></a>

```
  [ConcurrentExecutions](#cfn-gamelift-fleet-serverprocess-concurrentexecutions): {{Integer}}
  [LaunchPath](#cfn-gamelift-fleet-serverprocess-launchpath): {{String}}
  [Parameters](#cfn-gamelift-fleet-serverprocess-parameters): {{String}}
```

## Properties
<a name="aws-properties-gamelift-fleet-serverprocess-properties"></a>

`ConcurrentExecutions`  <a name="cfn-gamelift-fleet-serverprocess-concurrentexecutions"></a>
The number of server processes using this configuration that run concurrently on each instance or compute.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchPath`  <a name="cfn-gamelift-fleet-serverprocess-launchpath"></a>
The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root:
+ Windows (custom game builds only): `C:\game`. Example: "`C:\game\MyGame\server.exe`"
+ Linux: `/local/game`. Examples: "`/local/game/MyGame/server.exe`" or "`/local/game/MyRealtimeScript.js`"
Amazon GameLift Servers doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations `initSDK()` and `ProcessReady()`.
*Required*: Yes
*Type*: String
*Pattern*: `^([Cc]:\\game\S+|/local/game/\S+)`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-gamelift-fleet-serverprocess-parameters"></a>
An optional list of parameters to pass to the server executable or Realtime script on launch.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: [A-Za-z0-9\_:.\+\\/\\\\\\- =@{},?'\\[\\]"]\+
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-gamelift-fleet-serverprocess--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [Deploy a GameLift fleet for a custom game build](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating.html) in the *Amazon GameLift Developer Guide*
+ [Deploy a Realtime Servers fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-fleets-creating.html) in the *Amazon GameLift Developer Guide*
+ [Run multiple processes on a fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html) in the *Amazon GameLift Developer Guide*
+ [ServerProcess](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ServerProcess.html) in the *Amazon GameLift API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
