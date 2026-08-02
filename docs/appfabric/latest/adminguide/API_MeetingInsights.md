---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_MeetingInsights.html
---

# MeetingInsights
<a name="API_MeetingInsights"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains a summary of the top 3 meetings along with meeting purpose, related cross-app artifacts, and activities from tasks, emails, messages, and calendar events.

| Parameter | Description |
| --- | --- |
| **insightId** | The unique id for the generated insight. |
| **insightContent** | The description of the insight highlighting the details in a string format. As in, why is this insight important. |
| **insightTitle** | The title of the generated insight. |
| **createdAt** | When the insight was generated. |
| **calendarEvent** | The important calendar event or meeting that the user should focus on.<br />Calendar Event object:[See the AWS documentation website for more details](http://docs.aws.amazon.com/appfabric/latest/adminguide/API_MeetingInsights.html) |
| **resources** | The list containing the other resources related to the generate the insight.<br />Resource object:[See the AWS documentation website for more details](http://docs.aws.amazon.com/appfabric/latest/adminguide/API_MeetingInsights.html) |
| **nextToken** | The pagination token to fetch the next set of insights. It’s an optional field which if returned null means there are no more insights to load. |
