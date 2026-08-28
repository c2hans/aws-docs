---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/api-making-requests-response.html
---

# HTTP responses
<a name="api-making-requests-response"></a>

All Network Firewall API actions include JSON-formatted data in the response.

Here are some important headers in the HTTP response and how you should handle them in your application, if applicable.

**HTTP/1.1**
This header is followed by a status code. Status code 200 indicates a successful operation.
Type: String

**x-amzn-RequestId**
A value created by Network Firewall that uniquely identifies your request, for example, `K2QH8DNOU907N97FNA2GDLL8OBVV4KQNSO5AEMVJF66Q9ASUAAJG`. If you have a problem with Network Firewall, AWS can use this value to troubleshoot the problem.
Type: String

**Content-Length**
The length of the response body in bytes.
Type: String

**Date**
The date and time that Network Firewall responded, for example, Wed, 07 Oct 2019 12:00:00 GMT.
Type: String

## Error responses
<a name="api-making-requests-error-response"></a>

If a request results in an error, the HTTP response contains the following values:
+ A JSON error document as the response body
+ A `Content-Type` header
+ The applicable 3xx, 4xx, or 5xx HTTP status code

The following is an example of a JSON error document:

```
HTTP/1.1 400 Bad Request
x-amzn-RequestId: b0e91dc8-3807-11e2-83c6-5912bf8ad066
x-amzn-ErrorType: ValidationException
Content-Type: application/json
Content-Length: 125
Date: Mon, 26 Nov 2012 20:27:25 GMT

{"message":"1 validation error detected: Value null at 'TargetString' failed to satisfy constraint: Member must not be null"}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
