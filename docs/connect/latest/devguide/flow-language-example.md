---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-language-example.html
---

# Example flow in Connect Customer Flow language
<a name="flow-language-example"></a>

The following example shows a JSON string that represents the content of the flow. It shows a simple flow that plays a prompt using static text and disconnects.

To learn how to get block identifiers, we recommend creating a new flow in Connect Customer console, and then calling the [DescribeContactFlow](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContactFlow.html) API for it.

```
{
    "Version": "2019-10-30",  //A string representing the version of the Flow. Currently the only supported version is 2019-10-30.

    "StartAction": "12345678-1234-1234-1234-123456789012", //A string representing the first Action to run when the flow starts running.
                                                          //In this case, it's the identifier of the Play prompt block.
                                                         //The value of this field must match the Identifier of an Action in the Actions list.
    "Metadata": { //An object that may be filled in with data as desired.
        "EntryPointPosition": {
            "x": 88,
            "y": 100
        },
        "ActionMetadata": {
            "12345678-1234-1234-1234-123456789012": {//The identifier of the Play prompt block.
                "Position": {
                    "x": 270,
                    "y": 98
                }
            },
            "abcdef-abcd-abcd-abcd-abcdefghijkl": {//The identifier of the Disconnect/hang up block.
                "Position": {
                    "x": 545,
                    "y": 92
                }
            }

        }
    },
    "Actions": [  //A list of individual Action objects. These Actions are the definition of the Flow's behavior and are detailed below.
                  //A single Flow may have no more than 250 Actions defined.
        {
            "Identifier": "12345678-1234-1234-1234-123456789012", //The identifier of the Play prompt block.
            "Type": "MessageParticipant",  //This is the flow action.
            "Transitions": {
                "NextAction": "abcdef-abcd-abcd-abcd-abcdefghijkl", //The identifier of the Disconnect/hang up block.
                "Errors": [],
                "Conditions": []
            },
            "Parameters": {
                "Text": "Thanks for calling the sample flow!"
            }
        },
        {
            "Identifier": "abcdef-abcd-abcd-abcd-abcdefghijkl",  //The identifier of the Disconnect/hang up block.
            "Type": "DisconnectParticipant",  //This is the flow action.
            "Transitions": {},
            "Parameters": {}
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
