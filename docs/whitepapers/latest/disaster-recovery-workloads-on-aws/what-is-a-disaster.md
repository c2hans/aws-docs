---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/what-is-a-disaster.html
---

# What is a disaster?
<a name="what-is-a-disaster"></a>

 When planning for disaster recovery, evaluate your plan for these three main categories of disaster:
+  Natural disasters, such as earthquakes or floods
+  Technical failures, such as power failure or network connectivity
+  Human actions, such as inadvertent misconfiguration or unauthorized/outside party access or modification

 Each of these potential disasters will also have a geographical impact that can be local, regional, country-wide, continental, or global. Both the nature of the disaster and the geographical impact are important when considering your disaster recovery strategy. For example, you can mitigate a local flooding issue causing a data center outage by employing a Multi-AZ strategy, since it would not affect more than one Availability Zone. However, an attack on production data would require you to invoke a disaster recovery strategy that fails over to backup data in another AWS Region.
