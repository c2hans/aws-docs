---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/logging-interactions.html
---

# Logging interactions and mitigations
<a name="logging-interactions"></a>

A presigned URL contains a signature and can be used, during the period before expiration, to perform the specific API operation it was signed for. It should be treated as a temporary access credential. The signature should remain private to only parties that need to know it. In most environments, this is the client that sends the request and the server that receives it. Sending the signature as part of a direct HTTPS session maintains its private nature, because only a participant of the HTTPS session has visibility into the URI that transmits the signature.

For presigned URLs, the signature is transmitted as the `X-Amz-Signature` query string parameter. Query string parameters are a component of a URI. The risk is that clients could log the URI and the signature with it. Clients have access to the entire HTTP request and could log any part of the request, data, and headers (including authentication headers). However, this is by convention less common. URI logging is more common and is required in cases such as access logging. Clients should use redaction or masking to remove the signature before logging URIs.

In some environments, users allow intermediaries (proxies) to gain visibility into their HTTPS sessions. Enabling proxies requires a high level of privileged access to client systems, because they require configuration and trusted certificates. The installation of proxy configuration and trusted certificates, within the local context of the client intermediary environment, allows a very high level of privilege. For this reason, access to such intermediaries should be tightly controlled.

The purpose of an intermediary is usually to block unwanted egress and to track other egress. As such, it's common for such intermediaries to log requests. Although intermediaries could, like clients, log any content, headers, and data  (all of which would be very sensitive), it's more common for them to log URIs, such as those that include the `X-Amz-Signature` query string parameter.

## Mitigations
<a name="mitigations"></a>

We recommend that URI logging redact the `X-Amz-Signature` query string parameter, redact the entire query string, or treat the information as highly confidential, as with direct access to the intermediary server.

Although these protections are highly recommended, the fact that presigned URLs expire mitigates the risks of log exposure, as long as the exposure is delayed long enough for the signatures to expire.

Amazon S3 also sees the signatures and must handle them appropriately. Amazon S3 server access logs include the request URI but redact the `X-Amz-Signature`, as recommended. The same is true when CloudTrail data events are logged for Amazon S3. You can configure Amazon CloudWatch Logs to [mask data by using custom data identifiers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html).

The following regular expression matches the `X-Amz-Signature` as it appears in a URI:

```
X-Amz-Signature=[a-f0-9]{64}
```

This following regular expression adds grouping patterns to identify the text to replace more specifically:

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
