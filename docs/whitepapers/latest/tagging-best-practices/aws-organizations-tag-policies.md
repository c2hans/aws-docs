---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/aws-organizations-tag-policies.html
---

# AWS Organizations – Tag policies
<a name="aws-organizations-tag-policies"></a>

 Policies in AWS Organizations allow you to apply additional types of governance to AWS accounts in your organization. A [*tag policy*](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) is how you can express your tagging schema in JSON form so that the platform can report and optionally enforce the schema within your AWS environment. The tag policy defines the values that are acceptable for a tag key on specific resource types. This policy can be in the form of a list of values, or a prefix followed by a wildcard character (`*`). The simple prefix approach is less rigorous than a discrete list of values but requires less maintenance.

 The following examples show how to define a tagging policy to validate the values that are acceptable for a given key. Working from the human-friendly tabular definition of the schema, you can transcribe this information into one or more tag policies. Separate policies can be used to support delegated ownership or some policies might only apply in specific scenarios.

## ExampleInc-CostAllocation.json
<a name="exampleinc-costallocation.json"></a>

 The following is an example of a tag policy that reports on Cost Allocation tags:

```
{
  "tags": {
    "example-inc:cost-allocation:ApplicationId": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:ApplicationId"
      },
      "tag_value": {
        "@@assign": [
          "DataLakeX",
          "RetailSiteX"
        ]
      }
    },
    "example-inc:cost-allocation:BusinessUnitId": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:BusinessUnitId"
      },
      "tag_value": {
        "@@assign": [
          "Architecture",
          "DevOps",
          "FinanceDataLakeX"
        ]
      }
    },
    "example-inc:cost-allocation:CostCenter": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:CostCenter"
      },
      "tag_value": {
        "@@assign": [
          "123-*"
        ]
      }
    }
  }
}
```

## ExampleInc-DisasterRecovery.json
<a name="exampleinc-disasterrecovery.json"></a>

 The following is an example of a tag policy that reports on Disaster Recovery tags:

```
{
    "tags": {
        "example-inc:disaster-recovery:rpo": {
            "tag_key": {
                "@@assign": "example-inc:disaster-recovery:rpo"
            },
            "tag_value": {
                "@@assign": [
                    "6h",
                    "24h"
                ]
            }
        }
    }
}
```

 In this example, the `ExampleInc-CostAllocation` tag policy is attached to the `Workloads` OU, and therefore applies to all the accounts in both the `Prod` and `Test` child OUs. Similarly, the `ExampleInc-DisasterRecovery` tag policy is attached to the `Prod` OU and therefore only applies to accounts below this OU. The [Organizing Your Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper explores the recommended OU structures in more detail.

![Diagram showing the attachment of tag policies to an OU structure and the effective policy](http://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/images/adding-tagging-to-policies-in-ou-structure.png)

 Looking at the `marketing-prod` account in the diagram, both tag policies apply to this account, so we have the concept of an *effective policy*, which is the convolution of the policies of a given type that apply to an account. If you primarily manage your resources manually, then you can review the effective policy by visiting the [Resource Groups & Tag Editor:Tag policies](http://console.aws.amazon.com/resource-groups/tag-policies) in the console. If you use infrastructure as code (IaC) or scripting to manage your resources, you can use the [`AWS::Organizations::DescribeEffectivePolicy`](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) API call.
