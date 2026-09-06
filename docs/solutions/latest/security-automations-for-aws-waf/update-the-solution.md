---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

If you previously deployed the solution, follow this procedure to update the solution’s CloudFormation stack to get the latest version of the solution’s framework. Before you update the stack, read [Update considerations](#update-considerations) carefully.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select **Stacks** in the left navigation menu.

1. Select your existing `aws-waf-security-automations` CloudFormation stack.

1. Choose **Update**.

1. Select **Replace current template**.

1. Under **Specify template**:

   1. Select **Amazon S3 URL**.

   1. Copy the link of the `aws-waf-security-automations.template` [AWS CloudFormation](aws-cloudformation-templates.md).

   1. Paste the link in the **Amazon S3 URL** box.

   1. Verify that the correct template URL shows in the **Amazon S3 URL** text box.

   1. Choose **Next**.

   1. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Step 1. Launch the stack](step-1.-launch-the-stack.md) for details about the parameters.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings.

1. Select the box acknowledging that the template might create IAM resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can see the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of UPDATE\_COMPLETE in approximately 15 minutes.

## Update considerations
<a name="update-considerations"></a>

The following sections provide constraints and considerations for updating this solution.

### Resource type update
<a name="resource-type-update"></a>

You must deploy a new stack to update the **Endpoint** parameter after creating the stack. Don’t change the **Endpoint** parameter when updating the stack.

### WAFV2 upgrade
<a name="wafv2-upgrade"></a>

Starting from version 3.0, this solution supports AWS WAFV2. We replaced all the [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) API calls with [AWS WAFV2 API calls](https://docs.aws.amazon.com/waf/latest/APIReference/Welcome.html). This removes dependencies on Node.js and uses the most up-to-date Python runtime. To continue using this solution with the latest features and improvements, you must deploy version 3.0 or higher as a new stack.

### Customizations at stack update
<a name="customizations-at-stack-update"></a>

The out-of-box solution deploys a set of AWS WAF rules with default configurations into your AWS account with the CloudFormation stack. We don’t recommend applying customizations to rules deployed by the solution. Stack updates overwrite these changes. If you need customized rules, we recommend creating separate rules outside of the solution.

### Bad bot Protection upgrade
<a name="badbot-upgrade"></a>

In version **4.1.0**, the **Access Handler** Lambda with **API Gateway** has been deprecated and replaced with enhanced log functionality from the `Log parser - Bad bot` feature. Instead of using direct requests through API Gateway, the solution now re-uses the log stream to detect bad bots.

Previous Implementation:

1. Required Access Handler Lambda and API Gateway.

1. Used honeypot endpoint for direct request handling.

1. Required embedding honeypot endpoint in websites.

New Implementation (4.1.0\+): The **Bad Bot Protection** log parser now:

1. Inspects requests to the honeypot endpoint through logs.

1. Processes requests when **Bad Bot Protection** is activated.

1. Uses WAF filter **BadBotRuleFilter** to identify bad bot requests.

1. Analyzes log data to identify IP addresses exceeding defined quotas.

1. Updates AWS WAF IP set conditions to block identified addresses.

This change simplifies the architecture by eliminating duplicate functionality and leveraging existing log processing capabilities.

### CDK upgrade
<a name="CDK-upgrade"></a>

Starting from version v4.1.0, this solution is supported by CDK. If migrating from a version below v4.1.0 . Use the new template and update solution in Cloudformation . Then you can start to update the solution locally via your terminal using cdk deploy (see README for more information) If you try to use cdk deploy directly then you might see this error : Insufficient indentation in flow collection

The other way to update the solution will be to use the template provided by the solution and to go to the Cloudformation section of the AWS console and click update the solution and paste the new template there.

**Note**
If you are upgrading from version 3.0 or 3.1 to version 3.2 or newer of this solution, and you have manually inserted IP addresses into the [allowed or denied IP set](modify-the-allowed-and-denied-ip-sets-optional.md), you will be at risk of losing those IP addresses. To prevent that from happening, make a copy of the IP addresses in the allowed or denied IP set before upgrading the solution. Then after you complete the upgrade, add the IP addresses back to the IP set as needed. Refer to the [get-ip-set](https://docs.aws.amazon.com/cli/latest/reference/wafv2/get-ip-set.html) and [update-ip-set](https://docs.aws.amazon.com/cli/latest/reference/wafv2/update-ip-set.html) CLI commands. If you’re already using version 3.2 or newer, ignore this step.
