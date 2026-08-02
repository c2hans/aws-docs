---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/get-tracker-details.html
---

# Tutorial: Get tracker details with Amazon Location
<a name="get-tracker-details"></a>

You can get details about any tracker in your AWS account by using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To view tracker details by using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Trackers** from the left navigation.

1. Under **My trackers**, select the name link of the target tracker.

1. View the tracker details under **Information**.

------
#### [ API ]

Use the `[DescribeTracker](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_DescribeTracker.html)` operation from the Amazon Location Tracker APIs.

The following example is an API request to get the tracker details for {{ExampleTracker}}.

```
GET /tracking/v0/trackers/{{ExampleTracker}}
```

The following is an example response for `[DescribeTracker](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_DescribeTracker.html)`:

```
{
   "CreateTime": 2020-10-02T19:09:07.327Z,
   "Description": "string",
   "EventBridgeEnabled": false,
   "KmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
   "PositionFiltering": "TimeBased",
   "Tags": {
      "Tag1" : "Value1"
   },
   "TrackerArn": "arn:aws:geo:us-west-2:123456789012:tracker/ExampleTracker",
   "TrackerName": "{{ExampleTracker}}",
   "UpdateTime": 2020-10-02T19:10:07.327Z
}
```

------
#### [ CLI ]

Use the `[describe-tracker](https://docs.aws.amazon.com/cli/latest/reference/location/describe-tracker.html)` command.

The following example is an AWS CLI command to get tracker details for {{ExampleTracker}}.

```
aws location describe-tracker \
    --tracker-name "{{ExampleTracker}}"
```

------
