---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/identifying-requests.html
---

# Identifying presigned requests
<a name="identifying-requests"></a>

## Identifying requests that used a presigned URL
<a name="requests"></a>

Amazon S3 provides [two built-in mechanisms for monitoring usage at a request level](https://docs.aws.amazon.com/AmazonS3/latest/userguide/logging-with-S3.html): Amazon S3 server access logs and AWS CloudTrail data events. Both mechanisms can identify presigned URL usage.

To filter logs for presigned URL usage, you can use the authentication type. For server access logs, examine the [Authentication Type field](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html#:~:text=Authentication%20Type), which is typically named [authtype](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-s3-access-logs-to-identify-requests.html#:~:text=authtype) when it's defined in an Amazon Athena table. For CloudTrail, examine [AuthenticationMethod](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging-understanding-s3-entries.html#:~:text=AuthenticationMethod) in the `additionalEventData` field. In both cases, the field value for requests that use presigned URLs is `QueryString`, whereas `AuthHeader` is the value for most other requests.

`QueryString` usage isn't always associated with presigned URLs. To restrict your search to only presigned URL usage, find requests that contain the query string parameter `X-Amz-Expires`. For server access logs, examine [Request-URI](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html#:~:text=Request%2DURI) and look for requests that have an `X-Amz-Expires` parameter in the query string. For CloudTrail, examine the `requestParameters` element for an `X-Amz-Expires` element.

```
{"Records": [{…, "requestParameters": {…, "X-Amz-Expires": "300"}}, …]}
```

The following Athena query applies this filter:

```
SELECT * FROM {athena-table} WHERE
  authtype = 'QueryString' AND
  request_uri LIKE '%X-Amz-Expires=%';
```

For AWS CloudTrail Lake, the following query applies this filter:

```
SELECT * FROM {data-store-event-id} WHERE
  additionalEventData['AuthenticationMethod'] = 'QueryString' AND
  requestParameters['X-Amz-Expires'] IS NOT NULL
```

## Identifying other types of presigned requests
<a name="other"></a>

The POST request also has a unique authentication type, `HtmlForm`, in Amazon S3 server access logs and CloudTrail. This authentication type is less common, so you might not find these requests in your environment.

The following Athena query applies the filter for `HtmlForm`:

```
SELECT * FROM {athena-table} WHERE
  authtype = 'HtmlForm';
```

For CloudTrail Lake, the following query applies the filter:

```
SELECT * FROM {data-store-event-id} WHERE
  additionalEventData['AuthenticationMethod'] = 'HtmlForm'
```

## Identifying request patterns
<a name="patterns"></a>

You can find presigned requests by using the techniques discussed in the previous section. However, to make that data useful, you'll want to find patterns. The simple `TOP 10` results for your query might provide an insight, but if that's not enough, use the grouping options in the following table.

|
|
| Grouping option | Server access logs | CloudTrail Lake | Description |
| --- |--- |--- |--- |
| **User agent** | `GROUP BY useragent` | `GROUP BY userAgent` | This grouping option helps you find the source and purpose of requests. The user agent is user supplied and not reliable as an authentication or authorization mechanism. However, it can reveal a lot if you're looking for patterns, because most clients use a unique string that is at least partially human readable. |
| **Requester** | `GROUP BY requester` | `GROUP BY userIdentity['arn']` | This grouping option helps find IAM principals who signed requests. If your goal is to block these requests or to create an exception for existing requests, these queries provide enough information for that purpose. When you use roles in accordance with IAM best practices, the role has a clearly identified owner, and you can use that information to find out more. |
| **Source IP address** | `GROUP BY remoteip` | `GROUP BY sourceIPAddress` | This option groups by the last network translation hop before reaching Amazon S3.If the traffic passes through a NAT gateway, this will be the NAT Gateway address.If the traffic passes through an internet gateway, this will be the public IP address that sent the traffic to the internet gateway.If the traffic originates from outside AWS, this will be the public internet address that's associated with the origin.If it passes over a gateway virtual private cloud (VPC) endpoint, this will be the IP address of the instance in the VPC.If it passes through a public virtual interface (VIF), this will be the on-premises IP of the requester or any intermediary such as a proxy server or firewall that exposes only its IP address.If it passes through an interface VPC endpoint, this could be the IP address from an instance in the VPC. It could also be an IP address from another VPC or an on-premises network. As with public VIFs, this could be any intermediary's IP address.<br />This data is useful if your goal is to impose network controls. You might have to combine this option with data such as `endpoint` (for server access logs) or `vpcEndpointId` (for CloudTrail Lake) to clarify the source, because different networks might duplicate private IP addresses. |
| **S3 bucket name** | `GROUP BY bucket_name` | `GROUP BY requestParameters['bucketName']` | This grouping option helps find buckets that received requests. This helps you identify the need for exceptions. |
