---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-local-logs.html
---

# Use service logs in AWS IoT SiteWise
<a name="gateway-local-logs"></a>

SiteWise Edge gateway devices include service log files to help debug issues. The following sections will help you find and utilize the service log files for the AWS IoT SiteWise OPC UA Collector and AWS IoT SiteWise Publisher components.

## AWS IoT SiteWise OPC UA Collector service log file
<a name="collector-local-log-file"></a>

The AWS IoT SiteWise OPC UA Collector component uses the following log file.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgeCollectorOpcua.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgeCollectorOpcua.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace {{`/greengrass/v2`}} or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgeCollectorOpcua.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgeCollectorOpcua.log -Tail 10 -Wait
  ```

------

## AWS IoT SiteWise Publisher service log file
<a name="publisher-local-log-file"></a>

The AWS IoT SiteWise Publisher component uses the following log file.

------
#### [ Linux ]

```
{{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgePublisher.log
```

------
#### [ Windows ]

```
{{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgePublisher.log
```

------

**To view this component's logs**
+ Run the following command on the core device to view this component's log file in real time. Replace {{`/greengrass/v2`}} or {{C:\\greengrass\\v2}} with the path to the AWS IoT Greengrass root folder.

------
#### [ Linux ]

  ```
  sudo tail -f {{/greengrass/v2}}/logs/aws.iot.SiteWiseEdgePublisher.log
  ```

------
#### [ Windows (PowerShell) ]

  ```
  Get-Content {{C:\greengrass\v2}}\logs\aws.iot.SiteWiseEdgePublisher.log -Tail 10 -Wait
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
