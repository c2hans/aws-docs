---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.list-images-v3.html
---

# `pcluster list-images`
<a name="pcluster.list-images-v3"></a>

Retrieve the list of existing custom images.

```
pcluster list-images [-h]
                 --image-status {AVAILABLE,PENDING,FAILED}
                [--debug]
                [--next-token {{NEXT_TOKEN}}]
                [--query {{QUERY}}]
                [--region {{REGION}}]
```

## Named arguments
<a name="pcluster-v3.list-images.namedargs"></a>

**-h, --help**
Shows the help text for `pcluster list-images`.

**--image-status {`AVAILABLE`,`PENDING`,`FAILED`}**
Filter returned images by the status provided.

**--debug**
Enables debug logging.

**--next-token {{NEXT\_TOKEN}}**
The token for the next set of results.

**--query {{QUERY}}**
Specifies the JMESPath query to perform on the output.

**--region, -r {{REGION}}**
Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

**Example using AWS ParallelCluster version 3.1.2:**

```
$ pcluster list-images --image-status {{AVAILABLE}}
{
  "images": [
    {
      "imageId": "custom-alinux2-image",
      "imageBuildStatus": "BUILD_COMPLETE",
      "ec2AmiInfo": {
        "amiId": "ami-1234abcd5678efgh"
      },
      "region": "us-east-1",
      "version": "3.1.2"
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
