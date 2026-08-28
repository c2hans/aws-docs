---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/viewing-trackers.html
---

# Tutorial: List your trackers
<a name="viewing-trackers"></a>

You can view your trackers list using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view a list of existing trackers using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose** Trackers** from the left navigation.

1. View a list of your tracker resources under **My trackers**.

------
#### [ API ]

Use the `[ListTrackers](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_ListTrackers.html)` operation from the Amazon Location Trackers APIs.

The following example is an API request to get a list of trackers in your AWS account.

```
POST /tracking/v0/list-trackers
```

The following is an example response for `[ListTrackers](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_ListTrackers.html)`:

```
{
   "Entries": [
      {
         "CreateTime": 2020-10-02T19:09:07.327Z,
         "Description": "string",
         "TrackerName": "{{ExampleTracker}}",
         "UpdateTime": 2020-10-02T19:10:07.327Z
      }
   ],
   "NextToken": "1234-5678-9012"
}
```

------
#### [ CLI ]

Use the `[list-trackers](https://docs.aws.amazon.com/cli/latest/reference/location/list-trackers.html)` command.

The following example is an AWS CLI to get a list of trackers in your AWS account.

```
aws location list-trackers
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
