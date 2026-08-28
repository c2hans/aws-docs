---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html
---

# Modernize and deploy mainframe applications using AWS Transform and Terraform
<a name="modernize-mainframe-app-transform-terraform"></a>

*Mason Cahill, Polaris Jhandi, Prachi Khanna, Sivasubramanian Ramani, and Santosh Kumar Singh, Amazon Web Services*

## Summary
<a name="modernize-mainframe-app-transform-terraform-summary"></a>

[AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) can accelerate large-scale modernization of .NET, mainframe, and VMware workloads. It deploys specialized AI agents that automate complex tasks like assessments, code analysis, refactoring, decomposition, dependency mapping, validation, and transformation planning. This pattern demonstrates how to use AWS Transform to modernize a mainframe application and then deploy it to AWS infrastructure by using [Hashicorp Terraform](https://developer.hashicorp.com/terraform/intro). These step-by-step instructions help you transform [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo), which is a sample open source mainframe application, from COBOL to a modern Java application.

## Prerequisites and limitations
<a name="modernize-mainframe-app-transform-terraform-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Administrative permissions to create AWS resources and deploy applications
+ Terraform version 1.5.7 or higher, [configured](https://developer.hashicorp.com/terraform/tutorials/aws-get-started?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS)
+ AWS Provider for Terraform, [configured](https://registry.terraform.io/providers/hashicorp/aws/2.36.0/docs#authentication)
+ AWS IAM Identity Center, [enabled](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html)
+ AWS Transform, [enabled](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html)
+ A user, [onboarded](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-management.html) to an AWS Transform workspace with a contributor role that can run transformation jobs

**Limitations**
+ AWS Transform is available only in some AWS Regions. For a complete list of supported Regions, see [Supported Regions for AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/regions.html).
+ There is a service quota for mainframe transformation capabilities in AWS Transform. For more information, see [Quotas for AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-limits.html).
+ To collaborate on a shared workspace, all users must be registered users of the same instance of AWS IAM Identity Center that is associated with your instance of the AWS Transform web application.
+ The Amazon Simple Storage Service (Amazon S3) bucket and AWS Transform must be in the same AWS account and Region.

## Architecture
<a name="modernize-mainframe-app-transform-terraform-architecture"></a>

The following diagram shows the end-to-end modernization of the legacy application and deployment to the AWS Cloud. Application and database credentials are stored in AWS Secrets Manager, and Amazon CloudWatch provides monitoring and logging capabilities.

![AWS Transform modernizing a mainframe application and deployment through Terraform.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/78bc1e6e-cd3d-4c6d-ae4b-0675a6898fd9/images/332ccf35-f55a-449e-a05d-7e321b3867b7.png)

The diagram shows the following workflow:

1. Through AWS IAM Identity Center, the user authenticates and accesses AWS Transform in the AWS account.

1. The user uploads the COBOL mainframe code to the Amazon S3 bucket and initiates the transformation in AWS Transform.

1. AWS Transform modernizes the COBOL code into cloud-native Java code and stores the modernized code in the Amazon S3 bucket.

1. Terraform creates the AWS infrastructure to deploy the modernized application, including an Application Load Balancer, Amazon Elastic Compute Cloud (Amazon EC2) instance, and Amazon Relational Database Service (Amazon RDS) database. Terraform deploys the modernized code to the Amazon EC2 instance.

1. The VSAM files are uploaded to Amazon EC2 and are migrated from Amazon EC2 to the Amazon RDS database.

## Tools
<a name="modernize-mainframe-app-transform-terraform-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down. In this pattern, SQL Server failover cluster instances are installed on Amazon EC2 instances.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to your AWS accounts and cloud applications.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) uses agentic AI to help you accelerate the modernization of legacy workloads, such as .NET, mainframe, and VMware workloads.

**Other tools**
+ [Apache Maven](https://maven.apache.org/) is an open source software project management and build automation tool for Java projects.
+ [Apache Tomcat](https://tomcat.apache.org/) is an open source Servlet container and web server for Java code.
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [Spring Boot](https://spring.io/projects/spring-boot) is an open source framework built on top of the Spring Framework in Java.

**Code repository**

The code for this pattern is available in the GitHub [Mainframe Transformation E2E](https://github.com/aws-samples/sample-mainframe-transformation-e2e) repository. This pattern uses the open source AWS [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) mainframe application as a sample application.

## Best practices
<a name="modernize-mainframe-app-transform-terraform-best-practices"></a>
+ Assign full ownership of code and resources targeted for migration.
+ Develop and test a proof of concept before scaling to a full migration.
+ Secure commitment from all stakeholders.
+ Establish clear communication channels.
+ Define and document minimum viable product (MVP) requirements.
+ Set clear success criteria.

## Epics
<a name="modernize-mainframe-app-transform-terraform-epics"></a>

### Prepare and upload the mainframe application code
<a name="prepare-and-upload-the-mainframe-application-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a bucket. | Create an Amazon S3 bucket in the same AWS account and Region where AWS Transform is enabled. You use this bucket to store the mainframe application code, data and additional scripts required to build and run the application. AWS Transform uses this bucket to store the refactored code and other files associated with the transformation. For instructions, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. | General AWS, AWS administrator |
| Set the CORS permissions for the bucket. | When setting up your bucket for AWS Transform access, you need to configure cross-origin resource sharing (CORS) for the bucket. If this is not set up correctly, you might not be able to use the inline viewing or file comparison functionalities of AWS Transform. For instructions about how to configure CORS for a bucket, see [Using cross-origin resource sharing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html) in the Amazon S3 bucket. For the policy, see [S3 bucket CORS permissions](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-setup-connector-s3) in the AWS Transform documentation. | General AWS, AWS administrator |
| Prepare the sample mainframe application code. | 1. Enter the following command to clone the [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) repository to your local workstation:<pre>git clone https://github.com/aws-samples/aws-mainframe-modernization-carddemo.git</pre><br />2. Compress the `aws-mainframe-modernization-carddemo` folder into a ZIP file.<br />3. Upload the ZIP file to the Amazon S3 bucket that you created. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation. | General AWS, App developer |

### Transform the mainframe application
<a name="transform-the-mainframe-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the AWS Transform job. | 1. Access the AWS Transform web application by logging in with your credentials.<br />2. Create a new workspace by following the instructions in [Setting up your workspace](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-admin-workspace-setup.html) in the AWS Transform documentation.<br />3. On your workspace landing page, choose **Ask AWS Transform to create a job**.<br />4. Next, choose **Mainframe Modernization** as the type of job.<br />5. In the chat window, enter **Transform code to Java**.<br />6. Review the suggested job type, name, and objective. To confirm, enter **Yes**.<br />7. Choose **Create job**.   | App developer, App owner |
| Set up a connector. | 1. Set up a connector with the Amazon S3 bucket that you created. For instructions, see [Set up a connector](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-setup-connector) in the AWS Transform documentation. When prompted, enter the path for the `aws-mainframe-modernization-carddemo` zip file in the Amazon S3 bucket.<br />2. Wait for the analysis to complete. | App developer, App owner |
| Transform the code. | 1. Review the results of the code analysis according to the instructions in [Analyze code](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-code-analysis) in the AWS Transform documentation.<br />2. Refactor the mainframe code according to the instructions in [Refactor code](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-refactor-code) in the AWS Transform documentation. For the sample CardDemo mainframe application, you can accept the default settings.<br />3. Wait for the refactoring to complete.<br />4. Choose **View results** to see the path for the refactored code in the Amazon S3 bucket. Make note of this file path. You will need it later. | App developer, App owner |

### Deploy the infrastructure through Terraform
<a name="deploy-the-infrastructure-through-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the templates. | 1. Enter the following command to clone the [Mainframe Transformation E2E](https://github.com/aws-samples/sample-mainframe-transformation-e2e) repository to your local workstation:<pre>git clone https://github.com/aws-samples/sample-mainframe-transformation-e2e.git</pre><br />2. Enter the following command to retrieve your current public IP address:<pre>curl checkip.amazonaws.com</pre><br />3. Enter the following command to navigate to the infra directory:<pre>cd mainframe-transformation-e2e/infra</pre><br />4. Open the `variables.tf` file.<br />5. Replace `YOUR_IP_ADDRESS_HERE` with your IP address.<br />6. If you have a public hosted zone, do the following:Replace `hosted_zone_name` with your hosted zone name.Set `hosted_zone_enabled` to `true`.<br />If you do not have a public hosted zone, do the following:Enter the following commands to generate a self-signed certificate:<pre>openssl genrsa 2048 > my-private-key.pem<br />openssl req -new -x509 -nodes -sha256 -days 365 -key my-private-key.pem -outform PEM -out my-certificate.pem</pre>Enter the following command to import the certificate into AWS Certificate Manager (ACM):<pre>aws acm import-certificate \<br />  --certificate fileb://my-certificate.pem \<br />  --private-key fileb://my-private-key.pem</pre><br />The outpout of this command includes the Amazon Resource Name (ARN) of the imported certificate.Replace `self_signed_cert_arn` with the ARN of your certificate.Set `hosted_zone_enabled` to `false`.<br />7. Change `aws_region` to the target Region. The default is `us-east-1`.<br />8. Save and close the `variables.tf` file.For production or production-like environments, configure additional security components. For example, enable [AWS WAF protections for your Application Load Balancer](https://aws.amazon.com/about-aws/whats-new/2024/02/aws-application-load-balancer-one-click-waf-integrations/). | General AWS, AWS administrator |
| Deploy the infrastructure. | 1. Enter the following command to initialize Terraform:<pre>terraform init</pre><br />2. Enter the following command to generate an execution plan:<pre>terraform plan</pre><br />3. Review the plan, and validate the resources and infrastructure components that will be created.<br />4. Enter the following command to deploy the infrastructure:<pre>terraform apply</pre><br />5. When prompted, enter** yes **to confirm the deployment.<br />6. Wait until the deployment is completed. | Terraform |

### Install and configure Apache Tomcat on the Amazon EC2 instance
<a name="install-and-configure-apache-tomcat-on-the-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the required software. | 1. Connect to your Amazon EC2 instance by using [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-systems-manager-session-manager.html).<br />2. Enter the following command to switch to the root user:<pre>sudo su -</pre><br />3. Enter the following command to navigate to the `scripts` directory:<pre>cd /opt/scripts</pre><br />4. Review the **install\_software.sh **script. This script installs Java 17, Apache Maven, and Apache Tomcat 10.0.23.<br />5. Update the scripts as needed for your use case.<br />6. Enter the following command to make the script executable:<pre>chmod +x install_software.sh</pre><br />7. Enter the following command to run the script:<pre>./install_software.sh</pre> | App developer, Migration engineer |
| Verify software installation. | 1. Enter the following command to start the Tomcat server:<pre>/opt/tomcat/apache-tomcat-10.0.23/bin/startup.sh</pre><br />2. Enter the following command to verify the web server response:<pre>curl http://localhost:8080</pre><br />The output should confirm that Tomcat is serving an HTML page. | App developer, Migration engineer |

### Compile and package the modernized application code
<a name="compile-and-package-the-modernized-application-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download and extract the generated code. | 1. Enter the following command to make the **download\_and\_extract.sh** script executable. This script downloads the refactored code and Gapwalk runtime library stored in the Amazon S3 bucket:<pre>chmod +x /opt/scripts/download_and_extract.sh</pre><br />2. Enter the following command to run the script. Replace `<file_path>` with the path to the generated.zip file in your Amazon S3 bucket:<pre>./download_and_extract.sh <file_path></pre>The file path is typically `s3://<bucket-name>/transform_output/<aws_transform_job_id>/codetransformation/generated.zip`.<br />3. Enter the following command to navigate into the `shared` folder:<pre>cd /opt/runtime/velocity/shared</pre><br />4. Enter the following command to copy the **deploy-velocity-runtime.sh** script:<pre>cp /opt/scripts/deploy-velocity-runtime.sh .</pre><br />5. Enter the following command to make the copied script executable:<pre>chmod +x deploy-velocity-runtime.sh</pre><br />6. Enter the following command to run the script. This script copies all the required Web Application Archive (WAR) dependencies present in the Project Object Model (POM) files into the repository folder:<pre>./deploy-velocity-runtime.sh</pre><br />7. Verify successful execution by checking that that there are no errors and that the required WAR dependencies are installed in your local Maven repository. | App developer, Migration engineer |
| Build the modernized application. | 1. Enter the following command to navigate to the `app-pom` project directory:<pre>cd /opt/codebase/app-pom/</pre><br />2. Enter the following command to install Maven:<pre>mvn clean install</pre><br />3. Wait for the installation and build to complete.When running this command for the CardDemo application, you might encounter warning messages for the `app-web` project. You can safely ignore these warnings.<br />4. After successful build completion, confirm the presence of `app-service/target/app-service-1.0.0.war` and `app-web/target/app-web-1.0.0.war`.Do not restart the Tomcat server at this stage. It would result in errors due to the absence of required databases. You must set up the database before you can restart the server. | App developer, Migration engineer |

### Migrate the database
<a name="migrate-the-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the database and JICS schemas. | 1. Enter the following command to rename the `csd commands` folder to `csd_commands`. This remove the spaces from the folder name:<pre>mv /opt/codebase/extra/csd\ commands/ /opt/codebase/extra/csd_commands</pre><br />2. Enter the following command to navigate into the `scripts` directory:<pre>cd /opt/scripts</pre><br />3. Enter the following command to make the database migration script executable:<pre>chmod +x database_migration_setup.sh</pre><br />4. Enter the following commands to configure the following variables as parameters:<pre>RDS_ENDPOINT=<database_endpoint><br />SECRET_NAME=<secret_name><br />JICS_SQL_SCRIPT_DIR=/opt/runtime/velocity/jics/sql/jics.sql<br />INIT_JICS_SQL_SCRIPT_DIR=/opt/codebase/extra/csd_commands/sql/aws-mainframe-modernization-carddemo-main/app/csd/initJics.sql</pre><br />Where:`<database_endpoint>` is the endpoint of the Amazon RDS database that you deployed through Terraform.`<secret_name>` is the name of the AWS Secrets Manager secret that you deployed through Terraform.<br />5. Enter the following command to run the database migration script:<pre>./database_migration_setup.sh $RDS_ENDPOINT $SECRET_NAME $JICS_SQL_SCRIPT_DIR $INIT_JICS_SQL_SCRIPT_DIR</pre><br />6. Enter the following command to connect to the database from your Amazon EC2 instance:<pre>psql -h <Your Amazon RDS Endpoint> -U foo -p 5432 postgres</pre><br />7. When prompted, enter your database credentials. | App developer, Migration engineer |
| Validate database creation. | 1. Enter the following command to view all databases:<pre>\l</pre><br />2. Enter the following command to switch to the `jics` database:<pre>\c jics</pre><br />3. Enter the following command to review a list of the created tables:<pre>\dt</pre> | App developer, Migration engineer |
| Migrate data to the JICS database. | 1. Enter the following command to make the **execute\_listcat\_sql.sh** script executable:<pre>chmod +x execute_listcat_sql.sh</pre><br />2. Enter the following command to configure the `PATH_TO_LISTCAT_SQL_FILES` variable, which is the directory that contains your LISTCAT SQL files:<pre>PATH_TO_LISTCAT_SQL_FILES=/opt/codebase/extra/listcat/sql/cluster/aws-mainframe-modernization-carddemo-main/app/catlg</pre><br />3. Make sure that the `RDS_ENDPOINT`, `SECRET_NAME`, and `PATH_TO_LISTCAT_SQL_FILES` variables are properly set according to the previous instructions.<br />4. Enter the following command to run the **execute\_listcat\_sql.sh** script:<pre>./execute_listcat_sql.sh $RDS_ENDPOINT $SECRET_NAME $PATH_TO_LISTCAT_SQL_FILES</pre><br />This script updates the VSAM file properties in the JICS database and runs the necessary queries to modify the database. | App developer, Migration engineer |

### Install the modernized application
<a name="install-the-modernized-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the modernized application on the Amazon EC2 instance. | 1. Enter the following command to make the **application\_installer.sh **script executable:<pre>chmod +x /opt/scripts/application_installer.sh</pre><br />2. Enter the following commands to configure the following variables as parameters:<pre>RDS_ENDPOINT=<database_endpoint><br />SECRET_NAME=<secret_name><br />AIX_JSON_FILE_PATH=/opt/codebase/extra/csd_commands/json/aws-mainframe-modernization-carddemo-main/jicsFileAix.json<br />LISTCAT_JSON_FILES_DIR=/opt/codebase/extra/listcat/json/cluster/default/aws-mainframe-modernization-carddemo-main/app/catlg<br />S3_PATH_FOR_EBCDIC_DATA_FILES=s3://<bucket_name>/transform-output/<job_id>/inputs/aws-mainframe-modernization-carddemo-main/app/data/EBCDIC</pre><br />Where:`<database_endpoint>` is the endpoint of the Amazon RDS database that you deployed through Terraform.`<secret_name>` is the name of the AWS Secrets Manager secret that you deployed through Terraform.`<bucket_name>` is the name of the Amazon S3 bucket that contains the modernized application.`<job_id>` is the ID of the AWS Transform job.<br />3. Enter the following command to run the **application\_installer.sh **script:<pre>./application_installer.sh $RDS_ENDPOINT $SECRET_NAME $AIX_JSON_FILE_PATH $LISTCAT_JSON_FILES_DIR $S3_PATH_FOR_EBCDIC_DATA_FILES</pre><br />4. In the `/opt/tomcat/apache-tomcat-10.0.23/workingdir/config` folder, in the **application-utility-pgm.yml** file, change the encoding parameter to the following:<pre>encoding : CP1047</pre>When you refactor applications in AWS Transform automatically by using [AWS Blu Age](https://docs.aws.amazon.com/m2/latest/userguide/refactoring-m2.html), you configure the application and its runtime environment through YAML files. For example, you can configure logging in the **application-main.yml** file for the application. For more information about the available properties, see [Enable properties for AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-key-value.html). | App developer, Cloud architect |
| Restart the Tomcat server. | 1. Enter the following command to navigate into the working directory:<pre>cd /opt/tomcat/apache-tomcat-10.0.23/workingdir</pre><br />2. Enter the following commands to stop and start the Tomcat server:<pre>/opt/tomcat/apache-tomcat-10.0.23/bin/shutdown.sh<br />/opt/tomcat/apache-tomcat-10.0.23/bin/startup.sh</pre><br />3. Enter the following command to monitor the Tomcat service startup logs:<pre>tail -f /opt/tomcat/apache-tomcat-10.0.23/logs/catalina.out</pre> | App developer, Cloud architect |
| Migrate the VSAM dataset. | 1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).<br />2. In the navigation pane, choose **Load balancers**.<br />3. Choose the load balancer that was created through Terraform.<br />4. Locate the Domain Name System (DNS) name of your Application Load Balancer, such as `application-load-balancer-<id>.<region>.elb.amazonaws.com`.<br />5. In your browser, navigate to `http://<dns_name>/gapwalk-application/scripts/data-load`, where `<dns_name>` is the DSN name of the Application Load Balancer. This starts the data load script.<br />6. Wait for the script to complete. When finished, the browser will display **DONE**.<br />7. On the Amazon EC2 instance, open a new terminal.<br />8. Enter the following command to connect to the Amazon RDS database, replacing `<database_endpoint>` with your value:<pre>psql -h <database_endpoint> -U foo -p 5432 postgres</pre><br />9. When prompted, enter your credentials to connect to the database.<br />10. Enter the following command to view all databases:<pre>\l</pre><br />11. Enter the following command to switch to the `bluesam` database:<pre>\c bluesam</pre><br />12. Enter the following command to review a list of the created tables:<pre>\dt</pre><br />13. Enter the following command to validate the data load:<pre>SELECT * FROM public.aws_m2_carddemo_usrsec_vsam_ksds;</pre><br />The ouput should show 10 records returned. | App developer, Migration engineer |
| Update the parameters in the Groovy scripts. | 1. Enter the following command to navigate into the script directory:<pre>cd /opt/tomcat/apache-tomcat-10.0.23/webapps/workingdir/scripts</pre><br />2. In all of the Groovy files that contain reference to flat files, update the following file configurations:**Local file path** – The path to the flat file in the local directory of your Amazon EC2 instance**File system type** – The file system that contains the flat files**Record size** – The size of the flat file<br />For reference, see the sample [DUSRSECJ.jcl.groovy ](https://github.com/aws-samples/sample-mainframe-transformation-e2e/blob/main/scripts/DUSRSECJ.jcl.groovy)script in the code repository.<br />3. Save and close the files. | App developer |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the modernized application. | 1. Access the online application through the Application Load Balancer (`http://<your-load-balancer-dns>`) or through the hosted zone (`https://myhostedzone.dev/`).<br />2. For the transaction ID, enter `CC00`.<br />3. For the user name, enter `USER0001`.<br />4. For the password, enter `PASSWORD`.<br />After successful login, the main menu displays. | App developer, Test engineer |
| Verify the batch scripts. | 1. Access the scripts interface through either the Application Load Balancer (`http://<your-load-balancer-dns>/gapwalk-application/scripts`) or through the hosted zone (`https://myhostedzone.dev/gapwalk-application/scripts`).<br />2. Choose a script to run, such as the [DUSRSECJ.jcl.groovy](https://github.com/aws-samples/sample-mainframe-transformation-e2e/blob/main/scripts/DUSRSECJ.jcl.groovy) script.<br />3. Verify that the script runs successfully. The following is a sample output after successful execution.<pre>{ "exitCode": 0, "stepName": "STEP03", "program": "IDCAMS", "status": "Succeeded" }</pre> | App developer, Test engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare to delete the infrastructure. | 1. Enter the following command to remove deletion protection from the Amazon RDS instance:<pre>aws rds modify-db-instance \<br />  --db-instance-identifier <your-db-instance-name> \<br />  --no-deletion-protection \<br />  --apply-immediately</pre><br />2. Enter the following command to remove deletion protection from the Application Load Balancer:<pre>aws elbv2 modify-load-balancer-attributes \<br />  --load-balancer-arn <your-load-balancer-arn> \<br />  --attributes Key=deletion_protection.enabled,Value=false</pre><br />3. Enter the following commands to delete the contents of the Amazon S3 buckets:<pre>ACCOUNT_NUMBER=$(aws sts get-caller-identity --query Account --output text)<br />aws s3 rm s3://mf-carddemo-$ACCOUNT_NUMBER --recursive<br />aws s3 rm s3://mf-carddemo-logs-$ACCOUNT_NUMBER --recursive</pre> | General AWS |
| Delete the infrastructure. | These steps will permanently delete your resources. Make sure you have backed up any important data before proceeding.1. Enter the following command to navigate into the `infra` folder:<pre>cd /mainframe-transformation-e2e/infra</pre><br />2. Enter the following command to delete the infrastructure:<pre>terraform destroy --auto-approve    </pre> | General AWS |

## Troubleshooting
<a name="modernize-mainframe-app-transform-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Terraform authentication | 1. Make sure that the AWS credentials are properly configured.<br />2. Verify that you have selected the correct AWS profile.<br />3. Confirm that you have the necessary permissions. |
| Tomcat-related errors | 1. Check **catalina.out** in `/opt/tomcat/apache-tomcat-10.0.23/logs` for any exceptions.<br />2. Enter the following command to change ownership of the Tomcat folder to the Tomcat user:<pre>chown -R tomcat:tomcat /opt/tomcat/*</pre> |
| URL name not loading | Make sure that the Application Load Balancer security group has your IP address in the inbound rule as a source. |
| Authentication issue in Tomcat log | Confirm that the database secret password in AWS Secrets Manager and the password in **server.xml** match. |

## Related resources
<a name="modernize-mainframe-app-transform-terraform-resources"></a>

**AWS Prescriptive Guidance**
+ [Modernize the CardDemo mainframe application by using AWS Transform](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-carddemo-mainframe-app.html)

**AWS service documentation**
+ [AWS Blu Age Blusam Adminstration Console](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-bac-userguide.html)
+ [Infrastructure setup requirements for AWS Blu Age Runtime (non-managed)](https://docs.aws.amazon.com/m2/latest/userguide/ba-infrastructure-setup.html)
+ [Onboarding AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-setup-onboard.html)
+ [Modernization of mainframe applications](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-app-mainframe.html)
+ [Set up configuration for AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config.html)

**AWS blog posts**
+ [Accelerate Your Mainframe Modernization Journey using AI Agents with AWS Transform](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
