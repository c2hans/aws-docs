---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListReviewPolicyResultsForHITOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# ListReviewPolicyResultsForHIT
<a name="ApiReference_ListReviewPolicyResultsForHITOperation"></a>

## Description
<a name="ApiReference_ListReviewPolicyResultsForHITOperation-description"></a>

The `ListReviewPolicyResultsForHIT` operation retrieves the computed results and the actions taken in the course of executing your Review Policies during a CreateHIT operation. For information about how to apply Review Policies when you call CreateHIT, see Review Policies. The GetReviewResultsForHIT operation can return results for both Assignment-level and HIT-level review results. You can also specify to only return results pertaining to a particular Assignment.

## Request Syntax
<a name="ApiReference_ListReviewPolicyResultsForHITOperation-request-syntax"></a>

```
{
  "HITId": {{String}},

  "PolicyLevel": {{String}},

  "AssignmentId": {{String}},

  "RetrieveActions": {{String}},

  "RetrieveResults": {{String}},

  "NextToken": {{String}},

  "MaxResults": {{Integer}}
 }
```

## Request Parameters
<a name="ApiReference_ListReviewPolicyResultsForHITOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The unique identifier of the HIT to retrieve review results for.<br />Type: String | Yes |
|  ` PolicyLevel `  | The Policy Level(s) to retrieve review results for - HIT or Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see Review Policies.<br />Type: String | Yes |
|  ` AssignmentId `  | If supplied, the results are limited to those pertaining directly to this Assignment ID.<br />Type: String | No |
|  ` RetrieveActions `  | Retrieves a list of the actions taken executing the Review Policies and their outcomes. T or F.<br />Type: String | No |
|  ` RetrieveResults `  | Retrieves a list of the results computed by the Review Policies. T or F.<br />Type: String | No |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListReviewPolicyResultsForHITOperation-response-elements"></a>

A successful request operation has a ListReviewPolicyResultsForHITResponse element in the response. The ListReviewPolicyResultsForHITResponse element contains the name of the Review Policy applied as well as the AssignmentReviewReport element and the HITReviewReport element.
