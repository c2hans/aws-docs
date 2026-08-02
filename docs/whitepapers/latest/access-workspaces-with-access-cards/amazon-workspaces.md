---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/amazon-workspaces.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon WorkSpaces
<a name="amazon-workspaces"></a>

## WorkSpaces Directory registration
<a name="workspaces-directory-registration"></a>

Use the WorkSpaces portal to register the AD Connector Directory with WorkSpaces. Details about registering a directory with WorkSpaces can be found on the [Register a Directory with Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html) page. Once registration of the Directory is completed, update the Directory configuration within the WorkSpaces Console. Details for updating the Directory can be found on the [Update Directory Details for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html) page.

## WorkSpaces image and customer bundle creation
<a name="workspaces-image-and-customer-bundle-creation"></a>

Amazon WorkSpaces come with a default set of applications that includes Internet Explorer 11 and Firefox. You can choose to add “Plus” application bundles to your Amazon WorkSpaces with Windows 10, which include Microsoft Office Professional 2016 and Trend Micro Worry-Free Business Security.

A custom WorkSpace image and bundle can be created by following the steps located on the [Create a Custom WorkSpaces Image and Bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html) page. The custom WorkSpace image and bundle is used to create WorkSpaces for your users.

## Launch WorkSpaces
<a name="launch-workspaces"></a>

Using the WorkSpaces Console, follow the launch wizard to configure and launch a WorkSpace associated with specific user.

During the “Select Bundle” step of the wizard, be sure to select **only WSP enabled WorkSpace Bundles**. You must select a WSP-enabled bundle to use smart card authentication.

![A screenshot showing the selection of WSP Bundle to use smart cards with WorkSpaces.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard18.png)

*Select **WSP Bundle **to use smart cards with WorkSpaces *

For details about launching Amazon WorkSpaces, see [Launch a WorkSpace Using AD Connector](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-ad-connector.html).
