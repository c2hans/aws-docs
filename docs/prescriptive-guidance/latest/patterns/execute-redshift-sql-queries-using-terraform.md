---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/execute-redshift-sql-queries-using-terraform.html
---

# Execute Amazon Redshift SQL queries by using Terraform
<a name="execute-redshift-sql-queries-using-terraform"></a>

*Sylvia Qi and Aditya Ambati, Amazon Web Services*

## Summary
<a name="execute-redshift-sql-queries-using-terraform-summary"></a>

Using infrastructure as code (IaC) for the deployment and management of Amazon Redshift is a prevalent practice within DevOps. IaC facilitates the deployment and configuration of various Amazon Redshift resources, such as clusters, snapshots, and parameter groups. However, IaC doesn’t extend to the management of database resources like tables, schemas, views, and stored procedures. These database elements are managed through SQL queries and are not directly supported by IaC tools. Although solutions and tools exist for managing these resources, you might prefer not to introduce additional tools into your technology stack.

This pattern outlines a methodology that uses Terraform to deploy Amazon Redshift database resources, including tables, schemas, views, and stored procedures. The pattern distinguishes between two types of SQL queries:
+ **Nonrepeatable queries** – These queries are executed once during the initial Amazon Redshift deployment to establish the essential database components.
+ **Repeatable queries** – These queries are immutable and can be rerun without impacting the database. The solution uses Terraform to monitor changes in repeatable queries and apply them accordingly.

