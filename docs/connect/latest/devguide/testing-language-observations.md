---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/testing-language-observations.html
---

# Observations in the Connect Customer Testing language
<a name="testing-language-observations"></a>

Observations represent each complete interaction that includes one observed event expected from the system and many actions to validate or simulate system behaviors.

## Parameters
<a name="testing-language-observations-parameters"></a>
+ Version - The API version for the testing language, such as 2019-10-30.
+ Metadata - Optional object containing UI-specific or non-functional data
+ Observations - An array of observation objects that define the test flow

## Observation object
<a name="testing-language-observations-object"></a>

Each observation consists of an event to observe and actions to execute when that event occurs.
+ Identifier - Unique identifier for the observation
+ Event - Defines the expected event from the system to observe
+ Actions - Array of actions to execute when the event is observed
+ Usage - Defines how many times this observation should be matched
  + Type: Specifies how many times the observation must match. Valid values are `Exactly`, `AtLeast`, `AtMost`, or `Always` (case-sensitive).
  + Times: An integer value for the count. This field is required for all types except `Always`.
+ Transitions - Optional object defining flow control to next observations
  + NextObservations: Array of observation IDs to transition to

```
{
  "Version": "2019-10-30",
  "Metadata": { ... }, // Metadata to be used for data which is used for UI or any non-runtime impacting data as required.
  "Observations": [
    {
      "Identifier": "unique identifier",
      "Event": { ... },
      "Actions": [
            {
                "Identifier": "ActionId",
                "Type": "ActionType", // Action type could be of any type mentioned in recap (ObserveEvent, SendInstruction, Assertion, OverrideSystemBehavior, EndTest)
                "Parameters": {...},
                "Transitions" : {...}
            },
            ...
        ],
      "Usage": { "Type": "Exactly", "Times": 1 },
      "Transitions" : {
        "NextObservations": ["string-id", "string-id", "string-id"]
      }
    },
    // Additional observations...
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
