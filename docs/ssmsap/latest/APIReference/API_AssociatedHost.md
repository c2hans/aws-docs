---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_AssociatedHost.html
---

# AssociatedHost
<a name="API_AssociatedHost"></a>

Describes the properties of the associated host.

## Contents
<a name="API_AssociatedHost_Contents"></a>

 ** Ec2InstanceId **   <a name="ssmsap-Type-AssociatedHost-Ec2InstanceId"></a>
The ID of the Amazon EC2 instance.
Type: String
Required: No

 ** Hostname **   <a name="ssmsap-Type-AssociatedHost-Hostname"></a>
The name of the host.
Type: String
Required: No

 ** IpAddresses **   <a name="ssmsap-Type-AssociatedHost-IpAddresses"></a>
The IP addresses of the associated host.
Type: Array of [IpAddressMember](API_IpAddressMember.md) objects
Required: No

 ** OsVersion **   <a name="ssmsap-Type-AssociatedHost-OsVersion"></a>
The version of the operating system.
Type: String
Required: No

## See Also
<a name="API_AssociatedHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/AssociatedHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/AssociatedHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/AssociatedHost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
