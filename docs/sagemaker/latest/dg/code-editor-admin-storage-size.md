---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-admin-storage-size.html
---

# Change the default storage size
<a name="code-editor-admin-storage-size"></a>

You can change the default storage settings of your users. You can also change the default storage settings based on your organizational requirements and the needs of your users.

To change the storage size of your users, do the following:

1. Update the Amazon EBS storage settings in the domain.

1. Create a user profile and specify the storage settings within it.

Use the following AWS Command Line Interface (AWS CLI) command to update the domain.

```
aws --region $REGION sagemaker update-domain \
--domain-id $DOMAIN_ID \
--default-user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":5,
            "MaximumEbsVolumeSizeInGb":100
        }
    }
}'
```

Use the following AWS CLI command to create the user profile and specify the default storage settings.

```
aws --region $REGION sagemaker create-user-profile \
--domain-id $DOMAIN_ID \
--user-profile-name $USER_PROFILE_NAME \
--user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":5,
            "MaximumEbsVolumeSizeInGb":100
        }
    }
}'
```

Use the following AWS CLI commands to update the default storage settings in the user profile.

```
aws --region $REGION sagemaker update-user-profile \
--domain-id $DOMAIN_ID \
--user-profile-name $USER_PROFILE_NAME \
--user-settings '{
    "SpaceStorageSettings": {
        "DefaultEbsStorageSettings":{
            "DefaultEbsVolumeSizeInGb":25,
            "MaximumEbsVolumeSizeInGb":200
        }
    }
}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
