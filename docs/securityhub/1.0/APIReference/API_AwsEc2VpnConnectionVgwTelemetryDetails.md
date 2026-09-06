---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpnConnectionVgwTelemetryDetails.html
---

# AwsEc2VpnConnectionVgwTelemetryDetails
<a name="API_AwsEc2VpnConnectionVgwTelemetryDetails"></a>

Information about the VPN tunnel.

## Contents
<a name="API_AwsEc2VpnConnectionVgwTelemetryDetails_Contents"></a>

 ** AcceptedRouteCount **   <a name="securityhub-Type-AwsEc2VpnConnectionVgwTelemetryDetails-AcceptedRouteCount"></a>
The number of accepted routes.
Type: Integer
Required: No

 ** CertificateArn **   <a name="securityhub-Type-AwsEc2VpnConnectionVgwTelemetryDetails-CertificateArn"></a>
The ARN of the VPN tunnel endpoint certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastStatusChange **   <a name="securityhub-Type-AwsEc2VpnConnectionVgwTelemetryDetails-LastStatusChange"></a>
The date and time of the last change in status.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** OutsideIpAddress **   <a name="securityhub-Type-AwsEc2VpnConnectionVgwTelemetryDetails-OutsideIpAddress"></a>
The Internet-routable IP address of the virtual private gateway's outside interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsEc2VpnConnectionVgwTelemetryDetails-Status"></a>
The status of the VPN tunnel. Valid values are `DOWN` or `UP`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StatusMessage **   <a name="securityhub-Type-AwsEc2VpnConnectionVgwTelemetryDetails-StatusMessage"></a>
If an error occurs, a description of the error.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VpnConnectionVgwTelemetryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpnConnectionVgwTelemetryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpnConnectionVgwTelemetryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpnConnectionVgwTelemetryDetails)
