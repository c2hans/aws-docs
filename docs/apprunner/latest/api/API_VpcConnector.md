---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_VpcConnector.html
---

# VpcConnector
<a name="API_VpcConnector"></a>

Describes an AWS App Runner VPC connector resource. A VPC connector describes the Amazon Virtual Private Cloud (Amazon VPC) that an App Runner service is associated with, and the subnets and security group that are used.

Multiple revisions of a connector might have the same `Name` and different `Revision` values.

**Note**
At this time, App Runner supports only one revision per name.

## Contents
<a name="API_VpcConnector_Contents"></a>

 ** CreatedAt **   <a name="apprunner-Type-VpcConnector-CreatedAt"></a>
The time when the VPC connector was created. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** DeletedAt **   <a name="apprunner-Type-VpcConnector-DeletedAt"></a>
The time when the VPC connector was deleted. It's in Unix time stamp format.
Type: Timestamp
Required: No

 ** SecurityGroups **   <a name="apprunner-Type-VpcConnector-SecurityGroups"></a>
A list of IDs of security groups that App Runner uses for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** Status **   <a name="apprunner-Type-VpcConnector-Status"></a>
The current state of the VPC connector. If the status of a connector revision is `INACTIVE`, it was deleted and can't be used. Inactive connector revisions are permanently removed some time after they are deleted.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** Subnets **   <a name="apprunner-Type-VpcConnector-Subnets"></a>
A list of IDs of subnets that App Runner uses for your service. All IDs are of subnets of a single Amazon VPC.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

 ** VpcConnectorArn **   <a name="apprunner-Type-VpcConnector-VpcConnectorArn"></a>
The Amazon Resource Name (ARN) of this VPC connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** VpcConnectorName **   <a name="apprunner-Type-VpcConnector-VpcConnectorName"></a>
The customer-provided VPC connector name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,39}`
Required: No

 ** VpcConnectorRevision **   <a name="apprunner-Type-VpcConnector-VpcConnectorRevision"></a>
The revision of this VPC connector. It's unique among all the active connectors (`"Status": "ACTIVE"`) that share the same `Name`.
At this time, App Runner supports only one revision per name.
Type: Integer
Required: No

## See Also
<a name="API_VpcConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/VpcConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/VpcConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/VpcConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
