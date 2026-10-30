---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_WafBotControlConfig.html
---

# WafBotControlConfig
<a name="API_WafBotControlConfig"></a>

Describes the configuration of the bot control Web Application Firewall (WAF) rule group.

## Contents
<a name="API_WafBotControlConfig_Contents"></a>

 ** inspectionLevel **   <a name="Lightsail-Type-WafBotControlConfig-inspectionLevel"></a>
The inspection level of the bot control rule group.
The following inspection levels are possible:
+  `COMMON` – Detects a variety of bots that identify themselves, such as web scraping frameworks, search engines, and automated browsers.
+  `TARGETED` – Includes the `COMMON` protections, and adds detection for sophisticated bots that don't identify themselves. This level uses rate limiting, CAPTCHA, and background browser challenges.
Type: String
Valid Values: `COMMON | TARGETED`
Required: No

## See Also
<a name="API_WafBotControlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/WafBotControlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/WafBotControlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/WafBotControlConfig)
