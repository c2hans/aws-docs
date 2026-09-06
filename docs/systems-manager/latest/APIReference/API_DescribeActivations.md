---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeActivations.html
---

# DescribeActivations
<a name="API_DescribeActivations"></a>

Describes details about the activation, such as the date and time the activation was created, its expiration date, the AWS Identity and Access Management (IAM) role assigned to the managed nodes in the activation, and the number of nodes registered by using this activation.

## Request Syntax
<a name="API_DescribeActivations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "FilterKey": "{{string}}",
         "FilterValues": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeActivations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeActivations_RequestSyntax) **   <a name="systemsmanager-DescribeActivations-request-Filters"></a>
A filter to view information about your activations.
Type: Array of [DescribeActivationsFilter](API_DescribeActivationsFilter.md) objects
Required: No

 ** [MaxResults](#API_DescribeActivations_RequestSyntax) **   <a name="systemsmanager-DescribeActivations-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeActivations_RequestSyntax) **   <a name="systemsmanager-DescribeActivations-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeActivations_ResponseSyntax"></a>

```
{
   "ActivationList": [
      {
         "ActivationId": "string",
         "CreatedDate": number,
         "DefaultInstanceName": "string",
         "Description": "string",
         "ExpirationDate": number,
         "Expired": boolean,
         "IamRole": "string",
         "RegistrationLimit": number,
         "RegistrationsCount": number,
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeActivations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActivationList](#API_DescribeActivations_ResponseSyntax) **   <a name="systemsmanager-DescribeActivations-response-ActivationList"></a>
A list of activations for your AWS account.
Type: Array of [Activation](API_Activation.md) objects

 ** [NextToken](#API_DescribeActivations_ResponseSyntax) **   <a name="systemsmanager-DescribeActivations-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_DescribeActivations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeActivations_Examples"></a>

### Example
<a name="API_DescribeActivations_Example_1"></a>

This example illustrates one usage of DescribeActivations.

#### Sample Request
<a name="API_DescribeActivations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeActivations
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T152059Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_DescribeActivations_Example_1_Response"></a>

```
{
    "ActivationList": [
        {
            "ActivationId": "e9136c70-ba7b-4d7d-8e31-174a7EXAMPLE",
            "CreatedDate": 1581954699.792,
            "Description": "Example",
            "ExpirationDate": 1584316800,
            "Expired": true,
            "IamRole": "service-role/RoleForManagedInstances",
            "RegistrationLimit": 5,
            "RegistrationsCount": 1
        }
    ]
}
```

## See Also
<a name="API_DescribeActivations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeActivations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeActivations)
