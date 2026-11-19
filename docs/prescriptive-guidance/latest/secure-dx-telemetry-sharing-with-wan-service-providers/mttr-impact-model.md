---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/mttr-impact-model.html
---

# MTTR Impact Model

The following illustrative comparison quantifies the time-to-diagnosis compression achieved by this framework. The scenario: a Direct Connect connection experiences degrading optical light levels requiring WSP transport-side diagnosis.

## Reactive Operations Model (Before Framework)
<a name="reactive-operations-model--before-framework-.3d4acbf7-c543-50ff-be9e-51ddb07570b6"></a>

Without independent telemetry access, the WSP depends on sequential human coordination. Each step blocks on the previous step.

|
|
| Step | Action | Elapsed |
| --- |--- |--- |
| 1 | Customer monitoring detects packet loss or connection state change | T\+0 |
| 2 | Customer on-call engineer logs in, reviews CloudWatch metrics | T\+10 min |
| 3 | Engineer identifies affected connection, looks up WSP contact | T\+15 min |
| 4 | Engineer contacts WSP via phone or email | T\+20 min |
| 5 | WSP requests connection ID, light levels, BGP state, location | T\+25 min |
| 6 | Customer gathers data from Console, shares via email/screen share | T\+40 min |
| 7 | WSP begins diagnosis on transport side | T\+50 min |
| 8 | Resolution (WSP dispatches technician or reroutes traffic) | T\+90-180 min |

Time-to-diagnosis: approximately 50 minutes. The delay results from sequential human coordination, not technical complexity.

## Proactive Operations Model (After Framework)
<a name="proactive-operations-model--after-framework-.8f2d07b7-fd2e-5302-a619-efe7f9f138a6"></a>

With independent telemetry access, the WSP operates in parallel with the customer. Detection, investigation, and initial diagnosis proceed without human coordination.

The following timeline is illustrative and is not based on measured benchmark data. Actual elapsed times will vary based on the customer's monitoring maturity, WSP/ESP operating model, escalation process, and network topology. The purpose of the example is to show how independent telemetry access can reduce sequential coordination steps and enable parallel troubleshooting.

|
|
| Step | Action | Elapsed |
| --- |--- |--- |
| 1 | WSP monitoring detects ConnectionLightLevelRx degradation via CloudWatch | T\+0 |
| 2 | WSP queries connection config: ID, location, bandwidth, BGP state | T\+1 min |
| 3 | WSP retrieves customer NOC contact and circuit ID from resource tags | T\+2 min |
| 4 | WSP begins transport-side diagnosis using correlated data | T\+3 min |
| 5 | WSP contacts customer NOC with preliminary diagnosis and action plan | T\+10 min |
| 6 | Resolution (coordinated remediation with customer awareness) | T\+30-60 min |

Time-to-diagnosis: approximately 3 minutes — a 94% reduction. The WSP contacts the customer with a preliminary diagnosis rather than a data request, transforming the interaction from coordination overhead into collaborative resolution.

For organizations with multiple connections and frequent incidents, each incident resolved 45 minutes faster represents reduced production downtime, fewer AWS Support escalations, and lower operational cost.

**Note**
*The timelines presented in this section are illustrative and based on typical enterprise operational patterns. Actual MTTR improvements vary based on incident type, organizational monitoring maturity, WSP/ESP response capabilities, and the complexity of the underlying network topology. Organizations should establish their own baseline measurements before and after framework deployment to quantify the specific improvement achieved.*
