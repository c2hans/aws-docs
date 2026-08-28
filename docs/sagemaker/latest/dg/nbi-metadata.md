---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-metadata.html
---

# Notebook Instance Metadata
<a name="nbi-metadata"></a>

When you create a notebook instance, Amazon SageMaker AI creates a JSON file on the instance at the location `/opt/ml/metadata/resource-metadata.json` that contains the `ResourceName` and `ResourceArn` of the notebook instance. You can access this metadata from anywhere within the notebook instance, including in lifecycle configurations. For information about notebook instance lifecycle configurations, see [Customization of a SageMaker notebook instance using an LCC script](notebook-lifecycle-config.md).

**Note**
The `resource-metadata.json` file can be modified with root access.

The `resource-metadata.json` file has the following structure:

```
{
    "ResourceArn": "{{NotebookInstanceArn}}",
    "ResourceName": "{{NotebookInstanceName}}"
}
```

You can use this metadata from within the notebook instance to get other information about the notebook instance. For example, the following commands get the tags associated with the notebook instance:

```
NOTEBOOK_ARN=$(jq '.ResourceArn'
            /opt/ml/metadata/resource-metadata.json --raw-output)
aws sagemaker list-tags --resource-arn $NOTEBOOK_ARN
```

The output looks like the following:

```
{
    "Tags": [
        {
            "Key": "test",
            "Value": "true"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
