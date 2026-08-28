---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-challenge-rule-action.html
---

# AWS WAF – Challenge rule action
<a name="aws-waf-challenge-rule-action"></a>

 The [Challenge rule](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-actions.html) action provides an effective defense against DDoS botnets, which typically use basic scripts designed to maximize target impact while minimizing operational costs. This action requires clients to complete a JavaScript-based proof of work challenge and present a valid `aws-waf-token` cookie before allowing the request to proceed. This mechanism has proven highly effective against automated DDoS attacks, as most attack scripts can't process JavaScript or handle cookies properly.

 When implementing Challenge actions, it's important to consider potential impacts on legitimate users. Some visitors might be unable to access your application if they have JavaScript disabled, use older browsers, or rely on screen readers and accessibility tools.

 The token can only be acquired using HTTP GET requests with the Accept header containing text or html (unless there has been prior [client side integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html), which can be done for customers using [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html) or one of the other intelligent threat mitigations rule groups). After the token is acquired, it will be presented by the client on subsequent requests for the same domain until the TTL, in the form of cookie expiration, expires.

 AWS recommends implementing Challenge actions strategically. Consider using them selectively during active attacks rather than as a continuous protection measure and combine them with rate-based rules to optimize cost efficiency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
