---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html
---

# DescribeAccount
<a name="API_DescribeAccount"></a>

Retrieves AWS Organizations-related information about the specified account.

You can only call this operation from the management account or a member account that is a delegated administrator.

## Request Syntax
<a name="API_DescribeAccount_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_DescribeAccount_RequestSyntax) **   <a name="organizations-DescribeAccount-request-AccountId"></a>
The unique identifier (ID) of the AWS account that you want information about. You can get the ID from the [ListAccounts](API_ListAccounts.md) or [ListAccountsForParent](API_ListAccountsForParent.md) operations.
The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID string requires exactly 12 digits.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: Yes

## Response Syntax
<a name="API_DescribeAccount_ResponseSyntax"></a>

```
{
   "Account": {
      "Arn": "string",
      "Email": "string",
      "Id": "string",
      "JoinedMethod": "string",
      "JoinedTimestamp": number,
      "Name": "string",
      "Paths": [ "string" ],
      "State": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Account](#API_DescribeAccount_ResponseSyntax) **   <a name="organizations-DescribeAccount-response-Account"></a>
A structure that contains information about the requested account.
The `Status` parameter in the API response will be retired on September 9, 2026. Although both the account `State` and account `Status` parameters are currently available in the AWS Organizations APIs (`DescribeAccount`, `ListAccounts`, `ListAccountsForParent`), we recommend that you update your scripts or other code to use the `State` parameter instead of `Status` before September 9, 2026.
Type: [Account](API_Account.md) object

## Errors
<a name="API_DescribeAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 400

 ** AccountNotFoundException **
 We can't find an AWS account with the `AccountId` that you specified, or the account whose credentials you used to make this request isn't a member of an organization.
HTTP Status Code: 400

 ** AWSOrganizationsNotInUseException **
Your account isn't a member of an organization. To make this request, you must use the credentials of an account that belongs to an organization.
HTTP Status Code: 400

 ** InvalidInputException **
The requested operation failed because you provided invalid values for one or more of the request parameters. This exception includes a reason that contains additional information about the violated limit:
Some of the reasons in the following list might not be applicable to this specific API or operation.
+ CALLER\_REQUIRED\_FIELD\_MISSING: At least one of the required field is missing: Caller Account Id, Management Account Id or Organization Id.
+ DUPLICATE\_TAG\_KEY: Tag keys must be unique among the tags attached to the same entity.
+ END\_DATE\_NOT\_END\_OF\_MONTH: You provided an invalid end date. The end date must be the end of the last day of the month (23.59.59.999).
+ END\_DATE\_TOO\_EARLY: You provided an invalid end date. The end date is too early.
+ END\_DATE\_TOO\_LATE: You provided an invalid end date. The end date is too late.
+ IMMUTABLE\_POLICY: You specified a policy that is managed by AWS and can't be modified.
+ INPUT\_REQUIRED: You must include a value for all required parameters.
+ INVALID\_EMAIL\_ADDRESS\_TARGET: You specified an invalid email address for the invited account owner.
+ INVALID\_END\_DATE: The selected withdrawal date doesn't meet the terms of your partner agreement. Visit AWS Partner Central to view your partner agreements or contact your AWS Partner for help.
+ INVALID\_ENUM: You specified an invalid value.
+ INVALID\_ENUM\_POLICY\_TYPE: You specified an invalid policy type string.
+ INVALID\_FULL\_NAME\_TARGET: You specified a full name that contains invalid characters.
+ INVALID\_LIST\_MEMBER: You provided a list to a parameter that contains at least one invalid value.
+ INVALID\_PAGINATION\_TOKEN: Get the value for the `NextToken` parameter from the response to a previous call of the operation.
+ INVALID\_PARTY\_TYPE\_TARGET: You specified the wrong type of entity (account, organization, or email) as a party.
+ INVALID\_PATTERN: You provided a value that doesn't match the required pattern. The service also validates your free-text field values against common cross-site scripting (XSS) patterns and rejects requests that contain matching values.
+ INVALID\_PATTERN\_TARGET\_ID: You specified a policy target ID that doesn't match the required pattern.
+ INVALID\_PRINCIPAL: You specified an invalid principal element in the policy.
+ INVALID\_ROLE\_NAME: You provided a role name that isn't valid. A role name can't begin with the reserved prefix `AWSServiceRoleFor`.
+ INVALID\_START\_DATE: The start date doesn't meet the minimum requirements.
+ INVALID\_SYNTAX\_ORGANIZATION\_ARN: You specified an invalid Amazon Resource Name (ARN) for the organization.
+ INVALID\_SYNTAX\_POLICY\_ID: You specified an invalid policy ID.
+ INVALID\_SYSTEM\_TAGS\_PARAMETER: You specified a tag key that is a system tag. You can’t add, edit, or delete system tag keys because they're reserved for AWS use. System tags don’t count against your tags per resource limit.
+ MAX\_FILTER\_LIMIT\_EXCEEDED: You can specify only one filter parameter for the operation.
+ MAX\_LENGTH\_EXCEEDED: You provided a string parameter that is longer than allowed.
+ MAX\_VALUE\_EXCEEDED: You provided a numeric parameter that has a larger value than allowed.
+ MIN\_LENGTH\_EXCEEDED: You provided a string parameter that is shorter than allowed.
+ MIN\_VALUE\_EXCEEDED: You provided a numeric parameter that has a smaller value than allowed.
+ MOVING\_ACCOUNT\_BETWEEN\_DIFFERENT\_ROOTS: You can move an account only between entities in the same root.
+ NON\_DETACHABLE\_POLICY: You can't detach this AWS Managed Policy.
+ START\_DATE\_NOT\_BEGINNING\_OF\_DAY: You provided an invalid start date. The start date must be the beginning of the day (00:00:00.000).
+ START\_DATE\_NOT\_BEGINNING\_OF\_MONTH: You provided an invalid start date. The start date must be the first day of the month.
+ START\_DATE\_TOO\_EARLY: You provided an invalid start date. The start date is too early.
+ START\_DATE\_TOO\_LATE: You provided an invalid start date. The start date is too late.
+ TARGET\_NOT\_SUPPORTED: You can't perform the specified operation on that target entity.
+ UNRECOGNIZED\_SERVICE\_PRINCIPAL: You specified a service principal that isn't recognized.
+ UNSUPPORTED\_ACTION\_IN\_RESPONSIBILITY\_TRANSFER: You provided a value that is not supported by this operation.
HTTP Status Code: 400

 ** ServiceException **
 AWS Organizations can't complete your request because of an internal service error. Try again later.
HTTP Status Code: 500

 ** TooManyRequestsException **
You have sent too many requests in too short a period of time. The quota helps protect against denial-of-service attacks. Try again later.
For information about quotas that affect AWS Organizations, see [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the * AWS Organizations User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAccount_Examples"></a>

### Example
<a name="API_DescribeAccount_Example_1"></a>

The following example shows how to request information about member account 555555555555.

#### Sample Request
<a name="API_DescribeAccount_Example_1_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSOrganizationsV20161128.DescribeAccount

{ "AccountId": "555555555555" }
```

#### Sample Response
<a name="API_DescribeAccount_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
{
  "Account": {
    "Id": "555555555555",
    "Arn": "arn:aws:organizations::111111111111:account/o-exampleorgid/555555555555",
    "Name": "Beta account",
    "Email": "anika@example.com",
    "JoinedMethod": "INVITED",
    "JoinedTimeStamp": 1481756563.134,
    "State": "ACTIVE",
    "Status": "ACTIVE",
    "Paths": [
      "o-exampleorgid/r-examplerootid111/555555555555/"
    ]
  }
}
```

## See Also
<a name="API_DescribeAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/organizations-2016-11-28/DescribeAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/DescribeAccount)
