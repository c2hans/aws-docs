---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/controls.html
---

# Using controls to govern resources and monitor compliance

[AWS Control Tower controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) are high-level rules that provide ongoing governance and enforce specific policies for your AWS environment. You can apply controls to organizational units (OUs). Controls have three types: *preventive*, *detective*, and *proactive*.
+ **Preventive controls** help ensure that your accounts maintain compliance by disallowing actions that cause policy violations. Preventive controls use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), which are part of AWS Organizations. For example, the control [Disallow Actions as a Root User](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-controls.html#disallow-root-auser-actions) helps ensure that the high-privilege root user can't be used for unrestricted access to all resources in an account. Instead, users must use more restricted IAM roles.
+ **Detective controls** continuously monitor resources to detect non-compliance in your accounts, and then provide alerts through the dashboard. For example, the control [Detect Whether Unrestricted Incoming TCP Traffic is Allowed ](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-controls.html#rdp-disallow-internet)can detect whether a security group is set up with unrestricted incoming TCP traffic and alert the user to restrict their incoming protocols. Detective controls use [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html).
+ **Proactive controls **use [AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) to help ensure that custom configuration and compliance checks are automatically enforced during the deployment of CloudFormation resources. These controls make it easier to maintain a secure and compliant AWS environment.

**Note**
SCPs (preventive controls) don't have any effect in the management account. The root user and IAM administrators in the management account can perform any action that an SCP denies. This helps the management account retain full administrative control over the organization and helps prevent SCP errors from locking you out. The AWS CloudTrail and AWS Config recorder still track all actions in the management account and store them in the Log Archive account.

## Control guidance levels
<a name="control-guidance-levels.031e2d84-4dcb-5733-a241-e9b72e0249b5"></a>

AWS Control Tower controls have three different guidance levels: [mandatory](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html), [strongly recommended](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-controls.html), and [elective](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-controls.html).

Mandatory controls are automatically enabled and enforced by AWS Control Tower. Strongly recommended controls are optional and based on AWS best practices. Elective controls are also optional but are commonly used by enterprises. For more information, see the [controls library](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html) in the AWS Control Tower documentation.

**Note**
You can use custom SCPs and AWS Config Rules for additional detection and prevention. These aren't implemented in AWS Control Tower but can be implemented in AWS Organizations and AWS Config.

## Limitations for preventive controls
<a name="limitations-for-preventive-controls.ec81dee5-5c5c-59b8-818c-57a4c48e7980"></a>

You can have a maximum of 10 SCPs attached to an OU and a maximum of five OU levels. This includes both custom SCPs and AWS Control Tower–created SCPs, so try to consolidate your SCPs into fewer documents. (AWS Control Tower will do this automatically for its preventive controls.) If you need more SCPs on an account, you can nest OUs. For example, you can attach a maximum of 50 SCPs when you nest 5 OUs.

## Automating controls
<a name="automating-controls.0c2b1ffc-2b16-5c5b-937b-00ca9f05665d"></a>

AWS Control Tower supports operational concurrency for all controls. That is, you can activate or deactivate multiple preventive and detective controls without having to wait for control operations to complete.

You can automatically activate and deactivate controls by using any of the following with the [AWS Control Tower API](https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html):
+ [CloudFormation](https://docs.aws.amazon.com/controltower/latest/controlreference/enable-controls.html)
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/reference/controltower/enable-control.html)
+ [Language-specific AWS SDKs](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html#API_EnableControl_SeeAlso)

For more information about automating controls, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) in the AWS Control Tower documentation. The following sections discuss [mandatory controls](mandatory.md), [optional controls,](optional.md) and [custom controls](custom.md) in more detail.
