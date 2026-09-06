---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/credentials-management.html
---

# Credentials management
<a name="credentials-management"></a>

The Cloud Migration Factory on AWS solution features a Credentials Manager which integrates with AWS Secrets Manager within the account in which the instance is deployed. The feature allows administrators to save system credentials to AWS Secrets Manager for use in automation scripts without providing users access to retrieve the credentials directly, or needing to provide users access to AWS Secrets Manager. Users can select stored credentials based on their name and description when providing them to an automation job. The automation job will then only retrieve the credentials requested when running on the automation server, and at this point the IAM Role allocated to the EC2 instance will be used to access the required secrets.

The Credentials Manager administration area is only visible to users that are members of the **admin** group within Amazon Cognito. Non-admin users will only be able to view credential names and descriptions when referenced through an automation, or other records relationship.

The following three secret types can be stored in AWS Secrets Manager via Credentials Manager.

 **OS Credentials** - In the form of a ,`username` and `password`.

 **Secret key/value** - In the form of a `key` and `value`.

 **Plaintext** - In the form of a single plain text string.

## Add a secret
<a name="add-a-secret"></a>

1. Choose **Add** from the **Credential Manager Secrets** list.

1. Select the **Secret Type** to add.

1. Enter a **Secret Name**. This will be the same name that will be displayed inside AWS Secrets Manager for the secret name.

1. Enter a **Secret Description**. This will be the same description that will be displayed inside AWS Secrets Manager for the secret description.

1. Enter the credential information for the secret type.

**Note**
For **OS Credentials** secret type, there is an option to select the **OS Type** which can be referenced in custom scripts.

## Edit a secret
<a name="edit-a-secret"></a>

Except the secret name and type, you can edit all properties of the secret using the Credentials Manager user interface.

## Delete a secret
<a name="delete-a-secret"></a>

From the Credentials Manager view, select the secret you want to delete and choose **Delete**. The secret will be scheduled for deletion within AWS Secrets Manager which may take a few minutes to complete. Any attempt to add a new secret with the same name during this time will fail.
