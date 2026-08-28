---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/deployment-steps.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deployment steps
<a name="deployment-steps"></a>

 The procedure for deploying a Magento cluster on AWS consists of the following steps. For detailed instructions, follow the links for each step.

## Step 1. Prepare an AWS account
<a name="step-1.-prepare-an-aws-account"></a>

1.  If you don’t already have an AWS account, create one at [https://aws.amazon.com](https://aws.amazon.com) by following the on-screen instructions. Part of the sign-up process involves receiving a phone call and entering a PIN using the phone keypad.

1.  Use the Region selector in the navigation bar to choose the AWS Region where you want to deploy the Magento cluster on AWS. For more information, see [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html). Regions are dispersed and located in separate geographic areas. Each Region includes at least two Availability Zones that are isolated from one another but connected through low-latency links.
**Important**
 This Quick Start uses Amazon Aurora, which might not be available in all AWS Regions. Before you launch this Quick Start, check the [Region table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) for availability.
![Screen capture showing choosing an AWS Region](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/region-selection.png)
**Tip**
 Consider choosing a Region closest to your data center or corporate network to reduce network latency between systems running on AWS and the systems and users on your corporate network.

1.  Create a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in your preferred Region. In the navigation pane of the Amazon EC2 console, choose **Key Pairs**, **Create Key Pair**, type a name, and then choose **Create**.
![Screen showing creating a key pair](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/creating-key-pair.png)

    Amazon EC2 uses public-key cryptography to encrypt and decrypt login information. To be able to log into your instances, you must create a key pair. On Linux, we use the key pair to authenticate SSH login.

    For this deployment, store the private key you created in the previous step in [Secrets Manager](https://aws.amazon.com/secrets-manager/resources/) using the AWS Management Console as plaintext.

   1.  In the AWS Management Console, navigate to [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/home), choose your AWS Region, and choose **Store a new secret**.

   1.  Select **Other type of secrets** and choose **Plaintext**.

   1.  Clear the `{"":""}` JSON format from the **Plaintext** section.

   1.  Copy and paste your private key.
![Screen shot showing copying key](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/copying-key.png)

   1.  Keep the `DefaultEncryptionKey` to encrypt your SSH Key secret. Click **Next**.

   1.  Set the secret name as "**ssh-key-admin**"

   1.  Click **Next**. Leave the automatic rotation to disabled. Select **Next**.

   1.  Review and select **Store**.
![Screenshot showing reviewing secrets](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/reviewing-secrets.png)

1.  If necessary, request a service quota increase for the instance types used for the deployment. You might need to request an increase if you need additional Elastic IP addresses or if you already have an existing deployment that uses the same instance types as this architecture. On the [Service Quotas](https://console.aws.amazon.com/servicequotas/home) console, for each instance type that you want a service quota increase, choose the instance type, choose **Request quota increase**, and then complete the fields in the quota increase form. It can take a few days for the new service quota to become effective.
![Screenshot showing requesting a service quota increase](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/request-service-quota-increase.png)

## Step 2. Create Magento keys for deployment
<a name="step-2.-create-magento-keys-for-deployment"></a>

 This deployment use [Magento Composer](https://getcomposer.org/) to manage Magento components and their dependencies. To learn more about Magneto Composer, see the [Adobe documentation](https://devdocs.magento.com/guides/v2.4/extension-dev-guide/intro/intro-composer.html).

1.  Create a Magento public authentication key for Composer Username.

1. Create a Magento private authentication key for Composer Password.

For detailed instructions on creating keys, see the [Adobe documentation](https://devdocs.magento.com/guides/v2.4/install-gde/prereq/connect-auth.html).

![Screenshot showing creating a new Magento access key](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/new-magento-access-key.png)

## Step 3. Set up Terraform and a Terraform Cloud account
<a name="step-3.-setup-terraform-and-a-terraform-cloud-account"></a>

1.  Install Terraform. For installation steps, see the [Terraform documentation](https://learn.hashicorp.com/tutorials/terraform/install-cli).

1.  Set up a Terraform Cloud account. For setup instructions, see the [Terraform Cloud documentation](https://app.terraform.io/signup/account) (There is a free tier available.)

1. Create a workspace in Terraform to organize infrastructure. For setup instructions, see the [TerraForm Cloud workspace documentation](https://www.terraform.io/docs/cloud/workspaces/creating.html).

## Step 4. Prepare local environment with Terraform setup
<a name="step-4.-prepare-local-environment-with-terraform-setup"></a>

 Generate a Terraform Cloud token:

```
 terraform login
```

 Export the `TERRAFORM_CONFIG` variable:

```
 export TERRAFORM_CONFIG="$HOME/.terraform.d/credentials.tfrc.json"
```

### Configure the `tfvars` file
<a name="configure-the-tfvars-file"></a>

 Create `terraform.tfvars` in the following path:

```
$HOME/.aws/terraform.tfvars
```

 An example of the `tfvars` file contents:

```
AWS_ACCESS_KEY_ID = "{{{insert access key ID}}}"
AWS_SECRET_ACCESS_KEY = "{{{insert secret access key}}}"
AWS_SESSION_TOKEN = "{{{insert session token}}}"
```

**Note**
 We recommend using AWS Security Token Service (AWS STS)–based credentials.

**Warning**
Follow best practices for managing secrets, and ensure that your credentials are not stored in a public repository.

**Note**
Before deployment, you must create both an AWS key pair and a Magento deployment key.

### Deploy the module (Linux and iOS)
<a name="deploy-the-module-linux-and-ios"></a>

1.  [Clone the repository](https://github.com/aws-ia/terraform-adobe-magento) from GitHub.

1.  Navigate to the repository’s root directory.

1.  Navigate to the `setup_workspace` directory:

   ```
   cd setup_workspace
   ```

1.  Run the following commands in order:

   ```
   terraform init
   ```

    Alternatively, for the previous command, specify the file:

   ```
   terraform apply -var-file="$HOME/.aws/terraform.tfvars"
   ```

1.  You are asked for the following:

   1.  The AWS Region where you want to deploy this module. This must match the Region where you generated the key pair.

   1.  The organization under which Terraform Cloud runs. This can be found in the Terraform Cloud console.

   1.  Setup confirmation.
**Note**
Terraform Cloud creates the workspace, which contains the Terraform Cloud organization name.

1.  Navigate to the directory, and deploy Magento (the previous `terraform init` command generates `backend.hcl`):

   ```
    cd ../deploy
   ```
   +  Open, edit, and review all of the variables in the `variables.tf` file.
   +  Update the `default=` value for your deployment.
   +  The `description=` value provides additional context for each variable.

      The following items must be edited before deployment:
     +  Project-specific: `domain_name`
     +  Magento information: `mage_composer_username`
     +  Magento information: `mage_composer_password`
     +  Magento information: `magento_admin_password`
     +  Magento information: `magento_admin_email `
     +  Database: `magento_database_password`
     +  Variable `base_ami_os`: Use `amazon_linux_2` or `Debian_10`.
     +  Variable `use_aurora`: If you are using Amazon RDS for MySQL instead of Amazon Aurora, change to `false`.
**Important**
Don’t store secret information in a public repository.

1.  After you review, update and save the `./deploy/variables.tf` file, see the Deployment section.

### Run the following commands from an IDE or terminal with Terraform installed.
<a name="run-the-following-commands-from-an-ide-or-terminal-with-terraform-installed."></a>

1.  Initialize the environment:

   ```
   terraform init
   ```

1.  Verify that the deployed architecture is correct:

   ```
   terraform plan
   ```

1.  Validate the code:

   ```
   terraform validate
   ```

1.  Deploy the infrastructure run one of the following commands:

   ```
   terraform apply
   ```

   or

   ```
   terraform apply -var-file="$HOME/.aws/terraform.tfvars"
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
