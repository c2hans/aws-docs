---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_MonitoredResourceInfo.html
---

# MonitoredResourceInfo
<a name="API_MonitoredResourceInfo"></a>

Describes resource being monitored by an alarm.

An alarm is a way to monitor your Amazon Lightsail resource metrics. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms).

## Contents
<a name="API_MonitoredResourceInfo_Contents"></a>

 ** arn **   <a name="Lightsail-Type-MonitoredResourceInfo-arn"></a>
The Amazon Resource Name (ARN) of the resource being monitored.
Type: String
Pattern: `^arn:(aws[^:]*):([a-zA-Z0-9-]+):([a-z0-9-]+):([0-9]+):([a-zA-Z]+)/([a-zA-Z0-9-]+)$`
Required: No

 ** name **   <a name="Lightsail-Type-MonitoredResourceInfo-name"></a>
The name of the Lightsail resource being monitored.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-MonitoredResourceInfo-resourceType"></a>
The Lightsail resource type of the resource being monitored.
Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

## See Also
<a name="API_MonitoredResourceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/MonitoredResourceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/MonitoredResourceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/MonitoredResourceInfo)
