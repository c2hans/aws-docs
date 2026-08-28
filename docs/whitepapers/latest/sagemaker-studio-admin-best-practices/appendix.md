---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/appendix.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix
<a name="appendix"></a>

## Multi-tenancy comparison
<a name="multi-tenancy-comparison"></a>

*Table 2 — Multi-tenancy comparison*

|  Multi-domain  |  Multi-account  |  Attribute-based access control (ABAC) within a single domain  |
| --- | --- | --- |
| Resource isolation is achieved using tags. SageMaker AI Studio automatically tags all resources with the domain ARN and user profile/ space ARN. | Each tenant is in their own account, so there is absolute resource isolation. | Resource isolation is achieved using tags. Users have to manage the tagging of created resources for ABAC. |
| List APIs cannot be restricted by tags. UI filtering of resources is done on shared spaces, however, List API calls made through the AWS CLI or the Boto3 SDK will list resources across the Region. | List APIs isolation is also possible, since tenants are in their dedicated accounts. | List APIs cannot be restricted by tags. List API calls made through the AWS CLI or the Boto3 SDK will list resources across the Region. |
| SageMaker AI Studio compute and storage costs per tenant can be easily monitored by using Domain ARN as a cost allocation tag. | SageMaker AI Studio compute and storage costs per tenant are easy to monitor with a dedicated account. | SageMaker AI Studio compute costs per tenant need to be calculated using custom tags. <br /> SageMaker AI Studio storage costs cannot be monitored per domain since all tenants share the same EFS volume. |
| Service quotas are set at the account level, so a single tenant could still use up all resources.  | Service quotas can be set at the account level for each tenant.  | Service quotas are set at the account level, so a single tenant could still use up all resources.  |
| Scaling to multiple tenants can be achieved through infrastructure as code (IaC) or Service Catalog. | Scaling to multiple tenants involve Organizations and vending multiple accounts.  | Scaling needs a tenant specific role for each new tenant, and user profiles need to be manually tagged with tenant names. |
| Collaboration between users within a tenant is possible through shared spaces. | Collaboration between user within a tenant is possible through shared spaces. | All tenants will have access to the same shared space for collaboration. |

## SageMaker AI Studio domain backup and recovery
<a name="sagemaker-studio-domain-backup-and-recovery"></a>

In the event of an accidental EFS delete, or when a domain needs to be recreated due to changes in networking or authentication, follow these instructions.

### Option 1: Back up from existing EFS using EC2
<a name="option-1"></a>

#### SageMaker Studio domain backup
<a name="sagemaker-studio-domain-backup"></a>

1. List user profiles and spaces in SageMaker Studio ([CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-user-profiles.html), [SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)).

1. Map user profiles/spaces to UIDs on EFS.

   1. For each user in list of users/spaces, describe the user profile/space ([CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-user-profile.html), [SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)).

   1. Map user profile/space to `HomeEfsFileSystemUid`.

   1. Map user profile to `UserSettings['ExecutionRole']` if users have distinct execution roles.

   1. Identify the default Space execution role.

1. Create a new domain and specify the default Space execution role.

1. Create user profiles and spaces.
   + For each user in list of users, create user profile ([CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-user-profile.html), [SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)) using the execution role mapping.

1. Create a mapping for the new EFS and UIDs.

   1. For each user in list of users, describe user profile ([CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-user-profile.html), [SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)).

   1. Map user profile to `HomeEfsFileSystemUid`.

1. Optionally, delete all apps, user profiles, spaces, and then delete the domain.

#### EFS backup
<a name="efs-backup"></a>

To back up EFS, use the following instructions:

