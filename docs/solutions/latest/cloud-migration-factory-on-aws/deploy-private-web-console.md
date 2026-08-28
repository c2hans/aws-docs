---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/deploy-private-web-console.html
---

# Step 5: (Optional) Deploy private web console static content
<a name="deploy-private-web-console"></a>

If you selected the Private deployment type during the stack deployment, you are required to manually deploy the CMF web console code to the web server that you created and then specified in **Full URL used to access web user interface** parameter of the stack. For all other deployment types, skip this step.

Setup and configuration instructions for each web server are different, so this guide will only provide generic instructions on where to copy the content from, and you should configure the web server to your own requirements before updating the content.

1. Ensure that the web server has access to S3, and the AWS CLI installed and configured. Alternatively, download the contents of the front-end bucket and copy them to the web server using another device.

1. Using the AWS CLI, run the following command, replacing the environment name with the one specified during the stack deployment, AWS account ID with the ID of the AWS account the stack was deployed into, and the target directory with that of the web server’s default root directory. This will copy the static Cloud Migration Factory web console code along with the specific configuration needed for this Cloud Migration Factory solution deployment:

    **Windows example:**

   ```
   aws s3 cp s3://migration-factory-<environment name>-<AWS Account Id>-front-end/ C:\inetpub\wwwroot --recursive
   ```

    **Linux example:**

   ```
   aws s3 cp s3://migration-factory-<environment name>-<AWS Account Id>-front-end/ /var/www/html --recursive
   ```
**Note**
If an update is made to the stack parameters, it is required to replace the files on the web server from the frontend bucket to ensure that any configuration changes are available to the web console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
