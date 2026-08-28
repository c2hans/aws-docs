---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-example-imdsv2-v3.html
---

# Example of how to update a custom bootstrap script for IMDSv2
<a name="custom-bootstrap-actions-example-imdsv2-v3"></a>

In the following example, we update a custom bootstrap action script that was used with IMDSv1 for use with IMDSv2. The IMDSv1 script retrieves Amazon EC2 instance AMI ID metadata.

```
#!/bin/bash
AMI_ID=$(curl http://169.254.169.254/latest/meta-data/ami-id)
echo $AMI_ID >> /home/ami_id.txt
```

The following shows the custom bootstrap action script modified to be compatible with IMDSv2.

```
#!/bin/bash
AMI_ID=$(TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
         && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/ami-id)
echo $AMI_ID >> /home/ami_id.txt
```

For more information, see [ Retrieve instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#instancedata-meta-data-retrieval-examples) in the *Amazon EC2 User Guide for Linux Instances*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
