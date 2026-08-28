---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-example-imdsv1-v3.html
---

# Example of how to update a configuration for IMDSv1
<a name="custom-bootstrap-actions-example-imdsv1-v3"></a>

The following is an example of a cluster configuration that supports IMDSv1 when using AWS ParallelCluster versions 3.7.0 and older.

```
Region: {{us-east-1}}
Imds:
  ImdsSupport: v1.0
Image:
  Os: {{alinux2023}}
HeadNode:
  InstanceType: {{t2.micro}}
  Networking:
    SubnetId: {{subnet-abcdef01234567890}}
  Ssh:
    KeyName: {{key-name}}
  CustomActions:
    OnNodeConfigured:
      Script: {{Script-path}}
Scheduling:
  Scheduler: slurm
  SlurmQueues:
  - Name: {{queue1}}
    CustomActions:
      OnNodeConfigured:
        Script: {{Script-path}}
    ComputeResources:
    - Name: {{t2micro}}
      Instances:
      - InstanceType: {{t2.micro}}
      MinCount: {{1}}1
    Networking:
      SubnetIds:
      - {{subnet-abcdef01234567890}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
