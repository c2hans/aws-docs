---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientCertificateRevocationList.html
---

# ExportClientVpnClientCertificateRevocationList
<a name="API_ExportClientVpnClientCertificateRevocationList"></a>

Downloads the client certificate revocation list for the specified Client VPN endpoint.

## Request Parameters
<a name="API_ExportClientVpnClientCertificateRevocationList_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_ExportClientVpnClientCertificateRevocationList_ResponseElements"></a>

The following elements are returned by the service.

 **certificateRevocationList**
Information about the client certificate revocation list.
Type: String

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the client certificate revocation list.
Type: [ClientCertificateRevocationListStatus](API_ClientCertificateRevocationListStatus.md) object

## Errors
<a name="API_ExportClientVpnClientCertificateRevocationList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ExportClientVpnClientCertificateRevocationList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ExportClientVpnClientCertificateRevocationList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
