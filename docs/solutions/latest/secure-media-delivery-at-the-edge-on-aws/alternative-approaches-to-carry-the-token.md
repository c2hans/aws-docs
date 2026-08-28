---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/alternative-approaches-to-carry-the-token.html
---

# Alternative approaches to carry the token
<a name="alternative-approaches-to-carry-the-token"></a>

 The default and suggested method for including the token persistently throughout the viewer playback time is to use URL path. By inserting the token at the beginning of the playback URL which makes a reference point for the player for subsequent requests, it makes the solution more universally supported as it uses the most fundamental mechanism of HTTP delivery, and minimizes implementation efforts as this mechanism is transparent from the video origin standpoint. However, if this approach is not viable for your specific use case, you can choose a different way of attaching the token with the requests which does not have to rely on the URL path. Cookies, custom headers, query string parameters are potential other carriers for the token and using the solution’s library it is possible to generate a plain token that would normally appear in URL path in default mode. However, this involves customization of CloudFront Functions code to look up and parse the token and session ID in a place other than the URL path, by modifying the source code appropriately. The rest of the token validation logic would remain unchanged regardless of how the token is attached with the request. You must ensure token stickiness so that with a different approach to carry the token, this token is repeated in the future requests made by the same client for the protected objects.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
