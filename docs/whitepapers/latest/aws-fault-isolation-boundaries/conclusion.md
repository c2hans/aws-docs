---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

 AWS provides several fault isolation boundaries. You should consider how you architect for zonal, Regional, and global services as well as the potential impacts on your workload and your workload’s ability to recover during control plane impairments. Static stability is one of the primary ways that you can avoid control plane dependencies and create reliable and resilient recovery mechanisms when you use AWS services.

**Key takeaways**
+ AWS fault isolation boundaries create predictable scopes of impact that allow you to build consistent, bounded recovery.
+ Control planes are more complex and have more dependencies than data planes, which makes them statistically more likely to fail.
+ A dependency on a data plane is typically better than a dependency on a control plane.
+ Global service control planes and endpoints can introduce single points of failure in your recovery path; use regional endpoints or the service’s data plane for recovery instead.
+ Design for static stability so your application avoids dynamic changes during failure and recovers predictably.

 After you have implemented these best practices, you must continuously test and validate your recovery capabilities and the dependencies they rely on, so you are confident your recovery plan will work when you need it.
