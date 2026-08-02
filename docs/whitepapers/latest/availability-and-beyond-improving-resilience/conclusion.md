---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 We established 12 rules for high availability throughout this document.
+  **Rule 1** – Less frequent failure (longer MTBF), shorter failure detection times (shorter MTTD), and shorter repair times (shorter MTTR) are the three factors that are used to improve availability in distributed systems.
+  **Rule 2** – The availability of the software in your workload is an important factor of your workload’s overall availability and should receive an equal focus as other components.
+  **Rule 3** – Reducing dependencies can have a positive impact on availability.
+  **Rule 4** – In general, select dependencies whose availability goals are equal to or greater than the goals of your workload.
+  **Rule 5** – Use sparing to increase the availability of dependencies in a workload.
+  **Rule 6** – There is an upper bound to the cost efficiency of sparing. Utilize the fewest spares necessary to achieve the required availability.
+  **Rule 7** – Don’t take dependencies on control planes in your data plane, especially during recovery.
+  **Rule 8** – Loosely couple dependencies so your workload can operate correctly despite dependency impairment, where possible.
+  **Rule 9** – Observability and instrumentation are critical for reducing MTTD and MTTR.
+  **Rule 10** – Focus on impact mitigation, not problem resolution. Take the fastest path back to normal operation.
+  **Rule 11** – Fault isolation decreases scope of impact and increases the MTBF of the workload by reducing the overall failure rate.
+  **Rule 12** – Make it easy for operators to do the right thing.

 Improving workload availability is driven through reducing MTTD and MTTR, and increasing MTBF. In summary, we discussed the following ways to improve availability that cover technology, people, and process.
+  MTTD
  +  Reduce the MTTD through proactive monitoring of your Customer Experience metrics.
  +  Take advantage of granular health checks for quick failover.
+  MTTR
  +  Monitor Scope of Impact and Operational Health metrics.
  +  Reduce the MTTR by following 1/Restart, 2/Reboot, 3/Re-image/Redeploy, and 4/Replace.
  +  Route around failure by understanding scope of impact.
  +  Utilize services that have faster restart times, like containers and serverless functions over virtual machines or physical hosts.
  +  Automatically rollback failed deployments when possible.
  +  Establish runbooks and operational tools for diagnosis operations and restart procedures.
+  MTBF
  +  Eliminate bugs and defects in software through rigorous testing before they are released to production.
  +  Implement chaos engineering and fault injection.
  +  Utilize the right amount of sparing in dependencies to tolerate failure.
  +  Minimize the scope of impact during failures through fault containers.
  +  Implement standards for deployments and changes.
  +  Design simple, intuitive, consistent, and well-documented operator interfaces.
  +  Set goals for operational excellence.
  +  Favor stability over the release of new features when availability is a critical dimension of your workload.
  +  Implement usage quotas with throttling or load shedding or both to avoid overload.

 Remember that we will never be completely successful in preventing failure. Focus on software designs with best-possible failure isolation that limits scope and magnitude of impact, ideally keeping that impact below “downtime” thresholds AND invest in very fast, very reliable detection and mitigation. Modern distributed systems still need to embrace failure as inevitable and be designed at all levels for high availability.
