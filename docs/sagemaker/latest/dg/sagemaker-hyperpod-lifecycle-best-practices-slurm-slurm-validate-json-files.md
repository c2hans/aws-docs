---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-validate-json-files.html
---

# Validating the JSON configuration files before creating a Slurm cluster on HyperPod
<a name="sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-validate-json-files"></a>

To validate the JSON configuration files before submitting a cluster creation request, use the configuration validation script [`validate-config.py`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/validate-config.py). This script parses and compares your HyperPod cluster configuration JSON file and Slurm configuration JSON file, and identifies if there's any resource misconfiguration between the two files and also across Amazon EC2, Amazon VPC, and Amazon FSx resources. For example, to validate the `create_cluster.json` and `provisioning_parameters.json` files from the [Base lifecycle scripts provided by HyperPod](sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md) section, run the validation script as follows.

```
python3 validate-config.py --cluster-config {{create_cluster.json}} --provisioning-parameters {{provisioning_parameters.json}}
```

The following is an example output of a successful validation.

```
✔️  Validated instance group name worker-group-1 is correct ...

✔️  Validated subnet subnet-012345abcdef67890 ...
✔️  Validated security group sg-012345abcdef67890 ingress rules ...
✔️  Validated security group sg-012345abcdef67890 egress rules ...
✔️  Validated FSx Lustre DNS name fs-012345abcdef67890.fsx.us-east-1.amazonaws.com
✔️  Validated FSx Lustre mount name abcdefgh
✅ Cluster Validation succeeded
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
