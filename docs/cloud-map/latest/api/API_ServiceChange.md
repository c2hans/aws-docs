---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceChange.html
---

# ServiceChange
<a name="API_ServiceChange"></a>

A complex type that contains changes to an existing service.

## Contents
<a name="API_ServiceChange_Contents"></a>

 ** Description **   <a name="cloudmap-Type-ServiceChange-Description"></a>
A description for the service.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** DnsConfig **   <a name="cloudmap-Type-ServiceChange-DnsConfig"></a>
Information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
Type: [DnsConfigChange](API_DnsConfigChange.md) object
Required: No

 ** HealthCheckConfig **   <a name="cloudmap-Type-ServiceChange-HealthCheckConfig"></a>
 *Public DNS and HTTP namespaces only.* Settings for an optional health check. If you specify settings for a health check, AWS Cloud Map associates the health check with the records that you specify in `DnsConfig`.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: No

## See Also
<a name="API_ServiceChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ServiceChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ServiceChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ServiceChange)
