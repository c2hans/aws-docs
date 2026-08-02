---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html
---

# Build COBOL Db2 programs by using AWS Mainframe Modernization and AWS CodeBuild
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild"></a>

*Luis Gustavo Dantas and Eduardo Zimelewicz, Amazon Web Services*

## Summary
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-summary"></a>

**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

This pattern explains how to create a simple AWS CodeBuild project to precompile and bind COBOL Db2 programs by using the AWS Mainframe Modernization Replatform tools. This enables the deployment and execution of these programs in the AWS Mainframe Modernization Replatform runtime environment.

COBOL, a business-oriented programming language, powers many critical applications due to its reliability and readability. IBM Db2, a relational database management system, manages large volumes of data efficiently and integrates with COBOL programs through SQL. Together, COBOL and Db2 form the backbone of mission-critical operations in industries such as finance and government, despite the emergence of newer technologies.

Migrating COBOL and Db2 components from the mainframe environment to other platforms leads to challenges such as platform compatibility, integration complexity, data migration, and performance optimization. Moving these critical components requires careful planning, technical expertise, and resources to ensure a smooth migration while maintaining reliability and functionality.

The AWS Mainframe Modernization service provides tools and resources to replatform mainframe applications and databases to run on AWS infrastructure, such as Amazon Elastic Compute Cloud (Amazon EC2) instances. This involves moving mainframe workloads to the cloud without major code changes.

The Db2 precompile and bind process is essential for optimizing the performance and reliability of database applications. Precompilation transforms embedded SQL statements into executable code, which reduces runtime overhead and enhances efficiency. The bind process links the precompiled code with database structures, facilitating access paths and query optimization. This process ensures data integrity, improves application responsiveness, and guards against security vulnerabilities. Properly precompiled and bound applications minimize resource consumption, enhance scalability, and mitigate the risks of SQL injection attacks.

## Prerequisites and limitations
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-prereqs"></a>

