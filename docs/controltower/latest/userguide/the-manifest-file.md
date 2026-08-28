---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/the-manifest-file.html
---

# The CfCT manifest file
<a name="the-manifest-file"></a>

The CfCT `manifest.yaml` file is a text file that describes your AWS resources. The following example shows the structure of the CfCT manifest file.

```
---
region: String
version: 2021-03-15

resources:
  #set of CloudFormation resources, SCP policies, or RCP policies
...
```

As shown in the previous code example, the first two lines of the manifest file specify the values of the **region** and the **version** keywords. Here are the definitions of those keywords.

**region** – A text string for the AWS Control Tower default Region. This value must be a valid AWS Region name (such as `us-east-1`, `eu-west-1`, or `ap-southeast-1`). The AWS Control Tower home Region is the default when you create custom AWS Control Tower resources (such as CloudFormation StackSets), unless a more resource-specific Region is specified.

```
region:{{your-home-region}}
```

**version** – The manifest schema version number. The latest supported version is 2021-03-15.

```
version: 2021-03-15
```

**Note**
We strongly recommend you use the latest version. To update manifest properties in the latest version, refer to [Version upgrades for the CfCT manifest](cfct-compatibility.md).

The next keyword shown in the previous example is the **resources** keyword. The **resources** section of the manifest file is highly structured. It contains a detailed list of AWS resources, which will be deployed automatically by the CfCT pipeline. These descriptions of resources and their available parameters are given in the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
