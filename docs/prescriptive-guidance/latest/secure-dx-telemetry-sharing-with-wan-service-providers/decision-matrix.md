---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/decision-matrix.html
---

# Decision Matrix

The following matrix provides a structured comparison of the four implementation options across ten capability dimensions. It is intended to help customers, and their WSP/ESPs determine which combination of options best fits their operational requirements.

|
|
| Capability | Option 1 IAM Role | Option 2 EventBridge | Option 3 Network Monitor | Option 4 Health Events |
| --- |--- |--- |--- |--- |
| DX connection config | Yes | No | No | No |
| CloudWatch DX metrics | Yes | No | No | No |
| Resource tags / POC info | Yes | No | No | No |
| Real-time state change alerts | No (polling) | Yes | No | No |
| Synthetic path monitoring | No | No | Yes | No |
| AWS-side health events | No | No | No | Yes |
| Fault isolation (NHI) | No | No | Yes | No |
| Partition support | All | Verify availability | Verify availability | Verify availability |
| Additional services required | IAM only | EventBridge | Network Monitor \+ IAM | EventBridge |
| Deployment complexity | Low | Medium | Medium | Low |

Reading this matrix, several patterns emerge. Option 1 is the only option that provides access to connection configuration, CloudWatch metrics, and resource tags — the three data categories most needed for independent troubleshooting. No other option can substitute for it. Option 2 adds real-time alerting but provides no data access. Option 3 adds synthetic path monitoring and fault isolation but depends on Option 1 for metric sharing. Option 4 adds AWS-side health awareness but provides no customer-side data.

The recommended deployment strategy is therefore layered. All organizations should deploy Option 1 as the baseline. Organizations that need real-time alerting should add Options 2 and 4. Organizations that need enhanced diagnostics and fault isolation should add Option 3. In AWS isolated or restricted-access partition environments where EventBridge and CloudWatch Network Synthetic Monitor availability may be limited, Option 1 alone provides substantial operational value.
