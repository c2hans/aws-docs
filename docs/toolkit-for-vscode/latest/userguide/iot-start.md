---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/iot-start.html
---

# Working with AWS IoT in AWS Toolkit for Visual Studio Code
<a name="iot-start"></a>

AWS IoT in AWS Toolkit for Visual Studio Code allows you to interact with the AWS IoT service, while minimizing interruptions to your work flow in VS Code. This user guide is intended to help you get started using the AWS IoT service features that are available in the AWS Toolkit for Visual Studio Code. For additional information about the AWS IoT service, see the developer guide [What is AWS IoT?](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

## AWS IoT prerequisites
<a name="iot-vsctoolkit-prereq"></a>

To get started using AWS IoT from Toolkit for VS Code, make sure your AWS account and VS Code meet the requirements in these guides:
+ For AWS account requirements and AWS user permissions specific to the AWS IoT service, see the [Getting Started with AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/setting-up.html) developer guide.
+ For Toolkit for VS Code specific requirements, see the [Setting up the Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setting-up.html) user guide.

## AWS IoT Things
<a name="iot-vsctoolkit-things"></a>

AWS IoT connects devices to AWS cloud services and resources. You can connect your devices to AWS IoT by using objects called **things**. A thing is a representation of a specific device or logical entity. It can be a physical device or sensor (for example, a light bulb or a switch on a wall). For additional information about AWS IoT things, see the developer guide [Managing devices with AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html).

### Managing AWS IoT things
<a name="iot-vsctoolkit-things-actions"></a>

The Toolkit for VS Code has several features that make your AWS IoT thing management more efficient. These are ways that you can use the VS Code toolkit to manage your AWS IoT things:
+ [Create a thing](#thing-create)
+ [Attach a certificate to a thing](#thing-certificate-attach)
+ [Detach a certificate from a thing](#thing-certificate-detach)
+ [Delete a thing](#thing-delete)<a name="thing-create"></a>

**To create a thing**

1. From the AWS Explorer, expand the **IoT** service heading, and context-select (right-click) **Things**.

1. Choose **Create Thing** from the context-menu to open a dialog box.

1. Follow the prompt by entering a name for your IoT thing into the **Thing Name** field.

1. When this is complete, a **thing icon** followed by the name you specified will be visible in the **Thing** section.<a name="thing-certificate-attach"></a>

**To attach a certificate to a thing**

1. From the AWS Explorer, expand the **IoT** service section.

1. Under the **Things** subsection, locate the **thing** where you are attaching the certificate.

1. Context-select (right-click) the **thing** and choose **Attach Certificate** from the context-menu, to open an input selector with a list of your certificates.

1. From the list, choose the **certificate ID** that corresponds to the certificate you want to attach to your thing.

1. When this is complete, your certificate is accessible in the AWS explorer, as an item of the thing that you attached it to.<a name="thing-certificate-detach"></a>

**To detach a certificate from a thing**

1. From the AWS Explorer, expand the **IoT** service section

1. In the **Things** subsection, locate the **thing** that you want to detach a certificate from.

1. Context-select (right-click) the **thing** and choose **Detach Certificate** from the context-menu.

1. When this is complete, the detached certificate will no longer display under that thing in the AWS Explorer, but it will still be accessible from the **Certificates** subsection.<a name="thing-delete"></a>

**To delete a thing**

1. From the AWS Explorer, expand the **IoT** service section.

1. In the **Things** subsection, locate the **thing** you want to delete.

1. Context-select (right-click) the thing and choose **Delete Thing** from the context-menu to delete it.

1. When this is complete, the deleted thing will no longer be available from the **Things** subsection.
**Note**
Note: You can only delete a thing that doesn't have a certificate attached to it.

## AWS IoT certificates
<a name="iot-vsctoolkit-cert"></a>

Certificates are a common way to create a secure connection between your AWS IoT services and devices. X.509 certificates are digital certificates that use the X.509 public key infrastructure standard to associate a public key with an identity contained in a certificate. For additional information about AWS IoT certificates, see the developer guide [Authentication (IoT)](https://docs.aws.amazon.com/iot/latest/developerguide/authentication.html).

### Managing certificates
<a name="iot-vsctoolkit-cert-actions"></a>

The VS Code toolkit offers a variety of ways for you to manage your AWS IoT certificates, directly from the AWS Explorer.
+ [Create a certificate](#cert-create)
+ [Change a certificate status](#cert-status)
+ [Attach a policy to a certificate](#cert-attach-policy)
+ [Delete a certificate](#cert-delete)<a name="cert-create"></a>

**To create an AWS IoT certificate**

An X.509 certificate can be used to connect with your instance of AWS IoT.

1. From the AWS Explorer, expand the **IoT** service section, and context-select (right-click) **Certificates**.

1. Choose **Create Certificate** from the context-menu to open a dialog box.

1. Select a directory in your local file system to save your RSA key pair and X.509 certificate.
**Note**
The default file names contain the certificate ID as a prefix.
Only the X.509 certificate is stored with your AWS account, through the AWS IoT service.
Your RSA key pair can only be issued once, save them to a secure location in your file system when you're prompted.
If either the certificate or the key pair can't be saved to your file system at this time, then the AWS Toolkit deletes the certificate from your AWS account.<a name="cert-status"></a>

**To modify a certificate status**

The status of an individual certificate is displayed next to its ID in the AWS Explorer and can be set to: active, inactive, or revoked.
**Note**
Your certificate needs an **active** status before you can use it to connect your device to your AWS IoT service.
An **inactive** certificate can be activated, whether it has been deactivated previously or is inactive by default.
A certificate that has been **revoked** can't be reactivated.

1. From the AWS Explorer, expand the **IoT** service section.

1. In the **Certificates** subsection, locate the certificate you want to modify.

1. Context-select (right-click) the certificate to open a context menu that displays the status change options available for that certificate.
+ If a certificate has the status **inactive**, choose **activate** to change the status to **active**.
+ If a certificate has the status **active**, choose **deactivate** to change the status to **inactive**.
+ If a certificate has either an **active** or **inactive** status, choose **revoke** to change the status to **revoked**.

**Note**
Each of these status-changing actions are also available if you select a certificate that is attached to a thing while it's displayed in the **Things** subsection.<a name="cert-attach-policy"></a>

**To attach an IoT policy to a certificate**

1. From the AWS Explorer, expand the **IoT** service section.

1. In the **Certificates** subsection, locate the certificate you want to modify.

1. Context-select (right-click) the certificate and choose **Attach Policy** from the context menu, to open an input selector with a list of your available policies.

1. Choose the policy you want to attach to the certificate.

1. When this is complete, the policy you selected will be added to the certificate as a sub-menu item.<a name="cert-detach-policy"></a>

**To detach an IoT policy from a certificate**

1. From the AWS Explorer, expand the **IoT** service section.

1. In the **Certificates** subsection, locate the certificate you want to modify.

1. Expand the certificate and locate the policy you want to detach.

1. Context-select (right-click) the policy and choose **Detach** from the context menu.

1. When this is complete, the policy will no longer be an item that is accessible from your certificate, but it will be available from the **Policy** subsection.<a name="cert-delete"></a>

**To delete a certificate**

1. From the AWS Explorer, expand the **IoT** service heading.

1. In the **Certificates** subsection, locate the certificate you want to delete.

1. Context-select (right-click) the certificate and choose **Delete Certificate** from the context menu.
**Note**
You can't delete a certificate if it's attached to a thing or has an active status. You can delete a certificate that has attached policies.

## AWS IoT policies
<a name="iot-vsctoolkit-policy"></a>

AWS IoT Core policies are defined through JSON documents, each containing one or more policy statements. Policies define how AWS IoT, AWS, and your device can interact with each other. For more information about how to create a policy document, see the developer guide [IoT Polices](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html).

**Note**
Named policies are versioned so you can roll them back. In The AWS Explorer, your IoT polices are listed under the **Policies** subsection, in the IoT service. You can view policy versions by expanding a policy. The default version is denoted by an asterisk.

### Managing policies
<a name="iot-vsctoolkit-policy-actions"></a>

The Toolkit for VS Code offers several ways for you to manage your AWS IoT service policies. These are ways that you can manage or modify your policies directly from the AWS Explorer in VS Code:
+ [Create a policy](#policy-create)
+ [Upload a new policy version](#policy-version-upload)
+ [Edit a policy version](#policy-version-edit)
+ [Change the policy version defualt](#policy-version-default)
+ [Change the policy version defualt](#policy-delete)<a name="policy-create"></a>

**To create an AWS IoT policy**
**Note**
You can create a new policy from the AWS Explorer, but the JSON document that defines the policy must already exist in your file system.

1. From the AWS Explorer, expand the **IoT** service section.

1. Context-select (right-click) the **Policies** subsection and choose **Create Policy from Document**, to open the **Policy Name** input field.

1. Enter a name and follow the prompts to open a dialog asking you to select a JSON document from your file system.

1. Choose the JSON file that contains your policy definitions, the policy will be available in the AWS explorer when this is complete.<a name="policy-version-upload"></a>

**To upload a new AWS IoT policy version**

A new version of a policy can be created by uploading a JSON document to the policy.
**Note**
The new JSON document must be present on your file system to create a new version using the AWS Explorer.

1. From the AWS Explorer, expand the **IoT** service section.

1.  Expand the **Policies** subsection to view your AWS IoT policies

1. Context-select (right-click) the policy that you want to update and choose **Create new version from Document**.

1. When the dialog opens, choose the JSON file that contains the updates to your policy definitions.

1. The new version will be accessible from your policy in the AWS Explorer.<a name="policy-version-edit"></a>

**To edit an AWS IoT policy version**

A policy document can be opened and edited using VS Code. When you are finished editing the document, you can save it to your file system. Then, you can upload it to your AWS IoT service from the AWS Explorer.

1. From the AWS Explorer, expand the **IoT** service section.

1. Expand the **Policies** subsection and locate the policy you want to update.**Create Policy from Document** to open the **Policy Name** input field.

1. Expand the policy that you want to update and then Context-select (right-click) the policy version that you want to edit.

1. Choose **View** from the context-menu to open the policy version in VS Code

1. When the policy document is opened, make and save the changes you want.
**Note**
At this point, the changes you made to the policy are only saved to your local file system. To update the version and track it with the AWS Explorer, repeat the steps described in the [Upload a new policy version](#policy-version-upload) procedure.<a name="policy-version-default"></a>

**To select a new policy version default**

1. From the AWS Explorer, expand the **IoT** service section.

1. Expand the **Policies** subsection and locate the policy you want to update.

1. Expand the policy that you want to update and then Context-select (right-click) the policy version that you want to set and choose **Set as Default**.

1. When this is complete, the new default version you selected will have a star located next it.<a name="policy-delete"></a>

**To delete policies**
**Note**
Before you can delete a policy or a policy version, there are conditions that need to be met.
You can't delete a policy if it's attached to a certificate.
You can't delete a policy if it has any non-default versions.
You can't delete the default version of a policy unless a new default version is selected, or the entire policy is deleted.
Before you can delete an entire policy, all of the non-default version of that policy must be deleted first.

1. From the AWS Explorer, expand the **IoT** service section.

1. Expand the **Policies** subsection and locate the policy you want to update.

1. Expand the policy that you want to update and then Context-select (right-click) the policy version that you want delete and choose **Delete**.

1. When a version is deleted, it will no longer be visible from the Explorer.

1. When the only version left for a policy is the default, then you can context-select (right-click) the parent policy and choose **Delete** to delete it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
