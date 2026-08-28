---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/redshift-overview.html
---

# Working with Amazon Redshift from the Toolkit for VS Code
<a name="redshift-overview"></a>

The following sections describe how to get started working with Amazon Redshift from the AWS Toolkit for Visual Studio Code.

For detailed information about the Amazon Redshift service, see the [Amazon Redshift](https://docs.aws.amazon.com/redshift/) User Guide topics.

## Getting started
<a name="redshift-overview-prereqs"></a>

Before you start working with Amazon Redshift from the AWS Toolkit for Visual Studio Code, the following requirements must be met.

1. You're connected to your AWS account(s) from the Toolkit. For additional information about connecting to your AWS account from the Toolkit, see the [Connecting to AWS](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html) topic in this User Guide.

1. You've created a provisioned or serverless data warehouse.

If you've not yet created an Amazon Redshift Serverless or an Amazon Redshift provisioned cluster, the following procedures describe how to create a data warehouse with a sample dataset, from the AWS Console.

**Creating a provisioned data warehouse**

For additional details on creating an Amazon Redshift provisioned cluster data warehouse, see the [Create a sample Amazon Redshift cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-sample-data-load-create-cluster.html) topic in the *Amazon Redshift getting started* User Guide.

1. From your preferred internet browser, sign into the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshift/](https://console.aws.amazon.com/redshift/).

1. From the Amazon Redshift console, choose **Provisioned Clusters dashboard**.

1. From the **Provisioned Clusters dashboard**, choose the **Create cluster** button to open the **Create cluster** pane.

1. Complete the required fields in the **Cluster configuration** section.

1. In the **Sample data** section, select the **Load sample data** box to load the sample dataset **Tickit** into the default database **Dev** with the **public** schema.

1. In the **Database configurations** section, input values for the **Admin user name** and **Admin user password** fields.

1. Choose **Create cluster** to create your provisioned data warehouse.

**Creating a serverless data warehouse**

For additional details on creating an Amazon Redshift Serverless data warehouse, see the [Creating a data warehouse with Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html#serverless-console-resource-creation) section in the *Amazon Redshift getting started* User Guide.

1. From your preferred internet browser, sign into the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshift/](https://console.aws.amazon.com/redshift/).

1. From the Amazon Redshift console, choose the **Try Amazon Redshift Serverless** button to open the **Get started with Amazon Redshift Serverless** pane.

1. In the **Configurations** section, choose the **Use default settings** radial.

1. At the bottom of the **Get started with Amazon Redshift Serverless** pane, choose **Save configuration** to create a serverless data warehouse with default workgroup, namespace, credential, and encryption settings.

## Connecting to a data warehouse from the Toolkit
<a name="redshift-overview-connect"></a>

There are 3 methods to connect to a database from the Toolkit:
+ **Database user name and password**
+ **AWS Secrets Manager**
+ **Temporary credentials**

 To connect to a database located on an existing provisioned cluster or serverless data warehouse from the Toolkit, complete the following steps.

**Important**
If you've completed the steps in the *Prerequisites* section of this User Guide topic and your data warehouse is not visible in the Toolkit explorer, make sure that you're working from the correct AWS region in the explorer.

**Connecting to your data warehouse with the **Database user name and password** method**

1. From the Toolkit explorer, expand the AWS Region where your data warehouse exists.

1. Expand **Redshift** and choose your data warehouse to open the **Select a Connection Type** dialog in VS Code.

1. From the **Select a Connection Type** dialog, choose **Database user name and password** and provide the information required by each of the prompts.

1. Your available databases, tables, and schemas are visible in the Toolkit explorer when the Toolkit connects to your data warehouse and the procedure is complete.

**Connecting to your data warehouse with **AWS Secrets Manager****
**Note**
This procedure requires an AWS secrets manager database secret to complete. For instructions on how to set up a database secret, see the [Create an AWS Secrets Manager database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html) in the *AWS Secrets Manager* User Guide.

1. From the Toolkit explorer, expand the AWS Region where your data warehouse exists.

1. Expand **Redshift** and choose your data warehouse to open the **Select a Connection Type** dialog in VS Code.

1. From the **Select a Connection Type** dialog, choose **Secrets Manager** and provide the information required by each of the prompts.

1. Your available databases, tables, and schemas are visible in the Toolkit explorer when the Toolkit connects to your data warehouse and the procedure is complete.

**Connecting to your data warehouse with **Temporary credentials****

1. From the Toolkit explorer, expand the AWS region where your data warehouse exists.

1. Expand **Redshift** and choose your data warehouse to open the **Select a Connection Type** dialog in VS Code.

1. From the **Select a Connection Type** dialog, choose **Temporary credentials** and provide the information required by each of the prompts.

1. Your available databases, tables, and schemas are visible in the Toolkit explorer when the Toolkit connects to your data warehouse and the procedure is complete.

**Editing the connection to your data warehouse**

You can edit the connection to your data warehouse to change which database to connect to.

1. From the Toolkit explorer, expand the AWS Region where your data warehouse exists.

1. Expand **Redshift**, right-click the data warehouse you are connected to, choose **Edit connection**, and provide the name of the database you want to connect to.

1. Your available databases, tables, and schemas are visible in the Toolkit explorer when the Toolkit connects to your data warehouse and the procedure is complete.

**Deleting the connection to your data warehouse**

1. From the Toolkit explorer, expand the AWS Region where your data warehouse exists.

1. Expand **Redshift**, right-click the data warehouse with the connection you want to delete, and choose **Delete connection**. Doing so removes the available databases, tables, and schemas from the Toolkit explorer.

1. To reconnect to your data warehouse, choose **Click to connect** and provide the information required by each of the prompts. By default, reconnecting uses the previous method of authentication to connect to the data warehouse. To use a different method, choose the back arrow in the dialog until you reach the authentication prompt.

## Running SQL Statements
<a name="redshift-overview-sql"></a>

The following procedures describe how to create and run SQL statements in your database from the AWS Toolkit for Visual Studio Code.

**Note**
To complete the steps in each of the following procedures, you must first complete the section *Connecting to a data warehouse from the Toolkit*, located in this User Guide topic.

1. From the Toolkit explorer, expand **Redshift**, then expand that data warehouse that contains the database you want to query.

1. Choose **Create-Notebook** to specify a file name and location to store your notebook locally, then choose **OK** to open the notebook in your VS Code editor.

1. From the VS Code editor, input the SQL statements you want stored in this notebook.

1. Choose the **Run All** button to run the SQL statements you entered.

1. The output for your SQL statements is displayed below the statements that you entered.

**Adding Markdown to a notebook**

1. From your notebook in the VS Code editor, choose the **Markdown** button to add a Markdown cell to your notebook.

1. Input your Markdown into the provided cell.

1. The Markdown cell can be edited using the editor tools located in the upper-right corner of the Markdown cell.

**Adding code to a notebook**

1. From your notebook in the VS Code editor, choose the **Code** button to add a Code cell to your notebook.

1. Input your code into the provided cell.

1. You can choose to run your code above or below the Code cell by selecting the appropriate button from the cell editor tools, located in the upper-right corner of the Code cell.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
