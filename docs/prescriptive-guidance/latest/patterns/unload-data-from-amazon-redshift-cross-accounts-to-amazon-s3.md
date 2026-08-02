---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html
---

# Unload data from an Amazon Redshift cluster across accounts to Amazon S3
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3"></a>

*Andrew Kamel, Amazon Web Services*

## Summary
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-summary"></a>

When you test applications, it's helpful to have production data in your test environment. Using production data can give you a more accurate assessment of the application that you're developing.

This pattern extracts data from an Amazon Redshift cluster in a production environment to an Amazon Simple Storage Service (Amazon S3) bucket in a development environment on Amazon Web Services (AWS).

The pattern steps through the setup of both DEV and PROD accounts, including the following:
+ Required resources
+ AWS Identity and Access Management (IAM) roles
+ Network adjustments to subnets, security groups, and the virtual private cloud (VPC) to support the Amazon Redshift connection
+ An example AWS Lambda function with a Python runtime for testing the architecture

To grant access to the Amazon Redshift cluster, the pattern uses AWS Secrets Manager to store the relevant credentials. The benefit is having all the needed information to directly connect to the Amazon Redshift cluster without needing to know where the Amazon Redshift cluster resides. Additionally, you can [monitor use of the secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html).

The secret saved in Secrets Manager includes the Amazon Redshift cluster's host, database name, port, and relevant credentials.

