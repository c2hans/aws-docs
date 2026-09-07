---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/connect-to-deployment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connect to deployment
<a name="connect-to-deployment"></a>

 In the previous section, you deployed the stack for your environment that included three EC2 instances. The first EC2 instance is a Windows Server 2019 instance for the worker machine where you will run App2Container, the second is a Windows Server 2012 instance running the MvcMusicStore application, and the third is a Windows instance running SQL Server. Before you proceed to setting up App2Container, confirm that the deployment succeeded:

1.  Go to **CloudFormation** in the AWS Management Console and select the **App2Container-Demo** stack that you launched in the previous step.

1.  On the **Outputs** tab, select the **SSHKeyURL** link. This brings you to the Secure Shell (SSH) key that will be used to retrieve Administrator access. Save the key to your local machine.
![Screen shot showing selecting the SSHKeyURL link on the output tab](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/sshkeyurl.jpg)

1.  Go the EC2 service in the AWS Management Console and navigate to your instances.

1.  Select the **Source-NET-Webserver instance**, and choose **Connect** in the upper-right corner.
![Showing the selection of the webserver instance](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/webserver-inst.jpg)

1.  In the **Connect to instance** dialog box, choose the **RDP client** tab, and select **Get password**. A popup box appears.
![Screen shot showing password popup](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/rdp-password.jpg)

1.  In the **Get password** popup box, paste the SSH key that you saved to your local machine and select **Decrypt Password**. Copy the password that appears on the screen to your local machine. You will need it to log in to the remote machine through Remote Desktop Protocol (RDP).

1.  Go back to your **Instances** view and copy the Public IPv4 DNS string for the web server instance to your local machine.
![Screen showing setup of IPv4](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ipv4-dns.jpg)

1.  Go to your **DBServer** instance and copy the **Private IPv4** address to your local machine. You will need this while editing the `Web.config` file for the application to connect to the database.
![Screen showing private IPv4 address](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ipv4-private.jpg)

1.  Open Remote Desktop Connection on your local machine and paste the web server DNS string into the **Connection** field.

1.  Enter **Administrator** as the user name, and choose **Connect**.
![Screen showing entering Administrator as the user name.](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/admin.jpg)

1.  After you are connected to the web server instance, open PowerShell.

1.  Run the following command to configure your application to connect to the database. Replace `<change-this-to-your-private-db-ip>` with the private IPv4 address of your database instance that you copied in step 8.

   ```
   (Get-Content C:/dotnet-modernization-music-
   store/MvcMusicStore/Web.config).replace('Data Source=.',
   'Data Source=<change-this-to-your-private-db-ip>') | Set-Content
   C:/dotnet-modernization-music-store/MvcMusicStore/Web.config
   ```

1.  Go to **Administrative Tools > Internet Information Services (IIS) Manager**. Choose the **MvcMusicStore** application from the left pane.

1.  Choose **Restart** in the right pane, and then choose **Browse 8081**. The MvcMusicStore user interface should appear in the internet browser.
![Screen shot showing Internet Information Services (IIS) Manager](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/iis.jpg)
![Screen shot showing MvcMusicStore user interface](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/mvc-interface.jpg)

1.  Now that you have confirmed that the application is successfully running in your environment, you need to install WinRM so that App2Container can remotely connect to your web server instance to analyze and containerize your application. Run the following in PowerShell:

   ```
   cd Downloads
   .\WinRMSetup.ps1
   ```

 You should observe the following output:

![Screen shot showing PowerShell output](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ps-output.jpg)

 You have confirmed that your MvcMusicStore application is running on the web server instance on IIS. Additionally, you have set up your web server instance with WinRM so that App2Container can remotely access it from the worker machine. You are ready to move on to the next step to set up App2Container.
