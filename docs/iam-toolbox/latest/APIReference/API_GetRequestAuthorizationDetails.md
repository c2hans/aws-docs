---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_GetRequestAuthorizationDetails.html
---

# GetRequestAuthorizationDetails
<a name="API_GetRequestAuthorizationDetails"></a>

Retrieves the authorization details for a specific access denied request. The details include the request context, the evaluations performed, and the policies that were evaluated.

Use this operation to understand why a request was denied. Supported services include an authorization ID in the access denied error message. Pass that ID to this operation to retrieve the details.

Authorization details are available for at least 24 hours after the denial.

To use this operation, you must have the `iam:GetRequestAuthorizationDetails` permission.

## Request Syntax
<a name="API_GetRequestAuthorizationDetails_RequestSyntax"></a>

```
GET /authorization-details/{{authorizationId}}?nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRequestAuthorizationDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authorizationId](#API_GetRequestAuthorizationDetails_RequestSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationDetails-request-uri-authorizationId"></a>
The authorization ID received in the access denied error message. This ID identifies the specific request to retrieve details for.
Pattern: `[0123456789abcdefghijklmnopqrstuvwxyz]+`
Required: Yes

 ** [nextToken](#API_GetRequestAuthorizationDetails_RequestSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationDetails-request-uri-nextToken"></a>
The pagination token from a previous call, used to retrieve the next page of evaluations. Omit this value on the first call.

## Request Body
<a name="API_GetRequestAuthorizationDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRequestAuthorizationDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "evaluations": [
      {
         "action": "string",
         "context": {
            "string" : JSON value
         },
         "evaluatedEffect": "string",
         "matchedPolicies": [
            {
               "matchedStatements": [
                  {
                     "evaluatedEffect": "string",
                     "sid": "string"
                  }
               ],
               "uri": "string"
            }
         ],
         "resource": "string"
      }
   ],
   "nextToken": "string",
   "policies": [
      {
         "attachedTo": [
            {
               "arn": "string"
            }
         ],
         "inline": boolean,
         "type": "string",
         "uri": "string"
      }
   ],
   "requestContext": {
      "string" : JSON value
   }
}
```

