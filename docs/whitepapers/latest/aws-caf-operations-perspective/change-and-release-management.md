---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/change-and-release-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Change and release management
<a name="change-and-release-management"></a>

 **Introduce and modify workloads while minimizing the risk to production environments. **

 If you are migrating to the cloud, it’s important to understand that the pace of change will accelerate dramatically. This pace of change acts as an enabler for the business to achieve agility and allow it to be competitive with its peers. It also means that you need to rethink the way in which IT operates. Project teams no longer have to liaise with procurement teams to generate purchase orders and then place them with suppliers to await delivery and installation. Services can now become available within minutes or even seconds.

## Start
<a name="start-33"></a>

 The first thing to keep in mind is that change management is not designed to minimize business risk; instead, the process should ensure that overall business risk is optimized. A good change management process in any environment should enable the delivery of business value whilst protecting the business by balancing risk against business value, and it should do so in a way that maximizes productivity and minimizes wasted effort or cost for all participants in the process.

 Every change should deliver business value, and the change management processes should be geared towards enabling that delivery. Rather than acting as a gatekeeper, the process should enable developers to fulfil their function in adding business value, using the products they deploy to production environments.

 The key concepts of change management remain the same in the cloud. Change delivers business value, and it should be efficient. Agile methodologies and the automation capabilities of the cloud go hand in hand with the core principles of change management, as they are also designed to deliver business value quickly and efficiently. Nevertheless, there are some key areas that may require existing change processes to be modified to adapt to new methods of delivering change.

 Widening the scope of a standard change is the starting point for managing change in the cloud. Without doing this, you risk the change management process becoming a bottleneck for delivering business value. It’s always worth considering the business impact and risk of not implementing a change, or introducing a delay, keeping in mind that the purpose of managing change is to optimize business risk.

 If automation, pipelines, and deployment methods are in place, it may be possible to reconsider the approach to standard changes. A standard change is where:
+  There is a defined trigger to initiate the change request.
+  Actions are well known, documented, and proven
+  Authority is given in advance (or pre-authorized).
+  The risk is usually low.

 If the appropriate automation, testing, and deployment strategies are put in place, this should result in a scenario where large, infrequent, and risky changes are transformed into small, frequent, low-risk changes. By understanding the risk-reduction strategies enabled by the cloud, it should be possible, and it may even be necessary, to widen the scope of a standard change to include deployments that would have previously been considered as normal changes due to the risks associated with them in traditional IT environments.

 As changes become more frequent due to agile methodologies and increased automation, there is a risk that change management becomes overburdened with normal changes, which can lead to delaying changes due to bandwidth constraints. Important details might be missed as changes are not properly scrutinized due to resource constraints. Both of these scenarios introduce business risk that change management aims to optimize. In an environment of small, frequent changes, standard changes should become the new normal so that proper scrutiny can be given to normal changes, optimizing business risk and enabling the delivery of business value.

## Advance
<a name="advance-33"></a>

 Changes become safer the more that you automate them, and as outcomes become more predictable. Outside of development and deployment, the easiest place to start is with patching and standardization of items, such as agent installation and configuration.

 Automate the deployment of patches to operating systems (OS’) and applications without any human intervention and with automated rollback using [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html). Doing so will allow you to take automated actions, before and after deployment of patches, such as implementing post-deployment testing. This kind of automation allows you to continue to think differently about change management, because the risks have been dramatically reduced and the process has been proven. Inherently risky procedures that can be automated, such as patching, can be transformed into standard changes, because the risk has been significantly lowered and proven rollback strategies are in place.

 At this point, you should consider integrating your existing IT Service Management (ITSM) tooling, such as [ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-what-is.html) or [Jira Service Desk](https://docs.aws.amazon.com/smc/latest/ag/integrations-jiraservicedesk.html) with cloud services including AWS Config, [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html), [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html), and [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) to make it easier to manage and record incidents and changes that take place in the cloud.

 Use infrastructure as code tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) to deploy applications and infrastructure as code. This helps ensure consistency of deployments, reducing risk even further.

## Excel
<a name="excel-33"></a>

 To minimize risk, you should make deployments small and frequent. Because this will inevitably increase the number of changes, it’s vital that your deployment processes adapt to ensure repeatability and consistency throughout the lifecycle of your applications. You should automate your deployment and testing using an automated pipeline. This decreases the requirement for manual testing, and reduces the likelihood that your changes will need to be scrutinized by a change advisory board (CAB).

 Operations must be able to support a new release or service before it is made available to the end user. With the correct tooling, this process can be largely automated, including the creation of documentation, provisioning of automated runbooks and playbooks, and building predefined and automated patching plans. This process can be made even more robust using the correct tooling to ensure that only pre-approved services are used. Use [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to automate deployment, testing, documentation and the provisioning of runbooks, playbooks, dashboards, alerts, and patching schedules.

 The focus of a test manager should be to automate service acceptance testing as much as possible. This is made easier in the cloud with a wide variety of tools that are available for both validation and testing.
+  Use [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) to test your application on multiple devices and platforms.
+  Use [synthetic monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to monitor your endpoints and APIs.
+  Use [test events](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html) to create unit tests for your Lambda functions.
+  Use Lambda, [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html), or Amazon EC2 to automate pipelines using existing tooling or new tools designed for the cloud.
+  Add unit tests and synthetic transactions to your [CI/CD pipeline](https://aws.amazon.com/getting-started/hands-on/set-up-ci-cd-pipeline/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
