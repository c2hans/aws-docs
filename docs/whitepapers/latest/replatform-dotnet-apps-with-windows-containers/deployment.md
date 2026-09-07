---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/deployment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deployment
<a name="deployment"></a>

 You will use App2Container to generate the artifacts needed to deploy your application container in AWS. App2Container pre-fills key values in the artifacts based on your profile, the application analysis, and best practices. In this guide you will deploy your application to Amazon ECS; however, Amazon EKS is also a supported option.

1.  Run `app2container generate app-deployment` to automatically create a CloudFormation template for deploying the MvcMusicStore application to Amazon ECS.

   ```
    app2container generate app-deployment --application-id <net-app-id>
   ```

    This process will take a few minutes to complete, and will result in the following output.
![Successful generation of CloudFormation template for MvcMusic deployment](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/cftemplate.jpg)

    This process creates an Amazon ECR repository and pushes your app image to the registry. It also creates an ECS task definition and registers it with ECS, then uploads all CloudFormation resources to the selected S3 bucket. Lastly, it creates a CloudFormation template for the deployment and fills it with the generated configurations from the previous steps. You can verify the creation of these assets by viewing the services in the AWS Management Console and by confirming the `ecs-master.yml` file in the location specified in the output of the tool.

1.  Launch the CloudFormation stack by running the suggested `aws cloudformation deploy` command to pin the tool’s output. Replace the values in the following template with your actual value for your application’s ID.

   ```
   aws cloudformation deploy --template-file
   C:\Users\Administrator\AppData\Local\app2container\<net-app-id>
   \EcsDeployment\ecs-master.yml --capabilities CAPABILITY_NAMED_IAM
   --stack-name a2c-<net-app-id>-ECS
   ```

    This process will take several minutes to complete while the infrastructure is deployed in AWS. You can track the progress in the CloudFormation service in the AWS Management Console. When the command completes, the result will be the following output.
![Screen showing Successful deployment using CloudFormation template](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/cftemplatedeploy.jpg)

1.  After your stack is deployed, you can verify that your containerized application is successfully running by navigating to Amazon ECS in the EC2 console. In Amazon ECS, choose **Clusters** in the left pane, and choose the link for your newly created cluster.
![Screen showing clustoers](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/clusterf.jpg)

1.  Select the link to Amazon ECS running on your ECS cluster.
![Choose the link to Amazon ECS running on your ECS cluster](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/choose-ecs.jpg)

1.  Select the **Target Group Name** link.
![Screen showing selecting the target group name.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/target-group-name.jpg)

1.  Select the target group.
![Screen showing selecting the target group](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/target-group.jpg)

1.  Select the **Load Balancers details** link.
![Select load balancers.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/load-balancers.jpg)

1.  On the **Load Balancers** page, note the DNS name in the **Basic Configuration** details. Copy and paste the DNS link into your browser to view your containerized application running in Amazon ECS.
![Screen showing adding DNS link](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/dns-link-for-cont.jpg)
![Screen showing app.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/container-app.jpg)

 Now that you have your application up and running, you will create a CI/CD pipeline for it using App2Container.

 To create a CI/CD pipeline:

1.  Navigate to Amazon ECS in the AWS Management Console and copy your **Cluster** name and **Service** name to your local machine.
![Screen showing cluster name](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/cluster-name.jpg)

1.  On your worker machine, open the `pipeline.json` file at `C:\Users\Administrator\AppData\Local\app2container\<net-app-id>\ `and fill in the values for the `beta.clusterName` and `beta.serviceName` based on your deployment. Additionally, change `beta.enabled` to **`true`**, and save the file.
![Screen showing pipeline.json.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/pipeline-json.jpg)

1.  Open PowerShell and run the `app2container generate pipeline` command as follows:

   ```
   app2container generate pipeline --application-id <net-app-id>
   ```

1.  You should see the following output:
![Scren showing PowerShell output.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ps-output2.jpg)

1.  Run the suggested `aws cloudformation deploy` command to deploy your pipeline to AWS.

   ```
   aws cloudformation deploy --template-file
   C:\Users\Administrator\AppData\Local\app2container\<net-app-id>\
   Artifacts\Pipeline\CodePipeline\ecs-pipeline-master.yml
   --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
   --stack-name a2c-<net-app-id>-ecs-pipeline-stack
   ```

    This will take several minutes, because the command will not complete until the pipeline phases complete. Part of this is a build phase, which requires a build of the application (and Windows Server base image). You can monitor the progress in the CloudFormation service in the AWS Management Console. You will see the following output upon completion:
![Screen showing successful pipeline creation.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/pipeline-creation.jpg)

 To confirm that the pipeline was successfully created, go to the CodePipeline service in the AWS Management Console and choose your newly created pipeline.

![Screen confirming successful completion of newly created pipeline](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/new-pipeline.jpg)

 You have successfully containerized a Windows VM-based application and deployed it on Amazon ECS with a fully automated CI/CD pipeline. The following figure shows the architecture for this setup. If you are interested in doing a migration of the SQL Server instance running on Amazon EC2 to Amazon Relational Database Service, refer to the [Amazon RDS for SQL Server Workshop](https://workshops.aws/card/Amazon%20RDS%20for%20SQL%20Server%20Workshop).

![Diagram showing architecture for containerizing a Windows VM-based application and deploying it on Amazon ECS with a fully automated CI/CD pipeline](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/application-architecture.png)
