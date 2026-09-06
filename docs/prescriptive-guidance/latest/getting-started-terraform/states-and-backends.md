---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/states-and-backends.html
---

# States and backends
<a name="states-and-backends"></a>

One of the most important concepts in infrastructure as code (IaC) is the concept of *state*. IaC services maintain state, which allows you to declare a resource in an IaC file without having it recreated each time you deploy. IaC files document the state of all resources at the end of a deployment so that it can then compare that state to the target state, as declared in the next deployment. So if the current state contains an Amazon Simple Storage Service (Amazon S3) bucket named `my-s3-bucket` and the incoming changes also contain that same bucket, the new process will apply any changes found to the existing bucket rather than trying to create an all new bucket.

The following table provides examples of the general IaC state process.

|
|
| Current state | Target state | Action |
| --- |--- |--- |
| No S3 bucket named `my-s3-bucket` | S3 bucket named `my-s3-bucket` | Create an S3 bucket named `my-s3-bucket` |
| `my-s3-bucket` with no bucket versioning configured | `my-s3-bucket` with no bucket versioning configured | No action |
| `my-s3-bucket` with no bucket versioning configured | `my-s3-bucket` with bucket versioning configured | Configure `my-s3-bucket` to have bucket versioning |
| `my-s3-bucket` with bucket versioning configured | No S3 bucket named `my-s3-bucket` | Attempt to delete `my-s3-bucket` |

To understand the different ways in which AWS CloudFormation and Terraform track state, it's important to remember the first basic difference between the two tools: CloudFormation is hosted inside of the AWS Cloud, and Terraform is essentially remote. This fact allows CloudFormation to maintain state internally. You can go to the CloudFormation console and view the event history of a given stack, but the CloudFormation service itself enforces the state rules for you.

The three modes that CloudFormation operates under for a given resource are `Create`, `Update`, and `Delete`. The current mode is determined based on what happened in the last deployment, and it cannot be influenced otherwise. You can perhaps update CloudFormation resources manually in order to influence which mode is determined, but you can't pass a command to CloudFormation that says "For this resource, operate under `Create` mode."

Because Terraform is not hosted in the AWS Cloud, the process of maintaining state must be more configurable. For this reason, the [Terraform state](https://developer.hashicorp.com/terraform/language/state) is maintained within an automatically generated state file. A Terraform developer has to deal with state much more directly than they would with CloudFormation. The important thing to remember is that tracking state is equally as important for both tools.

By default, the Terraform state file is stored locally at the top-level of the main directory that runs your Terraform stack. If you run the `terraform apply` command from your local development environment, you can see Terraform generate the **terraform.tfstate** file that it uses to maintain state in real time. For better or for worse, this gives you much more control over state in Terraform than you have in CloudFormation. While you should never update the state file directly, there are several Terraform CLI commands you can run that will update state between deployments. For example, [terraform import](https://developer.hashicorp.com/terraform/cli/import) allows you to add resources created outside of Terraform into your deployment stack. Conversely, you can remove a resource from state by running [terraform state rm](https://developer.hashicorp.com/terraform/cli/commands/state/rm).

The fact that Terraform needs to store its state somewhere leads to another concept that doesn't apply to CloudFormation: the *backend*. A [Terraform backend](https://developer.hashicorp.com/terraform/language/settings/backends/configuration) is the place where a Terraform stack stores its state file after deployment. This is also where it expects to find the state file when a new deployment begins. When you run your stack locally, as described above, you can keep a copy of the Terraform state in the top-level local directory. This is known as a *local backend*.

When developing for a continuous integration and continuous deployment (CI/CD) environment, the local state file is generally included in the **.gitignore** file to keep it out of version control. Then there's no local state file present within the pipeline. In order to work properly, that pipeline stage needs to find the correct state file somewhere*. *This is why Terraform configuration files often contain a backend block. The backend block indicates to the Terraform stack that it needs to look somewhere besides its own top-level directory to find the state file.

A Terraform backend can be located almost anywhere: an [Amazon S3 bucket](https://developer.hashicorp.com/terraform/language/settings/backends/s3), an [API endpoint, ](https://developer.hashicorp.com/terraform/language/settings/backends/http)or even a [remote Terraform workspace](https://developer.hashicorp.com/terraform/language/settings/backends/remote). The following is an example of a Terraform backend stored in an Amazon S3 bucket.

```
terraform {
  backend "s3" {
    bucket = "my-s3-bucket"
    key    = "state-file-folder"
    region = "us-east-1"
  }
}
```

In order to avoid storing sensitive information within Terraform configuration files, backends also support partial configurations. In the previous example, the credentials needed to access the bucket are not present in the configuration. Credentials can be obtained from environment variables or by using other means, such as AWS Secrets Manager. For more information, see [Securing sensitive data by using AWS Secrets Manager and HashiCorp Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/introduction.html).

A common backend scenario is a local backend that is used in your local environment for testing purposes. The **terraform.tfstate **file is included in the **.gitignore** file so that it is not pushed to the remote repository. Then, each environment within the CI/CD pipeline would maintain its own backend. In this scenario, multiple developers might have access to this remote state, so you would want to protect the integrity of the state file. If multiple deployments are running and updating state at the same time, the state file could become corrupted. For this reason, in situations with non-local backends, the state file is typically [locked](https://developer.hashicorp.com/terraform/language/state/locking) during deployment.