**Prerequisites **
+ An AWS account and administrative-level console access.
+ An IBM Db2 database system, such as IBM Db2 for z/OS or Db2 for Linux, Unix, and Windows (LUW).
+ The IBM Data Server Client software, which is available for download from the [IBM website](https://www.ibm.com/support/pages/download-initial-version-115-clients-and-drivers). For more information, see [IBM Data Server Client and Data Server Driver types](https://www.ibm.com/docs/en/db2/11.5?topic=overviews-data-server-clients).
+ A COBOL Db2 program to be compiled and bound. Alternatively, this pattern provides a basic sample program that you can use.
+ A virtual private cloud (VPC) on AWS with a private network. For information about creating a VPC, see the [Amazon Virtual Private Cloud (Amazon VPC) documentation](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).
+ A source control repository such as GitHub or GitLab.

**Limitations **
+ For AWS CodeBuild quotas, see [Quotas for AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/limits.html).
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-architecture"></a>

**Source technology stack**

The source stack includes:
+ COBOL programs that use a Db2 database to store data
+ IBM COBOL compiler and Db2 for z/OS precompiler
+ Other parts of the mainframe setup, such as the file system, transaction manager, and spool

**Target technology stack**

This pattern's approach works for two options: moving data from Db2 for z/OS to Db2 for LUW, or staying on Db2 for z/OS. The target architecture includes:
+ COBOL programs that use a Db2 database to store data
+ AWS Mainframe Modernization Replatform compilation tools
+ AWS CodeBuild as the infrastructure to build the application
+ Other AWS Cloud resources such as Amazon Linux

**Target architecture**

![Architecture for building COBOL Db2 programs on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5895fa34-f05b-4cc3-a59f-a596f9116c66/images/0dda414a-21a7-41d1-b86b-7ff3b1c6fbda.png)

The diagram illustrates the following:

1. The user uploads their code to a source control repository such as GitHub or GitLab.

1. AWS CodePipeline notices the change and gets the code from the repository.

1. CodePipeline starts AWS CodeBuild and sends the code.

1. CodeBuild follows the instructions in the `buildspec.yml` template (provided in the [Additional information](#build-cobol-db2-programs-mainframe-modernization-codebuild-additional) section) to:

   1. Get the IBM Data Server Client from an Amazon Simple Storage Service (Amazon S3) bucket.

   1. Install and set up the IBM Data Server Client.

   1. Retrieve Db2 credentials from AWS Secrets Manager.

   1. Connect to the Db2 server.

   1. Precompile, compile, and bind the COBOL program.

   1. Save the finished products in an S3 bucket for AWS CodeDeploy to use.

1. CodePipeline starts CodeDeploy.

1. CodeDeploy coordinates its agents, which are already installed in the runtime environments. The agents fetch the application from Amazon S3 and install it based on the instructions in `appspec.yml`.

To keep things simple and focused on the build,  the instructions in this pattern cover steps 1 through 4 but don't include the deployment of the COBOL Db2 program.

**Automation and scale**

For simplicity, this pattern describes how to provision resources manually. However, there are numerous automation options available, such as CloudFormation, AWS Cloud Development Kit (AWS CDK), and HashiCorp Terraform, which automate these tasks. For more information, see the [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) documentation.

## Tools
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-tools"></a>

**AWS services**
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) automates deployments to Amazon EC2 or on-premises instances, AWS Lambda functions, or Amazon Elastic Container Service (Amazon ECS) services.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) provides tools and resources to help you plan and implement migration and modernization from mainframes to AWS managed runtime environments.

**Other tools**
+ **Amazon ECR image for AWS Mainframe Modernization Replatform tools**. To compile a COBOL application, you'll need to initiate CodeBuild by using an Amazon Elastic Container Registry (Amazon ECR) image that contains the AWS Mainframe Modernization Replatform tools:

  `673918848628.dkr.ecr.<your-region>.amazonaws.com/m2-enterprise-build-tools:9.0.7.R1`

  For more information about the ECR image available, see the [tutorial](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-build-mf.html) in the *AWS Mainframe Modernization User Guide*.
+ [IBM Data Server Client](https://www.ibm.com/docs/en/db2/11.5?topic=overviews-data-server-clients) software is essential for precompiling and binding COBOL Db2 programs in CodeBuild. It acts as a bridge between the COBOL compiler and Db2.

## Best practices
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-best-practices"></a>
+ Not every COBOL program relies on Db2 as its data persistence layer. Make sure that compilation directives for accessing Db2 are applied only to COBOL programs that are specifically designed to interact with Db2. Implement a logic to distinguish between COBOL Db2 programs and COBOL programs that do not use Db2.
+ We recommend that you avoid compiling programs that haven't been modified. Implement a process to identify which programs require compilation.

## Epics
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-epics"></a>

### Create the cloud infrastructure
<a name="create-the-cloud-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket to host the IBM Data Server Client and pipeline artifacts. | You need to set up an S3 bucket to (a) upload the IBM Data Server Client, (b) store your code from the repository, and (c) store the results of the build process.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html)<br />For ways to create an S3 bucket, see the [Amazon S3 documentation.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) | General AWS |
| Upload the IBM Data Server Client to the S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html) | General AWS |
| Create an AWS Secrets Manager secret for your Db2 credentials. | To create a secret to securely store your DB2 credentials:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html)<br />For more information about creating secrets, see the [Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html). | General AWS |
| Verify that Db2 is accessible from the VPC subnet. | AWS CodeBuild needs a connection to the Db2 server so that the Data Server Client can perform precompilation and bind operations. Make sure that CodeBuild can reach the Db2 server through a secure connection.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html) | Network administrator, General AWS |

### Create the application artifacts
<a name="create-the-application-artifacts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the COBOL Db2 asset. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html) | App developer |
| Create the `buildspec.yml` file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html) | AWS DevOps |
| Connect your repository to CodePipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html)You will need the Amazon Resource Name (ARN) for the connection when you create the AWS Identity and Access Management (IAM) policy for CodePipeline in a later step. | AWS DevOps |

