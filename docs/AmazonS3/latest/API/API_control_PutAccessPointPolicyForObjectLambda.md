---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html
---

# PutAccessPointPolicyForObjectLambda
<a name="API_control_PutAccessPointPolicyForObjectLambda"></a>

**Note**
This operation is not supported by directory buckets.

Creates or replaces resource policy for an Object Lambda Access Point. For an example policy, see [Creating Object Lambda Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-create.html#olap-create-cli) in the *Amazon S3 User Guide*.

The following actions are related to `PutAccessPointPolicyForObjectLambda`:
+  [DeleteAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html)
+  [GetAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html)

## Request Syntax
<a name="API_control_PutAccessPointPolicyForObjectLambda_RequestSyntax"></a>

```
PUT /v20180820/accesspointforobjectlambda/{{name}}/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<PutAccessPointPolicyForObjectLambdaRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Policy>{{string}}</Policy>
</PutAccessPointPolicyForObjectLambdaRequest>
```

## URI Request Parameters
<a name="API_control_PutAccessPointPolicyForObjectLambda_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointPolicyForObjectLambda-request-uri-uri-Name"></a>
The name of the Object Lambda Access Point.
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** [x-amz-account-id](#API_control_PutAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointPolicyForObjectLambda-request-header-AccountId"></a>
The account ID for the account that owns the specified Object Lambda Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutAccessPointPolicyForObjectLambda_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutAccessPointPolicyForObjectLambdaRequest](#API_control_PutAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointPolicyForObjectLambda-request-PutAccessPointPolicyForObjectLambdaRequest"></a>
Root level tag for the PutAccessPointPolicyForObjectLambdaRequest parameters.
Required: Yes

 ** [Policy](#API_control_PutAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointPolicyForObjectLambda-request-Policy"></a>
Object Lambda Access Point resource policy document.
Type: String
Required: Yes

## Response Syntax
<a name="API_control_PutAccessPointPolicyForObjectLambda_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutAccessPointPolicyForObjectLambda_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_control_PutAccessPointPolicyForObjectLambda_Examples"></a>

### Sample resource policy
<a name="API_control_PutAccessPointPolicyForObjectLambda_Example_1"></a>

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
<a name="API_control_PutAccessPointPolicyForObjectLambda_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointPolicyForObjectLambda)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
