---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/using-sdk.html
---

# Using AWS SDK for SAP ABAP
<a name="using-sdk"></a>

SDK for SAP ABAP has two major components.
+ SDK Runtime (package `/AWS1/RT`) – a set of objects that underpin the security, authentication, tracing, configuration, data conversion, and other cross-API functions. The API modules for Amazon S3, AWS STS, IAM Roles Anywhere, and Secrets Manager are mandatory.
+ APIs (package `/AWS1/API` and its sub-packages) – a sub-package for each API where the objects of each API are completely independent of each other, ensuring that a change in one API does not break another API. To see a complete list of AWS SDK for SAP ABAP APIs, see [AWS SDK for SAP ABAP - API Reference Guide](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html).

This section covers the following topics.

**Topics**
+ [Representation of data in ABAP](representation.md)
+ [Amazon S3 example program](example-program.md)
+ [SDK for SAP ABAP concepts](concepts.md)
+ [AWS SDK for SAP ABAP features](features.md)
+ [Building products with SDK](building-products.md)
+ [Customize HTTP requests to AWS](customize-http-request.md)
+ [Limitations](limitations.md)
