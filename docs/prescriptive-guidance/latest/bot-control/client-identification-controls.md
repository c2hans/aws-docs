---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/client-identification-controls.html
---

# Client identification controls for managing bots
<a name="client-identification-controls"></a>

If attack-related traffic cannot be easily recognized through static attributes, then detection needs to be able to accurately identify the client making the request. For example, rate-based rules are often more effective and harder to evade when the attribute being rate-limited is application-specific, such as a cookie or token. Using a cookie tied to a session prevents botnet operators from being able to duplicate similar request flows across many bots.

Token acquisition is commonly used for client identification. For token acquisition, a JavaScript code collects information to generate a token that is evaluated on the server side. The evaluation can range from verifying that JavaScript is running on the client to collecting device information for fingerprinting. Token acquisition requires integrating a JavaScript SDK into the site or application, or it requires that a service provider does the injection dynamically.

Requiring JavaScript support adds an additional hurdle for bots attempting to emulate browsers. When an SDK is involved, such as in a mobile application, token acquisition verifies the SDK implementation and prevents bots from mimicking the application's requests.

Token acquisition requires the use of SDKs implemented on the client side of the connection. The following AWS WAF features provide a JavaScript-based SDK for browsers and a application-based SDK for mobile devices: [Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html), [Fraud Control account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp.html) and [Fraud Control account creation fraud prevention (ACFP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp.html).

The techniques for client identification include CAPTCHA, browser profiling, device fingerprinting, and TLS fingerprinting.

## CAPTCHA
<a name="captcha"></a>

Completely automated public Turing test to tell computers and humans apart ([CAPTCHA](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha.html)) is used to distinguish between robotic and human visitors and to prevent web scraping, credential stuffing, and spam. There are a variety of implementations, but they often involve a puzzle that a human can solve. CAPTCHAs offer an additional layer of defense against common bots and can reduce the false positives in bot detection.

AWS WAF allows rules to run a CAPTCHA action against web requests that match a rule's inspection criteria. This action is the result of the evaluation of client identification information collected by the service. AWS WAF rules can require CAPTCHA challenges to be solved for specific resources that are frequently targeted by bots, such as login, search, and form submissions. AWS WAF can directly serve CAPTCHA through interstitial means or by using an SDK to handle it on the client side. For more information see [CAPTCHA and Challenge in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge.html).

## Browser profiling
<a name="browser-profiling"></a>

*Browser profiling* is a method of collecting and evaluating browser characteristics, as part of token acquisition, to distinguish real humans using an interactive browser from distributed bot activity. You can perform browser profiling passively through headers, header order, and other characteristics of requests that are inherent to how browsers work.

You can also perform browser profiling in code by using token acquisition. By using JavaScript for browser profiling, you can quickly determine if a client supports JavaScript. This helps you detect simple bots that do not support it. Browser profiling checks more than just HTTP headers and JavaScript support; browser profiling makes it difficult for bots to fully emulate a web browser. Both browser profiling options have the same goal: to find patterns in a browser profile that indicate inconsistency with how a real browser behaves.

AWS WAF bot control for targeted bots provides an indication, as part of token evaluation, of whether a browser shows evidence of automation or inconsistent signals. AWS WAF flags the request in order to take the action specified in the rule. For more information, see [Detect and block advanced bot traffic](https://aws.amazon.com/blogs/security/detect-and-block-advanced-bot-traffic/) in the AWS Security Blog.

## Device fingerprinting
<a name="device-fingerprinting"></a>

Device fingerprinting is similar to browser profiling, but it is not limited to browsers. Code running on a device (which can be a mobile device or a web browser) collects and reports details of the device to a backend server. The details can include system attributes, such as memory, CPU type, operating system (OS) kernel type, OS version, and virtualization.

You can use device fingerprinting to recognize if a bot is emulating an environment or if there are direct signs that automation is in use. Beyond this, device fingerprinting can also be used to recognize repeated requests from the same device.

Recognizing repeated requests from the same device, even if the device tries to change some characteristics of the request, allows a backend system to impose rate-limiting rules. Rate-limiting rules that are based on device fingerprinting are typically more effective than rate-limiting rules based on IP addresses. This helps you mitigate against bot traffic that is rotating between VPNs or proxies but is sourced from a small number of devices.

When used with application integration SDKs, AWS WAF bot control for targeted bots, can aggregate client session request behavior. This helps you detect and separate legitimate client sessions from malicious client sessions, even when both originate from the same IP address. For more information about AWS WAF bot control for targeted bots, see [Detect and block advanced bot traffic](https://aws.amazon.com/blogs/security/detect-and-block-advanced-bot-traffic/) in the AWS Security Blog.

## TLS fingerprinting
<a name="tls-fingerprinting"></a>

TLS fingerprinting, also known as *signature-based rules,* are commonly used when bots originate from many IP addresses but exhibit similar characteristics. When using HTTPS, the client and server sides exchange messages to acknowledge and verify one another. They establish cryptographic algorithms and sessions keys. This is called a *TLS handshake*. How a TLS handshake is implemented is a signature that is often valuable for recognizing large attacks spread across many IP addresses.

TLS fingerprinting enables web servers to determine a web client's identity with a high degree of accuracy. It requires only the parameters in the first packet connection, before any application data exchange occurs. In this case, *web client* refers to the application initiating a request, which might be a browser, CLI tool, script (bot), native application, or other client.

One SSL and TLS fingerprinting approach is [JA3 fingerprint](https://github.com/salesforce/ja3). JA3 fingerprints a client connection based on fields in the Client Hello message from the SSL or TLS handshake. It helps you profile specific SSL and TLS clients across different source IP addresses, ports, and X.509 certificates.

Amazon CloudFront supports [adding JA3 headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-cloudfront-headers.html) to requests. A `CloudFront-Viewer-JA3-Fingerprint` header contains a 32-character hash fingerprint of the TLS Client Hello packet of an incoming viewer request. The fingerprint encapsulates information about how the client communicates. This information can be used to profile clients that share the same pattern. You can add the `CloudFront-Viewer-JA3-Fingerprint` header to an origin request policy and attach the policy to a CloudFront distribution. You can then inspect the header value in origin applications or in Lambda@Edge and CloudFront Functions. You can compare the header value against a list of known malware fingerprints to block the malicious clients. You can also compare the header value against a list of expected fingerprints to allow requests only from known clients.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
