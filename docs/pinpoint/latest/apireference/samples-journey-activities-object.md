---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/samples-journey-activities-object.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Schema sample: JourneyResponse object
<a name="samples-journey-activities-object"></a>

When you retrieve information about a journey by sending a GET request to the [Journey](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id.html) or [Journeys](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys.html) resource, Amazon Pinpoint returns a `JourneyResponse` object. This object provides information about the status, configuration, and other settings for a journey. It also provides information about all the activities in a journey and the relationships between those activities. This information is stored in an `Activities` object.

An `Activities` object is a map that contains a set of `Activity` objects. It contains one `Activity` object for each activity in a journey. For each `Activity` object in the map, the key is the unique identifier for an activity and the value is one or more settings for the activity. By using an activity’s unique identifier in combination with the `NextActivity` property, you can trace the relationships between activities in a journey.

The following sample of a `JourneyResponse` object includes example data that shows the structure of an `Activities` object. It also shows the structure of individual `Activity` objects that the `Activities` object contains. In this sample, the journey has eight activities in addition to the start activity. It has: four email (`EMAIL`) activities; one wait (`Wait`) activity; one yes/no split (`ConditionalSplit`) activity; one multivariate split (`MultiCondition`) activity; and, one random split (`RandomSplit`) activity.

The `Activity` object for each of these activities specifies the settings for the activity. For example, the first activity in the `Activities` object has the following characteristics and settings:
+ The unique identifier is `Viv6yKziaa`.
+ The activity is an email (`EMAIL`) activity.
+ The activity sends an email message from the `welcome@example.com` address.
+ The activity sends an email message that uses a template named `Welcome_New_Subscribers`.
+ When participants complete the activity, they move to the multivariate split (`MultiCondition`) activity whose unique identifier is `1tvNWcuvXK`, as specified by the `NextActivity` property of the email activity.

Other types of activities specify settings that apply to that type of activity. For example, the multivariate split (`MultiCondition`) activity in this sample specifies two paths—participants in the activity are sent down one of the two paths based on a segment condition. Similarly, the random split (`RandomSplit`) activity in this sample specifies two paths—50% of randomly selected participants are sent down one path and 50% of randomly selected participants are sent down the other path.

 **Sample JourneyResponse object**

```
{
  "Name" : "Example Corp New Subscriber Journey",
  "Schedule" : {
    "Timezone" : "UTC-08"
  },
  "StartCondition" : {
    "SegmentStartCondition" : {
      "SegmentId" : "50a12f64634ca8e71e92005b9example"
    }
  },
  "StartActivity" : "0roHkysnX3",
  "Activities" : {
    "Viv6yKziaa" : {
      "EMAIL" : {
        "MessageConfig" : {
          "FromAddress" : "welcome@example.com"
        },
        "NextActivity" : "1tvNWcuvXK",
        "TemplateName" : "Welcome_New_Subscribers"
      }
    },
    "0roHkysnX3" : {
      "EMAIL" : {
        "MessageConfig" : {
          "FromAddress" : "welcome@example.com"
        },
        "NextActivity" : "p1gOHvWOhc"
      }
    },
    "12LUtDeRst" : {
      "Wait" : {
        "NextActivity" : "Viv6yKziaa"
      }
    },
    "p1gOHvWOhc" : {
      "ConditionalSplit" : {
        "Condition" : {
          "Conditions" : [ { } ],
          "Operator" : "ANY"
        },
        "TrueActivity" : "12LUtDeRst",
        "FalseActivity" : "3l1znWgu9N"
      }
    },
    "1tvNWcuvXK" : {
      "MultiCondition" : {
        "Branches" : [ {
          "Condition" : {
            "SegmentCondition" : {
              "SegmentId" : "42d8c7eb0990a57ba1d5476a3example"
            }
          },
          "NextActivity" : "nMvVg72WFd"
        }, {
          "NextActivity" : "HSGfxJ6itl"
        }, { } ]
      }
    },
    "nMvVg72WFd" : {
      "EMAIL" : { }
    },
    "HSGfxJ6itl" : {
      "EMAIL" : { }
    },
    "3l1znWgu9N" : {
      "RandomSplit" : {
        "Branches" : [ {
          "Percentage" : 50
        }, {
          "Percentage" : 50
        } ]
      }
    }
  },
  "LocalTime" : false,
  "CreationDate" : "2020-01-15T16:00:46.223Z",
  "LastModifiedDate" : "2020-01-20T17:17:37.149Z",
  "State" : "DRAFT",
  "Id" : "80b8efd84042ff8d9c96ce2f8example",
  "ApplicationId" : "810c7aab86d42fb2b56c8c966example"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
