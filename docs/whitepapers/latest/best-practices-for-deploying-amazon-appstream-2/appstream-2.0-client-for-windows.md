---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/appstream-2.0-client-for-windows.html
---

# WorkSpaces Applications client for Windows
<a name="appstream-2.0-client-for-windows"></a>

 The WorkSpaces Applications [*client for Windows*](https://clients.amazonappstream.com/) is an application that you install on your Windows PC. This application provides additional capabilities that are not available when you access WorkSpaces Applications using a web browser. For example, the WorkSpaces Applications client enables you do the following:
+  Use more than two monitors or 4K resolution
+  Use your USB devices with applications streamed through WorkSpaces Applications
+  Access your local drives and folders during your streaming sessions
+  Redirect print jobs from your streaming application to a printer that is connected to your local computer
+  Use your local webcam for video and audio conferencing within your streaming sessions
+  Use keyboard shortcuts in the applications being accessed during your streaming sessions
+  Interact with your remote streaming applications in much the same way as you interact with locally installed applications

## WorkSpaces Applications client connection modes
<a name="appstream-2.0-client-connection-modes"></a>

 The WorkSpaces Applications client provides two connection modes: Native application mode and classic mode. The connection mode that you choose determines the options that are available to you during application streaming, and how your streaming applications function and display. Administrators can control users’ ability to switch between native application mode and classic mode.
+  **Classic mode** streams applications in the WorkSpaces Applications session window. This is similar to how end users stream applications in a web browser. Use classic mode if end users prefer to stream applications in the same way as browsers, while making use of additional features such as connection for local file and printer redirection. Classic mode is the recommended default connection mode. Classic mode is the only mode supported for Desktop View.
+  **Native application mode** enables end users to work with remote streaming applications in a similar way as other locally installed applications. If end users are used to working with applications installed locally, native application mode provides a seamless experience. The remote streaming application functions in much the same way as a locally installed application. The application icon is displayed in the taskbar of your local PC, just as the icons do for your local applications. Unlike the icons for your local applications, the icons for your streaming applications in native application mode include the WorkSpaces Applications logo. Native application mode is the recommended connection mode when users want to use application keyboard shortcuts, and readily switch between individual local and individual remote applications using keyboard shortcuts.

## Client deployment and management
<a name="client-deployment-and-management"></a>

 Users can install the WorkSpaces Applications client themselves, or administrators can install the WorkSpaces Applications client for them by running PowerShell scripts remotely, or repackaging the WorkSpaces Applications client with customized settings.

 You must qualify the USB devices that you want to enable your users to use with their streaming session. If their USB device is not qualified, it won't be detected by WorkSpaces Applications and can't be shared with the session. After their devices are qualified, your users must share the devices with WorkSpaces Applications every time they start a new streaming session.

 When deploying the WorkSpaces Applications client at scale, AWS recommends using the [*Enterprise Deployment Tool*](https://docs.aws.amazon.com/appstream2/latest/developerguide/install-client-configure-settings.html#install-client-use-remote-deployment-tool). The Enterprise Deployment Tool includes the WorkSpaces Applications client installation files and a Group Policy administrative template.
