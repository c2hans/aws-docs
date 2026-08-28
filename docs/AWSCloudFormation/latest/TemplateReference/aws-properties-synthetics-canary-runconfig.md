---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-runconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary RunConfig
<a name="aws-properties-synthetics-canary-runconfig"></a>

A structure that contains input information for a canary run. This structure is required.

## Syntax
<a name="aws-properties-synthetics-canary-runconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-runconfig-syntax.json"></a>

```
{
  "[ActiveTracing](#cfn-synthetics-canary-runconfig-activetracing)" : {{Boolean}},
  "[EnvironmentVariables](#cfn-synthetics-canary-runconfig-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
  "[EphemeralStorage](#cfn-synthetics-canary-runconfig-ephemeralstorage)" : {{Integer}},
  "[MemoryInMB](#cfn-synthetics-canary-runconfig-memoryinmb)" : {{Integer}},
  "[TimeoutInSeconds](#cfn-synthetics-canary-runconfig-timeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-runconfig-syntax.yaml"></a>

```
  [ActiveTracing](#cfn-synthetics-canary-runconfig-activetracing): {{Boolean}}
  [EnvironmentVariables](#cfn-synthetics-canary-runconfig-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [EphemeralStorage](#cfn-synthetics-canary-runconfig-ephemeralstorage): {{Integer}}
  [MemoryInMB](#cfn-synthetics-canary-runconfig-memoryinmb): {{Integer}}
  [TimeoutInSeconds](#cfn-synthetics-canary-runconfig-timeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-synthetics-canary-runconfig-properties"></a>

`ActiveTracing`  <a name="cfn-synthetics-canary-runconfig-activetracing"></a>
Specifies whether this canary is to use active AWS X-Ray tracing when it runs. Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html).
 You can enable active tracing only for canaries that use version `syn-nodejs-2.0` or later for their canary runtime.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-synthetics-canary-runconfig-environmentvariables"></a>
Specifies the keys and values to use for any environment variables used in the canary script. Use the following format:
{ "key1" : "value1", "key2" : "value2", ...}
Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see [ Runtime environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime).
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z][a-zA-Z0-9_]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EphemeralStorage`  <a name="cfn-synthetics-canary-runconfig-ephemeralstorage"></a>
Specifies the amount of ephemeral storage (in MB) to allocate for the canary run during execution. This temporary storage is used for storing canary run artifacts (which are uploaded to an Amazon S3 bucket at the end of the run), and any canary browser operations. This temporary storage is cleared after the run is completed. Default storage value is 1024 MB.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryInMB`  <a name="cfn-synthetics-canary-runconfig-memoryinmb"></a>
The maximum amount of memory that the canary can use while running. This value must be a multiple of 64. The range is 960 to 3008.
*Required*: No
*Type*: Integer
*Minimum*: `960`
*Maximum*: `3008`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutInSeconds`  <a name="cfn-synthetics-canary-runconfig-timeoutinseconds"></a>
How long the canary is allowed to run before it must stop. You can't set this time to be longer than the frequency of the runs of this canary.
If you omit this field, the frequency of the canary is used as this value, up to a maximum of 900 seconds.
*Required*: No
*Type*: Integer
*Minimum*: `3`
*Maximum*: `840`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
