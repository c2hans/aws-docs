---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/post-deployment-steps.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Post-deployment steps
<a name="post-deployment-steps"></a>

 `terraform apply` runs remotely in Terraform Cloud and takes about 30–60 minutes to deploy.

 During the deployment, you should receive an AWS email to allow Amazon SES to send you emails. Verify this before you log into Magento.

 After the Terraform deployment completes, an output shows the relevant information for accessing Magento.

**Important**
After Terraform completes, Magento bootstraps the environment, which takes about 15–20 minutes. Various Magento install and configuration commands run during this time, and the site enters maintenance mode. After it exits maintenance mode, images sync with your Amazon Simple Storage Service (Amazon S3) bucket.

## Test the deployment
<a name="test-the-deployment"></a>

 After Terraform completes, it outputs the frontend and backend URLs. Use the credentials specified in the `variables.tf` file to log in as an administrator. Run the following command to connect to the web node:

```
ssh -i {{PATH_TO_GENERATED_KEY}} -J admin@{{BASTION_PUBLIC_IP}} admin{{@WEB_NODE_PRIVATE_IP}}
```

**Note**
 Ensure that you have SSH key forwarding enabled.

## Clean up the infrastructure
<a name="clean-up-the-infrastructure"></a>

**Note**
 If you want to retain the Magento files stored in your S3 bucket, copy and save the bucket’s objects before completing this step.

 When you no longer need the infrastructure, run one of the following commands to remove it:

```
terraform destroy
```

or

```
terraform destroy -var-file="$HOME/.aws/terraform.tfvars"
```

 After you remove the infrastructure, the database is stored as an artifact.
