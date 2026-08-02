---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/managing-proxy-configuration.html
---

# Managing Your Proxy Configuration
<a name="managing-proxy-configuration"></a>

**Note**
Network Firewall Proxy is in public preview release and is subject to change.

Proxy configurations use rule groups and other settings to define the traffic filtering behavior for a Proxy. In this procedure, you'll create a Proxy configuration using the rule groups that you created in the previous step. For information, see [Managing Your Rule Groups](managing-proxy-rule-groups.md).

## To create a Proxy configuration
<a name="create-proxy-configuration"></a>

**To create a Proxy configuration**

1. Sign in to the AWS Management Console and open the Amazon VPC console.

1. In the navigation pane, under **Network Firewall Proxy**, choose **Proxy configuration**.

1. Choose **Create Proxy configuration**.

1. Enter a name and optionally enter a description.

1. Under **Default action**, choose an action for each phase of the traffic. This determines what happens to traffic if it does not match any rules.

1. (Optional) Add a tag.

1. Choose **Next**.

1. Choose **Attach rule group**.

1. Set a priority for the rule group. Lower numbers indicate higher priority.

1. Select the rule group that you created in the previous step from the dropdown menu.

1. Choose Attach.

1. Verify that your rule group appears in the attach rule group screen and choose **Next**.

1. Review the details and choose **Create**.

## Proxy configuration operations
<a name="proxy-configuration-operations"></a>

A Network Firewall proxy configuration contains the rules that the proxy uses to filter your traffic. Here are the available proxy configuration management operations:

**Create configuration**
Creates a new proxy configuration to manage network traffic.

**Delete configuration**
Allowed only if the proxy configuration is not attached to a proxy. Proxy configuration cannot be deleted until all associated proxies are detached from it.

**Describe configuration**
Retrieves detailed information about a specific proxy configuration for an account.

**List configurations**
Displays all proxy configuration resource names present in an account.

**Modify configuration**
Updates attributes of an existing proxy configuration such as priority of the rule groups, excluding rule group modifications. Cannot attach a different proxy configuration when one proxy configuration has already been attached. You can modify the currently attached proxy configuration if needed.

**Modify rule group priorities**
Adjusts the priority order of rule groups within the proxy configuration.

**Attach rule groups**
Adds rule groups to a configuration at specific positions or appends them to the end of the list. Includes explicit priority settings for simplified user experience.
Steps to attach rule groups:

1. On AWS console, click on proxy configuration. Select the proxy that you want to make the change to.

1. Click on attach rule group.

1. Add a priority for the rule group.

1. Click on attach.

**Detach rule groups**
Removes rule groups from a configuration without deleting them. The rule groups continue to exist and must be deleted separately using the delete-egress-proxy-rule-group action.
Steps to detach rule groups:

1. On the AWS console, click on proxy configuration. Select the proxy that you want to make the change to.

1. Select the rule group.

1. Click on detach on the right top.

1. Type detach to confirm.

1. Click on detach.
