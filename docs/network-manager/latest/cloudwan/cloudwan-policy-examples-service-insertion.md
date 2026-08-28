---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-service-insertion.html
---

# AWS Cloud WAN example: Service insertion firewalls between on-premises and VPCs
<a name="cloudwan-policy-examples-service-insertion"></a>

In this policy, traffic on a segment named *development* is first sent to an Inspection VPC before being sent to a segment named *production* using a network function group named *InspectionVPC*. The on-premises attachment has already been set up and mapped to either the `development` or `production` segments. The segment action uses `send-via`, indicating that this is east-west traffic. The attachment policy rule uses the `and` condition logic with `InspectionVpcs` as the value of the key-value pair associated with the attachment.

```
{
    "version": "2021.12",
    "core-network-configuration": {
        "vpn-ecmp-support": true,
        "inside-cidr-blocks": [
            "10.0.0.0/16"
        ],
        "asn-ranges": [
            "64512-65534"
        ],
        "edge-locations": [
            {
                "location": "us-east-2"
            },
            {
                "location": "us-west-2"
            }
        ]
    },
    "segments": [
        {
            "name": "development",
            "edge-locations": [
                "us-east-2"
            ],
            "require-attachment-acceptance": true,
            "isolate-attachments": true
        },
        {
            "name": "production",
            "edge-locations": [
                "us-east-2"
            ],
            "require-attachment-acceptance": true,
            "isolate-attachments": true
        }
    ],
    "network-function-groups": [
        {
            "name": "InspectionVPC",
            "description": "Route segment traffic to the inspection VPC",
            "require-attachment-acceptance": true
        }
    ],
    "segment-actions": [
        {
            "action": "send-via",
            "segment": "development",
            "mode": "single-hop",
            "when-sent-to": {
                "segments": [
                    "production"
                ]
            },
            "via": {
                "network-function-groups": [
                    "InspectionVPC"
                ]
            }
        }
    ],
    "attachment-policies": [
        {
            "rule-number": 125,
            "condition-logic": "and",
            "conditions": [
                {
                    "type": "tag-exists",
                    "key": "InspectionVpcs"
                }
            ],
            "action": {
                "add-to-network-function-group": "InspectionVPC"
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
