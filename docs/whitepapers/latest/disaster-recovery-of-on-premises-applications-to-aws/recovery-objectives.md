---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/recovery-objectives.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Recovery objectives
<a name="recovery-objectives"></a>

 As part of disaster recovery planning, you need to define an RTO and RPO for each application based on impact analysis and risk assessment.

 **RTO** is the maximum acceptable delay between the interruption of an application and the restoration of its service. This objective determines what is considered an acceptable time window for an application to be unavailable.

 **RPO** is the maximum acceptable gap between the data in the disaster recovery site and the latest data stored in the application when the disaster strikes. This objective determines what is considered the maximum amount of time acceptable for interruption/loss of data that can be caused by a disaster.

![This image shows recovery objectives](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/images/recoveryobjectives.png)

 RTO and RPO for each application depend on many factors (such as service level agreements (SLA) and external compliance requirements), but there are some common standards. Common figures for mission-critical applications (tier-1 applications) include an RTO of 15 minutes and a near-zero RPO. For important applications that are not mission critical (tier-2 applications), the RTO is typically four hours and the RPO is two hours. For all other applications (tier-3 applications), a typical RTO is 8 to 24 hours and RPO is four hours.
