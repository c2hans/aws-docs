---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateAdditionalAssignmentsForHITOperation.html
---

# CreateAdditionalAssignmentsForHIT
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation"></a>

## Description
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-description"></a>

 The `CreateAdditionalAssignmentsForHIT` operation increases the maximum number of assignments of an existing HIT.

 To extend the maximum number of assignments, specify the number of additional assignments.

**Note**
HITs created with fewer than 10 assignments cannot be extended to have 10 or more assignments. Attempting to add assignments in a way that brings the total number of assignments for a HIT from fewer than 10 assignments to 10 or more assignments will result in an `AWS.MechanicalTurk.InvalidMaximumAssignmentsIncrease` exception.
HITs that were created before July 22, 2015 cannot be extended. Attempting to extend HITs that were created before July 22, 2015 will result in an `AWS.MechanicalTurk.HITTooOldForExtension` exception.

## Request Syntax
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-request-syntax"></a>

```
{
  "HITId": {{String}},

  "NumberOfAdditionalAssignments": {{Integer}},

  "UniqueRequestToken": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The ID of the HIT to for which to request more assignments.<br />Type: String | Yes |
|  ` NumberOfAdditionalAssignments `  | The number of additional assignments to request for this HIT.<br />Type: Integer | Yes |
|  ` UniqueRequestToken `  | A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same `UniqueRequestToken`, subsequent calls will return an error with a message containing the request ID.<br />Type: String<br />Constraints: must not be longer than 64 characters in length. | No |

## Response Elements
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-response-elements"></a>

 A successful request for the `CreateAdditionalAssignmentsForHIT` operation returns with no errors and an empty body.

## Example
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-examples"></a>

The following example shows how to use the `CreateAdditionalAssignmentsForHIT` operation:

### Sample Request
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-examples-sample-request"></a>

The following example adds 2 more assignments to a HIT.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
  HITId:"123RVAZW00EXAMPLE2SL3LSK",
  HITNumberOfAdditionalAssignments:2
}
```

### Sample Response
<a name="ApiReference_CreateAdditionalAssignmentsForHITOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
