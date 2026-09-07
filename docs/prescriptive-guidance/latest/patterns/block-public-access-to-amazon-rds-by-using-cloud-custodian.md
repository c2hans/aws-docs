---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/block-public-access-to-amazon-rds-by-using-cloud-custodian.html
---

# Block public access to Amazon RDS by using Cloud Custodian
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian"></a>

*abhay kumar and Dwarika Patra, Amazon Web Services*

## Summary
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-summary"></a>

Many organizations run their workloads and services on multiple cloud vendors. In these hybrid cloud environments, the cloud infrastructure needs strict cloud governance, in addition to the security provided by the individual cloud providers. A cloud database such as Amazon Relational Database Service (Amazon RDS) is one important service that must be monitored for any access and permission vulnerabilities. Although you can restrict access to the Amazon RDS database by configuring a security group, you can add a second layer of protection to prohibit actions such as public access. Blocking public access helps you with General Data Protection Regulation (GDPR), Health Insurance Portability and Accountability Act (HIPAA), National Institute of Standards and Technology (NIST), and Payment Card Industry Data Security Standard (PCI DSS) compliance.

Cloud Custodian is an open-source rules engine that you can use to enforce access restrictions for Amazon Web Services (AWS) resources such as Amazon RDS. With Cloud Custodian, you can set rules that validate the environment against defined security and compliance standards. You can use Cloud Custodian to manage your cloud environments by helping to ensure compliance with security policies, tag policies, and garbage collection of unused resources and cost management. With Cloud Custodian, you can use a single interface for implementing governance in a hybrid cloud environment. For example, you could use the Cloud Custodian interface to interact with AWS and Microsoft Azure, reducing the effort of working with mechanisms such as AWS Config, AWS security groups, and Azure policies.

This pattern provides instructions for using Cloud Custodian on AWS to enforce restriction of public accessibility on Amazon RDS instances.

## Prerequisites and limitations
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ [A key pair](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds-create)
+ AWS Lambda installed

## Architecture
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-architecture"></a>

The following diagram shows Cloud Custodian deploying the policy to AWS Lambda, AWS CloudTrail initiating the `CreateDBInstance` event, and the Lambda function setting `PubliclyAccessible` to false on Amazon RDS.

![Using Cloud Custodian on AWS to restrict public access to Amazon RDS instances.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/90f9537e-9365-4da2-8a28-da0ff374743c/images/6d04ca3b-6aa4-4c62-ade9-8b7474928c5e.png)

## Tools
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-tools"></a>

**AWS services**
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.

**Other tools**
+ [Cloud Custodian](https://cloudcustodian.io/) unifies the tools and scripts that many organizations use to manage their public cloud accounts into one open source tool. It uses a stateless rules engine for policy definition and enforcement, with metrics, structured outputs, and detailed reporting for cloud infrastructure. It integrates tightly with a serverless runtime to provide real-time remediation and response with low operational overhead.

## Epics
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-epics"></a>

### Set up the AWS CLI
<a name="set-up-the-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the AWS CLI. | To install the AWS CLI, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html). | AWS administrator |
| Set up AWS credentials. | Configure the settings that the AWS CLI uses to interact with AWS, including the AWS Region and the output format that you want to use.<pre>$>aws configure<br />AWS Access Key ID [None]: <your_access_key_id><br />AWS Secret Access Key [None]: <your_secret_access_key><br />Default region name [None]:<br />Default output format [None]:</pre><br />For more information, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html). | AWS administrator |
| Create an IAM role. | To create an IAM role with the Lambda execution role, run the following command.<pre>aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17",		 	 	 "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}</pre> | AWS DevOps |

