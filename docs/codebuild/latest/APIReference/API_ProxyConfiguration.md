---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProxyConfiguration.html
---

# ProxyConfiguration
<a name="API_ProxyConfiguration"></a>

Information about the proxy configurations that apply network access control to your reserved capacity instances.

## Contents
<a name="API_ProxyConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** defaultBehavior **   <a name="CodeBuild-Type-ProxyConfiguration-defaultBehavior"></a>
The default behavior of outgoing traffic.
Type: String
Valid Values: `ALLOW_ALL | DENY_ALL`
Required: No

 ** orderedProxyRules **   <a name="CodeBuild-Type-ProxyConfiguration-orderedProxyRules"></a>
An array of `FleetProxyRule` objects that represent the specified destination domains or IPs to allow or deny network access control to.
Type: Array of [FleetProxyRule](API_FleetProxyRule.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_ProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ProxyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ProxyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ProxyConfiguration)
