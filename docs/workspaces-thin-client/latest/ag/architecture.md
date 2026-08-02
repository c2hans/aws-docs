---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/architecture.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Architecture
<a name="architecture"></a>

Each WorkSpaces Thin Client is associated with a virtual desktop interface (VDI) provider. WorkSpaces Thin Client supports three VDI providers:
+ [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html)
+ [WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)
+ [Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/what-is-workspaces-web.html)

Depending on the VDI used, information for your WorkSpaces Thin Client is accessed and managed either via directories for WorkSpaces, stacks for WorkSpaces Applications, and web portal endpoints for WorkSpaces Secure Browser.

For more information on Amazon WorkSpaces, see [Get started with WorkSpaces quick setup](https://docs.aws.amazon.com/workspaces/latest/adminguide/getting-started.html). Directories are managed through the Directory Service, which offers the following options: Simple AD, AD Connector, or Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD. For more information, see the [Directory Service Administration Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html).

For more information on WorkSpaces Applications, see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/getting-started.html). WorkSpaces Applications manages the AWS resources required to host and run your applications, scales automatically, and provides access to your users on demand. WorkSpaces Applications provides users access to the applications they need on the device of their choice, with a responsive, fluid user experience that is indistinguishable from natively installed applications.

For information on WorkSpaces Secure Browser, see [Getting started with Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started.html). Amazon WorkSpaces Secure Browser is an on-demand, fully managed, Linux-based service designed to facilitate secure browser access to internal websites and software-as-a-service (SaaS) applications. Access the service from existing web browsers, without the administrative burden of infrastructure management, specialized client software, or virtual private network (VPN) solutions.

The following diagram shows the architecture of WorkSpaces Thin Client.

![WorkSpaces Thin Client architecture](http://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/thin-client-diagram-customer-facing.png)
