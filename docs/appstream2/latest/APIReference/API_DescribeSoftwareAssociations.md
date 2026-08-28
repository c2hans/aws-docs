---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeSoftwareAssociations.html
---

# DescribeSoftwareAssociations
<a name="API_DescribeSoftwareAssociations"></a>

Retrieves license included application associations for a specified resource.

## Request Syntax
<a name="API_DescribeSoftwareAssociations_RequestSyntax"></a>

```
{
   "AssociatedResource": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSoftwareAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociatedResource](#API_DescribeSoftwareAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSoftwareAssociations-request-AssociatedResource"></a>
The ARN of the resource to describe software associations. Possible resources are Image and ImageBuilder.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** [MaxResults](#API_DescribeSoftwareAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSoftwareAssociations-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeSoftwareAssociations_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSoftwareAssociations-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeSoftwareAssociations_ResponseSyntax"></a>

```
{
   "AssociatedResource": "string",
   "NextToken": "string",
   "SoftwareAssociations": [
      {
         "DeploymentError": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "SoftwareName": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSoftwareAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociatedResource](#API_DescribeSoftwareAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeSoftwareAssociations-response-AssociatedResource"></a>
The ARN of the resource to describe software associations.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`

 ** [NextToken](#API_DescribeSoftwareAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeSoftwareAssociations-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.

 ** [SoftwareAssociations](#API_DescribeSoftwareAssociations_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeSoftwareAssociations-response-SoftwareAssociations"></a>
Collection of license included applications association details including:
+ License included application name and version information
+ Deployment status (SoftwareDeploymentStatus enum)
+ Error details for failed deployments
+ Association timestamps
Type: Array of [SoftwareAssociations](API_SoftwareAssociations.md) objects

## Errors
<a name="API_DescribeSoftwareAssociations_Errors"></a>

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
<a name="API_DescribeSoftwareAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeSoftwareAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeSoftwareAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
