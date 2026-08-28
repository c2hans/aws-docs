---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-terraform-engine-state.html
---

# Managing the Terraform Open Source product state file
<a name="getstarted-terraform-engine-state"></a>

Every Terraform Open Source provisioned product has a **single-state file**. There is a 1:1 relationship between the provisioned product and its state file. The files are stored in an Amazon S3 bucket named `sc-terraform-engine-state-${AWS::AccountId}-${AWS::Region}`. The state file is saved under the `AccountID` or `ProvisionedProductID` object key.

State file access is limited to the `GetStateFile` AWS Lambda and Amazon EC2 launch templates. AWS Service Catalog administrators do **not** have direct access to the state files in Amazon S3. Administrators must access the files using Amazon EC2. By default, AWS Service Catalog administrators can see the list of state files, but cannot read or write the file contents. Only the Terraform provisioning engine can read or write the file contents.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
