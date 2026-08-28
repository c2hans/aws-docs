---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/SOAPGetObjectExtended.html
---

# GetObjectExtended (SOAP API)
<a name="SOAPGetObjectExtended"></a>

**Note**
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs.

`GetObjectExtended` is exactly like [GetObject (SOAP API)](SOAPGetObject.md), except that it supports the following additional elements that can be used to accomplish much of the same functionality provided by HTTP GET headers (go to [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)).

GetObjectExtended supports the following elements in addition to those supported by GetObject:
+ `ByteRangeStart, ByteRangeEnd:` These elements specify that only a portion of the object data should be retrieved. They follow the behavior of the HTTP byte ranges (go to [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\#sec14.35](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35)).
+ `IfModifiedSince:` Return the object only if the object's timestamp is later than the specified timestamp. ([http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\#sec14.25](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.25))
+ `IfUnmodifiedSince:` Return the object only if the object's timestamp is earlier than or equal to the specified timestamp. (go to [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\#sec14.28](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.28))
+ `IfMatch:` Return the object only if its ETag matches the supplied tag(s). (go to [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\#sec14.24](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.24))
+ `IfNoneMatch:` Return the object only if its ETag does not match the supplied tag(s). (go to [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\#sec14.26](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.26))
+ `ReturnCompleteObjectOnConditionFailure:`ReturnCompleteObjectOnConditionFailure: If true, then if the request includes a range element and one or both of IfUnmodifiedSince/IfMatch elements, and the condition fails, return the entire object rather than a fault. This enables the If-Range functionality (go to [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html\#sec14.27](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.27)).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
