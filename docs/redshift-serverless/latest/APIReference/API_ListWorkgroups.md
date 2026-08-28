---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListWorkgroups.html
---

# ListWorkgroups
<a name="API_ListWorkgroups"></a>

Returns information about a list of specified workgroups.

## Request Syntax
<a name="API_ListWorkgroups_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "ownerAccount": "{{string}}"
}
```

## Request Parameters
<a name="API_ListWorkgroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkgroups_RequestSyntax) **   <a name="redshiftserverless-ListWorkgroups-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListWorkgroups_RequestSyntax) **   <a name="redshiftserverless-ListWorkgroups-request-nextToken"></a>
If your initial ListWorkgroups operation returns a `nextToken`, you can include the returned `nextToken` in following ListNamespaces operations, which returns results in the next page.
Type: String
Required: No

 ** [ownerAccount](#API_ListWorkgroups_RequestSyntax) **   <a name="redshiftserverless-ListWorkgroups-request-ownerAccount"></a>
The owner AWS account for the Amazon Redshift Serverless workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `.*(\d{12}).*`
Required: No

## Response Syntax
<a name="API_ListWorkgroups_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "workgroups": [
      {
         "baseCapacity": number,
         "configParameters": [
            {
               "parameterKey": "string",
               "parameterValue": "string"
            }
         ],
         "creationDate": "string",
         "crossAccountVpcs": [ "string" ],
         "customDomainCertificateArn": "string",
         "customDomainCertificateExpiryTime": "string",
         "customDomainName": "string",
         "endpoint": {
            "address": "string",
            "port": number,
            "vpcEndpoints": [
               {
                  "networkInterfaces": [
                     {
                        "availabilityZone": "string",
                        "ipv6Address": "string",
                        "networkInterfaceId": "string",
                        "privateIpAddress": "string",
                        "subnetId": "string"
                     }
                  ],
                  "vpcEndpointId": "string",
                  "vpcId": "string"
               }
            ]
         },
         "enhancedVpcRouting": boolean,
         "extraComputeForAutomaticOptimization": boolean,
         "ipAddressType": "string",
         "maxCapacity": number,
         "namespaceName": "string",
         "patchVersion": "string",
         "pendingTrackName": "string",
         "port": number,
         "pricePerformanceTarget": {
            "level": number,
            "status": "string"
         },
         "publiclyAccessible": boolean,
         "securityGroupIds": [ "string" ],
         "status": "string",
         "subnetIds": [ "string" ],
         "trackName": "string",
         "workgroupArn": "string",
         "workgroupId": "string",
         "workgroupName": "string",
         "workgroupVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkgroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkgroups_ResponseSyntax) **   <a name="redshiftserverless-ListWorkgroups-response-nextToken"></a>
 If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.
Type: String

 ** [workgroups](#API_ListWorkgroups_ResponseSyntax) **   <a name="redshiftserverless-ListWorkgroups-response-workgroups"></a>
The returned array of workgroups.
Type: Array of [Workgroup](API_Workgroup.md) objects

## Errors
<a name="API_ListWorkgroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListWorkgroups_Examples"></a>

### Example
<a name="API_ListWorkgroups_Example_1"></a>

This example illustrates one usage of ListWorkgroups.

#### Sample Request
<a name="API_ListWorkgroups_Example_1_Request"></a>

```
aws redshift-serverless list-workgroups
--region us-east-1
```

#### Sample Response
<a name="API_ListWorkgroups_Example_1_Response"></a>

```
{
  "workgroups": [
    {
      "workgroupId": "aff51189-e570-474d-9feb-ae83286e057c",
      "workgroupArn": "arn:aws:redshift-serverless:us-east-1:012345678901:workgroup/aff51189-e570-474d-9feb-ae83286e057c",
      "workgroupName": "test-track-1",
      "namespaceName": "test-track-ns",
      "baseCapacity": 32,
      "enhancedVpcRouting": false,
      "trackName": "current",
      "pendingTrackName": "trailing"
    ]
  },
  ...
}
```

## See Also
<a name="API_ListWorkgroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListWorkgroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListWorkgroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
