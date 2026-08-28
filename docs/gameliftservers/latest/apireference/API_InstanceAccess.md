---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_InstanceAccess.html
---

# InstanceAccess
<a name="API_InstanceAccess"></a>

Information and credentials that you can use to remotely connect to an instance in an EC2 managed fleet. This data type is returned in response to a call to [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess).

## Contents
<a name="API_InstanceAccess_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Credentials **   <a name="gameliftservers-Type-InstanceAccess-Credentials"></a>
Security credentials that are required to access the instance.
Type: [InstanceCredentials](API_InstanceCredentials.md) object
Required: No

 ** FleetId **   <a name="gameliftservers-Type-InstanceAccess-FleetId"></a>
A unique identifier for the fleet containing the instance to be accessed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** InstanceId **   <a name="gameliftservers-Type-InstanceAccess-InstanceId"></a>
A unique identifier for the instance to be accessed.
Type: String
Pattern: `[a-zA-Z0-9\.-]+`
Required: No

 ** IpAddress **   <a name="gameliftservers-Type-InstanceAccess-IpAddress"></a>
IP address assigned to the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** OperatingSystem **   <a name="gameliftservers-Type-InstanceAccess-OperatingSystem"></a>
Operating system that is running on the instance.
Type: String
Valid Values: `WINDOWS_2012 | AMAZON_LINUX | AMAZON_LINUX_2 | WINDOWS_2016 | AMAZON_LINUX_2023 | WINDOWS_2022`
Required: No

## See Also
<a name="API_InstanceAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/InstanceAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/InstanceAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/InstanceAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
