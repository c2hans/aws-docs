---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LightsailDistributionSubdomain.html
---

# LightsailDistributionSubdomain
<a name="API_LightsailDistributionSubdomain"></a>

Describes the Lightsail subdomain of a distribution. The distribution is reachable at the subdomain's web address, which is the subdomain followed by `amazonlightsail.com`.

## Contents
<a name="API_LightsailDistributionSubdomain_Contents"></a>

 ** name **   <a name="Lightsail-Type-LightsailDistributionSubdomain-name"></a>
The subdomain (for example, `mysite`), not its web address.
Type: String
Required: Yes

 ** state **   <a name="Lightsail-Type-LightsailDistributionSubdomain-state"></a>
The state of the subdomain for the distribution.
The following states are possible:
+  `Creating` – The subdomain is being created.
+  `Attaching` – The subdomain is being associated with the distribution.
+  `Attached` – The subdomain is associated with the distribution.
+  `Error` – The subdomain couldn't be created or associated with the distribution. For more information, see the `errorCode` and `errorDetails` parameters.
Type: String
Valid Values: `Creating | Attaching | Attached | Error`
Required: Yes

 ** errorCode **   <a name="Lightsail-Type-LightsailDistributionSubdomain-errorCode"></a>
The error code that describes why the subdomain is in the `Error` state.
Type: String
Required: No

 ** errorDetails **   <a name="Lightsail-Type-LightsailDistributionSubdomain-errorDetails"></a>
The details of the error that caused the subdomain to be in the `Error` state.
Type: String
Required: No

## See Also
<a name="API_LightsailDistributionSubdomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LightsailDistributionSubdomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LightsailDistributionSubdomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LightsailDistributionSubdomain)