## Response Elements
<a name="API_GetRequestAuthorizationDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evaluations](#API_GetRequestAuthorizationDetails_ResponseSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationDetails-response-evaluations"></a>
The list of evaluations for this request. Each evaluation shows how a single action and resource pair was evaluated. This includes the context, the effect, and any policies that matched.
Type: Array of [Evaluation](API_Evaluation.md) objects

 ** [nextToken](#API_GetRequestAuthorizationDetails_ResponseSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationDetails-response-nextToken"></a>
The pagination token for retrieving the next page of evaluations. This value is absent when there are no more results.
Type: String

 ** [policies](#API_GetRequestAuthorizationDetails_ResponseSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationDetails-response-policies"></a>
The list of policies that were evaluated.
Type: Array of [PolicyInfo](API_PolicyInfo.md) objects

 ** [requestContext](#API_GetRequestAuthorizationDetails_ResponseSyntax) **   <a name="iamtoolbox-GetRequestAuthorizationDetails-response-requestContext"></a>
The request context is the set of context keys and values that apply to the entire request and are shared by all evaluations.
Type: String to JSON value map

## Errors
<a name="API_GetRequestAuthorizationDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested authorization details do not exist in this region or have expired. Verify that the authorization ID from the access denied error message is correct and the call is made in the region where the denial occurred. Ensure that the calling principal belongs to the same account or organization as the original denied request.
HTTP Status Code: 404

 ** ValidationException **
The request is malformed or is missing one or more required parameters. Check the request parameters and try again.
HTTP Status Code: 400

## Examples
<a name="API_GetRequestAuthorizationDetails_Examples"></a>

### Example – Retrieve authorization details for an implicitly denied iam:GetUser request
<a name="API_GetRequestAuthorizationDetails_Example_1"></a>

This example illustrates one usage of GetRequestAuthorizationDetails.

#### Sample Request
<a name="API_GetRequestAuthorizationDetails_Example_1_Request"></a>

```
{
  "authorizationId": "a1b2c3d4e5f6g7h8i9j0"
}
```

#### Sample Response
<a name="API_GetRequestAuthorizationDetails_Example_1_Response"></a>

```
{
  "evaluations": [
    {
      "action": "iam:GetUser",
      "context": {},
      "evaluatedEffect": "IMPLICIT_DENY",
      "matchedPolicies": [],
      "resource": "arn:aws:iam::111122223333:user/ExampleUser"
    }
  ],
  "policies": [
    {
      "attachedTo": [
        {
          "arn": "arn:aws:iam::111122223333:role/ImplicitDeny"
        }
      ],
      "inline": true,
      "type": "SESSION_POLICY",
      "uri": "inline:b6cf943c21a1966b"
    }
  ],
  "requestContext": {
    "aws:ViaAWSService": "false",
    "aws:MultiFactorAuthPresent": "false",
    "aws:TokenIssueTime": "2026-01-01T00:00:00Z",
    "aws:ResourceOrgPaths": "[o-exampleorgid/r-examp/]",
    "aws:UserAgent": "aws-cli/2.0.0 md/command#iam.get-user",
    "aws:UserId": "AROADBQP57FF2AEXAMPLE:example-session",
    "aws:ResourceOrgID": "o-exampleorgid",
    "aws:PrincipalAccount": "111122223333",
    "aws:EpochTime": "2026-01-01T00:00:00Z",
    "aws:PrincipalARN": "arn:aws:iam::111122223333:role/ImplicitDeny",
    "aws:ViaAWSMCPService": "false",
    "aws:SourceIp": "192.0.2.1/32",
    "aws:RequestedRegion": "us-east-1",
    "aws:PrincipalIsAWSService": "false",
    "aws:SecureTransport": "true",
    "aws:PrincipalOrgPaths": "[o-exampleorgid/r-examp/]",
    "aws:PrincipalOrgID": "o-exampleorgid",
    "aws:CurrentTime": "2026-01-01T00:00:00Z"
  }
}
```

### Example – Retrieve authorization details for an explicitly denied iam:GetUser request
<a name="API_GetRequestAuthorizationDetails_Example_2"></a>

This example illustrates one usage of GetRequestAuthorizationDetails.

#### Sample Request
<a name="API_GetRequestAuthorizationDetails_Example_2_Request"></a>

```
{
  "authorizationId": "z9y8x7w6v5u4t3s2r1q0"
}
```

#### Sample Response
<a name="API_GetRequestAuthorizationDetails_Example_2_Response"></a>

```
{
  "evaluations": [
    {
      "action": "iam:GetUser",
      "context": {},
      "evaluatedEffect": "EXPLICIT_DENY",
      "matchedPolicies": [
        {
          "matchedStatements": [
            {
              "evaluatedEffect": "DENY",
              "sid": "DenyAll"
            }
          ],
          "uri": "arn:aws:iam::aws:policy/AWSDenyAll"
        }
      ],
      "resource": "arn:aws:iam::111122223333:user/ExampleUser"
    }
  ],
  "policies": [
    {
      "attachedTo": [
        {
          "arn": "arn:aws:iam::111122223333:role/ExplicitDeny"
        }
      ],
      "inline": false,
      "type": "IDENTITY_BASED_POLICY",
      "uri": "arn:aws:iam::aws:policy/AWSDenyAll"
    }
  ],
  "requestContext": {
    "aws:ViaAWSService": "false",
    "aws:MultiFactorAuthPresent": "false",
    "aws:TokenIssueTime": "2026-01-01T00:00:00Z",
    "aws:ResourceOrgPaths": "[o-exampleorgid/r-examp/]",
    "aws:UserAgent": "aws-cli/2.0.0 md/command#iam.get-user",
    "aws:UserId": "AROADBQP57FF2AEXAMPLE:example-session",
    "aws:ResourceOrgID": "o-exampleorgid",
    "aws:PrincipalAccount": "111122223333",
    "aws:EpochTime": "2026-01-01T00:00:00Z",
    "aws:PrincipalARN": "arn:aws:iam::111122223333:role/ExplicitDeny",
    "aws:ViaAWSMCPService": "false",
    "aws:SourceIp": "192.0.2.1/32",
    "aws:RequestedRegion": "us-east-1",
    "aws:PrincipalIsAWSService": "false",
    "aws:SecureTransport": "true",
    "aws:PrincipalOrgPaths": "[o-exampleorgid/r-examp/]",
    "aws:PrincipalOrgID": "o-exampleorgid",
    "aws:CurrentTime": "2026-01-01T00:00:00Z"
  }
}
```

## See Also
<a name="API_GetRequestAuthorizationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/GetRequestAuthorizationDetails)
