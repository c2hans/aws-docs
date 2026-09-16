---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetAccountBalanceOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# GetAccountBalance
<a name="ApiReference_GetAccountBalanceOperation"></a>

## Description
<a name="ApiReference_GetAccountBalanceOperation-description"></a>

The `GetAccountBalance` operation retrieves the Prepaid HITs balance in your Amazon Mechanical Turk account if you are a Prepaid Requester. Alternatively, this operation will retrieve the remaining available AWS Billing usage if you have enabled AWS Billing.

Note: If you have enabled AWS Billing and still have a remaining Prepaid HITs balance, this balance can be viewed on the My Account page in the Requester console.

## Request Syntax
<a name="ApiReference_GetAccountBalanceOperation-request-syntax"></a>

```
{  }
```

## Request Parameters
<a name="ApiReference_GetAccountBalanceOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

## Response Elements
<a name="ApiReference_GetAccountBalanceOperation-response-elements"></a>

A successful request returns a string representing your available balance details in US Dollars.

## Example
<a name="ApiReference_GetAccountBalanceOperation-examples"></a>

The following example shows how to use the `GetAccountBalance` operation:

### Sample Request
<a name="ApiReference_GetAccountBalanceOperation-examples-sample-request"></a>

The following makes a GetAccountBalance request.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
}
```

### Sample Response
<a name="ApiReference_GetAccountBalanceOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  AvailableBalance:10000.00
}
```
