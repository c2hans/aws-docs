---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started-with-network-firewall-proxy.html
---

# Getting started with Network Firewall Proxy
<a name="getting-started-with-network-firewall-proxy"></a>

**Note**
Network Firewall Proxy is in public preview release and is subject to change.

AWS Network Firewall Proxy provides network traffic filtering and protection for your applications hosted in Amazon VPCs and on-premises environment. This tutorial provides steps for getting started with Network Firewall Proxy using the AWS Management Console. You can also use Network Firewall API operations to create and manage your firewalls. For more information about working with Network Firewall API operations, see the *AWS Network Firewall Proxy Reference.*

## Before you begin
<a name="before-you-begin-proxy"></a>

This tutorial walks you through the steps required to configure your Proxy in the same VPC as your application., like the one depicted in the [Architecture overview](proxy-architecture-overview.md).

To follow this tutorial, you'll need a test VPC where you want to configure a Network Firewall Proxy . Additionally, ensure you have set up all the prerequisites until pre-requisite step 4 (setting up trust) as mentioned in the [Pre-requisites](proxy-pre-requisites.md).

## High-level steps for implementation
<a name="high-level-steps-for-proxy-implementation"></a>

Setting up Network Firewall Proxy involves the following main configuration steps:

1. **Create Rule Groups** – Create rules to define your security controls, specifying which phase each rule should be applied in (pre-DNS, pre-request, or post-response). You can create multiple rules within each rule group to handle different security requirements.

1. **Configure Proxy Configuration** – Set up your proxy configuration by defining default (catch-all) rules for each phase (pre-DNS, pre-request, or post-response) and attaching the relevant rule groups created in step 1. This configuration establishes the processing order and priority for rule evaluation.

1. **Create Proxy** – While creating the proxy, you must select the NAT Gateway that it is created on. The Proxy uses this NAT Gateway for network address translation

1. Test and validate the proxy behavior

1. Monitor logs and metrics for proper operation

These steps work together to create a complete proxy configuration that processes and secures your outbound traffic according to your security policies.

## Step 1. Creating Rule Groups
<a name="step-1-creating-proxy-rule-groups"></a>

A Rule Group in VPC proxy is a reusable collection of ordered access control rules (ACLs) used to evaluate and filter HTTP/s traffic. For information about Rule Groups, see [Managing Your Rule Groups](managing-proxy-rule-groups.md).

**To create a Rule Group**

1. Sign in to the AWS Management Console and open the Amazon VPC console.

1. In the navigation pane, under **Network Firewall Proxy**, choose **Proxy rule groups**.

1. Choose **Create rule group.**

1. Enter a name.

1. Optionally enter the description for your Rule Group and add a tag.

1. Click Next.

1. Enter the phase to which this rule would apply. If you want the rule to apply to all 3 phases, select all 3 phases (Note: This will create 3 different rules for each phase).

1. Next, enter the action that you would like to take on the traffic. This can be allow, deny or alert.

1. Optionally, enter a description for the rule.

1. Enter the conditions, operators and values. Condition operators will be used to define how to perform a match. This is similar to how conditions are defined in AWS IAM service. For more details, look [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html). Condition keys define what is to be matched. Condition value specifies the exact value that needs to be matched against. For example, if you want to deny traffic for certain social media sites, you would define the following:
   + Rule group name: Deny social media.

   Create a rule with the following
   + Action: deny.
   + Description: Rule that will deny if requests attempt to go to social media websites.
   + ConditionOperator: "StringLike"
   + ConditionKey: "request:DestinationDomain"
   + "ConditionValues": [ \*facebook.com, \*instagram.com, wa.com, whatsapp.net, whatsapp.com, x.com ]

1. Click next

1. Review the details and click Create

## Step 2. Creating Proxy Configuration
<a name="step-2-creating-proxy-configuration"></a>

Proxy configurations use rule groups and other settings to define the traffic filtering behavior for a Proxy. In this procedure, you'll create a Proxy configuration using the rule groups that you created in the previous step. For information, see [Managing Your Proxy Configuration](managing-proxy-configuration.md).

**To create a Proxy configuration**

1. Sign in to the AWS Management Console and open the Amazon VPC console.

1. In the navigation pane, under **Network Firewall Proxy**, choose Proxy configuration

1. Choose Create Proxy configuration

1. Enter a name, optionally enter a description

1. Under default action, choose an action for each phase of the traffic. This will determine what will happen to traffic incase it does not match any rules.

1. Optionally add a tag

1. Click next

1. Click on attach rule group

1. Set a priority for the rule group. Lower the number means higher the priority.

1. Select the rule group that you created in the last step from the drop down.

1. Click Attach.

1. Check to make sure your rule group shows up in the attach rule group screen and click next.

1. Review the details and click create.

## Step 3. Creating Proxy
<a name="step-3-creating-proxy"></a>

Configure and deploy Proxy with NAT Gateway associations. A proxy configuration serves as the container for your filtering rules and settings. You create the configuration first. Then you attach it to one or more NAT gateways to enable traffic inspection.

Note: If the proxy creation fails and you need to attach another proxy to the NAT Gateway, you will need to delete the proxy resource that failed and then try to attach a new proxy.

**To create a Proxy**

1. Sign in to the AWS Management Console and open the Amazon VPC console.

1. In the navigation pane, under **Network Firewall Proxy**, choose Proxy

1. Enter a name.

1. Add the proxy configuration that you created in the previous step from the dropdown.

1. Attach to the right NAT Gateway.

1. Optionally, if you want to perform TLS interception on your traffic to filter on attributes in the HTTP header, check the box to enable TLS intercept mode. These are optional values you can enter:

   1. TLS interception \+ PCM

   1. Listener ports

   1. AWS account number

   1. Logging configuration

   1. Tags

1. Select a certificate (in PCA) from the dropdown with which the Proxy can establish trust with your applications.

1. Under VPC settings, select the NAT GW ARN from the dropdown that you want to associate the Proxy with.

1. Next, Enter the listener ports, usually it would be 8080 and 443 for HTTP and HTTPS traffic.

1. Next, enter your AWS account number.

1. Optionally, add tags.

1. Click Next.

1. Review the details and click Create.

Your configuration is now complete. You can setup your proxy variables on the workloads as mentioned in [Pre-requisites](proxy-pre-requisites.md) and send traffic from your VPCs and test out the proxy.
