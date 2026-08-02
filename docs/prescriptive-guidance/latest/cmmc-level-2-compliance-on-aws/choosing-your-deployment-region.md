---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/choosing-your-deployment-region.html
---

# Choosing your deployment Region
<a name="choosing-your-deployment-region"></a>

One of the first architectural decisions you will make is where to deploy your CUI workloads. CMMC Level 2 does not mandate a specific AWS Region. It requires that you implement NIST SP 800-171 controls and that any CSP you use meets the FedRAMP Moderate baseline equivalent, as required by DFARS 252.204-7012. Both [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) and the commercial US East/West Regions meet this requirement.

## Decision flow for deployment region identification
<a name="decision-flow-for-deployment-region-identification"></a>

Use the following decision logic to determine the right deployment target for each workload:
+ Does your contract involve International Traffic in Arms Regulations (ITAR) or Export Administration Regulations (EAR) controlled data? If yes, deploy in AWS GovCloud (US). ITAR workloads require the jurisdictional isolation that AWS GovCloud (US) provides.
+ Does your contract require DoD Security Requirements Guide (SRG) Impact Level 4 or 5? If yes, deploy in AWS GovCloud (US). Commercial regions support Impact Level 2 (IL2) only.
+ Do your workloads involve CUI without ITAR/EAR restrictions and without IL4/5 requirements? You can deploy in commercial US East/West Regions using FIPS-validated endpoints and still meet CMMC Level 2 requirements.
+ Do you have mixed workloads with different regulatory overlays? Consider a hybrid approach: AWS GovCloud (US) for ITAR programs, commercial regions for standard CUI workloads. Use separate AWS Organizations to maintain clear boundaries.

## Comparison of deployment options
<a name="comparison-of-deployment-options"></a>

|
|
| Attribute | AWS GovCloud (US) | Commercial US East/West \+ FIPS |
| --- |--- |--- |
| FedRAMP authorization | FedRAMP High | FedRAMP Moderate |
| FIPS 140-2/3 endpoints | Default for all services | Available via FIPS-specific endpoints |
| DoD SRG impact levels | IL2, IL4, IL5 | IL2 |
| Operator citizenship | U.S. persons only | No restriction |
| Service availability | Subset of commercial services | Broadest service catalog |
| CMMC Level 2 eligible | Yes | Yes |
| Best fit | ITAR, IL4/5, maximum isolation | Standard CUI, broader services, lower cost |

The key takeaway: if your contract involves CUI without ITAR or EAR restrictions, and you do not require DoD SRG Impact Levels 4 or 5, you can deploy in commercial US East/West Regions using FIPS-validated endpoints and still meet CMMC Level 2 requirements. If your workloads carry ITAR obligations or require higher DoD SRG impact levels, AWS GovCloud (US) provides the additional isolation and regulatory coverage you need.

## FIPS endpoints in GovCloud and commercial regions
<a name="fips-endpoints-in-gov-cloud-and-commercial-regions"></a>

When deploying in commercial or AWS GovCloud (US) regions, you activate FIPS-validated cryptography by directing application traffic to FIPS-specific service endpoints. For example, instead of calling `kms.us-east-1.amazonaws.com`, you use `kms-fips.us-east-1.amazonaws.com`. AWS publishes a [complete list of FIPS endpoints ](https://aws.amazon.com/compliance/fips/)for each service and Region. Your SDK configurations and service endpoint URLs must be updated to reference these endpoints throughout your CUI boundary in both partitions.
