---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/introduction.html
---

# Modernizing ASP.NET (ASMX) web services incrementally by using containers and Amazon API Gateway
<a name="introduction"></a>

*Dan Broadway and Silas Silva, Amazon Web Services*

This guide describes approaches and best practices for implementing the strangler fig pattern to modernize legacy ASP.NET web services on Amazon Web Services (AWS). The strangler fig pattern is a modernization approach in which the existing functionalities of a legacy system are incrementally replaced with new applications and services until the new system eventually replaces all the old or key parts of the legacy system. As functionality is replaced, the inactive parts of the legacy (and often monolithic) system can be removed or retired.

The guide discusses a modified *branch by abstraction* approach, which is a common technique for incrementally changing software systems, combined with *service delegation*, where a service defers its behavior to another, newer service, to help manage breaking changes to service consumers.

## Targeted business outcomes
<a name="business-outcomes"></a>

The intent of this guide is to help customers modernize legacy ASP.NET services that are based on the Representational State Transfer (REST) or Simple Object Access Protocol (SOAP) standard on AWS. It focuses on scenarios where an incremental modernization approach is required in order to manage the delivery risk that is often associated with decoupling larger, monolithic applications. It also discusses scenarios where services with multiple consumers cannot be upgraded in synchrony without introducing breaking changes.

This guide is intended to help you:
+ Migrate, modernize, and scale your ASP.NET applications on AWS
+ Manage the delivery risk associated with modernizing legacy applications
+ Decouple services that have multiple, highly available consumers
