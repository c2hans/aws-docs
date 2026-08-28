---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html
---

# DescribeParameters
<a name="API_DescribeParameters"></a>

Lists the parameters in your AWS account or the parameters shared with you when you enable the [Shared](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html#systemsmanager-DescribeParameters-request-Shared) option.

Request results are returned on a best-effort basis. If you specify `MaxResults` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of `MaxResults`. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a `NextToken`. You can specify the `NextToken` in a subsequent call to get the next set of results.

Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

**Important**
If you change the AWS KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, `DescribeParameters` retrieves whatever the original key alias was referencing.

## Request Syntax
<a name="API_DescribeParameters_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterFilters": [
      {
         "Key": "{{string}}",
         "Option": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Shared": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeParameters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeParameters_RequestSyntax) **   <a name="systemsmanager-DescribeParameters-request-Filters"></a>
This data type is deprecated. Instead, use `ParameterFilters`.
Type: Array of [ParametersFilter](API_ParametersFilter.md) objects
Required: No

 ** [MaxResults](#API_DescribeParameters_RequestSyntax) **   <a name="systemsmanager-DescribeParameters-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeParameters_RequestSyntax) **   <a name="systemsmanager-DescribeParameters-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [ParameterFilters](#API_DescribeParameters_RequestSyntax) **   <a name="systemsmanager-DescribeParameters-request-ParameterFilters"></a>
Filters to limit the request results.
Type: Array of [ParameterStringFilter](API_ParameterStringFilter.md) objects
Required: No

 ** [Shared](#API_DescribeParameters_RequestSyntax) **   <a name="systemsmanager-DescribeParameters-request-Shared"></a>
Lists parameters that are shared with you.
By default when using this option, the command returns parameters that have been shared using a standard AWS Resource Access Manager Resource Share. In order for a parameter that was shared using the [PutResourcePolicy](API_PutResourcePolicy.md) command to be returned, the associated ` AWS RAM Resource Share Created From Policy` must have been promoted to a standard Resource Share using the AWS RAM [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) API operation.
For more information about sharing parameters, see [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html) in the * AWS Systems Manager User Guide*.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeParameters_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Parameters": [
      {
         "AllowedPattern": "string",
         "ARN": "string",
         "DataType": "string",
         "Description": "string",
         "KeyId": "string",
         "LastModifiedDate": number,
         "LastModifiedUser": "string",
         "Name": "string",
         "Policies": [
            {
               "PolicyStatus": "string",
               "PolicyText": "string",
               "PolicyType": "string"
            }
         ],
         "Tier": "string",
         "Type": "string",
         "Version": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeParameters_ResponseSyntax) **   <a name="systemsmanager-DescribeParameters-response-NextToken"></a>
The token to use when requesting the next set of items.
Type: String

 ** [Parameters](#API_DescribeParameters_ResponseSyntax) **   <a name="systemsmanager-DescribeParameters-response-Parameters"></a>
Parameters returned by the request.
Type: Array of [ParameterMetadata](API_ParameterMetadata.md) objects

## Errors
<a name="API_DescribeParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilterKey **
The specified key isn't valid.
HTTP Status Code: 400

 ** InvalidFilterOption **
The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
 ** message **
The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
HTTP Status Code: 400

 ** InvalidFilterValue **
The filter value isn't valid. Verify the value and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeParameters_Examples"></a>

### Example
<a name="API_DescribeParameters_Example_1"></a>

This example illustrates one usage of DescribeParameters.

#### Sample Request
<a name="API_DescribeParameters_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 95
X-Amz-Target: AmazonSSM.DescribeParameters
X-Amz-Date: 20240316T010204Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "ParameterFilters": [
        {
            "Values": [
                "String"
            ],
            "Key": "Type"
        },
        {
            "Values": [
                "/Branch312"
            ],
            "Key": "Name"
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeParameters_Example_1_Response"></a>

```
{
    "Parameters": [
        {
            "LastModifiedDate": 1521160696.821,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Name": "/Branch312/Dev/Engineer1",
            "Policies": [],
            "Type": "String",
            "Version": 1,
            "Tier": "Standard"
        },
        {
            "LastModifiedDate": 1521160709.358,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Name": "/Branch312/Dev/Engineer2",
            "Policies": [],
            "Type": "String",
            "Version": 1,
            "Tier": "Standard"
        },
        {
            "LastModifiedDate": 1521160717.945,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Name": "/Branch312/Dev/Engineer3",
            "Policies": [],
            "Type": "String",
            "Version": 1,
            "Tier": "Standard"
        },
        {
            "LastModifiedDate": 1521160747.499,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mary.Major",
            "Name": "/Branch312/Dev/Intern",
            "Policies": [
                {
                    "PolicyStatus": "Pending",
                    "PolicyText": "{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2024-03-31T17:00:00Z\"}}",
                    "PolicyType": "Expiration"
                },
                {
                    "PolicyStatus": "Pending",
                    "PolicyText": "{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"14\",\"Unit\":\"Days\"}}",
                    "PolicyType": "ExpirationNotification"
                }
            ],
            "Type": "String",
            "Version": 1,
            "Tier": "Standard"
        },
        {
            "LastModifiedDate": 1521160588.291,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/John.Stiles",
            "Name": "/Branch312/Dev/TeamLead",
            "Policies": [],
            "Type": "String",
            "Version": 1,
            "Tier": "Standard"
        }
    ]
}
```

## See Also
<a name="API_DescribeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
