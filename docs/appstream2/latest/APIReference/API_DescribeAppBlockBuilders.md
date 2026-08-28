---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppBlockBuilders.html
---

# DescribeAppBlockBuilders
<a name="API_DescribeAppBlockBuilders"></a>

Retrieves a list that describes one or more app block builders.

## Request Syntax
<a name="API_DescribeAppBlockBuilders_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAppBlockBuilders_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeAppBlockBuilders_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilders-request-MaxResults"></a>
The maximum size of each page of results. The maximum value is 25.
Type: Integer
Required: No

 ** [Names](#API_DescribeAppBlockBuilders_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilders-request-Names"></a>
The names of the app block builders.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** [NextToken](#API_DescribeAppBlockBuilders_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilders-request-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeAppBlockBuilders_ResponseSyntax"></a>

```
{
   "AppBlockBuilders": [
      {
         "AccessEndpoints": [
            {
               "EndpointType": "string",
               "VpceId": "string"
            }
         ],
         "AppBlockBuilderErrors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string",
               "ErrorTimestamp": number
            }
         ],
         "Arn": "string",
         "CreatedTime": number,
         "Description": "string",
         "DisableIMDSV1": boolean,
         "DisplayName": "string",
         "EnableDefaultInternetAccess": boolean,
         "IamRoleArn": "string",
         "InstanceType": "string",
         "Name": "string",
         "Platform": "string",
         "State": "string",
         "StateChangeReason": {
            "Code": "string",
            "Message": "string"
         },
         "VpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ]
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAppBlockBuilders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlockBuilders](#API_DescribeAppBlockBuilders_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilders-response-AppBlockBuilders"></a>
The list that describes one or more app block builders.
Type: Array of [AppBlockBuilder](API_AppBlockBuilder.md) objects

 ** [NextToken](#API_DescribeAppBlockBuilders_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilders-response-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeAppBlockBuilders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAppBlockBuilders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeAppBlockBuilders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeAppBlockBuilders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
