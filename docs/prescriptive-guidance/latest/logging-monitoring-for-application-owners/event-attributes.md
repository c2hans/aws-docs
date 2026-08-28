---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/event-attributes.html
---

# Event attributes
<a name="event-attributes"></a>

Each log entry needs to include sufficiently detailed information for monitoring and analysis. You could log full content data, but it's more efficient to log an extract or summary properties. The application logs must record the *when*, *where*, *who*, *what*, and *which* of each event. The properties for these will be different depending on the architecture, class of application, and the host system or device.

When logging date and time stamps, use Coordinated Universal Time (UTC) and the internationally recognized date and time formats in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) (ISO website).

|
|
| Note Consider using a network time synchronization service to help ensure accurate time stamps. Amazon provides the Amazon Time Sync Service, which is used by many AWS services, including Amazon Elastic Compute Cloud (Amazon EC2). Amazon Time Sync Service uses a fleet of satellite-connected and atomic reference clocks in each AWS Region to deliver accurate current time readings of the UTC global standard through Network Time Protocol (NTP). For more information, see [Keeping Time with Amazon Time Sync Service](https://aws.amazon.com/blogs/aws/keeping-time-with-amazon-time-sync-service/) (AWS blog post). |
| --- |

The following event attributes are commonly included in logs.

|
|
| **Attribute category** | **Event attribute** | **Description** |
| --- |--- |--- |
| When | Logging date and time | Record the date and time that the event was added to the log. |
| Event date and time | Record the date and time that the event occurred. This might be different than the logging record, such as when logging is delayed because the client application is hosted on a remote device that is periodically or intermittently online. |
| Event identifier | Log a user name, account number, or other unique attribute that ensures the event can always be identified. |
| Where | Application identifier | Log the application name and version. |
| Application address | Log the cluster or hostname, server IPv4 or IPv6 address, port number, workstation identity, and local device identifier. |
| Service | Log the service name and protocol. |
| Geolocation | Log the geographic locations of the user. |
| Window, form, or page | Log the entry point URL, HTTP method for a web application, or dialogue box name where the action was taken. |
| Code location | Log the script or module name. |
| Who (human or machine user) | Source address | Log the user's device identifier, IP address, cellular or radio frequency (RF) tower ID, or mobile telephone number. |
| User identity | If the user is authenticated or otherwise known, log the user database table primary key value, user name, or license number. |
| User type classification | Log the type of user, such as public, authenticated, CMS, search engine, authorized penetration tester, or uptime monitor. For more information about uptime monitors, see [Cautions and exclusions](logging-best-practices.md#cautions-exclusions) in this guide. |
| Request HTTP headers or HTTP user agent<br />  | (Web applications only) Log HTTP request header information, including the HTTP user-agent string, because these values affect the information that the client sends to the server. |
| What | Type of event | Log whether the event is informational, a warning, or an error. |
| Severity of event | Classify the event severity, such as high, medium, and low. |
| Security event flag | If the log contains data not related to security events, create a flag for security-related events to help you identify them. |
| Event description | (Optional) Include a brief description of the event. |
| Action or intent | Log the original intended purpose of the request, such as logging in, refreshing the session ID, logging out, or updating a profile. |
| User or application response | Log the user's or application's response to the event, such as a status code, custom text messages, stopping the session, or administrator alerts. |
| Result status | Log whether the action was successful, such as success, fail, or defer. |
| Result reason | Log the reason the status occurred. For example, a sign in request might fail because the user is not authenticated in the database. |
| Extended details | Log any additional information associated with the event, such as a stack trace, system error messages, debug information, and the HTTP request body. |
| HTTP response status code | (Web applications only) Log the HTTP response status code returned to the user, such as `200` or `301`. For more information, see [Logging levels](logging-best-practices.md#logging-levels) in this guide. |
| Which | Resources affected | Log which resources were acted upon. |
| Object | Log affected components or other objects, such as a user account, data resource, file, URL, or session ID. |
| Name of resource | Log the names of affected resources. |
| Resource tags | Log the tags assigned to the affected resources. For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) (AWS General Reference). |
| Other | Analytical confidence | Record the logging service's confidence in the event detection, such as assigning a low, medium, or high rating or a numeric value. |
| Internal classifications | Log any internal classifications for standards or compliance adherence. |
| External classifications | Log any external classifications for standards or compliance adherence, such as NIST Security Content Automation Protocol (SCAP). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
