---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/proxy-logging-and-monitoring.html
---

# Logging and Monitoring
<a name="proxy-logging-and-monitoring"></a>

**Note**
Network Firewall Proxy is in public preview release and is subject to change.

Logging provides detailed information about network traffic, including the time that the proxy received a packet, detailed information about the packet, and any rule action taken against the packet. The logs are published to the log destination that you configure, where you can retrieve and view them.

Steps to configure logging:

1. Go to the proxy page on the AWS console.

1. Click on proxies. Choose the proxy you want to configure logging on.

1. Click on Log delivery tab.

1. Click on the add log delivery.

1. Choose the destination for delivering the logs - CloudWatch, S3 or Kinesis.

1. We will go through the steps for CloudWatch logs here.

1. Select the type of log between allow log, deny log and alert log. You can only select one at a time. If you need multiple logs, create multiple subscriptions by going through the steps above again.

1. Select the cloudwatch log group. Note: This log group will need to be created beforehand on Cloudwatch. For more details, check [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group).

1. (Optional) Select the log fields that you require to be shown in the log.

**Note**
There are some mandatory fields that cannot be unselected if you choose to configure logging. These include - event\_timestamp, proxy\_name and final\_action. Some log fields will be selected by default and if you do not make changes, these will be included in the logs. You can enable/ disable fields to customize the fields that will appear in your log.

1. (Optional) You can also configure other fields such as output format and field delimiter.

1. Click Add.

Log delivery is now successfully created.

## Contents of a proxy log
<a name="contents-of-proxy-log"></a>

Proxy provides comprehensive logs that include details of each request it receives from the client and each response it sends back to the client. The logs contain the following information:

**Basic Request Information**

+ Proxy name
+ Event timestamp
+ Client source IP and port
+ Source VPC and VPCE identifiers
+ AWS account ID

**URL Components**

+ Destination domain
+ URL scheme (http/https)
+ Authority
+ Path
+ Query parameters
+ URL fragments

**Connection Details**

+ HTTP method (e.g., GET, POST)
+ Destination IP and port
+ HTTP status code

**Rule Evaluation Information**

+ First alert match
+ All matching rules, including:
  + Rule IDs
  + Hook points (pre\_dns, pre\_request, post\_response)
  + Actions taken (alert, allow)
+ Final action
+ Final rule name
+ Final rule group name

This logging structure allows for detailed tracking and analysis of all proxy traffic, providing ability for effective monitoring and troubleshooting of network requests.

## Example alert log entry
<a name="proxy-example-alert-log-entry"></a>

The following example shows an alert log entry for Network Firewall Proxy.

```
{
  "proxy_name": "my-awesome-proxy",
  "event_timestamp": 1717171,
  "client_src_ip": "192.168.10.1",
  "client_src_port": 123,
  "src_vpc": "vpc-aabbccdd",
  "src_vpce": "vpce-xxyyzz",
  "account_id": "1122334455",
  "dest_domain": "www.amazon.com",
  "url": {
    "scheme": "https",
    "authority": "www.amazon.com",
    "path": "/xyz",
    "query":"crid=U7M9K3I5QT25&dib",
    "fragment": ""
  },
  "http_method": "GET",
  "dest_ip": "205.251.242.103",
  "dest_port": 443,
  "http_status_code": 200,
  "first_alert_match": "rule-that-alerts-if-it-goes-to-amazon.com",
  "all_matches": {
    "matches": [{
      "rule_id": "rule-that-alerts-if-it-goes-to-amazon.com",
      "hook": "pre_dns",
      "action": "alert"
    },
    {
      "rule_id": "default",
      "hook": "pre_dns",
      "action": "allow"
    }, {
      "rule_id": "default",
      "hook": "pre_request",
      "action": "allow"
    }, {
      "rule_id": "rule-that-alerts-if-it-returns-html",
      "hook": "post_response",
      "action": "alert"
    }, {
      "rule_id": "default",
      "hook": "post_response",
      "action": "allow"
    }]
  },
  "final_action": "allow",
  "final_rule_name": "",
  "final_rule_group_name": ""
}
```
