---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ChallengeAction.html
---

# ChallengeAction
<a name="API_ChallengeAction"></a>

Specifies that AWS WAF should run a `Challenge` check against the request to verify that the request is coming from a legitimate client session:
+ If the request includes a valid, unexpired challenge token, AWS WAF applies any custom request handling and labels that you've configured and then allows the web request inspection to proceed to the next rule, similar to a `CountAction`.
+ If the request doesn't include a valid, unexpired challenge token, AWS WAF discontinues the web ACL evaluation of the request and blocks it from going to its intended destination.

   AWS WAF then generates a challenge response that it sends back to the client, which includes the following:
  + The header `x-amzn-waf-action` with a value of `challenge`.
  + The HTTP status code `202 Request Accepted`.
  + If the request contains an `Accept` header with a value of `text/html`, the response includes a JavaScript page interstitial with a challenge script.

  Challenges run silent browser interrogations in the background, and don't generally affect the end user experience.

  A challenge enforces token acquisition using an interstitial JavaScript challenge that inspects the client session for legitimate behavior. The challenge blocks bots or at least increases the cost of operating sophisticated bots.

  After the client session successfully responds to the challenge, it receives a new token from AWS WAF, which the challenge script uses to resubmit the original request.

You can configure the expiration time in the `ChallengeConfig` `ImmunityTimeProperty` setting at the rule and web ACL level. The rule setting overrides the web ACL setting.

This action option is available for rules. It isn't available for web ACL default actions.

## Contents
<a name="API_ChallengeAction_Contents"></a>

 ** CustomRequestHandling **   <a name="WAF-Type-ChallengeAction-CustomRequestHandling"></a>
Defines custom handling for the web request, used when the challenge inspection determines that the request's token is valid and unexpired.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.
Type: [CustomRequestHandling](API_CustomRequestHandling.md) object
Required: No

## See Also
<a name="API_ChallengeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ChallengeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ChallengeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ChallengeAction)
