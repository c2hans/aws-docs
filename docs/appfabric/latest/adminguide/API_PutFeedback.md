---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/API_PutFeedback.html
---

# PutFeedback
<a name="API_PutFeedback"></a>

|  |
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Allows users to submit feedback for a given insight or action.

**Topics**
+ [Request body](#API_PutFeedback_request)
+ [Response elements](#API_PutFeedback_response)

## Request body
<a name="API_PutFeedback_request"></a>

The request accepts the following data in JSON format.

| Parameter | Description |
| --- | --- |
| **id** | The ID of the object for which feedback is being submitted. This can be either the InsightId or the ActionId. |
| **feedbackFor** | The insight type for which the feedback is being submitted.<br />Possible values: `ACTIONABLE_INSIGHT \| MEETING_INSIGHT \| ACTION` |
| **feedbackRating** | Feedback Rating from `1` to `5`. Higher rating the better. |

## Response elements
<a name="API_PutFeedback_response"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
