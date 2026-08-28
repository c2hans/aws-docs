---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ConnectionPortRange.html
---

# ConnectionPortRange
<a name="API_ConnectionPortRange"></a>

The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.

The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.

## Contents
<a name="API_ConnectionPortRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FromPort **   <a name="gameliftservers-Type-ConnectionPortRange-FromPort"></a>
Starting value for the port range.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: Yes

 ** ToPort **   <a name="gameliftservers-Type-ConnectionPortRange-ToPort"></a>
Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: Yes

## See Also
<a name="API_ConnectionPortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ConnectionPortRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ConnectionPortRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ConnectionPortRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
