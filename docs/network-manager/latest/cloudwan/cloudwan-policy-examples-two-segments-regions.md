---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-two-segments-regions.html
---

# AWS Cloud WAN example: Two segments and multiple AWS Regions
<a name="cloudwan-policy-examples-two-segments-regions"></a>

This policy sets up two networks, `Secured` and `Non-Secured`, across three AWS Regions. Attachments with the tag `"Network" : "Secured"` map to `"Secured"`, while attachments with the tag `"Network" : "Non-Secured"` map to `"Non-Secured"`. All attachments require acceptance. Attachments can only talk within their segment but not across segments.

```
{
    "version": "2021.12",
    "core-network-configuration": {
        "asn-ranges": [
            "64512-65534"
        ],
        "edge-locations": [
            {
                "location": "us-east-1"
            },
            {
                "location": "us-east-2"
            },
            {
                "location": "eu-west-1"
            }
        ]
    },
    "segments": [
        {
            "name": "secured"
        },
        {
            "name": "nonSecured"
        }
    ],
    "attachment-policies": [
        {
            "rule-number": 100,
            "conditions": [
                {
                    "type": "tag-value",
                    "key": "Network",
                    "value": "Secured",
                    "operator": "equals"
                }
            ],
            "action": {
                "association-method": "constant",
                "segment": "secured"
            }
        },
        {
            "rule-number": 200,
            "conditions": [
                {
                    "type": "tag-value",
                    "key": "Network",
                    "value": "Non-Secured",
                    "operator": "equals"
                }
            ],
            "action": {
                "association-method": "constant",
                "segment": "non-secured"
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
