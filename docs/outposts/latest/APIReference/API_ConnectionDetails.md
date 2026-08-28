---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ConnectionDetails.html
---

# ConnectionDetails
<a name="API_ConnectionDetails"></a>

 Information about a connection.

## Contents
<a name="API_ConnectionDetails_Contents"></a>

 ** AllowedIps **   <a name="outposts-Type-ConnectionDetails-AllowedIps"></a>
 The allowed IP addresses.
Type: Array of strings
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$`
Required: No

 ** ClientPublicKey **   <a name="outposts-Type-ConnectionDetails-ClientPublicKey"></a>
 The public key of the client.
Type: String
Length Constraints: Fixed length of 44.
Pattern: `^[a-zA-Z0-9/+]{43}=$`
Required: No

 ** ClientTunnelAddress **   <a name="outposts-Type-ConnectionDetails-ClientTunnelAddress"></a>
 The client tunnel address.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$`
Required: No

 ** ServerEndpoint **   <a name="outposts-Type-ConnectionDetails-ServerEndpoint"></a>
 The endpoint for the server.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 21.
Pattern: `^([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$`
Required: No

 ** ServerPublicKey **   <a name="outposts-Type-ConnectionDetails-ServerPublicKey"></a>
 The public key of the server.
Type: String
Length Constraints: Fixed length of 44.
Pattern: `^[a-zA-Z0-9/+]{43}=$`
Required: No

 ** ServerTunnelAddress **   <a name="outposts-Type-ConnectionDetails-ServerTunnelAddress"></a>
 The server tunnel address.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 18.
Pattern: `^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$`
Required: No

## See Also
<a name="API_ConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ConnectionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
