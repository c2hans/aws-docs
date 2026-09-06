---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceEntry.html
---

# InstanceEntry
<a name="API_InstanceEntry"></a>

Describes the Amazon Elastic Compute Cloud instance and related resources to be created using the `create cloud formation stack` operation.

## Contents
<a name="API_InstanceEntry_Contents"></a>

 ** availabilityZone **   <a name="Lightsail-Type-InstanceEntry-availabilityZone"></a>
The Availability Zone for the new Amazon EC2 instance.
Type: String
Required: Yes

 ** instanceType **   <a name="Lightsail-Type-InstanceEntry-instanceType"></a>
The instance type (`t2.micro`) to use for the new Amazon EC2 instance.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** portInfoSource **   <a name="Lightsail-Type-InstanceEntry-portInfoSource"></a>
The port configuration to use for the new Amazon EC2 instance.
The following configuration options are available:
+  `DEFAULT` - Use the default firewall settings from the Lightsail instance blueprint. If this is specified, then IPv4 and IPv6 will be configured for the new instance that is created in Amazon EC2.
+  `INSTANCE` - Use the configured firewall settings from the source Lightsail instance. If this is specified, the new instance that is created in Amazon EC2 will be configured to match the configuration of the source Lightsail instance. For example, if the source instance is configured for dual-stack (IPv4 and IPv6), then IPv4 and IPv6 will be configured for the new instance that is created in Amazon EC2. If the source instance is configured for IPv4 only, then only IPv4 will be configured for the new instance that is created in Amazon EC2.
+  `NONE` - Use the default Amazon EC2 security group. If this is specified, then only IPv4 will be configured for the new instance that is created in Amazon EC2.
+  `CLOSED` - All ports closed. If this is specified, then only IPv4 will be configured for the new instance that is created in Amazon EC2.
If you configured `lightsail-connect` as a `cidrListAliases` on your instance, or if you chose to allow the Lightsail browser-based SSH or RDP clients to connect to your instance, that configuration is not carried over to your new Amazon EC2 instance.
Type: String
Valid Values: `DEFAULT | INSTANCE | NONE | CLOSED`
Required: Yes

 ** sourceName **   <a name="Lightsail-Type-InstanceEntry-sourceName"></a>
The name of the export snapshot record, which contains the exported Lightsail instance snapshot that will be used as the source of the new Amazon EC2 instance.
Use the `get export snapshot records` operation to get a list of export snapshot records that you can use to create a CloudFormation stack.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** userData **   <a name="Lightsail-Type-InstanceEntry-userData"></a>
A launch script you can create that configures a server with additional user data. For example, you might want to run `apt-get -y update`.
Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu use `apt-get`, and FreeBSD uses `pkg`.
Type: String
Required: No

## See Also
<a name="API_InstanceEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceEntry)
