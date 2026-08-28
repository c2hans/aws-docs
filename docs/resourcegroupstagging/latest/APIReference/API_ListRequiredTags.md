---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_ListRequiredTags.html
---

# ListRequiredTags
<a name="API_ListRequiredTags"></a>

Lists the required tags for supported resource types in an AWS account.

## Request Syntax
<a name="API_ListRequiredTags_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRequiredTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRequiredTags_RequestSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-request-MaxResults"></a>
The maximum number of required tags.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListRequiredTags_RequestSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-request-NextToken"></a>
A token for requesting another page of required tags if the `NextToken` response element indicates that more required tags are available. Use the value of the returned `NextToken` element in your request until the token comes back as null. Pass null if this is the first call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_ListRequiredTags_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RequiredTags": [
      {
         "CloudFormationResourceTypes": [ "string" ],
         "ReportingTagKeys": [ "string" ],
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRequiredTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRequiredTags_ResponseSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-response-NextToken"></a>
A token for requesting another page of required tags if the `NextToken` response element indicates that more required tags are available. Use the value of the returned `NextToken` element in your request until the token comes back as null. Pass null if this is the first call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [RequiredTags](#API_ListRequiredTags_ResponseSyntax) **   <a name="resourcegrouptagging-ListRequiredTags-response-RequiredTags"></a>
The required tags.
Type: Array of [RequiredTag](API_RequiredTag.md) objects

## Errors
<a name="API_ListRequiredTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The request processing failed because of an unknown error, exception, or failure. You can retry the request.
HTTP Status Code: 500

 ** InvalidParameterException **
The request failed because of one of the following reasons:
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide.
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.
HTTP Status Code: 400

 ** ThrottledException **
The request failed because it exceeded the allowed frequency of submitted requests.
HTTP Status Code: 400

## Examples
<a name="API_ListRequiredTags_Examples"></a>

### Example
<a name="API_ListRequiredTags_Example_1"></a>

This example illustrates one usage of ListRequiredTags.

#### Sample Request
<a name="API_ListRequiredTags_Example_1_Request"></a>

```
                    POST / HTTP/1.1
                    Host: tagging.us-east-1.amazonaws.com
                    Accept-Encoding: identity
                    Content-Length: 20
                    X-Amz-Target: ResourceGroupsTaggingAPI_20170126.ListRequiredTags
                    X-Amz-Date: 20191201T214524Z
                    User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
                    Content-Type: application/x-amz-json-1.1
                    Authorization:  AUTHPARAMS

                    {}
```

#### Sample Response
<a name="API_ListRequiredTags_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
                    x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
                    Content-Type: application/x-amz-json-1.1
                    Date: Sun, 1 Dec 2019 21:45:25 GMT

                    {
                        "RequiredTags": [
                            {
                                "ResourceType": "ec2:instance",
                                "CloudFormationResourceTypes": ["AWS::EC2::Instance"],
                                "ReportingTagKeys": ["example_tag_key"]
                            },
                            {
                                "ResourceType": "s3:bucket",
                                "CloudFormationResourceTypes": ["AWS::S3:Bucket"],
                                "ReportingTagKeys": ["example_tag_key"]
                            }
                        ]
                    }
```

## See Also
<a name="API_ListRequiredTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/ListRequiredTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resourcegroupstagging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
