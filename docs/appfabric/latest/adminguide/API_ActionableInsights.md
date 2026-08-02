---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_ActionableInsights.html
---

# ActionableInsights
<a name="API_ActionableInsights"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains a summary of important and suitable actions for a user based on emails, calendar invites, messages, and tasks from their app portfolio. Users can see proactive insights from across their applications to help them best orient their day. These insights provide justification on why a user should care about the insight summary along with references, such as embedded links, to individual apps and artifacts that generated the insight.

| Parameter | Description |
| --- | --- |
| **insightId** | The unique id for the generated insight. |
| **insightContent** | This returns a summary of the insight and embedded links to artifacts used to generate the insight.<br />This would be an HTML content containing embedded links (`<a>` tags). |
| **insightTitle** | The title of the generated insight. |
| **createdAt** | When the insight was generated. |
| **actions** | A list of actions recommend for the generated insight.<br />The action object contains the following parameters:[See the AWS documentation website for more details](http://docs.aws.amazon.com/appfabric/latest/adminguide/API_ActionableInsights.html) |
