---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html
---

# ListRoots
<a name="API_ListRoots"></a>

Lists the roots that are defined in the current organization.

**Note**
When calling List\* operations, always check the `NextToken` response parameter value, even if you receive an empty result set. These operations can occasionally return an empty set of results even when more results are available. Continue making requests until `NextToken` returns null. A null `NextToken` value indicates that you have retrieved all available results.

You can only call this operation from the management account or a member account that is a delegated administrator.

**Note**
Policy types can be enabled and disabled in roots. This is distinct from whether they're available in the organization. When you enable all features, you make policy types available for use in that organization. Individual policy types can then be enabled and disabled in a root. To see the availability of a policy type in an organization, use [DescribeOrganization](API_DescribeOrganization.md).

## Request Syntax
<a name="API_ListRoots_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRoots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRoots_RequestSyntax) **   <a name="organizations-ListRoots-request-MaxResults"></a>
The maximum number of items to return in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that you can retrieve the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListRoots_RequestSyntax) **   <a name="organizations-ListRoots-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from.
Type: String
Length Constraints: Maximum length of 100000.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_ListRoots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Roots": [
      {
         "Arn": "string",
         "Id": "string",
         "Name": "string",
         "PolicyTypes": [
            {
               "Status": "string",
               "Type": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListRoots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRoots_ResponseSyntax) **   <a name="organizations-ListRoots-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`.
Type: String
Length Constraints: Maximum length of 100000.
Pattern: `[\s\S]*`

 ** [Roots](#API_ListRoots_ResponseSyntax) **   <a name="organizations-ListRoots-response-Roots"></a>
A list of roots that are defined in an organization.
Type: Array of [Root](API_Root.md) objects

## Errors
<a name="API_ListRoots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
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
<a name="API_ListRoots_Examples"></a>

### Example
<a name="API_ListRoots_Example_1"></a>

The following example shows how to get a list of roots for an organization.

#### Sample Request
<a name="API_ListRoots_Example_1_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSOrganizationsV20161128.ListRoots

{}
```

#### Sample Response
<a name="API_ListRoots_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "Roots": [
        {
            "Name": "Root",
            "Arn": "arn:aws:organizations::111111111111:root/o-exampleorgid/r-examplerootid111",
            "Id": "r-examplerootid111",
            "PolicyTypes": [
                {
                    "Type": "AISERVICES_OPT_OUT_POLICY",
                    "Status": "ENABLED"
                },
                {
                    "Type": "BACKUP_POLICY",
                    "Status": "ENABLED"
                },
                {
                    "Type": "TAG_POLICY",
                    "Status": "ENABLED"
                },
                {
                    "Type": "SERVICE_CONTROL_POLICY",
                    "Status": "ENABLED"
                },
                {
                    "Type": "RESOURCE_CONTROL_POLICY",
                    "Status": "ENABLED"
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_ListRoots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/organizations-2016-11-28/ListRoots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/organizations-2016-11-28/ListRoots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/ListRoots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/organizations-2016-11-28/ListRoots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/ListRoots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/organizations-2016-11-28/ListRoots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/organizations-2016-11-28/ListRoots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/organizations-2016-11-28/ListRoots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/organizations-2016-11-28/ListRoots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/ListRoots)
