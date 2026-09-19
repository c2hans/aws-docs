---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/install-and-initialize-app2container.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Install and initialize App2Container
<a name="install-and-initialize-app2container"></a>

 Now that you have set up your environment for replatforming, you will install and initialize App2Container on your worker machine. App2Container can be run locally on the same machine as the application, or it can be run remotely from a separate machine. This walkthrough uses the latter approach, using App2Container’s remote functionality.

 To install and initialize App2Container on your worker machine:

1.  On the worker machine, open a web browser and [download the AWSApp2Container Windows installer to your server](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AWSApp2Container-installer-windows.zip).

1.  The installer file is saved to the **Downloads** folder. Navigate to the **Downloads** folder and extract the `AWSApp2Container-installer-windows.zip` file.

1.  Run the `install.ps1` PowerShell script and enter **R** when prompted by the command output. Then press **y** to accept the terms and conditions.
![install.ps1 PowerShell script](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/install-ps1.jpg)

    Now you will perform the one-time initialization command for App2Container. This interactive command prompts for the information required to set up the App2Container environment.

1.  Go to Amazon S3 in the AWS Management Console and create an S3 bucket where App2Container will store artifacts during the containerization process. Enter a unique name for your bucket.
![Screen showing Create bucket dialog](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/create-bucket.jpg)

1.  On your worker machine, run the following command.

   ```
   app2container init
   ```
![Screen showing running the app2container init command](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/app2container.jpg)

   * Table 5 — App2Container PowerShell initialization parameter description *

<table>
<thead>
  <tr><th> Parameter </th><th> Value </th></tr>
</thead>
<tbody>
  <tr><td> Workspace directory path </td><td> Leave default (<code>C:\Users\Administrator\AppData\Local\app2container</code>) </td></tr>
  <tr><td> AWS profile </td><td> Y (Contains information needed to run App2Container) </td></tr>
  <tr><td> S3 bucket </td><td> Enter the S3 bucket name that you created in the previous step (such as <code>app2container-demo-artifacts-july-2021</code>) </td></tr>
  <tr><td> AWS Region </td><td> <code>us-west-2</code> (default) </td></tr>
  <tr><td> Permission to collect metrics </td><td> Leave default (allow App2Container to collect information about the host operating system, app type, and the commands run) </td></tr>
  <tr><td> Enforce signed images </td><td> Leave default (optionally require that images are signed using Docker Content Trust) </td></tr>
</tbody>
</table>

1.  Now you need to give App2Container the information it needs to access your web server instance. You do this by running the following command and providing the following information in the command prompts.

   ```
   app2container remote configure
   ```

   * Table 6 — App2Container web server access parameters *

<table>
<thead>
  <tr><th> Parameter </th><th> Value </th></tr>
</thead>
<tbody>
  <tr><td> Server IP address </td><td> Web server Private IPv4 address (found at the <b>EC2</b> &gt; <b>Source-NET-Webserver</b> &gt; <b>Details</b> &gt; <b>Private IPv4 Address</b>) </td></tr>
  <tr><td> Server FQDN </td><td> Leave blank </td></tr>
  <tr><td> Secret ARN </td><td> ARN for the secret you created in AWS Secret Manager </td></tr>
  <tr><td> Continue to another server? </td><td> n </td></tr>
</tbody>
</table>

![Screen showing configuring App2Container for remote access to IIS web server.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/cfg-for-iis.jpg)

 This concludes the prerequisite steps to run App2Container on your worker machine. In the next section, you will use App2Container to discover, analyze, and containerize the MvcMusicStore application that is running on the web server instance without directly touching the application server.
