---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3.html
---

# Migrate data from an on-premises Hadoop environment to Amazon S3 using DistCp with AWS PrivateLink for Amazon S3
<a name="migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3"></a>

*Jason Owens, Andres Cantor, Jeff Klopfenstein, Bruno Rocha Oliveira, and Samuel Schmidt, Amazon Web Services*

## Summary
<a name="migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3-summary"></a>

This pattern demonstrates how to migrate nearly any amount of data from an on-premises Apache Hadoop environment to the Amazon Web Services (AWS) Cloud by using the Apache open-source tool [DistCp](https://hadoop.apache.org/docs/r1.2.1/distcp.html) with AWS PrivateLink for Amazon Simple Storage Service (Amazon S3). Instead of using the public internet or a proxy solution to migrate data, you can use [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) to migrate data to Amazon S3 over a private network connection between your on-premises data center and an Amazon Virtual Private Cloud (Amazon VPC). If you use DNS entries in Amazon Route 53 or add entries in the **/etc/hosts** file in all nodes of your on-premises Hadoop cluster, then you are automatically directed to the correct interface endpoint.

This guide provides instructions for using DistCp for migrating data to the AWS Cloud. DistCp is the most commonly used tool, but other migration tools are available. For example, you can use offline AWS tools like [AWS Snowball](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-snow-family.html#aws-snowball) or [AWS Snowmobile](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-snow-family.html#aws-snowmobile), or online AWS tools like [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/migrate-data.html) or [AWS DataSync](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-datasync-hadoop-aws-storage-services/). Additionally, you can use other open-source tools like [Apache NiFi](https://nifi.apache.org/).

## Prerequisites and limitations
<a name="migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3-prereqs"></a>

**Prerequisites**
+ An active AWS account with a private network connection between your on-premises data center and the AWS Cloud
+ [Hadoop](https://hadoop.apache.org/releases.html), installed on premises with [DistCp](https://hadoop.apache.org/docs/r1.2.1/distcp.html)
+ A Hadoop user with access to the migration data in the Hadoop Distributed File System (HDFS)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket-console.html) to put objects into an S3 bucket

**Limitations**

Virtual private cloud (VPC) limitations apply to AWS PrivateLink for Amazon S3. For more information, see [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) and [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html) (AWS PrivateLink documentation).

AWS PrivateLink for Amazon S3 doesn't support the following:
+ [Federal Information Processing Standard (FIPS) endpoints](https://aws.amazon.com/compliance/fips/)
+ [Website endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteEndpoints.html)
+ [Legacy global endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#deprecated-global-endpoint)

## Architecture
<a name="migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3-architecture"></a>

**Source technology stack**
+ Hadoop cluster with DistCp installed

**Target technology stack**
+ Amazon S3
+ Amazon VPC

**Target architecture**

![Hadoop cluster with DistCp copies data from on-premises environment through Direct Connect to S3.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8d2b47ae-e854-4e5d-8f19-b9c2606f2c59/images/b8a249bd-307b-41ec-b939-5039d0ae7123.png)

The diagram shows how the Hadoop administrator uses DistCp to copy data from an on-premises environment through a private network connection, such as AWS Direct Connect, to Amazon S3 through an Amazon S3 interface endpoint.

## Tools
<a name="migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3-tools"></a>

**AWS services**
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [Apache Hadoop DistCp](https://hadoop.apache.org/docs/current/hadoop-distcp/DistCp.html) (distributed copy) is a tool used for copying large inter-clusters and intra-clusters. DistCp uses Apache MapReduce for distribution, error handling and recovery, and reporting.

## Epics
<a name="migrate-data-from-an-on-premises-hadoop-environment-to-amazon-s3-using-distcp-with-aws-privatelink-for-amazon-s3-epics"></a>

### Migrate data to the AWS Cloud
<a name="migrate-data-to-the-aws-cloud"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an endpoint for AWS PrivateLink for Amazon S3. | 1. Sign in to the AWS Management Console and open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).<br />2. On the navigation pane, choose **Endpoints**, and then choose **Create Endpoint**.<br />3. For **Service category**, choose **AWS services**.<br />4. In the search box, enter **s3**, and then press **Enter**.<br />5. In the search results, choose the **com.amazonaws.<your-aws-region>.s3** service name where the value in the **Type** column is **Interface**.<br />6. For **VPC**, choose your VPC. For **Subnets**, choose your subnets.<br />7. For **Security group**, choose or create a security group that allows TCP 443.<br />8. Add tags based on your requirements and then choose **Create endpoint**. | AWS administrator |
| Verify the endpoints and find the DNS entries. | 1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/), choose **Endpoints**, and then select the endpoint that you created earlier.<br />2. On the **Details** tab, find the first DNS entry for **DNS names**. This is the Regional DNS entry. When you use this DNS name, requests alternate between DNS entries specific to Availability Zones.<br />3. Choose the **Subnets** tab. You can find the address of the endpoint’s elastic network interface in each Availability Zone. | AWS administrator |
| Check the firewall rules and routing configurations. | To confirm that your firewall rules are open and that your networking configuration is correctly set up, use Telnet to test the endpoint on port 443. For example:<pre>$ telnet vpce-<your-VPC-endpoint-ID>.s3.us-east-2.vpce.amazonaws.com 443<br /><br />Trying 10.104.88.6...<br /><br />Connected to vpce-<your-VPC-endpoint-ID>.s3.us-east-2.vpce.amazonaws.com.<br /><br />...<br /><br />$ telnet vpce-<your-VPC-endpoint-ID>.s3.us-east-2.vpce.amazonaws.com 443<br /><br />Trying 10.104.71.141...<br /><br />Connected to vpce-<your-VPC-endpoint-ID>.s3.us-east-2.vpce.amazonaws.com.</pre>If you use the Regional entry, a successful test shows that the DNS is alternating between the two IP addresses that you can see on the **Subnets** tab for your selected endpoint in the Amazon VPC console. | Network administrator, AWS administrator |
| Configure the name resolution. | You must configure the name resolution to allow Hadoop to access the Amazon S3 interface endpoint. You can’t use the endpoint name itself. Instead, you must resolve `<your-bucket-name>.s3.<your-aws-region>.amazonaws.com` or `*.s3.<your-aws-region>.amazonaws.com`. For more information on this naming limitation, see [Introducing the Hadoop S3A client](https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html#Introducing_the_Hadoop_S3A_client.) (Hadoop website).<br />Choose one of the following configuration options:+ Use on-premises DNS to resolve the private IP address of the endpoint. You can override behavior for all buckets or selected buckets. For more information, see "Option 2: Access Amazon S3 using Domain Name System Response Policy Zones (DNS RPZ)" in [Secure hybrid access to Amazon S3 using AWS PrivateLink](https://aws.amazon.com/blogs/networking-and-content-delivery/secure-hybrid-access-to-amazon-s3-using-aws-privatelink/) (AWS blog post).<br />+ Configure on-premises DNS to conditionally forward traffic to the resolver inbound endpoints in the VPC. Traffic is forwarded to Route 53. For more information, see "Option 3: Forwarding DNS requests from on premises using Amazon Route 53 Resolver Inbound Endpoints" in [Secure hybrid access to Amazon S3 using AWS PrivateLink](https://aws.amazon.com/blogs/networking-and-content-delivery/secure-hybrid-access-to-amazon-s3-using-aws-privatelink/) (AWS blog post).<br />+ Edit the **/etc/hosts** file on all the nodes in your Hadoop cluster. This is a temporary solution for testing and isn't recommended for production. To edit the **/etc/hosts** file, add an entry for either `<your-bucket-name>.s3.<your-aws-region>.amazonaws.com` or `s3.<your-aws-region>.amazonaws.com`. The **/etc/hosts** file can’t have multiple IP addresses for an entry. You must choose a single IP address from one of the Availability Zones, which then becomes a single point of failure. | AWS administrator |
| Configure authentication for Amazon S3. | To authenticate to Amazon S3 through Hadoop, we recommend that you export temporary role credentials to the Hadoop environment. For more information, see [Authenticating with S3](https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html#Authenticating_with_S3) (Hadoop website). For long-running jobs, you can create a user and assign a policy that has permissions to put data into an S3 bucket only. The access key and secret key can be stored on Hadoop, accessible only to the DistCp job itself and to the Hadoop administrator. For more information on storing secrets, see [Storing secrets with Hadoop Credential Providers](https://hadoop.apache.org/docs/r3.1.1/hadoop-aws/tools/hadoop-aws/index.html#hadoop_credential_providers) (Hadoop website). For more information on other authentication methods, see [How to get credentials of an IAM role for use with CLI access to an AWS account](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) in the documentation for AWS IAM Identity Center (successor to AWS Single Sign-On).<br />To use temporary credentials, add the temporary credentials to your credentials file, or run the following commands to export the credentials to your environment:<pre>export AWS_SESSION_TOKEN=SECRET-SESSION-TOKEN<br />export AWS_ACCESS_KEY_ID=SESSION-ACCESS-KEY<br />export AWS_SECRET_ACCESS_KEY=SESSION-SECRET-KEY</pre><br />If you have a traditional access key and secret key combination, run the following commands:<pre>export AWS_ACCESS_KEY_ID=my.aws.key<br />export AWS_SECRET_ACCESS_KEY=my.secret.key</pre>If you use an access key and secret key combination, then change the credentials provider in the DistCp commands from `"org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider"` to `"org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider"`. | AWS administrator |
| Transfer data by using DistCp. | To use DistCp to transfer data, run the following commands:<pre>hadoop distcp -Dfs.s3a.aws.credentials.provider=\<br />"org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider" \<br />-Dfs.s3a.access.key="${AWS_ACCESS_KEY_ID}" \<br />-Dfs.s3a.secret.key="${AWS_SECRET_ACCESS_KEY}" \<br />-Dfs.s3a.session.token="${AWS_SESSION_TOKEN}" \<br />-Dfs.s3a.path.style.access=true \<br />-Dfs.s3a.connection.ssl.enabled=true \<br />-Dfs.s3a.endpoint=s3.<your-aws-region>.amazonaws.com \<br />hdfs:///user/root/ s3a://<your-bucket-name></pre>The AWS Region of the endpoint isn’t automatically discovered when you use the DistCp command with AWS PrivateLink for Amazon S3. Hadoop 3.3.2 and later versions resolve this issue by enabling the option to explicitly set the AWS Region of the S3 bucket. For more information, see [S3A to add option fs.s3a.endpoint.region to set AWS region](https://issues.apache.org/jira/browse/HADOOP-17705) (Hadoop website).<br />For more information on additional S3A providers, see [General S3A Client configuration](https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html#General_S3A_Client_configuration) (Hadoop website). For example, if you use encryption, you can add the following option to the series of commands above depending on your type of encryption:<pre>-Dfs.s3a.server-side-encryption-algorithm=AES-256 [or SSE-C or SSE-KMS]</pre>To use the interface endpoint with S3A, you must create a DNS alias entry for the S3 Regional name (for example, `s3.<your-aws-region>.amazonaws.com`) to the interface endpoint. See the *Configure authentication for Amazon S3* section for instructions. This workaround is required for Hadoop 3.3.2 and earlier versions. Future versions of S3A won’t require this workaround.<br />If you have signature issues with Amazon S3, add an option to use Signature Version 4 (SigV4) signing:<pre>-Dmapreduce.map.java.opts="-Dcom.amazonaws.services.s3.enableV4=true"</pre> | Migration engineer, AWS administrator |