For information about security considerations when using this pattern, see the [Best practices](#unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-best-practices) section.

## Prerequisites and limitations
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-prereqs"></a>

**Prerequisites **
+ An [Amazon Redshift cluster running](https://docs.aws.amazon.com/redshift/latest/gsg/new-user.html) in the PROD account
+ An [S3 bucket created](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the DEV account
+ [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html) between the DEV and PROD accounts, with [route tables adjusted](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html) accordingly
+ [DNS hostnames and DNS resolution enabled](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) for both peered VPCs

**Limitations **
+ Depending on the amount of data that you want to query, the Lambda function might time out.

  If your run takes more time than the maximum Lambda timeout (15 minutes), use an asynchronous approach for your Lambda code. The code example for this pattern uses the [psycopg2](https://github.com/psycopg/psycopg2) library for Python, which doesn't currently support asynchronous processing.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-architecture"></a>

The following diagram shows the target architecture, with DEV and PROD accounts.

![The Lambda VPC in the DEV account and the Amazon Redshift VPC in the PROD account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5c83c617-3a85-4aea-a7a7-930f406d1cef/images/fa4d01df-483d-4454-9711-b391ebbe4629.png)

The diagram shows the following workflow:

1. The Lambda function in the DEV account assumes the IAM role that's required to access the Amazon Redshift credentials in Secrets Manager in the PROD account.

   The Lambda function then retrieves the Amazon Redshift cluster secret.

1. The Lambda function in the DEV account uses the information to connect to the Amazon Redshift cluster in the PROD account through the peered VPCs.

   The Lambda function then sends an unload command to query the Amazon Redshift cluster in the PROD account.

1. The Amazon Redshift cluster in the PROD account assumes the relevant IAM role to access the S3 bucket in the DEV account.

   The Amazon Redshift cluster unloads the queried data to the S3 bucket in the DEV account.

**Querying data from Amazon Redshift**

The following diagram shows the roles that are used to retrieve the Amazon Redshift credentials and connect to the Amazon Redshift cluster. The workflow is initiated by the Lambda function.

![The three-step process for assuming roles across accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5c83c617-3a85-4aea-a7a7-930f406d1cef/images/ab25b72c-773c-4d58-9012-4a3755c181ff.png)

The diagram shows the following workflow:

1. The `CrossAccount-SM-Read-Role` in the DEV account assumes the `SM-Read-Role` in the PROD account.

1. The `SM-Read-Role` role uses the attached policy to retrieve the secret from Secrets Manager.

1. The credentials are used to access the Amazon Redshift cluster.

**Uploading data to Amazon S3**

The following diagram shows the cross-account read-write process for extracting data and uploading it to Amazon S3. The workflow is initiated by the Lambda function. The pattern [chains IAM roles in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html#authorizing-redshift-service-chaining-roles). The unload command that comes from the Amazon Redshift cluster assumes the `CrossAccount-S3-Write-Role`, and then assumes the `S3-Write-Role`. This role chaining gives Amazon Redshift access to Amazon S3.

![The roles that get credentials, access Amazon Redshift, and upload data to Amazon S3.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5c83c617-3a85-4aea-a7a7-930f406d1cef/images/d2982fc6-1d12-4f9d-9493-a99ce691d693.png)

The workflow includes the following steps:

1. The `CrossAccount-SM-Read-Role` in the DEV account assumes the `SM-Read-Role` in the PROD account.

1. The `SM-Read-Role` retrieves the Amazon Redshift credentials from Secrets Manager.

1. The Lambda function connects to the Amazon Redshift cluster and sends a query.

1. The Amazon Redshift cluster assumes the `CrossAccount-S3-Write-Role`.

1. The `CrossAccount-S3-Write-Role` assumes the `S3-Write-Role` in the DEV account.

1. The query results are unloaded to the S3 bucket in the DEV account.

## Tools
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-tools"></a>

**AWS services**
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) is a managed petabyte-scale data warehouse service in the AWS Cloud.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

The code for this pattern is available in the GitHub [unload-redshift-to-s3-python](https://github.com/aws-samples/unload-redshift-to-s3-python/) repository.

## Best practices
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-best-practices"></a>

**Security disclaimer**

Before you implement this solution, consider the following important security recommendations:
+ Remember that connecting development and production accounts can increase the scope and lower overall security posture. We recommend deploying this solution only temporarily, extracting the required portion of data and then immediately destroying the deployed resources. To destroy the resources, you should delete the Lambda function, remove any IAM roles and policies created for this solution, and revoke any network access that was granted between the accounts.
+ Consult your security and compliance teams before copying any data from production to development environments. Personally identifiable information (PII), Protected health information (PHI), and other confidential or regulated data should generally not be copied in this manner. Copy only publicly available, non-confidential information (for example, public stock data from a shop frontend). Consider tokenizing or anonymizing data, or generating synthetic test data, instead of using production data whenever possible. One of the [AWS security principles](https://docs.aws.amazon.com/en_us/wellarchitected/2022-03-31/framework/sec-design.html) is to keep people away from data. In other words, developers should not perform operations in the production account.
+ Restrict access to the Lambda function in the development account because it can read data from the Amazon Redshift cluster in the production environment.
+ To avoid disrupting the production environment, implement the following recommendations:
  + Use a separate, dedicated development account for testing and development activities.
  + Implement strict network access controls and limit traffic between accounts to only what is necessary.
  + Monitor and audit access to the production environment and data sources.
  + Implement least-privilege access controls for all resources and services involved.
  + Regularly review and rotate credentials, such as AWS Secrets Manager secrets and IAM role access keys.
+ Refer to the following security documentation for the services used in this article:
  + [AWS Lambda security](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html)
  + [Amazon Redshift security](https://docs.aws.amazon.com/redshift/latest/mgmt/iam-redshift-user-mgmt.html)
  + [Amazon S3 security](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html)
  + [AWS Secrets Manager security](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security.html)
  + [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

Security is a top priority when accessing production data and resources. Always follow best practices, implement least-privilege access controls, and regularly review and update your security measures.

## Epics
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-epics"></a>

### Query data from Amazon Redshift
<a name="query-data-from-amazon-redshift"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a secret for the Amazon Redshift cluster. | To create the secret for the Amazon Redshift cluster, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Create a role to access Secrets Manager. | To create the role, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |

### Upload data to Amazon S3
<a name="upload-data-to-s3"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a role to access the S3 bucket. | To create the role for accessing the S3 bucket, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Create the Amazon Redshift role. | To create the Amazon Redshift role, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |

### Deploy the Lambda function
<a name="deploy-the-lam-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Lambda function. | To deploy a Lambda function in the peered VPC, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |

### Test the architecture
<a name="test-the-architecture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Import the required resources. | To import the required resources, run the following commands:<pre>import ast<br />import boto3<br />import psycopg2<br />import base64<br />from botocore.exceptions import ClientError</pre> | App developer |
| Run the Lambda handler function. | The Lambda function uses AWS Security Token Service (AWS STS) for cross-account access and temporary credential management. The function uses the AssumeRole API operation to temporarily assume the permissions of the `sm_read_role` IAM role.<br />To run the Lambda function, use the following example code:<pre>def lambda_handler(event, context):<br />    sts_client = boto3.client('sts')<br /><br />    # Secrets Manager Configurations<br />    secret_name = "redshift_creds"<br />    sm_region = "eu-west-1"<br />    sm_read_role = "arn:aws:iam::PROD_ACCOUNT_NUMBER:role/SM-Read-Role"<br /><br />    # S3 Bucket Configurations<br />    s3_bucket_path = "s3://mybucket/"<br />    s3_bucket_region = "eu-west-1"<br />    s3_write_role = "arn:aws:iam::DEV_ACCOUNT_NUMBER:role/S3-Write-Role"<br /><br />    # Redshift Configurations<br />    sql_query = "select * from category"<br />    redshift_db = "dev"<br />    redshift_s3_write_role = "arn:aws:iam::PROD_ACCOUNT_NUMBER:role/CrossAccount-S3-Write-Role"<br /><br />    chained_s3_write_role = "%s,%s" % (redshift_s3_write_role, s3_write_role)<br /><br />    assumed_role_object = sts_client.assume_role(<br />        RoleArn=sm_read_role,<br />        RoleSessionName="CrossAccountRoleAssumption",<br />        ExternalId="YOUR_EXTERNAL_ID",<br />    )<br />    credentials = assumed_role_object['Credentials']<br /><br />    secret_dict = ast.literal_eval(get_secret(credentials, secret_name, sm_region))<br />    execute_query(secret_dict, sql_query, s3_bucket_path, chained_s3_write_role, s3_bucket_region, redshift_db)<br /><br />    return {<br />        'statusCode': 200<br />    }</pre> | App developer |
| Get the secret. | To get the Amazon Redshift secret, use the following example code:<pre>def get_secret(credentials, secret_name, sm_region):<br />    # Create a Secrets Manager client<br />    session = boto3.session.Session()<br />    sm_client = session.client(<br />        service_name='secretsmanager',<br />        aws_access_key_id=credentials['AccessKeyId'],<br />        aws_secret_access_key=credentials['SecretAccessKey'],<br />        aws_session_token=credentials['SessionToken'],<br />        region_name=sm_region<br />    )<br /><br />    try:<br />        get_secret_value_response = sm_client.get_secret_value(<br />            SecretId=secret_name<br />        )<br />    except ClientError as e:<br />        print(e)<br />        raise e<br />    else:<br />        if 'SecretString' in get_secret_value_response:<br />            return get_secret_value_response['SecretString']<br />        else:<br />            return base64.b64decode(get_secret_value_response['SecretBinary'])</pre> | App developer |
| Run the unload command. | To unload the data to the S3 bucket, use the following example code.<pre>def execute_query(secret_dict, sql_query, s3_bucket_path, chained_s3_write_role, s3_bucket_region, redshift_db):<br />    conn_string = "dbname='%s' port='%s' user='%s' password='%s' host='%s'" \<br />                  % (redshift_db,<br />                     secret_dict["port"],<br />                     secret_dict["username"],<br />                     secret_dict["password"],<br />                     secret_dict["host"])<br /><br />    con = psycopg2.connect(conn_string)<br /><br />    unload_command = "UNLOAD ('{}') TO '{}' IAM_ROLE '{}' DELIMITER '|' REGION '{}';" \<br />        .format(sql_query,<br />                s3_bucket_path + str(datetime.datetime.now()) + ".csv",<br />                chained_s3_write_role,<br />                s3_bucket_region)<br /><br />    # Opening a cursor and run query<br />    cur = con.cursor()<br />    cur.execute(unload_command)<br /><br />    print(cur.fetchone())<br />    cur.close()<br />    con.close()</pre> | App developer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the Lambda function. | To avoid incurring unplanned costs, remove the resources and the connection between the DEV and PROD accounts.<br />To remove the Lambda function, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Remove the IAM roles and policies. | Remove the IAM roles and policies from the DEV and PROD accounts.<br />In the DEV account, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html)<br />In the PROD account, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Delete the secret in Secrets Manager. | To delete the secret, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Remove VPC peering and security group rules. | To remove VPC peering and security group rules, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Remove data from the S3 bucket. | To remove the data from Amazon S3, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Clean up AWS KMS keys. | If you created any custom AWS KMS keys for encryption, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |
| Review and delete Amazon CloudWatch logs. | To delete the CloudWatch logs, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3.html) | DevOps engineer |

## Related resources
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-resources"></a>
+ [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
+ [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html)
+ [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
+ [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+ [AWS security principles](https://docs.aws.amazon.com/en_us/wellarchitected/2022-03-31/framework/sec-design.html)

## Additional information
<a name="unload-data-from-amazon-redshift-cross-accounts-to-amazon-s3-additional"></a>

After you unload the data from Amazon Redshift to Amazon S3, you can analyze it by using Amazon Athena.

[Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) is a big data query service that's beneficial when you need to access large volumes of data. You can use Athena without having to provision servers or databases. Athena supports complex queries, and you can run it on different objects.

As with most AWS services, the main benefit to using Athena is that it provides great flexibility in how you run queries without the added complexity. When you use Athena, you can query different data types, such as CSV and JSON, in Amazon S3 without changing the data type. You can query data from various sources, including outside AWS. Athena reduces complexity because you don't have to manage servers. Athena reads data directly from Amazon S3 without loading or changing the data before you run the query.
