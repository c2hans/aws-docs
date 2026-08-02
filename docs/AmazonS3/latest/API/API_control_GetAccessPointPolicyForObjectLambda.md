---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html
---

# GetAccessPointPolicyForObjectLambda
<a name="API_control_GetAccessPointPolicyForObjectLambda"></a>

**Note**
This operation is not supported by directory buckets.

Returns the resource policy for an Object Lambda Access Point.

The following actions are related to `GetAccessPointPolicyForObjectLambda`:
+  [DeleteAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html)
+  [PutAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html)

## Request Syntax
<a name="API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax"></a>

```
GET /v20180820/accesspointforobjectlambda/{{name}}/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessPointPolicyForObjectLambda_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyForObjectLambda-request-uri-uri-Name"></a>
The name of the Object Lambda Access Point.
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyForObjectLambda-request-header-AccountId"></a>
The account ID for the account that owns the specified Object Lambda Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessPointPolicyForObjectLambda_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointPolicyForObjectLambdaResult>
   <Policy>string</Policy>
</GetAccessPointPolicyForObjectLambdaResult>
```

## Response Elements
<a name="API_control_GetAccessPointPolicyForObjectLambda_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessPointPolicyForObjectLambdaResult](#API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-GetAccessPointPolicyForObjectLambdaResult"></a>
Root level tag for the GetAccessPointPolicyForObjectLambdaResult parameters.
Required: Yes

 ** [Policy](#API_control_GetAccessPointPolicyForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyForObjectLambda-response-Policy"></a>
Object Lambda Access Point resource policy document.
Type: String

## Examples
<a name="API_control_GetAccessPointPolicyForObjectLambda_Examples"></a>

### Sample resource policy
<a name="API_control_GetAccessPointPolicyForObjectLambda_Example_1"></a>

The following illustrates a sample resource policy.

```
{
    "Version" : "2008-10-17",
    "Statement":[{
        "Sid": "Grant account 123456789012 GetObject access",
        "Effect":"Allow",
        "Principal" : {
            "AWS": "arn:aws:iam::123456789012:root"
        },
        "Action":["s3-object-lambda:GetObject"],
        "Resource":["arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/my-object-lambda-ap"]
        },
        {
        "Sid": "Grant account 444455556666 GetObject access",
        "Effect":"Allow",
        "Principal" : {
            "AWS": "arn:aws:iam::444455556666:root"
        },
        "Action":["s3-object-lambda:GetObject"],
        "Resource":["arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/my-object-lambda-ap"]
        }
    ]
}
```

## See Also
<a name="API_control_GetAccessPointPolicyForObjectLambda_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyForObjectLambda)
