---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/case-study-scenario-a.html
---

# Scenario A: 45-minute screening time
<a name="case-study-scenario-a"></a>

Scenario A represents recruitment operations where human recruiters spend 45 minutes screening each resume. This scenario models a mid-level recruiter with an annual fully-loaded cost of $112,250. This recruiter processes applications during standard business hours with typical human performance characteristics. In contrast, the agentic AI system requires an initial investment of $23,000 for development, customization, and ATS integration, and it has a minimal monthly operating costs of $500 for the cloud infrastructure. The agent processes applications in just 5 minutes with 24/7 availability, achieving a 2% error rate and monthly capacity exceeding 8,600 applications. This is a dramatic efficiency gap, where the agent operates 9 times faster per application and 39 times greater monthly capacity. This section examines cost structure analysis, operational metrics, volume-based comparisons, and cumulative ROI calculations over the first six months of operation.

## Base cost structure
<a name="case-study-scenario-a-base-cost"></a>

The following table shows initial setup costs for scenario A.

|
|
| **Component** | **Human operations** | **Agentic AI system** |
| --- |--- |--- |
| Agent development and customization | N/A | $15,000 |
| Applicant tracking system (ATS) integration | N/A | $5,000 |
| Training  and optimization | N/A | $3,000 |
| **Total initial setup cost** | **$0** | **$23,000** |

The following table shows annual fixed costs for scenario A.

|
|
| **Component** | **Human operations** | **Agentic AI system** |
| --- |--- |--- |
| Base salary | $65,000 | N/A |
| Benefits (30%) | $19,500 | N/A |
| Workspace and equipment | $12,000 | N/A |
| Management oversight (15%) | $9,750 | N/A |
| Training and development | $6,000 | N/A |
| **Total annual fixed cost** | **$112,250** | **N/A** |

The following table shows monthly operating costs for scenario A.

|
|
| **Component** | **Human operations** | **Agentic AI system** |
| --- |--- |--- |
| Cloud computing | N/A | $200 |
| Storage | N/A | $100 |
| Database operations | N/A | $100 |
| Monitoring | N/A | $100 |
| **Total monthly fixed cost** | **$9,354** | **$500** |

## Operational metrics
<a name="case-study-scenario-a-operational-metrics"></a>

The following table shows operational metrics for scenario A.

|
|
| **Metric** | **Human operations** | **Agentic AI system** |
| --- |--- |--- |
| Processing time per application | 45 minutes | 5 minutes |
| Hourly capacity | 1.33 applications | 12 applications |
| Daily capacity (24 hours) | 10-11 applications | 288 applications |
| Monthly capacity | 220 applications | 8,640 applications |
| Cost per application | $45 | $2.50 |
| Cost per successful hire | $2,200 | $125 |
| Error rate | 5% | 2% |
| Error correction cost | $90 per error | $45 per escalation |

## Volume-based cost analysis
<a name="case-study-scenario-a-volume"></a>

The following table shows a volume-based cost analysis for scenario A. In this example, the agentic AI system cost includes fixed costs and amortized setup costs of $1,917 per month over 12 months.

|
|
| **Monthly volume** | **Human cost** | **Agentic AI system cost** | **Monthly savings** |
| --- |--- |--- |--- |
| 100 applications | $4,500 | $750 | $3,750 |
| 500 applications | $22,500 | $2,667 | $19,833 |
| 1,000 applications | $45,000 | $4,917 | $40,083 |

## ROI analysis
<a name="case-study-scenario-a-roi-analysis"></a>

The following table shows an ROI analysis for scenario A that is based on processing 500 applications per month.

|
|
| **Metric** | **Value** |
| --- |--- |
| Monthly human cost | $22,500 |
| Monthly agent cost | $2,667 |
| Monthly savings | $19,833 |
| Annual savings | $237,996 |
| Break-even period | 1.16 months |

## Cumulative cost comparison
<a name="case-study-scenario-a-cumulative-cost-comparison"></a>

The following table shows a cumulative cost comparison for scenario A for the first six months, assuming 500 applications per month.

|
|
| **Month** | **Human cost** | **Agentic AI system cost** | **Cumulative savings** |
| --- |--- |--- |--- |
| 1 | $22,500 | $25,667 | -$3,167 |
| 2 | $45,000 | $28,334 | $16,666 |
| 3 | $67,500 | $31,001 | $36,499 |
| 4 | $90,000 | $33,668 | $56,332 |
| 5 | $112,500 | $36,335 | $76,165 |
| 6 | $135,000 | $39,002 | $95,998 |

## Additional benefits of the agentic AI system
<a name="case-study-scenario-a-add-benefits"></a>

The following are additional benefits provided by the agentic AI system in Scenario A:
+ **Scalability** – Can handle volume spikes without additional cost
+ **Availability** – 24/7 operation with immediate response
+ **Consistency** – Uniform screening criteria application
+ **Time efficiency** – Significantly reduced time-to-hire
+ **User experience** – Instant feedback to candidates

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