1. Launch the EC2 instance, and attach the old SageMaker Studio domain’s inbound/outbound security groups to the new EC2 instance (allow NFS traffic over TCP on port 2049. Refer to [Connect SageMaker Studio Notebooks in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html#:~:text=NFS%20traffic%20over%20TCP%20on%20port%202049%20between%20the%20domain%20and%20the%20Amazon%20EFS%20volume.).

1. Mount the SageMaker Studio EFS volume to the new EC2 instance. Refer to [Mounting EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html).

1. Copy over the files to EBS local storage: `>sudo cp -rp /efs /studio-backup:`

   1. Attach the new domain security groups to the EC2 instance.

   1. Mount the new EFS volume to the EC2 instance.

   1. Copy files to the new EFS volume.

   1. For each user in user’s collection:

      1. Create the directory: `mkdir new_uid`.

      1. Copy files from old UID directory to new UID directory.

      1. Change ownership for all files: `chown <new_UID>` for all files.

### Option 2: Back up from existing EFS using S3 and lifecycle configuration
<a name="option-2"></a>

1. Refer to [Migrate your work to an Amazon SageMaker notebook instance with Amazon Linux 2](https://aws.amazon.com/blogs/machine-learning/migrate-your-work-to-amazon-sagemaker-notebook-instance-with-amazon-linux-2/).

1. Create an S3 bucket for backup (such as `>studio-backup`.

1. List all user profiles with execution roles.

1. In the current SageMaker Studio domain, set a default LCC script at the domain level.
   + In the LCC, copy everything in `/home/sagemaker-user` to the user profile prefix in S3 (for example, `s3://studio-backup/studio-user1`).

1. Restart all default Jupyter Server apps (for the LCC to be run).

1. Delete all apps, user profiles, and domains.

1. Create a new SageMaker Studio domain.

1. Create new user profiles from the list of user profiles and execution roles.

1. Set up an LCC at the domain level:
   + In the LCC, copy everything in the user profile prefix in S3 to `/home/sagemaker-user`

1. Create default Jupyter Server apps for all users with the [LCC configuration](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateApp.html#:~:text=%22ResourceSpec%22%3A%20%7B%20%0A%20%20%20%20%20%20%22InstanceType%22%3A%20%22string%22%2C%0A%20%20%20%20%20%20%22LifecycleConfigArn%22%3A%20%22string%22%2C) ([CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-app.html), [SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app)).

## SageMaker Studio access using SAML assertion
<a name="sagemaker-studio-access-using-saml"></a>

Solution setup:

1. Create a SAML application in your external IdP.

1. Set up the external IdP as an Identity Provider in IAM.

1. Create a `SAMLValidator` Lambda function that can be accessed by the IdP (through a function URL or API Gateway).

1. Create a `GeneratePresignedUrl` Lambda function and an API Gateway to access the function.

1. Create an IAM role that users can assume to invoke the API Gateway. This role should be passed in SAML assertion as an attribute in the following format:
   + Attribute name: https://aws.amazon.com/SAML/Attributes/Role
   + Attribute value: `<IdentityProviderARN>`, `<RoleARN>`

1. Update the SAML Assertion Consumer Service (ACS) endpoint to the `SAMLValidator` invoke URL.

SAML validator example code:

```
import requests
import os
import boto3
from urllib.parse import urlparse, parse_qs
import base64
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
import json

# Config for calling AssumeRoleWithSAML
idp_arn = "arn:aws:iam::0123456789:saml-provider/MyIdentityProvider"
api_gw_role_arn = 'arn:aws:iam:: 0123456789:role/APIGWAccessRole'
studio_api_url = "abcdef.execute-api.us-east-1.amazonaws.com"
studio_api_gw_path = "https://" + studio_api_url + "/Prod "

# Every customer will need to get SAML Response from the POST call
def get_saml_response(event):
    saml_response_uri = base64.b64decode(event['body']).decode('ascii')
    request_body = parse_qs(saml_response_uri)
    print(f"b64 saml response: {request_body['SAMLResponse'][0]}")
    return request_body['SAMLResponse'][0]

def lambda_handler(event, context):
    sts = boto3.client('sts')

    # get temporary credentials
    response = sts.assume_role_with_saml(
                    RoleArn=api_gw_role_arn,
                    PrincipalArn=durga_idp_arn,
                    SAMLAssertion=get_saml_response(event)
                )
    auth = AWSRequestsAuth(aws_access_key=response['Credentials']['AccessKeyId'],
                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                      aws_host=studio_api_url,
                      aws_region='us-west-2',
                      aws_service='execute-api',
                      aws_token=response['Credentials']['SessionToken'])

    presigned_response = requests.post(
        studio_api_gw_path,
        data=saml_response_data,
        auth=auth)

    return presigned_response
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
