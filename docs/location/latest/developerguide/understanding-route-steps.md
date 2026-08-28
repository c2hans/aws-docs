---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/understanding-route-steps.html
---

# Understanding route steps
<a name="understanding-route-steps"></a>

This section defines various actions and steps that need to be taken to complete a leg of a journey. Route steps vary by travel mode and provide guidance for both overview applications and detailed turn-by-turn navigation.

## Route steps overview
<a name="route-steps-overview"></a>

The following types of route steps define the actions needed to complete a route leg, varying by travel mode and the stage of the journey.

| **Step type** | **Description** |
| --- | --- |
| Default steps | Basic steps providing human-readable instructions, often used in web-based applications to offer an overview of the route. |
| Turn by turn steps | Detailed steps for creating a turn-by-turn navigation application, offering more granular directions. |
| Before travel steps | Steps that need to be completed before starting the travel section, such as boarding a ferry. |
| After travel steps | Steps to be performed after the travel section is complete, like de-boarding a ferry. |

## Step breakdown by travel mode
<a name="route-step-types"></a>

| **Section** | **Step** | **Before Travel** | **Travel** | **After Travel** |
| --- | --- | --- | --- | --- |
| Vehicle | Arrive | No | Yes | No |
| Vehicle | Continue | No | Yes | No |
| Vehicle | ContinueHighway | No | Yes | No |
| Vehicle | Depart | No | Yes | No |
| Vehicle | Exit | No | Yes | No |
| Pedestrian | Arrive | No | Yes | No |
| Pedestrian | Charge | No | Yes | No |
| Ferry | Wait | No | No | Yes |
| Ferry | Board | Yes | No | No |
| Ferry | Deboard | No | No | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
