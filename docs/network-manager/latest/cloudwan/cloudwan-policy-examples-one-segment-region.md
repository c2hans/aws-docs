---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-one-segment-region.html
---

# AWS Cloud WAN example: One segment, one AWS Region
<a name="cloudwan-policy-examples-one-segment-region"></a>

This policy sets up one network in `us-east-1` with the name **my-network**. Any attachment is automatically added to the network without requiring approval.

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
			}
		]
	},
	"segments": [
		{
			"name": "mynetwork",
			"require-attachment-acceptance": false
		}
	],
	"attachment-policies": [
		{
			"rule-number": 100,
			"condition-logic": "and",
			"conditions": [
				{
					"type": "any"
				}
			],
			"action": {
				"association-method": "constant",
				"segment": "mynetwork"
			}
		}
	]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