### Configure permissions
<a name="configure-permissions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM policy for CodeBuild. | The CodeBuild project requires access to some resources, including Secrets Manager and Amazon S3.<br />To set up the necessary permissions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html)<br />For more information about creating IAM policies, see the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html). | General AWS |
| Create an IAM role for CodeBuild. | To make the security policies available for CodeBuild, you need to configure an IAM role.<br />To create this role:<br />1. On the[ IAM console](https://console.aws.amazon.com/iam), in the navigation pane, choose **Roles**, **Create Role**.<br />3. For **Trusted entity type**, keep the default **AWS service** setting.<br />4. For **Use case**, select the CodeBuild service, and then choose **Next**.<br />4. In the list of available IAM policies, locate the policy you created for CodeBuild, and then choose **Next** to attach it to the role.<br />5. Specify a name for the role, and choose **Create role **to save it for future reference in CodeBuild.<br />For more information about creating an IAM role for an AWS service, see the[ IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). | General AWS |
| Create an IAM policy for CodePipeline. | The AWS CodePipeline pipeline requires access to some resources, including your code repository and Amazon S3.<br />Repeat the steps provided previously for CodeBuild to create an IAM policy for CodePipeline (in step 2, choose **CodePipeline** instead of **CodeBuild**). | AWS DevOps |
| Create an IAM role for CodePipeline. | To make the security policies available for CodePipeline, you need to configure an IAM role.<br />To create this role:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html) | AWS DevOps |

### Compile and bind the COBOL Db2 program
<a name="compile-and-bind-the-cobol-db2-program"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CodePipeline pipeline and CodeBuild project. | To create a CodePipeline pipeline and the CodeBuild project that compiles and binds the COBOL Db2 program:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-cobol-db2-programs-mainframe-modernization-codebuild.html) | AWS DevOps |
| Review the output. | Verify the success of the build by reviewing the CodePipeline build logs. | AWS DevOps |
| Check results in Db2. | Verify the package version on the SYSPLAN table.<pre>select CAST(NAME AS VARCHAR(10)) as name, VALIDATE, LAST_BIND_TIME, LASTUSED, CAST(PKGVERSION AS VARCHAR(10)) as PKGVERSION from SYSIBM.SYSPLAN where NAME = 'CDB2SMP' order by LAST_BIND_TIME desc<br /></pre><br />The version must match the CodeBuild build ID, which is `CDB2SMP` in our example:<pre>NAME       VALIDATE LAST_BIND_TIME             LASTUSED   PKGVERSION<br />---------- -------- -------------------------- ---------- ----------<br />CDB2SMP    B        2024-05-18-11.53.11.503738 01/01/0001 19</pre> |  |

## Troubleshooting
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Occasionally, the AWS console switches Regions when you move between services. | Make sure to verify the selected AWS Region whenever you switch between services.<br />The AWS Region selector is in the upper-right corner of the console window. |
| It can be difficult to identify Db2 connectivity issues from CodeBuild. | To troubleshoot connectivity problems, add the following DB2 connect command to the `buildspec.yml` file. This addition helps you debug and resolve connectivity issues.<pre>db2 connect to $DB_NAME user $DB2USER using $DB2PASS</pre> |
| Occasionally, the role pane in the IAM console doesn't immediately show the IAM policy you've created. | If you encounter a delay, refresh the screen to display the latest information. |

## Related resources
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-resources"></a>

