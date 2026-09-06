---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/validate-scope-assess-alert-impact.html
---

# Validate, scope, and assess impact of alert
<a name="validate-scope-assess-alert-impact"></a>

 During the analysis phase, comprehensive log analysis is performed with the goal to validate alerts, define scope, and assess impact of the possible compromise.
+  *Validation* of the alert is the entry point of the analysis phase. Incident responders will be looking for log entries from various sources and directly engaging with owners of the affected workload.
+  *Scoping* is the next step, when all resources involved are inventoried and alert criticality is adjusted after stakeholders agree that it is unlikely to be a false-positive.
+  Finally,* impact analysis* details the actual business disruption.

Once the affected workload components are identified, scoping results can be correlated with the related workload’s recovery point objective (RPO) and recovery time objective (RTO), adjusting for alert criticality, which will initiate resource allocation and all activity happening next. Not all incidents will directly disrupt operations of a workload supporting a business process. Incidents such as sensitive data disclosure, intellectual property theft, or resource hijacking (as in cryptocurrency mining) might not stop or debilitate a business process immediately, but can result in consequences at a later time.
