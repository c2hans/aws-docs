---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/sdk-manual.html
---

# SDK manual
<a name="sdk-manual"></a>

 Clickstream Analytics on AWS provides purpose-built software development kits (SDKs), which can make it easier for you to report events to the data pipeline created in the guidance. Currently, the guidance supports the following platforms:
+  [Android](android-sdk.md)
+  [Swift](swift-sdk.md)
+  [Web](web-sdk.md)
+ [Flutter](flutter-sdk.md)
+ [ReactNative SDK](reactnative-sdk.md)

In addition, HTTP API is also provided to collect clickstream data from other platforms, such as server, through HTTP request.

## Key features and benefits
<a name="key-features-and-benefits"></a>
+  **Automatic data collection.** Clickstream SDKs provide built-in capabilities to automatically collect common events, such as screen view, session, and user engagement, so that you only need to focus on recording business-specific events.
+  **Ease of use.** Clickstream SDKs provide multiple APIs and configuration options to simplify the event reporting and attribute setting process.
+  **Cross-platform analytics.** Clickstream SDKs are consistent in event data structure, attribute validation rules, and event sending mechanism, so that data can be normalized in the same structure for cross-platform analytics.

**Note**
All Clickstream SDKs are open source under Apache 2.0 License in [Github](https://github.com/awslabs/?q=clickstream&type=all&language=&sort=). You can customize the SDKs if needed. All contributions are welcome.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
