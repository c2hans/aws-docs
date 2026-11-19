---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/logging-interactions.html
---

# Logging interactions and mitigations

A presigned URL contains a signature that you can use, before it expires, to perform the specific API operation it was signed for. Treat a presigned URL as a temporary access credential. Keep the signature private to the parties that need it. In most environments, these parties are the client that sends the request and the server that receives it. Sending the signature as part of a direct HTTPS session maintains its private nature, because only participants in the HTTPS session can see the URI that transmits the signature.

For presigned URLs, the client transmits the signature as the `X-Amz-Signature` query string parameter. Query string parameters are a component of a URI. The risk is that clients could log the URI and the signature with it. Clients have access to the entire HTTP request and could log any part of the request, data, and headers (including authentication headers). However, this is less common. URI logging is more common, and some cases, such as access logging, require it. Clients should use redaction or masking to remove the signature before logging URIs.

In some environments, users allow intermediaries (proxies) to gain visibility into their HTTPS sessions. Enabling proxies requires privileged access to client systems, because proxies require configuration and trusted certificates. Installing proxy configuration and trusted certificates within the local context of the client intermediary environment grants a high level of privilege. For this reason, tightly control access to such intermediaries.

The purpose of an intermediary is usually to block unwanted egress and to track other egress. As such, intermediaries commonly log requests. Although intermediaries could, like clients, log any content, headers, and data (all of which would be sensitive), they more commonly log URIs, such as those that include the `X-Amz-Signature` query string parameter.

## Mitigations
<a name="mitigations"></a>

We recommend that you redact the `X-Amz-Signature` query string parameter or the entire query string in URI logs. Alternatively, treat the logged information as confidential, in the same way that you treat direct access to the intermediary server.

Although we recommend these protections, the expiration of presigned URLs mitigates the risk of log exposure if the logs are exposed after the signatures expire.

Amazon S3 also receives the signatures. Amazon S3 server access logs include the request URI but redact the `X-Amz-Signature`, as recommended. The same is true when CloudTrail logs data events for Amazon S3. You can configure Amazon CloudWatch Logs to [mask data by using custom data identifiers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html).

The following regular expression matches the `X-Amz-Signature` as it appears in a URI:

```
X-Amz-Signature=[a-f0-9]{64}
```

The following regular expression adds grouping patterns to identify the text to replace more specifically:

```
(?:X-Amz-Signature=)([a-f0-9]{64})
```

If you have an access log entry such as the following:

```
X-Amz-Signature=733255ef022bec3f2a8701cd61d4b371f3f28c9f193a1f02279211d48d5193d7
```

The first regular expression translates the access log entry to:

```
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

The second regular expression, on systems that support non-capturing groups, translates the access log entry to:

```
X-Amz-Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
