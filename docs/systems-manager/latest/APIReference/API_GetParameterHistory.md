---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameterHistory.html
---

# GetParameterHistory
<a name="API_GetParameterHistory"></a>

Retrieves the history of all changes to a parameter.

Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

**Important**
If you change the AWS KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, `GetParameterHistory` retrieves whatever the original key alias was referencing.

## Request Syntax
<a name="API_GetParameterHistory_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}",
   "WithDecryption": {{boolean}}
}
```

## Request Parameters
<a name="API_GetParameterHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetParameterHistory_RequestSyntax) **   <a name="systemsmanager-GetParameterHistory-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Name](#API_GetParameterHistory_RequestSyntax) **   <a name="systemsmanager-GetParameterHistory-request-Name"></a>
The name or Amazon Resource Name (ARN) of the parameter for which you want to review history. For parameters shared with you from another account, you must use the full ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [NextToken](#API_GetParameterHistory_RequestSyntax) **   <a name="systemsmanager-GetParameterHistory-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [WithDecryption](#API_GetParameterHistory_RequestSyntax) **   <a name="systemsmanager-GetParameterHistory-request-WithDecryption"></a>
Return decrypted values for secure string parameters. This flag is ignored for `String` and `StringList` parameter types.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetParameterHistory_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Parameters": [
      {
         "AllowedPattern": "string",
         "DataType": "string",
         "Description": "string",
         "KeyId": "string",
         "Labels": [ "string" ],
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
         "Value": "string",
         "Version": number
      }
   ]
}
```

## Response Elements
<a name="API_GetParameterHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetParameterHistory_ResponseSyntax) **   <a name="systemsmanager-GetParameterHistory-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Parameters](#API_GetParameterHistory_ResponseSyntax) **   <a name="systemsmanager-GetParameterHistory-response-Parameters"></a>
A list of parameters returned by the request.
Type: Array of [ParameterHistory](API_ParameterHistory.md) objects

## Errors
<a name="API_GetParameterHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidKeyId **
The query key ID isn't valid.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** ParameterNotFound **
The parameter couldn't be found. Verify the name and try again.
For the `DeleteParameter` and `GetParameter` actions, if the specified parameter doesn't exist, the `ParameterNotFound` exception is *not* recorded in AWS CloudTrail event logs.
HTTP Status Code: 400

## Examples
<a name="API_GetParameterHistory_Examples"></a>

### Example
<a name="API_GetParameterHistory_Example_1"></a>

This example illustrates one usage of GetParameterHistory.

#### Sample Request
<a name="API_GetParameterHistory_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 29
X-Amz-Target: AmazonSSM.GetParameterHistory
X-Amz-Date: 20240316T005206Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Name": "EC2TestServerType"
}
```

#### Sample Response
<a name="API_GetParameterHistory_Example_1_Response"></a>

```
{
    "Parameters": [
        {
            "Description": "Instance type for Test servers",
            "LastModifiedDate": 1521158745.607,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Name": "EC2TestServerType",
            "Policies": [],
            "Type": "String",
            "Value": "t2.nano",
            "Version": 1
        },
        {
            "Description": "Instance type for Test servers",
            "LastModifiedDate": 1521158834.467,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Name": "EC2TestServerType",
            "Policies": [],
            "Type": "String",
            "Value": "t2.micro",
            "Version": 2
        },
        {
            "Description": "Instance type for Test servers",
            "LastModifiedDate": 1521158912.828,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Jane.Roe",
            "Name": "EC2TestServerType",
            "Policies": [],
            "Type": "String",
            "Value": "t2.large",
            "Version": 3
        }
    ]
}
```

## See Also
<a name="API_GetParameterHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetParameterHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetParameterHistory)
