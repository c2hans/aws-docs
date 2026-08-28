---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/containerization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Containerization
<a name="containerization"></a>

 Because you are using the worker machine for all of your App2container process, you will use a remote process. After you run the remote commands from your worker machine, it will connect with your application web server and run the commands on it.

 The following steps will allow you to containerize .NET applications running on a remote server using App2Container:

1.  Run the `app2container remote inventory` command (as follows) for App2Container to gather the .NET applications that are running on your web server.

   ```
   app2container remote inventory --target &lt;webserver-private-ip>
   ```
![Screening showing App2Container output for retrieving the inventory of .NET applications from a server](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/app-out.jpg)

1.  Confirm that your application is listed in the `inventory.json` file at the location specified in the tool’s output.
![Screen showing inventory.json confirmation](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/inventory-json.jpg)

1.  Locate the application ID for the application in the `inventory.json` file and then run the following command, replacing `net-app-id` with the application ID that you located in the `inventory.json`.

   ```
    app2container remote analyze --application-id <net-app-id> --target <webserver-private-ip>
   ```
![App2Container successfully analyzes a .NET application for containerization](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/app2net.jpg)

1.  Open the `analysis.json` file at the location specified in the tool’s output.

    This file has two sections, EDITABLE and NON-EDITABLE. The EDITABLE section includes container parameters that specify settings such as `containerBaseImage` or image tag. These parameters will be used in the subsequent containerization process.

    The `containerBaseImage` is not populated in the file. This is because App2Container will automatically configure the image during the next containerization step using the worker machine version to determine the `containerBaseImage` to use. However, to provide visibility into the behavior, populate that field in the `analysis.json` file with `mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2019`, as shown in the following figure, and save the file.
**Note**
This guide recommends that you use the SAC version for container-based applications because it has the most up-to-date improvements for Windows containers. However, App2Container requires the `containerBaseImage` to match the worker machine version and SAC version 2004 does not have a desktop experience. We chose LTSC version 2019 to provide a more effective walkthrough. If you use SAC version 2004, deploy a worker machine of that version and replace `containerBaseImage` with the `4.8-windowsservercore-2004` tag.
![Screen showing populating the field in the analysis.json file with mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2019](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/analysis-json.jpg)

    The NON-EDITABLE section of `analysis.json` includes application-level information that App2Container uses during the containerization step such as OS data, ports in use, dependencies, software libraries, and so on.

1.  Now you will transform your application with App2Container by extracting the artifacts from the worker machine which will be used to produce the container image. The extraction process takes a few minutes and App2Container will create a ZIP file that includes all of the artifacts. As a suggested next step from the `app2container analyze` command output, run the `app2container remote extract` command to retrieve all application artifacts to the worker machine. Update the `application-id` and target IP address based on your environment.

   ```
    app2container remote extract --application-id <net-app-id> --target <webserver-private-ip>
   ```
![App2Container successfully extracting the artifacts required for containerization](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/app2artifacts.jpg)

1.  Now you will run the `app2container containerize` command to create the container image based on the extracted files. This process will take several minutes, because the worker machine needs to download the container image .NET framework base layers, extract, and build the container image.

   ```
    app2container containerize --input-archive C:\Users\Administrator\AppData\Local\app2container\remote\<webserver-private-ip>\<application-id>\<application-id>
   ```

    After the process completes, you will see the following output:
![App2Container successfully creates a container image of the .NET application](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/app2containerimage.jpg)

1.  Run docker images to see the container image that App2Container created for you using the `windowsservercore-ltsc-2019` and `latest` image tag.
![Screen showing List of container images available on the local machine](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/container-image-list.jpg)

1.  Running the app2container containerize command creates a `deployment.json` file inside the application folder as noted in the output of the command. This file includes the AWS deployment configurations and you can update this file to fit your desired target environment such as changing the VPC or defining the CPU/memory allocation. Open the `deployment.json` file and ensure that `createEcsArtifacts` is set to true and set the target `vpc-id` to deploy the application to the target environment that you deployed previously. You can find the target `vpc-id` in the VPC service in the AWS Management Console.
![Target vpc-id](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/target-vpcid.jpg)
![Screen showing sample deployment.json file](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/deployment-json.jpg)

 You have successfully containerized your application, and are ready to deploy your newly containerized application to AWS. In the next section you will deploy your application to Amazon ECS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
