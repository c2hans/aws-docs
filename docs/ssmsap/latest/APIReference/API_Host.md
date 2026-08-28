---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Host.html
---

# Host
<a name="API_Host"></a>

Describes the properties of the Dedicated Host.

## Contents
<a name="API_Host_Contents"></a>

 ** EC2InstanceId **   <a name="ssmsap-Type-Host-EC2InstanceId"></a>
The ID of Amazon EC2 instance.
Type: String
Required: No

 ** HostIp **   <a name="ssmsap-Type-Host-HostIp"></a>
The IP address of the Dedicated Host.
Type: String
Required: No

 ** HostName **   <a name="ssmsap-Type-Host-HostName"></a>
The name of the Dedicated Host.
Type: String
Required: No

 ** HostRole **   <a name="ssmsap-Type-Host-HostRole"></a>
The role of the Dedicated Host.
Type: String
Valid Values: `LEADER | WORKER | STANDBY | UNKNOWN`
Required: No

 ** InstanceId **   <a name="ssmsap-Type-Host-InstanceId"></a>
The instance ID of the instance on the Dedicated Host.
Type: String
Required: No

 ** OsVersion **   <a name="ssmsap-Type-Host-OsVersion"></a>
The version of the operating system.
Type: String
Required: No

## See Also
<a name="API_Host_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Host)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Host)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Host)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
