---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VgwTelemetry.html
---

# VgwTelemetry
<a name="API_VgwTelemetry"></a>

Describes telemetry for a VPN tunnel.

## Contents
<a name="API_VgwTelemetry_Contents"></a>

 ** acceptedRouteCount **
The number of accepted routes.
Type: Integer
Required: No

 ** certificateArn **
The Amazon Resource Name (ARN) of the VPN tunnel endpoint certificate.
Type: String
Required: No

 ** lastStatusChange **
The date and time of the last change in status. This field is updated when changes in IKE (Phase 1), IPSec (Phase 2), or BGP status are detected.
Type: Timestamp
Required: No

 ** outsideIpAddress **
The Internet-routable IP address of the virtual private gateway's outside interface.
Type: String
Required: No

 ** status **
The status of the VPN tunnel.
Type: String
Valid Values: `UP | DOWN`
Required: No

 ** statusMessage **
If an error occurs, a description of the error.
Type: String
Required: No

## See Also
<a name="API_VgwTelemetry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VgwTelemetry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VgwTelemetry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VgwTelemetry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
