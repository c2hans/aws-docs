---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateHITReviewStatusOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# UpdateHITReviewStatus
<a name="ApiReference_UpdateHITReviewStatusOperation"></a>

## Description
<a name="ApiReference_UpdateHITReviewStatusOperation-description"></a>

The `UpdateHITReviewStatus` operation toggles the status of a HIT. If the status is Reviewable, this operation updates the status to Reviewing, or reverts a Reviewing HIT back to the Reviewable status.

For example, when processing assignments from Workers if you do not want to make an immediate decision about approving or rejecting assignments, you can use this operation to set the status of the HIT to Reviewing . To retrieve a list of HITs in reviewing status, add `"Status": "Reviewing"` to your request parameters in the [ListReviewableHITs](ApiReference_ListReviewableHITsOperation.md) Operation.

## Request Syntax
<a name="ApiReference_UpdateHITReviewStatusOperation-request-syntax"></a>

```
{
  "HITId": {{String}},

  "Revert": {{Boolean}}
 }
```

## Request Parameters
<a name="ApiReference_UpdateHITReviewStatusOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The HIT to update.<br />Type: String | Yes |
|  ` Revert `  | Specifies whether to update the HIT Status from Reviewing to Reviewable.<br />Type: Boolean<br />Default: false; the operation promotes the HIT from Reviewable to Reviewing. | No |

## Response Elements
<a name="ApiReference_UpdateHITReviewStatusOperation-response-elements"></a>

 A successful request for the `UpdateHITReviewStatus` operation returns with no errors and an empty body.
