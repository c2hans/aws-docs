---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/about-dynamic-framework.html
---

# About the Dynamic Application Framework
<a name="about-dynamic-framework"></a>

The dynamic application framework uses the [Apache Thrift software framework](https://thrift.apache.org/) for inter-process messaging. It is exposed through Named Pipes in Windows. Using the Thrift framework allows you to build your dynamic app provider in your software development language of choice. The dynamic application framework consists of three API operations: `AddApplications`, `RemoveApplications`, and `ClearApplications`.