### Set up Cloud Custodian
<a name="set-up-cloud-custodian"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Cloud Custodian. | To install Cloud Custodian for your operating system and environment, follow the instructions in the [Cloud Custodian documentation](https://cloudcustodian.io/docs/quickstart/index.html#install-cc). | DevOps engineer |
| Check the Cloud Custodian schema. | To see the complete list of Amazon RDS resources against which you can run policies, use the following command.<pre>custodian schema aws.rds</pre> | DevOps engineer |
| Create the Cloud Custodian policy. | Save the code that’s under *Cloud Custodian policy file* in the [Additional information](#block-public-access-to-amazon-rds-by-using-cloud-custodian-additional) section using a YAML extension. | DevOps engineer |
| Define Cloud Custodian actions to change the publicly accessible flag. | 1. Locate the custodian code (for example, `/Users/abcd/custodian/lib/python3.9/site-packages/c7n/resources/rds.py`).<br />2. Locate the `RDSSetPublicAvailability` class in `rds.py`, and modify this class by using the code that’s under *c7n resources rds.py file* in the [Additional information](#block-public-access-to-amazon-rds-by-using-cloud-custodian-additional) section. | DevOps engineer |
| Perform a dry run. | (Optional) To check which resources are identified by the policy without running any actions on the resources, use the following command.<pre>custodian run -dryrun <policy_name>.yaml -s <output_directory></pre> | DevOps engineer |

### Deploy the policy
<a name="deploy-the-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the policy by using Lambda. | To create the Lambda function that will run the policy, use the following command.<pre>custodian run -s policy.yaml</pre><br />This policy will then be initiated by the AWS CloudTrail `CreateDBInstance` event.<br />As a result, AWS Lambda will set the publicly accessible flag to `false` for instances that match the criteria. | DevOps engineer |

## Related resources
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-resources"></a>
+ [AWS Lambda website](https://aws.amazon.com/lambda/)
+ [Amazon RDS website](https://aws.amazon.com/rds/)
+ [Cloud Custodian documentation](https://cloudcustodian.io/docs/quickstart/index.html)

## Additional information
<a name="block-public-access-to-amazon-rds-by-using-cloud-custodian-additional"></a>

**Cloud Custodian policy YAML file**

```
policies:
  - name: "block-public-access"
    resource: rds
    description: |
      This Enforcement blocks public access for RDS instances.
    mode:
      type: cloudtrail
      events:
        - event: CreateDBInstance # Create RDS instance cloudtrail event
          source: rds.amazonaws.com
          ids: requestParameters.dBInstanceIdentifier
      role: arn:aws:iam::1234567890:role/Custodian-compliance-role
    filters:
      - type: event
        key: 'detail.requestParameters.publiclyAccessible'
        value: true
    actions:
      - type: set-public-access
        state: false
```

**c7n resources rds.py file**

```
@actions.register('set-public-access')
 class RDSSetPublicAvailability(BaseAction):

     schema = type_schema(
         "set-public-access",
         state={'type': 'boolean'})
     permissions = ('rds:ModifyDBInstance',)

     def set_accessibility(self, r):
         client = local_session(self.manager.session_factory).client('rds')
         waiter = client.get_waiter('db_instance_available')
         waiter.wait(DBInstanceIdentifier=r['DBInstanceIdentifier'])
         client.modify_db_instance(
             DBInstanceIdentifier=r['DBInstanceIdentifier'],
             PubliclyAccessible=self.data.get('state', False))

     def process(self, rds):
         with self.executor_factory(max_workers=2) as w:
             futures = {w.submit(self.set_accessibility, r): r for r in rds}
             for f in as_completed(futures):
                 if f.exception():
                     self.log.error(
                         "Exception setting public access on %s  \n %s",
                         futures[f]['DBInstanceIdentifier'], f.exception())
         return rds
```

**Security Hub CSPM integration**

Cloud Custodian can be integrated with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) to send security findings and attempt remediation actions. For more information, see [Announcing Cloud Custodian Integration with AWS Security Hub CSPM](https://aws.amazon.com/blogs/opensource/announcing-cloud-custodian-integration-aws-security-hub/).
