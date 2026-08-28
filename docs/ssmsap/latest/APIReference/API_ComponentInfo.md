---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ComponentInfo.html
---

# ComponentInfo
<a name="API_ComponentInfo"></a>

This is information about the component of your SAP application, such as Web Dispatcher.

## Contents
<a name="API_ComponentInfo_Contents"></a>

 ** ComponentType **   <a name="ssmsap-Type-ComponentInfo-ComponentType"></a>
This string is the type of the component.
Accepted value is `WD`.
Type: String
Valid Values: `HANA | HANA_NODE | ABAP | ASCS | DIALOG | WEBDISP | WD | ERS`
Required: Yes

 ** Ec2InstanceId **   <a name="ssmsap-Type-ComponentInfo-Ec2InstanceId"></a>
This is the Amazon EC2 instance on which your SAP component is running.
Accepted values are alphanumeric.
Type: String
Pattern: `i-[\w\d]{8}$|^i-[\w\d]{17}`
Required: Yes

 ** Sid **   <a name="ssmsap-Type-ComponentInfo-Sid"></a>
This string is the SAP System ID of the component.
Accepted values are alphanumeric.
Type: String
Pattern: `[A-Z][A-Z0-9]{2}`
Required: Yes

## See Also
<a name="API_ComponentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ComponentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ComponentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ComponentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
