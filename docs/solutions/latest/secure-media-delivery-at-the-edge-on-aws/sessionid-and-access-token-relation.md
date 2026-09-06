---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/sessionid-and-access-token-relation.html
---

# SessionId and access token relation
<a name="sessionid-and-access-token-relation"></a>

 When preparing the inputs required for issuing an access token, you can also attach a **sessionId** with that token, which makes a unique identifier of the playback session. The **sessionId** has to be present alongside the access token when viewer makes a request. While the access token is a JWT token that has all the necessary claims in the payload, subject to the verification by the CloudFront Function logic, **sessionId** value is not encapsulated in the payload itself but appended to the JWT token string at the beginning of the URL path. This approach optimizes the utilization of WAF rule group capacity available, as the session blocking rules created for compromised sessions are defined with specific URL path matching conditions consuming the least amount of WCU capacity (2 WCU units per each session blocking rule). JWT access token only holds a claim – **ssn**, assuming true or false value indicative if **sessionId** was attached with the token. If the claim is set to true any attempt to remove or modify the **sessionId** value in the URL path will result in an error upon token validation. This is because the **sessionId** associated with the token is used as one of the inputs when calculating viewer attributes specific signature.