**IBM documentation**
+ [IBM Data Server Client and driver types](https://www.ibm.com/docs/en/db2/11.5?topic=overviews-data-server-clients)
+ [Download IBM Data Server Client and driver types](https://www.ibm.com/support/pages/download-initial-version-115-clients-and-drivers)

**AWS documentation**
+ [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
+ [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
+ [AWS Mainframe Modernization User Guide](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html)
+ [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+ [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [AWS CodeDeploy User Guide** **](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-codedeploy.html)

## Additional information
<a name="build-cobol-db2-programs-mainframe-modernization-codebuild-additional"></a>

**CodeBuild policy**

Replace the placeholders `<RegionID>`, `<AccountID>`, `<SubnetARN>`, `<BucketARN>`, and `<DB2CredSecretARN>` with your values.

```
{"Version": "2012-10-17",
    "Statement": [
        {"Action": "ecr:GetAuthorizationToken", "Effect": "Allow", "Resource": "*" },
        {"Action": ["ecr:GetDownloadUrlForLayer", "ecr:BatchGetImage",
                    "ecr:BatchCheckLayerAvailability"],
         "Effect": "Allow",
         "Resource": "arn:aws:ecr:*:673918848628:repository/m2-enterprise-build-tools"},
        {"Action": "s3:PutObject", "Effect": "Allow", "Resource": "arn:aws:s3:::aws-m2-repo-*/*"},
        {"Action": ["logs:PutLogEvents", "logs:CreateLogStream", "logs:CreateLogGroup"],
         "Effect": "Allow", "Resource": "arn:aws:logs:<RegionId>:<AccountId>:*"},
        {"Action": ["ec2:DescribeVpcs", "ec2:DescribeSubnets",
                    "ec2:DescribeSecurityGroups", "ec2:DescribeNetworkInterfaces",
                    "ec2:DescribeDhcpOptions", "ec2:DeleteNetworkInterface",
                    "ec2:CreateNetworkInterface"],
         "Effect": "Allow", "Resource": "*"},
        {"Action": "ec2:CreateNetworkInterfacePermission",
         "Effect": "Allow", "Resource": ["<SubnetARN>"]},
        {"Action": "s3:*", "Effect": "Allow", "Resource": ["<BucketARN>/*","<BucketARN>"]},
        {"Action": "secretsmanager:GetSecretValue",
         "Effect": "Allow", "Resource": "<DB2CredSecretARN>"}
    ]
}
```

**CodePipeline policy**

Replace the placeholders `<BucketARN>` and `<ConnectionARN>` with your values.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {"Action": ["s3:List*", "s3:GetObjectVersion", "s3:GetObject", "s3:GetBucketVersioning" ],
        "Effect": "Allow",
        "Resource": ["<BucketARN>/*", "<BucketARN>"]},
        {"Action": ["codebuild:StartBuild", "codebuild:BatchGetBuilds"],
         "Effect": "Allow", "Resource": "*"},
        {"Action": ["codestar-connections:UseConnection"],
         "Effect": "Allow", "Resource": "<ConnectionARN>"}
        ]
}
```

**`buildspec.yml`**

Replace the `<your-bucket-name>` placeholder with your actual S3 bucket name.

```
version: 0.2
phases:
  pre_build:
    commands:
      - /var/microfocuslicensing/bin/mfcesd -no > /var/microfocuslicensing/logs/mfcesd_startup.log 2>&1 &
      - |
        mkdir $CODEBUILD_SRC_DIR/db2client
        aws s3 cp s3://<your-bucket-name>/v11.5.8_linuxx64_client.tar.gz $CODEBUILD_SRC_DIR/db2client/ >> /dev/null 2>&1
        tar -xf $CODEBUILD_SRC_DIR/db2client/v11.5.8_linuxx64_client.tar.gz -C $CODEBUILD_SRC_DIR/db2client/
        cd $CODEBUILD_SRC_DIR/db2client/
        ./client/db2_install -f sysreq -y -b /opt/ibm/db2/V11.5 >> /dev/null 2>&1
        useradd db2cli
        /opt/ibm/db2/V11.5/instance/db2icrt -s client -u db2cli db2cli
        DB2CRED=$(aws secretsmanager get-secret-value --secret-id dev-db2-cred | jq -r '.SecretString | fromjson')
        read -r DB2USER DB2PASS DB_NODE DB_HOST DB_PORT DB_NAME DB_QUAL <<<$(echo $DB2CRED | jq -r '.username, .password, .db2node, .db2host, .db2port, .db2name, .qualifier')
        . /home/db2cli/sqllib/db2profile
        db2 catalog tcpip node $DB_NODE remote $DB_HOST server $DB_PORT
        db2 catalog db $DB_NAME as $DB_NAME at node $DB_NODE authentication server
  build:
    commands:
      - |
        revision=$CODEBUILD_SRC_DIR/loadlib
        mkdir -p $revision; cd $revision
        . /opt/microfocus/EnterpriseDeveloper/bin/cobsetenv
        cob -zU $CODEBUILD_SRC_DIR/CDB2SMP.cbl -C "DB2(DB==${DB_NAME} PASS==${DB2USER}.${DB2PASS} VERSION==${CODEBUILD_BUILD_NUMBER} COLLECTION==DB2AWSDB"
artifacts:
  files:
    - "**/*"
  base-directory: $revision
```
