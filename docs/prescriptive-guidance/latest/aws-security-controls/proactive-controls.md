---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/proactive-controls.html
---

# Proactive controls
<a name="proactive-controls"></a>

*Proactive controls* are security controls that are designed to prevent the creation of noncompliant resources. These controls can reduce the number of security events handled by responsive and detective controls. These controls make sure that deployed resources are compliant before they are deployed; therefore, there is no detection event that requires response or remediation.

For example, you might have a detective control in place that notifies you if an Amazon Simple Storage Service (Amazon S3) bucket becomes publicly accessible. You might also have a responsive control that remediates it. Although you already have these two controls in place, you can add another layer of protection by adding a proactive control. Through AWS CloudFormation, the proactive control can prevent the creation of update of any S3 bucket that has public access enabled. Threat actors could still bypass this control and deploy or modify resources outside of CloudFormation. In this case, the detective and responsive controls would remediate the security event.

Review the following about this type of control:
+ [Objectives](#proactive-objectives)
+ [Process](#proactive-process)
+ [Use cases](#proactive-use-cases)
+ [Technology](#proactive-technology)
+ [Business outcomes](#proactive-business-outcomes)

## Objectives
<a name="proactive-objectives"></a>
+ Proactive controls help you improve security operations and quality processes.
+ Proactive controls can help you adhere to security policies, standards, and regulatory or compliance obligations.
+ Proactive controls can prevent the creation of noncompliant resources.
+ Proactive controls can reduce the number of security findings.
+ Proactive controls provide another layer of protection against threat actors who bypass preventative controls and attempt to deploy noncompliant resources.
+ In combination with preventative, detective, and responsive controls, proactive controls can help you address potential security incidents.

## Process
<a name="proactive-process"></a>

Proactive controls complement preventative controls. Proactive controls reduce your organization's security risk and enforce the deployment of compliant resources. These controls evaluate resource compliance before the resource is created or updated. Proactive controls are generally implemented by using CloudFormation hooks. If the resource fails the proactive control validation, you can choose to either fail the resource deployment or present a warning message. The following are some tips and best practices for building proactive controls:
+ Make sure that proactive controls are mapped to your organization's compliance requirements.
+ Make sure that proactive controls follow security best practices for the associated service.
+ Use CloudFormation StackSets or another solution to deploy proactive controls across multiple AWS Regions or accounts.
+ Make sure that the warning or failure message associated with a proactive control is explicit and clear. This helps developers understand the reason why the resource did not pass the evaluation.
+ When building new proactive controls, start in observe mode. This means that you send a warning message instead of failing the resource deployment. This helps you understand the impact of the proactive control.
+ Enable logging in Amazon CloudWatch Logs for proactive controls.
+ If you need to monitor the invocation of a specific proactive control, use an Amazon EventBridge rule and subscribe to invocation events for the CloudFormation hook.

## Use cases
<a name="proactive-use-cases"></a>
+ Prevent deployment of noncompliant resources
+ Meet compliance requirements
+ Improve code quality by enforcing remediation of a security issue before deployment
+ Reduce operational downtime associated with remediating security issues after deployment

## Technology
<a name="proactive-technology"></a>

### CloudFormation hooks
<a name="9999999999999999cfnshort--hooks.f57873dd-5f8e-5dcf-af27-dc67f1234cab"></a>

[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions. [CloudFormation hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks.html) proactively evaluate the configuration of your CloudFormation resources before they are deployed. If noncompliant resources are found, it returns a failure status. Based on the hook failure mode, CloudFormation can fail the operation or present a warning that allows the user to continue with the deployment. You can use available hooks, or you can develop your own.

### AWS Control Tower
<a name="9999999999999999ctowerlong-.f3641eb2-8162-561d-9b51-cda670fd796e"></a>

[AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices. AWS Control Tower offers preconfigured [proactive controls](https://docs.aws.amazon.com/controltower/latest/userguide/proactive-controls.html) that you can enable in your landing zone. If your landing zone is setup using AWS Control Tower, you can use these optional proactive controls as a starting point for your organization. You can build additional, custom proactive controls in CloudFormation as needed.

## Business outcomes
<a name="proactive-business-outcomes"></a>

### Less human effort and error
<a name="less-human-effort-and-error.dd4774db-7958-5241-9091-092e9368d9bf"></a>

Proactive controls reduce the risk of human error that leads to the deployment of noncompliant resources. They also reduce human effort later in the development cycle because they make developers consider resource security prior to deployment. This applies the *shift left* practice to building secure resources because it forces compliance earlier in the development lifecycle.

### Reduced costs
<a name="reduced-costs.39cfbb78-47bd-5b06-bb1b-b76917465b50"></a>

It is generally more expensive to fix a security issue after deployment. Identifying and fixing issues earlier in the development cycle reduces the cost of development.

### Time savings
<a name="time-savings.8a7b8e47-daf4-507c-87e4-b767a2a8683e"></a>

Because proactive controls prevent the deployment of noncompliant resources, they reduce the amount of time you spend triaging and fixing security issues. They also the number of security findings, which detective controls would identify later in the development cycle.

### Regulatory compliance
<a name="regulatory-compliance.321e14bf-124d-5db6-9313-7d0f251f6ba0"></a>

If your organization needs to comply with internal or industry regulations, proactive controls can help you stay compliant and avoid violation penalties.

### Risk reduction
<a name="risk-reduction.3cfdf0ca-7d71-51a1-a21e-42d4d2a33e02"></a>

Proactive controls help developers deploy compliant and more securely built resources, so proactive controls reduce your organization's security risk.
