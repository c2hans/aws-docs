---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppBlockBuilderAppBlockAssociations.html
---

# DescribeAppBlockBuilderAppBlockAssociations
<a name="API_DescribeAppBlockBuilderAppBlockAssociations"></a>

Retrieves a list that describes one or more app block builder associations.

## Request Syntax
<a name="API_DescribeAppBlockBuilderAppBlockAssociations_RequestSyntax"></a>

```
{
   "AppBlockArn": "{{string}}",
   "AppBlockBuilderName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAppBlockBuilderAppBlockAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppBlockArn](#API_DescribeAppBlockBuilderAppBlockAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilderAppBlockAssociations-request-AppBlockArn"></a>
The ARN of the app block.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [AppBlockBuilderName](#API_DescribeAppBlockBuilderAppBlockAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilderAppBlockAssociations-request-AppBlockBuilderName"></a>
The name of the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: No

 ** [MaxResults](#API_DescribeAppBlockBuilderAppBlockAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilderAppBlockAssociations-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeAppBlockBuilderAppBlockAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilderAppBlockAssociations-request-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeAppBlockBuilderAppBlockAssociations_ResponseSyntax"></a>

```
{
   "AppBlockBuilderAppBlockAssociations": [
      {
         "AppBlockArn": "string",
         "AppBlockBuilderName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAppBlockBuilderAppBlockAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlockBuilderAppBlockAssociations](#API_DescribeAppBlockBuilderAppBlockAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilderAppBlockAssociations-response-AppBlockBuilderAppBlockAssociations"></a>
This list of app block builders associated with app blocks.
Type: Array of [AppBlockBuilderAppBlockAssociation](API_AppBlockBuilderAppBlockAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.

 ** [NextToken](#API_DescribeAppBlockBuilderAppBlockAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlockBuilderAppBlockAssociations-response-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeAppBlockBuilderAppBlockAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAppBlockBuilderAppBlockAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeAppBlockBuilderAppBlockAssociations)
