---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/event-types.html
---

# Event types
<a name="event-types"></a>

One of the most important considerations when establishing an application logging strategy is deciding which events and actions to log. Although the requirements of your organization and application might affect this decision, we recommend that you always log the following if they apply to your application:
+ **Input validation failures** – Examples include protocol violations, unacceptable encodings, and invalid parameter names and values.
+ **Output validation failures** – Examples include database record set mismatches and invalid data encoding.
+ **Identity authentication successes and failures** – Log authentication activities, but do not log user names and passwords. Because users can accidentally type their passwords into a user name field, we recommend that you don't log user names. This might unintentionally expose credentials and result in authorized access. Implement security controls for any logs that contain authentication data.
+ **Authorization (access control) failures** – For related authorization systems, log failed access attempts. You can monitor this log data for patterns that might indicate an attack or issues with the authorization system in the application.
+ **Session management failures** – Examples include modifying session cookies or tokens. Applications often use cookies or tokens to manage user states. Malicious users can attempt to modify cookie values to gain unauthorized access. Logging tampered session tokens provides a way to detect this behavior.
+ **Application errors and system events** – Examples include syntax and runtime errors, connectivity problems, performance issues, error messages from third-party services, file system errors, virus detection for file uploads, and configuration changes.
+ **Application state** – Starting or stopping the application and its related resources.
+ **Logging state** – Starting, stopping, or pausing logging.
+ **Use of higher-risk functionality** – Examples include network connection changes, adding or deleting users, changing privileges, assigning users to tokens, adding or deleting tokens, using system administrative privileges, access by application administrators, all actions performed by users with administrative privileges, accessing payment cardholder data, using data encryption keys, changing encryption keys, creating and deleting of system-level objects, submitting user-generated content (especially file uploads), and importing and exporting data (including reports).
+ **Legal and other opt-ins** – Examples include permissions for mobile phone capabilities, terms of use, terms and conditions, personal data usage consent, and permissions to receive marketing communications.

In addition to the recommended attributes, for your application, consider what additional attributes might provide useful data for monitoring, alerting, and reporting. Examples include:
+ Sequencing failures
+ Attributes that help you assess user behavior that violates your organization's acceptable use policy
+ Data changes
+ Attributes required to comply with standards or regulations, such as preventing financial crimes, limiting equity trading, or collecting health or other personal information.
+ Attributes that help you identify suspicious or unexpected behavior, such as attempts to perform unauthorized actions
+ Configuration changes
+ Application code file or memory changes
