---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# Using the dataset browser API
<a name="fs-using-the-finspace-api"></a>

Use the topics in this section to understand how to use the FinSpace Dataset browser APIs.

**Topics**
+ [Accessing the FinSpace credentials](#accessing-credentials)
+ [Loading data from an Amazon S3 Bucket using the dataset browser API](#access-s3-buckets)

## Accessing the FinSpace credentials
<a name="accessing-credentials"></a>

To use the FinSpace Dataset browser API operations, you need to configure a user for programmatic access using the FinSpace web application. For more information, see [Configuring a user for programmatic access using FinSpace](https://docs.aws.amazon.com/finspace/latest/userguide/temporary-credentials.html#obtaining-credentials-programmatically) in the *Amazon FinSpace User Guide*. There are two ways to access the API credentials.

1. **Copy the API credentials from FinSpace web application - **Use API credentials that are associated with your user profile in Dataset browser. The credentials are only valid for 60 minutes. Use the following procedure to procure short term API credentials to use with FinSpace SDK.

   1. From the Dataset browser homepage, go to the gear menu. Choose **API Credentials**.

   1. Copy the **Access Key ID, Secret Access Key, Session Token**.

   1. Use the credentials to use the FinSpace Dataset browser APIs.

      ```
                                #!/usr/bin/env python
                                import boto3
                                session = boto3.session.Session()
                                finSpaceClient = session.client(
                                    region_name='us-east-1',
                                    service_name='finspace-data',
                                    aws_access_key_id='Specify Access Key ID',
                                    aws_secret_access_key='Specify Secret Access Key',
                                    aws_session_token='Specify Session Token'
                                )
      ```

1. **Access credentials programmatically using IAM access key id and secret access key - ** Your Amazon Resource Name (ARN) must be registered with your user profile in the FinSpace Dataset browser web application to use this method. Please contact your administrator to verify. You can find your FinSpace environment id from the sign-in URL that you use to login to your Dataset browser web application. For example, if your FinSpace sign-in URL is https://vs57phhvijir4kv5rf6ywt.us-east-1.amazonfinspace.com, the environment id is vs57phhvijir4kv5rf6ywt.

   ```
                             #!/usr/bin/env python
                             import boto3
                             REGION = "us-east-1"
                             PROD_ENVIRONMENT_ID = "Specify FinSpace environment id"
                             AWS_ACCESS_KEY_ID = "Specify AWS_ACCESS_KEY_ID" # Access key id of your user
                             AWS_SECRET_ACCESS_KEY = "Specify AWS_SECRET_ACCESS_KEY" # Secret access key for your user
                             session = boto3.Session(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, region_name=REGION)
                             client = session.client(
                                 region_name=REGION,
                                 service_name='finspace-data',
                                 aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                             )
                             apiCredentials = client.get_programmatic_access_credentials(environmentId=PROD_ENVIRONMENT_ID)
                             finSpaceClient = session.client(
                                 service_name='finspace-data',
                                 aws_access_key_id=apiCredentials['credentials']['AccessKeyId'],
                                 aws_secret_access_key=apiCredentials['credentials']['SecretAccessKey'],
                                 aws_session_token=apiCredentials['credentials']['SessionToken']
   			)
   ```

## Loading data from an Amazon S3 Bucket using the dataset browser API
<a name="access-s3-buckets"></a>

 You can load data from an external S3 bucket into your Dataset browser environment when you create or update a change set. To do this, you will first need to enable access from your Dataset browser environment to an S3 bucket where the data resides.

**Note**
 In order to setup access to an S3 bucket, you must be authorized to access the FinSpace page in AWS Management Console and make changes to bucket-level permissions in Amazon S3.

 ** Find your FinSpace Dataset browser infrastructure account number in AWS Management console **

1.  Sign in to your AWS account and open FinSpace from the AWS Management Console. It is located under Analytics, and you can find it by searching for *FinSpace*.

1. In FinSpace, choose **Dataset browser**.

1.  In the Dataset browser page, from the list of environments, choose the environment that you want to setup to access an S3 bucket.

1.  On the environment page, copy and save the **FinSpace infrastructure account** name.

 ** Setup access for FinSpace infrastructure account in S3 bucket policy **

1.  Sign in to your AWS account and open Amazon S3 from the AWS Management Console. It is located under Storage, and you can find it by searching for S3.

1.  Choose the bucket that you want to access from your FinSpace Dataset browser environment.

1.  Set a bucket policy for the bucket with following json code. For example, if your bucket name is `example-bucket` and your FinSpace infrastructure account number is `123456789101` below would be the example policy.

    Using the above policy, you should be able to access `example-bucket` from the FinSpace environment, which is associated with the FinSpace infrastructure account number `123456789101` .

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
