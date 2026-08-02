---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# AMS environment basic components
<a name="basic-components"></a>

------
#### [ Multi-Account Landing Zone ]

This is an estimate of the components, and potential costs, of the infrastructure in the core accounts. This does not include other costs such as bandwidth, CloudWatch detailed monitoring, logging, alarms, Route53, Amazon S3, Simple Notification Service (Amazon SNS), snapshots, or reserved Amazon EC2 instances.

You pay for the components required by the AMS-Managed AWS landing zone infrastructure. Estimates place the cost of a plain AMS multi-account landing zone environment at $2,450 per month and $50 for a plain application account.

For information about pricing, see [AWS pricing](https://aws.amazon.com/pricing/).

**Basic Environment Components**

| Component | Est. Cost | Description |
| --- | --- | --- |
| Management account | $60 | An AWS Organizations Management account; creates and financially manages member accounts. It contains the AWS Landing Zone (ALZ) framework, account configuration stack sets, and AWS Organization service control policies (SCPs).[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html) |
| Shared Services Account | $2000 | Contains infrastructure and resources required for access management (i.e., Active Directory), end-point security management (Trend Micro), and your bastions (SSH/RDP); estimate is $2400 a month. This estimate does not include the cost of the Trend Micro licenses.[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html) |
| Networking Account | $350 | The central hub for network routing between AMS accounts, your on-premise network, and egress traffic to the Internet. Additionally, contains public DMZ bastions (the entry point for AMS engineers to access hosts in your AMS environment). Price may increase depending on traffic traversing the Transit Gateway and Direct Connect.[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html) |
| Log Archive Account | $20 | An S3 bucket with copies of AWS CloudTrail and AWS Config log files from each of your AMS environment accounts. Costs increase as more logs are collected.[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html) |
| Security Account | $20 |  The central hub for security related operations, and the main point for funneling notifications and alerts to AMS control plane services. Additionally, houses the Amazon Guard Duty management account. Costs increase as more events are analyzed using Amazon GuardDuty.[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/userguide/basic-components.html) |

------
#### [ Single-Account Landing Zone ]

The following table lists the components of an example AMS-managed infrastructure.

**Basic Environment Components, Last Updated 2020/07/09**

| Name | Instance Type | OS | \# of Components |
| --- | --- | --- | --- |
| mc-eps-dsm | m5.large | Linux | 2 |
| mc-management | m5.large | Windows | 2 |
| mc-bastion-dmz-ssh | m5.large | Linux | 2 |
| mc-bastion-customer-rdp | m5.large | Windows | 2 |
| mc-eps-relay | m5.large | Linux | 2 |
| directory services | N/A | N/A |  |
| additional components | N/A | N/A |  |

For information about pricing, see [AWS Pricing](https://aws.amazon.com/pricing/).

------