For more details, see *Solution walkthrough* in [Additional information](#execute-redshift-sql-queries-using-terraform-additional).

## Prerequisites and limitations
<a name="execute-redshift-sql-queries-using-terraform-prereqs"></a>

**Prerequisites**

You must have an active AWS account and install the following on your deployment machine:
+ [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (AWS CLI)
+ An [AWS CLI profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) configured with Amazon Redshift read/write permissions
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) version 1.6.2 or later
+ [Python3](https://www.python.org/downloads/)
+ [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

**Limitations**
+ This solution supports a single Amazon Redshift database because Terraform only allows for the creation of one database during cluster creation.
+ This pattern doesn’t include tests to validate changes to the repeatable queries before applying them. We recommend that you incorporate such tests for enhanced reliability.
+ To illustrate the solution, this pattern provides a sample `redshift.tf` file that uses a local Terraform state file. However, for production environments, we strongly recommend that you employ a remote state file with a locking mechanism for enhanced stability and collaboration.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**

This solution is developed and tested on [Amazon Redshift patch 179](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html#cluster-version-179).

**Code repository**

The code for this pattern is available in the GitHub [amazon-redshift-sql-deploy-terraform](https://github.com/aws-samples/amazon-redshift-sql-deploy-terraform) repository.

## Architecture
<a name="execute-redshift-sql-queries-using-terraform-architecture"></a>

The following diagram illustrates how Terraform manages the Amazon Redshift database resources by handling both nonrepeatable and repeatable SQL queries.

![Process for Terraform to manage Amazon Redshift database resources using SQL queries.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0f4467ac-761b-4b6b-a32f-e18a2ca2245d/images/3b6ff9e8-e3d1-48ed-9fa1-4b14f7d3d65b.png)

The diagram shows the following steps:

1. Terraform applies nonrepeatable SQL queries during the initial Amazon Redshift cluster deployment.

1. The developer commits changes to the repeatable SQL queries.

1. Terraform monitors changes in the repeatable SQL queries.

1. Terraform applies repeatable SQL queries to the Amazon Redshift database.

The solution provided by this pattern is built based on the [Terraform module for Amazon Redshift](https://registry.terraform.io/modules/terraform-aws-modules/redshift/aws/latest). The Terraform module provisions an Amazon Redshift cluster and database. To enhance the module, we used `terraform_data` resources, which invokes a custom Python script to execute SQL queries using the Amazon Redshift [ExecuteStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ExecuteStatement.html) API operation. As a result, the module can do the following:
+ Deploy any number of database resources by using SQL queries after the database is provisioned.
+ Monitor continuously for changes in the repeatable SQL queries and apply those changes using Terraform.

For more details, see *Solution walkthrough* in [Additional information](#execute-redshift-sql-queries-using-terraform-additional).

## Tools
<a name="execute-redshift-sql-queries-using-terraform-tools"></a>

**AWS services**
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) is a fully managed petabyte-scale data warehouse service in the AWS Cloud.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.
+ [Python](https://www.python.org/) is a general-purpose programming language that’s used in this pattern to execute SQL queries.

## Best practices
<a name="execute-redshift-sql-queries-using-terraform-best-practices"></a>
+ [Amazon Redshift best practices](https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html)
+ [Using the Amazon Redshift Data API to interact with Amazon Redshift clusters](https://aws.amazon.com/blogs/big-data/using-the-amazon-redshift-data-api-to-interact-with-amazon-redshift-clusters/)

## Epics
<a name="execute-redshift-sql-queries-using-terraform-epics"></a>

### Deploy the solution using Terraform
<a name="deploy-the-solution-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| **Clone the repository.** | To clone the Git repository containing the Terraform code for provisioning an Amazon Redshift cluster, use the following command.<pre>git clone https://github.com/aws-samples/amazon-redshift-sql-deploy-terraform.git</pre> | DevOps engineer |
| **Update the Terraform variables.** | To customize the Amazon Redshift cluster deployment according to your specific requirements, update the following parameters in the `terraform.tfvars` file.<pre>region                    = "<AWS_REGION>"<br />cluster_identifier        = "<REDSHIFT_CLUSTER_IDENTIFIER>"<br />node_type                 = "<REDSHIFT_NODE_TYPE>"<br />number_of_nodes           = "<REDSHIFT_NODE_COUNT>"<br />database_name             = "<REDSHIFT_DB_NAME>"<br />subnet_ids                = "<REDSHIFT_SUBNET_IDS>"<br />vpc_security_group_ids    = "<REDSHIFT_SECURITY_GROUP_IDS>"<br />run_nonrepeatable_queries = true<br />run_repeatable_queries    = true<br />sql_path_bootstrap        = "<BOOTSTRAP_SQLS_PATH>"<br />sql_path_nonrepeatable    = "<NON-REPEATABLE_SQLS_PATH>"<br />sql_path_repeatable       = "<REPEATABLE_SQLS_PATH>"<br />sql_path_finalize         = "<FINALIZE_SQLS_PATH>"<br />create_random_password    = false<br />master_username           = "<REDSHIFT_MASTER_USERNAME>"</pre> | DevOps engineer |
| Deploy the resources using Terraform. | 1. To prepare for the deployment process, use the following command to initialize Terraform within the cloned repository.<pre>terraform init</pre><br />2. To preview the changes that Terraform will apply to the infrastructure, use the following command to create an execution plan.<pre>terraform plan -var-file terraform.tfvars</pre><br />3. To provision the Amazon Redshift cluster and associated resources, use the following command to apply the Terraform execution plan.<pre>terraform apply -var-file terraform.tfvars</pre> | DevOps engineer |
| (Optional) Execute additional SQL queries. | The sample repository provides several SQL queries for demo purposes. To execute your own SQL queries, add them to the following folders:<br />`/bootstrap` <br />`/nonrepeatable` <br />`/repeatable` <br />`/finalize` |  |

### Monitor the execution of SQL statements
<a name="monitor-the-execution-of-sql-statements"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Monitor the deployment of SQL statements. | You can monitor the results of the SQL executions to an Amazon Redshift cluster. For examples of output that show a failed and a successful SQL execution, see *Example SQL statements* in [Additional information](#execute-redshift-sql-queries-using-terraform-additional).  | DBA, DevOps engineer |
| Clean up resources. | To delete all the resources deployed by Terraform, run the following command.<pre>terraform destroy</pre> | DevOps engineer |

### Validate the results
<a name="validate-the-results"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the data in the Amazon Redshift cluster. | 1. Sign in to the AWS Management Console, and open the Amazon Redshift console.<br />2. On the navigation menu, choose **Clusters**. Choose the relevant cluster name in the list.<br />3. Follow the instructions in [Querying a database using the Amazon Redshift query editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) in the Amazon Redshift documentation. | DBA, AWS DevOps |

## Related resources
<a name="execute-redshift-sql-queries-using-terraform-resources"></a>

**AWS documentation**
+ [Amazon Redshift provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)
+ [Troubleshooting issues for Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-troubleshooting.html)

**Other resources**
+ [Command: apply](https://developer.hashicorp.com/terraform/cli/commands/apply) (Terraform documentation)

## Additional information
<a name="execute-redshift-sql-queries-using-terraform-additional"></a>

**Solution walkthrough**

To use the solution, you must organize your Amazon Redshift SQL queries in a specific way. All SQL queries must be stored in files with a `.sql` extension.

In the code example provided with this pattern, the SQL queries are organized in the following folder structure. You can modify the code (`sql-queries.tf` and `sql-queries.py`) to work with any structure that fits your unique use case.

```
/bootstrap
     |- Any # of files
     |- Any # of sub-folders
/nonrepeatable
     |- Any # of files
     |- Any # of sub-folders
/repeatable
     /udf
          |- Any # of files
          |- Any # of sub-folders
     /table
          |- Any # of files
          |- Any # of sub-folders
     /view
          |- Any # of files
          |- Any # of sub-folders
     /stored-procedure
          |- Any # of files
          |- Any # of sub-folders
/finalize
     |- Any # of files
     |- Any # of sub-folders
```

Given the preceding folder structure, during Amazon Redshift cluster deployment, Terraform executes the queries in the following order:

1. `/bootstrap`

1. `/nonrepeatable`

1. `/repeatable`

1. `/finalize`

The `/repeatable` folder contains four subfolders: `/udf`, `/table`, `/view`, and `/stored-procedure`. These subfolders indicate the order in which Terraform executes the SQL queries.

The Python script that executes the SQL queries is `sql-queries.py`. First, the script reads all the files and subfolders of a specific source directory, for example, the `sql_path_bootstrap` parameter. Then the script executes the queries by calling the Amazon Redshift [ExecuteStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ExecuteStatement.html) API operation. You might have one or more SQL queries in a file. The following code snippet shows the Python function that executes SQL statements stored in a file against an Amazon Redshift cluster.

```
def execute_sql_statement(filename, cluster_id, db_name, secret_arn, aws_region):
    """Execute SQL statements in a file"""
    redshift_client = boto3.client(
        'redshift-data', region_name=aws_region)
    contents = get_contents_from_file(filename),
    response = redshift_client.execute_statement(
        Sql=contents[0],
        ClusterIdentifier=cluster_id,
        Database=db_name,
        WithEvent=True,
        StatementName=filename,
        SecretArn=secret_arn
    )
    ...
```

The Terraform script `sql-queries.tf` creates the [terraform\_data](https://developer.hashicorp.com/terraform/language/resources/terraform-data) resources that invoke the `sql-queries.py` script. There is a `terraform_data` resource for each of the four folders: `/bootstrap`, `/nonrepeatable`, `/repeatable`, and `/finalize`. The following code snippet shows the `terraform_data` resource that execute the SQL queries in the `/bootstrap` folder.

```
locals {
  program               = "${path.module}/sql-queries.py"
  redshift_cluster_name = try(aws_redshift_cluster.this[0].id, null)
}

resource "terraform_data" "run_bootstrap_queries" {
  count      = var.create && var.run_nonrepeatable_queries && (var.sql_path_bootstrap != "") && (var.snapshot_identifier == null) ? 1 : 0
  depends_on = [aws_redshift_cluster.this[0]]

  provisioner "local-exec" {
    command = "python3 ${local.program} ${var.sql_path_bootstrap} ${local.redshift_cluster_name} ${var.database_name} ${var.redshift_secret_arn} ${local.aws_region}"
  }
}
```

You can control whether to run these queries by using the following variables. If you don’t want to run queries in `sql_path_bootstrap`, `sql_path_nonrepeatable`, `sql_path_repeatable`, or `sql_path_finalize`, set their values to `""`.

```
  run_nonrepeatable_queries = true
  run_repeatable_queries    = true
  sql_path_bootstrap        = "src/redshift/bootstrap"
  sql_path_nonrepeatable    = "src/redshift/nonrepeatable"
  sql_path_repeatable       = "src/redshift/repeatable"
  sql_path_finalize         = "src/redshift/finalize"
```

When you run `terraform apply`, Terraform considers the `terraform_data` resource added after the script is completed, regardless of the results of the script. If some SQL queries failed, and you want to rerun them, you can manually remove the resource from the Terraform state, and run `terraform apply` again. For example, the following command removes the `run_bootstrap_queries` resource from the Terraform state.

`terraform state rm module.redshift.terraform_data.run_bootstrap_queries[0]`

The following code example shows how the `run_repeatable_queries` resource monitors changes in the `repeatable` folder by using the [sha256 hash](https://developer.hashicorp.com/terraform/language/functions/sha256). If any file within the folder is updated, Terraform marks the entire directory for an update. Then, Terraform runs the queries in the directory again during the next `terraform apply`.

```
resource "terraform_data" "run_repeatable_queries" {
  count      = var.create_redshift && var.run_repeatable_queries && (var.sql_path_repeatable != "") ? 1 : 0
  depends_on = [terraform_data.run_nonrepeatable_queries]

  # Continuously monitor and apply changes in the repeatable folder
  triggers_replace = {
    dir_sha256 = sha256(join("", [for f in fileset("${var.sql_path_repeatable}", "**") : filesha256("${var.sql_path_repeatable}/${f}")]))
  }

  provisioner "local-exec" {
    command = "python3 ${local.sql_queries} ${var.sql_path_repeatable} ${local.redshift_cluster_name} ${var.database_name} ${var.redshift_secret_arn}"
  }
}
```

To refine the code, you can implement a mechanism to detect and apply changes only to the files that have been updated within the `repeatable` folder, rather than applying changes to all files indiscriminately.

**Example SQL statements**

The following output shows a failed SQL execution, along with an error message.

```
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): Executing: ["/bin/sh" "-c" "python3 modules/redshift/sql-queries.py src/redshift/nonrepeatable testcluster-1 db1 arn:aws:secretsmanager:us-east-1:XXXXXXXXXXXX:secret:/redshift/master_user/password-8RapGH us-east-1"]
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): -------------------------------------------------------------------
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): src/redshift/nonrepeatable/table/admin/admin.application_family.sql
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): -------------------------------------------------------------------
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): Status: FAILED
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): SQL execution failed.
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec): Error message: ERROR: syntax error at or near ")"
module.redshift.terraform_data.run_nonrepeatable_queries[0] (local-exec):   Position: 244
module.redshift.terraform_data.run_nonrepeatable_queries[0]: Creation complete after 3s [id=ee50ba6c-11ae-5b64-7e2f-86fd8caa8b76]
```

The following output shows a successful SQL execution.

```
module.redshift.terraform_data.run_bootstrap_queries[0]: Provisioning with 'local-exec'...
module.redshift.terraform_data.run_bootstrap_queries[0] (local-exec): Executing: ["/bin/sh" "-c" "python3 modules/redshift/sql-queries.py src/redshift/bootstrap testcluster-1 db1 arn:aws:secretsmanager:us-east-1:XXXXXXXXXXXX:secret:/redshift/master_user/password-8RapGH us-east-1"]
module.redshift.terraform_data.run_bootstrap_queries[0] (local-exec): -------------------------------------------------------------------
module.redshift.terraform_data.run_bootstrap_queries[0] (local-exec): src/redshift/bootstrap/db.sql
module.redshift.terraform_data.run_bootstrap_queries[0] (local-exec): -------------------------------------------------------------------
module.redshift.terraform_data.run_bootstrap_queries[0] (local-exec): Status: FINISHED
module.redshift.terraform_data.run_bootstrap_queries[0] (local-exec): SQL execution successful.
module.redshift.terraform_data.run_bootstrap_queries[0]: Creation complete after 2s [id=d565ef6d-be86-8afd-8e90-111e5ea4a1be]
```
